# Scientific account

The receiver estimates one bit from an ordered stream of three qubits. A calibrated unital memory across the first arrival gap improves the worst-case score exactly when the Frobenius norm of its Bloch matrix exceeds one. One Bell measurement at the second arrival and one local measurement at the third attain the optimum.

| Read | Result |
|---|---|
| [Model and theorem](model.md) | Source promises, causal access, score, and the exact unital result |
| [Instrument converse](converse.md) | Rotational prior, singlet-triplet blocks, and the bound over arbitrary first measurements |
| [Staged receiver](receiver.md) | Immediate Pauli strategy, weighted Bell circuit, and channel-axis symmetrization |
| [Memory channels](memory-channels.md) | Unitarity, same-fidelity examples, and a zero-second-gap amplitude-damping extension |
| [Flagged polarization memory](flagged-polarization-memory.md) | One four-carrier block, optimal staged receiver and exact spin-tag comparison |
| [Related work](../references/RELATED_WORK.md) | Attribution and problem comparisons |
| [Verification](../verification/README.md) | Reproduction of operator identities and numerical checks |

The unital theorem assumes an exactly known, fixed memory map and ideal receiver operations. The amplitude-damping construction gives an achievable score and establishes a region where a weak first measurement improves on both endpoints.


The [flagged-memory result](flagged-polarization-memory.md) assumes known transmissivities, unknown filter axes shared within the block, and a fixed spin-zero encoder and Schur decoder. Its comparison keeps every labeled survival mask in both receivers.
