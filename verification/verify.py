"""Reproduce the receiver's matrix identities and finite benchmarks."""

from itertools import permutations, product

import numpy as np


I = np.eye(2, dtype=complex)
PAULI = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.diag([1, -1]).astype(complex),
)
X, _, Z = PAULI
ORDERS = tuple(permutations(range(3)))
PAULI_BASIS = (I, *PAULI)
TOL = 1e-11


def parity(order):
    inversions = sum(order[a] > order[b] for a in range(3) for b in range(a + 1, 3))
    return (-1) ** inversions


def kron(*items):
    result = items[0]
    for item in items[1:]:
        result = np.kron(result, item)
    return result


def spin(direction):
    return sum(value * pauli for value, pauli in zip(direction, PAULI))


def chirality(weights=(1, 1, 1)):
    return sum(
        parity(order) * weights[order[0]] * kron(*(PAULI[i] for i in order))
        for order in ORDERS
    )


def signed_rotations():
    for order in ORDERS:
        for signs in product((1, -1), repeat=3):
            if np.prod(signs) == parity(order):
                yield np.eye(3, dtype=int)[list(order)] * np.array(signs)[:, None]


def check_twirl_and_spectrum():
    rotations = np.array(tuple(signed_rotations()))
    assert len(rotations) == 24
    np.testing.assert_array_equal(rotations.sum(axis=0), np.zeros((3, 3)))
    np.testing.assert_array_equal(
        np.einsum("aij,akl->ijkl", rotations, rotations),
        8 * np.einsum("ik,jl->ijkl", np.eye(3, dtype=int), np.eye(3, dtype=int)),
    )
    epsilon = np.zeros((3, 3, 3), dtype=int)
    for order in ORDERS:
        epsilon[order] = parity(order)
    np.testing.assert_array_equal(
        np.einsum("aij,akl,amn->ijklmn", rotations, rotations, rotations),
        4 * np.einsum("ikm,jln->ijklmn", epsilon, epsilon),
    )

    chi = chirality()
    np.testing.assert_array_equal(chi @ chi @ chi, 12 * chi)
    assert np.trace(chi) == 0
    assert np.trace(chi @ chi) == 48

    triples = (
        np.eye(3),
        np.array([[1, 0, 1], [1, 2, 0], [0, 1, 2]]) / 4,
        np.array([[0, -2, 1], [2, 0, 1], [1, 1, -2]]) / 4,
    )
    for triple in triples:
        mirror = triple @ np.diag([-1, 1, 1])
        sums = [
            sum(kron(*(I + spin(rotation @ row) for row in states)) for rotation in rotations)
            for states in (triple, mirror)
        ]
        scale = len(rotations) * 8
        determinant = np.dot(triple[0], np.cross(triple[1], triple[2]))
        np.testing.assert_array_equal(
            sums[0] - sums[1], (scale / 24) * determinant * chi
        )
    print("Exact integer rotation moments, mirror twirl and chirality spectrum passed.")


def check_classical_benchmark():
    observable = np.zeros((8, 8), dtype=complex)
    for order in ORDERS:
        for signs in product((1, -1), repeat=3):
            projector = kron(*((I + s * PAULI[i]) / 2 for i, s in zip(order, signs)))
            observable += parity(order) * np.prod(signs) * projector / 6
    np.testing.assert_allclose(observable, chirality() / 6, atol=TOL, rtol=0)

    for r in (np.zeros(3), np.array([2, 3, 6]) / 7, np.array([0, -2, 1]) / 4):
        effect = (I + spin(r)) / 3
        projected = sum(
            parity((i, j, k)) * np.trace(effect @ PAULI[i]) * kron(PAULI[j], PAULI[k])
            for i, j, k in ORDERS
        )
        np.testing.assert_allclose(trace_norm(projected), 8 * np.linalg.norm(r) / 3,
                                   atol=TOL, rtol=0)
    depolarizing = np.array([0.5, 0.5, 0.5])
    dephasing = np.array([1.0, 0.25, 0.25])
    assert 0.5 + depolarizing.sum() / 6 == 0.5 + dephasing.sum() / 6 == 0.75
    assert np.linalg.norm(depolarizing) < 1 < np.linalg.norm(dephasing)
    print("Classical Pauli receiver, first-cut trace norm and equal-fidelity example passed.")


