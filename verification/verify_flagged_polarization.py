"""Check the four-carrier channel and staged chirality scores with NumPy."""

from itertools import product
from math import sqrt

import numpy as np


I = np.eye(2)
X = np.array([[0, 1], [1, 0]])
Y = np.array([[0, -1j], [1j, 0]])
Z = np.diag([1, -1])
PAULI = (X, Y, Z)
TOLERANCE = 2e-10


def close(actual, expected):
    np.testing.assert_allclose(actual, expected, atol=TOLERANCE, rtol=0)


def kron(*matrices):
    result = matrices[0]
    for matrix in matrices[1:]:
        result = np.kron(result, matrix)
    return result


def vector_operator(vector, operators):
    return sum(component * matrix for component, matrix in zip(vector, operators))


PAIR_CHIRALITY = tuple(
    kron(PAULI[j], PAULI[k]) - kron(PAULI[k], PAULI[j])
    for j, k in ((1, 2), (2, 0), (0, 1))
)
CHIRALITY = sum(kron(pauli, pair) for pauli, pair in zip(PAULI, PAIR_CHIRALITY))

ZERO, ONE = I
SINGLET = (kron(ZERO, ONE) - kron(ONE, ZERO)) / sqrt(2)
TRIPLET_0 = (kron(ZERO, ONE) + kron(ONE, ZERO)) / sqrt(2)
TRIPLET_PLUS = kron(ZERO, ZERO)
TRIPLET_MINUS = kron(ONE, ONE)
CARTESIAN_TRIPLETS = np.column_stack(
    tuple(-1j * kron(pauli, I) @ SINGLET for pauli in PAULI)
)
CODE = np.column_stack(
    (
        kron(SINGLET, SINGLET),
        (
            kron(TRIPLET_PLUS, TRIPLET_MINUS)
            - kron(TRIPLET_0, TRIPLET_0)
            + kron(TRIPLET_MINUS, TRIPLET_PLUS)
        )
        / sqrt(3),
    )
)


def random_unitary(rng):
    matrix = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    q, r = np.linalg.qr(matrix)
    diagonal = np.diag(r)
    return q * (diagonal / np.abs(diagonal))


def channel_weights(x, y):
    p_b = 2 * x * y * (x + y) - 3 * (x * y) ** 2
    p_e = 2 * (1 - x) * (1 - y) * (2 - x - y) - 3 * ((1 - x) * (1 - y)) ** 2
    w0 = x * y * (1 - x) * (1 - y)
    w1 = w0 + (x - y) ** 2 / 3
    close(1 - p_b - p_e, 3 * (w0 + w1))
    return p_b, p_e, w0, w1


def decoded_identity_kraus(kraus, ordered_code, survivor_count):
    if survivor_count == 4:
        gauges = [CODE]
    else:
        # Resolving the lost qubit in its computational basis gives two
        # orthogonal spin-half gauges with the same logical coordinates.
        gauges = [sqrt(2) * ordered_code[:, index, :] for index in range(2)]
    gauge_space = np.column_stack(gauges)
    close(gauge_space.conj().T @ gauge_space, np.eye(gauge_space.shape[1]))
    projection = gauge_space @ gauge_space.conj().T
    decoded = []
    for operator in kraus:
        close(projection @ operator, operator)
        decoded.extend(gauge.conj().T @ operator for gauge in gauges)
    return decoded


def physical_channel(x, y, rng):
    """Decode all 16 masks from the physical filters at random input and output axes."""
    input_axis = random_unitary(rng)
    output_axis = random_unitary(rng)
    survival = output_axis @ np.diag(np.sqrt([x, y])) @ input_axis
    loss = input_axis.conj().T @ np.diag(np.sqrt([1 - x, 1 - y])) @ input_axis
    p_b, p_e, w0, w1 = channel_weights(x, y)
    pass_weight = 0.0
    erase_effect = np.zeros((2, 2), dtype=complex)
    spin_tags = []
    singlet_projection = np.outer(SINGLET, SINGLET)
    for mask in product((False, True), repeat=4):
        survivors = [index for index, retained in enumerate(mask) if retained]
        losses = [index for index, retained in enumerate(mask) if not retained]
        order = survivors + losses + [4]
        s = len(survivors)
        shape = (2**s, 2 ** len(losses), 2)
        ordered_code = CODE.reshape(2, 2, 2, 2, 2).transpose(order).reshape(shape)
        filtered = kron(*(survival if retained else loss for retained in mask)) @ CODE
        kraus = filtered.reshape(2, 2, 2, 2, 2).transpose(order).reshape(shape)
        kraus = kraus.transpose(1, 0, 2)

        if s >= 3:
            for operator in decoded_identity_kraus(kraus, ordered_code, s):
                scalar = np.trace(operator) / 2
                close(operator, scalar * I)
                pass_weight += abs(scalar) ** 2
        elif s == 2:
            pairing = kron(SINGLET, SINGLET) @ ordered_code.reshape(16, 2)
            logical_singlet = np.outer(pairing, pairing)
            effects = []
            for projection, expected in (
                (singlet_projection, w0 * logical_singlet),
                (np.eye(4) - singlet_projection, w1 * (I - logical_singlet)),
            ):
                effect = sum(operator.conj().T @ projection @ operator for operator in kraus)
                close(effect, expected)
                effects.append(effect.real)
            spin_tags.append(tuple(effects))
        else:
            # A map that sends every traceless Pauli to zero is a replacement map.
            for pauli in PAULI:
                close(sum(operator @ pauli @ operator.conj().T for operator in kraus), 0)
            erase_effect += sum(operator.conj().T @ operator for operator in kraus)

    close(pass_weight, p_b)
    close(erase_effect, p_e * I)
    close(sum(singlet + triplet for singlet, triplet in spin_tags), 3 * (w0 + w1) * I)
    return pass_weight, erase_effect.real, spin_tags


