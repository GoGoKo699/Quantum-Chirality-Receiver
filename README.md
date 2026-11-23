# Quantum Chirality Receiver

**How much quantum memory does a receiver need to tell whether three arriving qubits form a right-handed or left-handed Bloch triad?**

The source sends one specimen of each qubit in order. Their Bloch vectors share an unknown orientation. The receiver reports the sign of their scalar triple product. For absolute volume $`d\gt 0`$ and a calibrated unital qubit memory with Bloch matrix $`T`$, the exact worst-case success probability is

```math
P^\star(d,T)=\frac12+\frac d{12}\max\{1,\lVert T\rVert_F\}.
```

The decision uses one pass through the source. If the channel crosses the threshold $`\lVert T\rVert_F\gt 1`$, store the first qubit, make a Bell measurement when the second arrives, then use its outcome to choose how to measure the third. Only a classical record spans the second gap. If the first gap carries just a classical record, later quantum storage cannot improve the score.

| Receiver or memory | Supported result |
|---|---|
| Classical record across the first gap | Optimum $`1/2+d/12`$, even with unrestricted later storage |
| Ideal first-gap qubit | Joint-measurement optimum $`1/2+d/(4\sqrt3)`$ |
| Depolarizing first-gap qubit | Strict gain at visibility above $`1/\sqrt3`$ |
| Calibrated unital qubit memory | Strict gain exactly when channel unitarity exceeds $`1/3`$ |
| Amplitude damping | A staged weak-measurement receiver beats both immediate readout and plain storage for survival $`1/3\lt \eta\lt 1`$ |

The [channel examples](science/memory-channels.md) give two memories with the same average fidelity and different decision scores. The [amplitude-damping construction](science/memory-channels.md#amplitude-damping-rewards-a-weak-first-measurement) is an achievable result for one nonunital family. Its optimum over all instruments is open.

## Polarization loss across the first gap

A four-carrier spin-zero memory gives a second exact result. If both polarization transmissivities are positive, a weak first measurement and a staged receiver improve on the classical-first-gap score. At transmissivities $`(x,y)=(0.490,0.509)`$, retaining the two-survivor spin tag beats a receiver that retains every loss mask and may measure jointly in the last slot. The link has zero robust quantum capacity at that spectrum. [Decision theorem](science/flagged-polarization-memory.md) · [Quantum Polarization Loss Coding](https://github.com/GoGoKo699/Quantum-Polarization-Loss-Coding)

## Read the science

| Start here | What it covers |
|---|---|
| [Source and theorem](science/model.md) | The unknown frame, decision task and allowed memory |
| [Receiver](science/receiver.md) | The two Bell settings and one-qubit feed-forward |
| [Converse](science/converse.md) | The minimax bound for arbitrary first-slot instruments |
| [Flagged polarization memory](science/flagged-polarization-memory.md) | Exact staged optimum and the value of the two-survivor spin tag |
| [Related work](references/RELATED_WORK.md) | Prior chirality measurements, noisy storage, and channel unitarity |

## Learn the framework

The [learning route](learning/README.md) uses Bartlett, Rudolph and Spekkens's *Reference frames, superselection rules, and quantum information* (2007). The [source bridge](learning/BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) and [30 milestones](learning/MILESTONES.md) connect collective rotations and spin multiplicity to the receiver.

## Reproduce the checks

```sh
python -m pip install -r verification/requirements.txt
python verification/verify.py
python verification/verify_flagged_polarization.py
```

The [verification guide](verification/README.md) describes the finite matrix checks. The [proofs](science/README.md) establish the claims across the stated parameter ranges. The unital-memory theorem assumes a calibrated map. The polarization-memory theorem assumes one common filter with known transmissivities inside a block, with unknown axes. Both assume ideal local operations.

## Purpose and contact

This repository serves as a record of the work and a guide for the author's self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