def bell_readout(weights):
    scale = np.linalg.norm(weights)
    result = np.zeros((8, 8), dtype=complex)
    for orientation in (1, -1):
        orders = [order for order in ORDERS if parity(order) == orientation]
        pair_ops = [kron(PAULI[i], PAULI[j]) for i, j, _ in orders]
        np.testing.assert_array_equal(pair_ops[0] @ pair_ops[1], -pair_ops[2])
        np.testing.assert_array_equal(pair_ops[1] @ pair_ops[0], -pair_ops[2])
        projectors = []
        for a, b in product((1, -1), repeat=2):
            signs = (a, b, -a * b)
            projector = (np.eye(4) + a * pair_ops[0]) @ (np.eye(4) + b * pair_ops[1]) / 4
            np.testing.assert_array_equal(projector @ projector, projector)
            assert np.trace(projector) == 1
            projectors.append(projector)
            followup = sum(s * weights[i] * PAULI[k] for s, (i, _, k) in zip(signs, orders))
            followup /= scale
            np.testing.assert_allclose(followup @ followup, I, atol=TOL, rtol=0)
            result += orientation * kron(projector, followup) / 2
        np.testing.assert_array_equal(sum(projectors), np.eye(4))
    return result


def apply_channel(op, matrix, shift):
    scalar = np.trace(op) / 2
    vector = np.array([np.trace(pauli @ op) / 2 for pauli in PAULI])
    return scalar * I + spin(matrix @ vector + scalar * shift)


def adjoint_channel(op, matrix, shift):
    scalar = np.trace(op) / 2
    vector = np.array([np.trace(pauli @ op) / 2 for pauli in PAULI])
    return (scalar + np.dot(shift, vector)) * I + spin(matrix.T @ vector)


def pull_back_first(observable, transform):
    blocks = observable.reshape((2, 4, 2, 4))
    return sum(
        kron(transform(basis), np.einsum("ab,bcad->cd", basis, blocks) / 2)
        for basis in PAULI_BASIS
    )


def trace_norm(matrix):
    return np.abs(np.linalg.eigvalsh(matrix)).sum()


def filtered_branch(t, axis):
    axis_op = spin(axis)
    return sum(np.sqrt(1 + s * t) * (I + s * axis_op) / 2 for s in (1, -1))


def branch_chirality(kraus, matrix, shift):
    first = [apply_channel(kraus @ p @ kraus.conj().T, matrix, shift) for p in PAULI]
    return sum(parity((i, j, k)) * kron(first[i], PAULI[j], PAULI[k]) for i, j, k in ORDERS)


def random_rotation(rng):
    q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    q[:, 0] *= np.sign(np.linalg.det(q))
    return q


def norm_expression(a, coupling):
    assert a - coupling >= -TOL
    return np.sqrt(a + coupling) + np.sqrt(max(0, a - coupling))


def check_unital_channels():
    rng = np.random.default_rng(20261123)
    fixed = np.array([[1, 1, 1], [0, 0, 0], [0.5, 0.5, 0.5], [1, 0.25, 0.25],
                      [1, 0, 0], [1, -1, -1], [0.25, -0.25, 0.25],
                      [1 / np.sqrt(3)] * 3])
    pauli_signs = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]])
    spectra = np.vstack((fixed, rng.dirichlet(np.ones(4), size=640) @ pauli_signs))
    max_error = 0.0
    bell_cases = 0
    branch_cases = 0
    zero = np.zeros(3)
    for weights in spectra:
        F = float(weights @ weights)
        if F:
            effects = []
            for k in range(3):
                permuted = np.roll(weights, k)
                effect = bell_readout(permuted)
                np.testing.assert_allclose(effect, chirality(permuted) / (2 * np.sqrt(F)),
                                           atol=TOL, rtol=0)
                matrix = np.diag(permuted)
                effects.append(pull_back_first(effect, lambda op: adjoint_channel(op, matrix, zero)))
            np.testing.assert_allclose(sum(effects) / 3, np.sqrt(F) * chirality() / 6,
                                       atol=TOL, rtol=0)
            bell_cases += 1

        matrix = random_rotation(rng) @ np.diag(weights) @ random_rotation(rng)
        for t in [0.0, 1.0, float(rng.random())]:
            axis = rng.normal(size=3)
            axis /= np.linalg.norm(axis)
            b = np.linalg.norm(matrix @ axis) ** 2
            a = F + (1 - F + b) * t * t
            expected = 4 * norm_expression(a, 2 * t * np.sqrt(b))
            actual = trace_norm(branch_chirality(filtered_branch(t, axis), matrix, zero))
            max_error = max(max_error, abs(expected - actual))
            np.testing.assert_allclose(actual, expected, atol=TOL, rtol=0)
            assert actual <= 8 * np.sqrt(max(1, F)) + TOL
            branch_cases += 1
    print(f"Unital converse passed on {branch_cases} Kraus branches across {len(spectra)}"
          f" channel spectra (max trace-norm error {max_error:.3g}).")
    print(f"Weighted Bell construction and cyclic pullback passed for {bell_cases} nonzero spectra.")