def matrix_sign(operator):
    values, vectors = np.linalg.eigh(operator)
    signs = np.sign(values) * (np.abs(values) > TOLERANCE / 20)
    return (vectors * signs) @ vectors.conj().T


def signed_axis_rotations():
    """Generate the 24 distinct proper signed-axis rotations as qubit unitaries."""
    hadamard = np.array([[1, 1], [1, -1]]) / sqrt(2)
    phase = np.diag([1, 1j])
    seen = {tuple(np.eye(3, dtype=int).flat)}
    rotations = [I]
    for rotation in rotations:
        for generator in (hadamard, phase):
            candidate = rotation @ generator
            action = tuple(
                round((np.trace(pauli @ candidate @ other @ candidate.conj().T) / 2).real)
                for pauli, other in product(PAULI, repeat=2)
            )
            if action not in seen:
                seen.add(action)
                rotations.append(candidate)
    close(len(rotations), 24)
    return tuple(kron(rotation, rotation, rotation) for rotation in rotations)


SIGNED_AXIS_ROTATIONS = signed_axis_rotations()


def joint_gain(strength):
    t = strength
    return (sqrt((1 + t) * (3 - t)) + sqrt((1 - t) * (3 + t))) / 2


def staged_gain(strength):
    a = sqrt(1 - strength**2)
    return sqrt(1 + a + a**2)


def staged_dual(strength, samples):
    """Check a pair-POVM dual bound independently of the six-outcome construction."""
    t = strength
    roots = np.sqrt([1 + t, 1 - t])
    scale = 2 * staged_gain(t)
    tau = 4 / scale
    alpha, delta = 2 * sum(roots) / (scale * roots)
    pair_basis = np.column_stack((TRIPLET_PLUS, TRIPLET_MINUS, SINGLET, TRIPLET_0))
    dual = np.diag([alpha, delta, scale + t**2 * tau, tau])
    dual[2, 3] = dual[3, 2] = -t * tau
    dual = pair_basis @ dual @ pair_basis.T
    for direction in samples:
        constraint = dual - vector_operator(direction, PAIR_CHIRALITY)
        close(np.linalg.eigvalsh(constraint)[0], 0)
    close(np.trace(dual @ kron(I + t * Z, I)), 4 * staged_gain(t))


def staged_observable(strength, rng):
    """Build the six-effect measurement followed by a one-qubit Pauli readout."""
    t = strength
    if t == 1:
        return kron(I, PAIR_CHIRALITY[2] / 2)
    a = sqrt(1 - t**2)
    inverse = kron(np.diag(1 / np.sqrt([1 + t, 1 - t])), I)
    effects, directions = [], []
    for angle, pole in product(np.arange(3) * (2 * np.pi / 3), (-1, 1)):
        u = np.array([sqrt(1 + a) * np.cos(angle), sqrt(1 + a) * np.sin(angle), pole * a])
        v = np.array([-t * u[1] / (1 + a), t * u[0] / (1 + a), t])
        vector = inverse @ (SINGLET + CARTESIAN_TRIPLETS @ (u + 1j * v))
        effects.append(np.outer(vector, vector.conj()) / 6)
        directions.append(u / staged_gain(t))
    close(sum(effects), np.eye(4))
    close([np.linalg.norm(direction) for direction in directions], 1)
    decision = sum(
        kron(effect, vector_operator(direction, PAULI))
        for effect, direction in zip(effects, directions)
    )
    filtered = kron(np.diag(np.sqrt([1 + t, 1 - t])), I, I)
    close(np.trace(decision @ filtered @ CHIRALITY @ filtered), 8 * staged_gain(t))
    np.testing.assert_array_less(np.linalg.norm(decision, ord=2), 1 + TOLERANCE)
    samples = rng.normal(size=(16, 3))
    samples /= np.linalg.norm(samples, axis=1, keepdims=True)
    staged_dual(t, [*samples, *directions])
    return decision


