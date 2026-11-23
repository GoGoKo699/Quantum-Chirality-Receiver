# Reproduce the matrix checks

From the repository root, install NumPy in a Python 3 environment and run the verifier.

```sh
python -m pip install -r verification/requirements.txt
python verification/verify.py
```

The fixed-seed script checks these identities in matrices of size 2, 4, and 8.

- The first three tensor moments of the 24 proper signed-axis rotations with integer arithmetic. These reproduce the Haar twirl for product triples of Bloch vectors. The matrix checks also establish the chirality polynomial $`\chi^3=12\chi`$ and traces $`\mathrm{tr}\chi=0`$ and $`\mathrm{tr}\chi^2=48`$.
- The classical Pauli receiver and the conditional trace norm for sample first-slot effects. The equal-fidelity example independently checks that two idealized channels at average fidelity $`3/4`$ fall on opposite sides of the threshold.
- The unital converse with 1,944 Kraus branches, including the endpoints and random partial measurements, across 648 channel spectra in rotated frames. The spectral samples come from fixed boundary cases and a reproducible set of Pauli-channel mixtures.
- Both parity choices of the Bell measurement, its rank-one projectors, and the weighted final-spin measurement. The cyclic pullback is checked for each of the 647 nonzero channel spectra.
- The staged amplitude-damping lower bound by direct pullback of the branch-conditioned readout and explicit common input rotations. It also checks sample cases of the later-joint-access construction that beats the classical benchmark.

The [scientific account](../science/README.md) gives the analytic arguments for the full parameter ranges. The finite floating-point checks use a tolerance of $`10^{-11}`$.
