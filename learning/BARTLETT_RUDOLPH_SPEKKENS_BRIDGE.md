# From rotation symmetry to a staged chirality decision

The source for the learning route is Stephen D. Bartlett, Terry Rudolph and Robert W. Spekkens, *Reference frames, superselection rules, and quantum information*, Reviews of Modern Physics 79, 555–609 (2007). The section numbers below refer to the published review and its open version. [Published review](https://doi.org/10.1103/RevModPhys.79.555) · [Open v3 text](https://arxiv.org/pdf/quant-ph/0610030v3)

The receiver sees three ordered qubits one at a time. It decides whether their Bloch vectors form a right- or left-handed triad. The source orientation is unknown. In the flagged-memory experiment, the polarization filter also has unknown axes. Collective rotations enter twice, in the hypothesis average and in the loss code.

## Reading the review

| Review section | Use in the receiver |
|---|---|
| § II.C, especially Eq. (2.14) and Theorem 1 | Average over an unknown rotation. An invariant effect depends on the twirled state. The [converse](../science/converse.md#a-rotational-prior) uses this to isolate the handedness component of mirror triples. |
| §§ III.A.2(b–d) | Distinguish a spin representation from its multiplicity. The [flagged-memory decoder](../science/flagged-polarization-memory.md#the-decoded-first-gap-channel) retains information from multiplicities and discards the spin gauge. |
| § III.B, especially Eq. (3.24) | Read a real pair-coupled basis for four spins. A two-survivor tag distinguishes a product of singlets from a singlet formed out of triplets. |
| § VI.A.2 | Interpret joint observables that encode relative information. In this problem the scalar triple product changes sign under a mirror, while every pairwise overlap stays fixed. |

The review supplies the symmetry tools. The score and the measurement sequence follow from the [unital proof](../science/README.md) and the [flagged-memory proof](../science/flagged-polarization-memory.md).

## Two mirror triples

Take ordered unit Bloch vectors $`(e_x,e_y,e_z)`$ and $`(e_x,e_y,-e_z)`$. They have volumes $`+1`$ and $`-1`$, and each pair of distinct vectors is orthogonal. A proper rotation leaves the volume invariant. To recover the sign, the classical receiver chooses one of the six ordered permutations of the three axes uniformly, measures in sequence, and reports the product of the measured signs times the permutation parity. For the listed orientations, one setting reveals the sign with certainty and the others give fair decisions. The score is $`1/2+1/12`$. The [staged Bell receiver](../science/receiver.md) improves this score with ideal storage before the second arrival.

## Two survivors and one classical bit

For the filter with transmissivities $`x=0.490`$ and $`y=0.509`$, every run uses four carriers to try to retain the first specimen. When two carriers survive, the decoder can read their spin. With the survival mask fixed, the singlet and triplet tags reveal two rank-one logical effects. If only the mask is retained, the two effects are summed. The sum can still provide partial information because the filter is anisotropic.

The [exact scores](../science/flagged-polarization-memory.md#the-unequal-transmissivity-example) show that the tagged receiver with a classical second gap succeeds more often than a mask-only receiver that can make a joint final measurement. The quantum capacity of the link is zero at this spectrum. Compare this finite decision, which accepts every trial and asks for one bit, to a communication task that must preserve arbitrary input qubits with fidelity approaching one.

Continue through the [30 milestones](MILESTONES.md). Work from [M10](MILESTONES.md#m10-averaging-a-common-rotation) and [M24](MILESTONES.md#m24-the-singlet-and-triplet-blocks) to [M27](MILESTONES.md#m27-interpreting-the-threshold), [M28](MILESTONES.md#m28-the-storage-schedule), and [M30](MILESTONES.md#m30-the-complete-result).