def decision_observables(channel, strength, staged, *, mask_only):
    pass_weight, erase_effect, spin_tags = channel
    if mask_only:
        tags = [singlet + triplet for singlet, triplet in spin_tags]
    else:
        tags = [effect for pair in spin_tags for effect in pair]
    joint = np.zeros((8, 8), dtype=complex)
    classical_gap = np.zeros((8, 8), dtype=complex)
    # The spin-tag effects are real, so Y is perpendicular to all their Bloch axes.
    input_rotation = (I + 1j * X) / sqrt(2) if mask_only else I
    t = strength
    filter_arm = np.diag(np.sqrt([(1 + t) / 2, (1 - t) / 2]))
    for arm_rotation in (I, X):
        rotation = input_rotation @ arm_rotation
        triple_rotation = kron(rotation, rotation, rotation)
        first_filter = rotation @ filter_arm @ rotation.conj().T
        coherent_filter = kron(first_filter, I, I)
        difference = coherent_filter @ CHIRALITY @ coherent_filter
        joint += pass_weight * coherent_filter @ matrix_sign(difference) @ coherent_filter
        rotated = triple_rotation @ staged @ triple_rotation.conj().T
        classical_gap += pass_weight * coherent_filter @ rotated @ coherent_filter
        for effect in [erase_effect, *tags]:
            pullback = first_filter @ effect @ first_filter
            bloch = np.array([np.trace(pullback @ pauli).real for pauli in PAULI])
            remaining = vector_operator(bloch, PAIR_CHIRALITY)
            joint += kron(pullback, matrix_sign(remaining))
            length = np.linalg.norm(bloch)
            if length > TOLERANCE / 20:
                classical_gap += kron(pullback, remaining / (2 * length))
    return joint, classical_gap


def normalized_bias(p_b, p_e, q, x, y, t, gain, *, mask_only):
    flag = sqrt(q**2 * t**2 + (x - y) ** 4 * (1 - t**2)) if mask_only else q
    return p_b * gain(t) + p_e * t + flag


def check_filter(x, y, rng):
    channel = physical_channel(x, y, rng)
    p_b, p_e, w0, w1 = channel_weights(x, y)
    q = 3 * (w0 + w1)
    for t in (0, 0.3, sqrt(0.5), 0.97, 1):
        staged = staged_observable(t, rng)
        for mask_only in (False, True):
            decisions = decision_observables(channel, t, staged, mask_only=mask_only)
            for decision, gain in zip(decisions, (joint_gain, staged_gain)):
                expected = normalized_bias(p_b, p_e, q, x, y, t, gain, mask_only=mask_only)
                # Conjugate the controls and flip their decision, then twirl the inputs.
                odd = (decision - decision.conj()) / 2
                twirled = sum(
                    rotation.conj().T @ odd @ rotation for rotation in SIGNED_AXIS_ROTATIONS
                ) / len(SIGNED_AXIS_ROTATIONS)
                close(twirled, expected * CHIRALITY / 6)


def maximize(objective):
    """Use the concavity of the scalar objective in the squared strength."""
    left, right = 0.0, 1.0
    for _ in range(55):
        low, high = (2 * left + right) / 3, (left + 2 * right) / 3
        if objective(sqrt(low)) < objective(sqrt(high)):
            left = low
        else:
            right = high
    t = sqrt((left + right) / 2)
    return t, objective(t)


def check_example():
    x, y = 0.490, 0.509
    p_b, p_e, w0, w1 = channel_weights(x, y)
    q = 3 * (w0 + w1)
    print(f"At x={x:.3f}, y={y:.3f}: p_B={p_b:.9f}, p_E={p_e:.9f}, q={q:.9f}")
    scores = {}
    for timing, gain in (("joint", joint_gain), ("staged", staged_gain)):
        for mask_only in (False, True):
            def objective(t):
                return normalized_bias(p_b, p_e, q, x, y, t, gain, mask_only=mask_only)

            t, score = maximize(objective)
            scores[timing, mask_only] = score
            flags = "mask only" if mask_only else "spin tag and mask"
            print(f"{timing}, {flags}: coefficient {score:.9f} at t={t:.9f}")
    np.testing.assert_array_less(1, scores["joint", True])
    np.testing.assert_array_less(scores["joint", True], scores["staged", False])
    np.testing.assert_array_less(scores["staged", False], scores["joint", False])
    np.testing.assert_array_less(q + p_b * sqrt(3), 1)
    # This separation does not depend on the numerical maximization.
    witness = normalized_bias(p_b, p_e, q, x, y, sqrt(0.5), staged_gain, mask_only=False)
    joint_mask_upper = 1 + p_b**2 / (4 * (1 - p_b)) + (x - y)**2
    np.testing.assert_array_less(joint_mask_upper, witness)


def main():
    rng = np.random.default_rng(91)
    examples = [
        (0, 0), (1, 1), (0, 1), (0, 0.6), (1, 0.6), (0.5, 0.5),
        (0.490, 0.509), (0.55, 0.42), (0.8, 0.4), (0.1, 0.05),
    ]
    examples.extend(rng.uniform(0, 1, (10, 2)))
    for x, y in examples:
        check_filter(x, y, rng)
    print(
        f"PASS: {len(examples)} filters, all 16 masks per filter, five strengths, "
        "joint and staged observables with and without spin tags."
    )
    check_example()


if __name__ == "__main__":
    main()