def amplitude_damping(eta):
    matrix = np.diag([np.sqrt(eta), np.sqrt(eta), eta])
    shift = np.array([0, 0, 1 - eta])
    return matrix, shift


def check_amplitude_damping():
    axis = np.array([0, 0, 1])
    matched_sign = kron(I, X, X)
    rotate = (I - 1j * sum(PAULI)) / 2
    common_rotate = kron(rotate, rotate, rotate)
    benchmark = 1 / 12
    for eta in (0.0, 0.002, 0.05, 1 / 3, 0.37, 0.6, 0.9, 1.0):
        matrix, shift = amplitude_damping(eta)
        a = 4 * eta - eta * eta - 1
        strength = eta * (1 - eta) / a if eta > 1 / 3 else 1.0
        positive = filtered_branch(strength, axis) / np.sqrt(2)
        negative = positive @ X
        np.testing.assert_allclose(positive.conj().T @ positive + negative.conj().T @ negative,
                                   I, atol=TOL, rtol=0)
        w = np.array([np.sqrt(eta * (1 - strength**2))] * 2 + [eta + strength * (1 - eta)])
        observable = bell_readout(w)
        pullback = sum(
            pull_back_first(op, lambda x: k.conj().T @ adjoint_channel(x, matrix, shift) @ k)
            for op, k in ((observable, positive), (matched_sign @ observable @ matched_sign, negative))
        )
        np.testing.assert_allclose(pullback, chirality(w**2) / (2 * np.linalg.norm(w)),
                                   atol=TOL, rtol=0)
        rotated_pullback = common_rotate.conj().T @ pullback @ common_rotate
        cyclic_pullback = (
            pullback + rotated_pullback + common_rotate.conj().T @ rotated_pullback @ common_rotate
        ) / 3
        np.testing.assert_allclose(cyclic_pullback, np.linalg.norm(w) * chirality() / 6,
                                   atol=TOL, rtol=0)
        expected = 1 + (3 * eta - 1) ** 2 / a if eta > 1 / 3 else 1.0
        np.testing.assert_allclose(w @ w, expected, atol=TOL, rtol=0)
        assert np.linalg.norm(w) / 12 >= benchmark - TOL

        if 0 < eta < 1:
            min_strength = (np.sqrt(max(0, 1 - 2 * eta)) - eta) / (1 - eta)
            late_strength = (1 + max(0, min_strength)) / 2
            late_kraus = filtered_branch(late_strength, axis)
            beta = eta + late_strength * (1 - eta)
            center = 2 * eta * (1 - late_strength**2) + late_strength**2 + beta**2
            expected_norm = 4 * norm_expression(center, 2 * late_strength * beta)
            observed_norm = trace_norm(branch_chirality(late_kraus, matrix, shift))
            np.testing.assert_allclose(observed_norm, expected_norm, atol=TOL, rtol=0)
            assert observed_norm > 8
    print("Amplitude-damping pullback, optimized staged lower bound and relaxed late-storage examples passed.")


def main():
    check_twirl_and_spectrum()
    check_classical_benchmark()
    check_unital_channels()
    check_amplitude_damping()


if __name__ == "__main__":
    main()
