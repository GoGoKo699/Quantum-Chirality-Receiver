# From Watrous to the chirality receiver

The receiver has three arrival slots and a one-qubit memory available in the first gap. It must infer the sign of the volume spanned by three Bloch vectors, which represent the input qubit states. Each run supplies one copy of each state. The source's common orientation is unknown, and the receiver uses its own calibrated axes.

The educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018**. Section numbers below follow the author's 2018 manuscript. The targeted reading uses one textbook, with the receiver-specific symmetry, timing model, and protocol developed in the [scientific account](../science/README.md). See the [author's manuscript page](https://cs.uwaterloo.ca/~watrous/TQI/) and the [publisher's contents](https://doi.org/10.1017/9781316848142).

## Targeted reading

| Read in Watrous | Use here |
|---|---|
| [§§1.1.2–1.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) | Tensor products, positive operators, singular values, and the trace and Frobenius norms. A trace norm measures distinguishability; a Frobenius norm summarizes the three memory gains. |
| [§2.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Density operators and composition of registers. Express one qubit in the Pauli basis and represent the ordered triple by a tensor product. |
| [§§2.2.1–2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Completely positive maps, channels, and Kraus operators. Represent both a noisy memory and the quantum output accompanying a classical measurement result. |
| [§§2.3.1–2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Effects, projective measurements, and outcome probabilities. Interpret a Bell measurement and follow its outcome into the last measurement. |
| [§3.1.1, Theorem 3.4](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | The Holevo–Helstrom formula for binary state discrimination. Apply it to the two orientation-averaged states and later to the channel outputs labeled by classical records. |
| [§4.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf) | Weyl-covariant channels, which supply Pauli-channel examples in dimension two. Use the receiver analysis to evaluate what each channel preserves across the first gap. |
| [§7.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) | Haar measure as a rotation-invariant average. Use the same proper rotation on all three vectors in the converse. |

The first pass uses the state and measurement readings in Chapter 2 and the binary-discrimination theorem in Chapter 3. The other sections support particular steps in the [milestone map](MILESTONES.md).

## Objects and notation

| Textbook object | Receiver notation and meaning |
|---|---|
| A state $`\rho\in\mathrm D(\mathcal X)`$ | A positive, trace-one matrix. Here $`\rho_j=(I+r_j\cdot\sigma)/2`$ represents input $`j`$ and $`r_j\in\mathbb R^3`$ is its Bloch vector. |
| A composite state on $`\mathcal X\otimes\mathcal Y`$ | The full input is $`\rho_1\otimes\rho_2\otimes\rho_3`$. The factor labels are arrival slots. |
| A measurement effect $`\mu(a)`$ | A positive operator $`E_a`$ whose trace pairing with the state is the probability of outcome $`a`$. Retaining a quantum system after the measurement additionally requires a branch map. |
| A channel $`\Phi`$ | The first-gap memory $`\mathcal N`$. For unital memory, $`\mathcal N(I)=I`$ and the Bloch action is $`r\mapsto Tr`$ with a real $`3\times3`$ matrix $`T`$. |
| $`\lVert A\rVert_1`$ and $`\lVert A\rVert_2`$ | The trace norm of an operator and the Frobenius norm, respectively. Write $`\lVert T\rVert_F`$ for the Frobenius norm of the real Bloch matrix. |
| Two hypotheses of prior weight $`\lambda`$ and $`1-\lambda`$ | Equal-weight chirality alternatives of determinant signs $`+1`$ and $`-1`$ when evaluating the average upper bound. The receiver achieves the same guarantee for either sign and every allowed orientation. |

The volume is $`\det[r_1,r_2,r_3]`$, with the vectors in arrival order as columns. Write $`d`$ for its magnitude. A common proper rotation preserves the determinant. Exchanging the first two input labels reverses it. This is a property of the ordered Bloch vectors, with each component defined by a Pauli expectation.

## A complete first example

Suppose the three Bloch vectors form an orthonormal frame, so $`d=1`$, and the memory is ideal. A receiver with only classical storage chooses one of the six ordered permutations $`(i,j,k)`$ of the lab's $`x,y,z`$ axes. It measures the specified axis at each arrival. Its returned sign is the product of the three outcomes times the parity of the permutation. The sign has expectation $`\det[r_1,r_2,r_3]/6`$ by the determinant expansion. Therefore the success probability is $`1/2+1/12=7/12`$, for any orientation.

Now let the receiver keep the first qubit until the second arrives. Choose an even or odd permutation class with equal probability. The three pair observables in either class commute, so a single Bell-basis measurement gives their joint signs. For the even class these observables are $`X_1Y_2`$, $`Y_1Z_2`$ and $`Z_1X_2`$. On the third arrival, measure a spin component along the unit vector whose coordinates are specified by those signs. For example, if the three listed pair outcomes are $`(+1,+1,-1)`$, measure $`(X_3-Y_3+Z_3)/\sqrt3`$. Reverse the final sign after an odd-class measurement. The pair is gone by this stage and its two independent signs are available as classical data.

For the ideal memory, let

```math
\chi = \sum_{i,j,k}\epsilon_{ijk}\,\sigma_i\otimes\sigma_j\otimes\sigma_k.
```

The resulting binary measurement has sign observable $`\chi/(2\sqrt3)`$. Its expectation is $`\det[r_1,r_2,r_3]/(2\sqrt3)`$, so the success probability is $`1/2+1/(4\sqrt3)\simeq0.6443`$. The [receiver construction](../science/receiver.md) derives the observable directly from the two Bell settings. It also explains how to coordinate axis weights and memory rotations under known anisotropic noise.

## From the example to an exact limit

Watrous's binary-discrimination theorem says that two equal-prior states $`\rho_+,\rho_-`$ can be distinguished with probability at most $`1/2+\lVert \rho_+-\rho_-\rVert_1/4`$. Average each of the two mirror alternatives over their common proper rotation. The one- and two-body terms cancel in their difference, since mirrors have the same pairwise dot products. The leading sign is carried by the third-order term. Its average is proportional to $`\chi`$.

This yields a bound even when the receiver takes arbitrary actions before the first gap. The proof tracks each first-slot branch through the memory, keeps its classical label, and grants the receiver a joint measurement on all remaining registers. On the lower-bound side, the Bell receiver needs only the first-gap memory and the classical outcome of the pair measurement. Their agreement gives

```math
P^\star(d,T)=\frac12+\frac{d}{12}\max\{1,\lVert T\rVert_F\}.
```

Thus the memory improves the one-shot success probability precisely when $`\lVert T\rVert_F>1`$. For a depolarizing memory $`T=vI_3`$, the threshold is $`v>1/\sqrt3`$. For a general unital memory, the cost of waiting is summarized by the lengths of the three transformed axes. The [converse](../science/converse.md) and [channel examples](../science/memory-channels.md) give the complete derivation and operating assumptions.

