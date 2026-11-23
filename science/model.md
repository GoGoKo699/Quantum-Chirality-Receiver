# The handedness decision

The source supplies three independently prepared qubits with Bloch vectors $`r_1,r_2,r_3`$. They arrive in that order, one per slot. The source and receiver frames differ by an unknown common proper rotation. The receiver decides the sign of the ordered volume $`v=r_1\cdot(r_2\times r_3)`$. A common proper rotation preserves this volume, and a mirror transformation reverses its sign. Here handedness refers to the orientation of the Bloch vectors.

## Source and operations

Write $`\rho(r)=(I+r\cdot\sigma)/2`$, with $`\sigma=(X,Y,Z)`$ and $`\|r\|_2\leq 1`$. The joint input is the product $`\rho(r_1)\otimes\rho(r_2)\otimes\rho(r_3)`$. Each specimen becomes available only in its arrival slot. The receiver has a stable local frame, one specimen per slot, free classical randomness and records, and fresh local ancillas within a slot. The model supplies neither additional source specimens nor preshared entanglement.

Across the first gap, all retained quantum information passes through at most one use of the specified, calibrated qubit memory channel. The first-stage instrument may depend on classical randomness and produce a classical outcome. The channel and within-slot operations are fixed in the receiver's frame. All within-slot operations and the subsequent readout are ideal in the model. The theorem permits unlimited coherent storage across the second gap in its upper bound. An attaining receiver uses only classical records there.

The unital memory channel $`\mathcal N`$ has real Bloch matrix $`T`$, defined by

```math
\mathcal N(\rho(r))=\rho(Tr).
```

The receiver knows $`T`$ and can implement local rotations in the trusted frame. The analyst may fix $`|v|=d>0`$, or impose just a lower bound $`|v|\geq\delta>0`$. A strategy's score is its smallest probability of reporting the correct sign over all eligible triples. The upper bound already holds with two matched-Gram mirror alternatives and an unknown proper orientation of each. Their Bloch lengths and pairwise inner products agree. The alternative sign and frame are unavailable to the receiver.

## Exact result for unital memory

For fixed magnitude $`d`$, the optimal score is

```math
P^\star(d,T)=\frac12+\frac d{12}\max\{1,\|T\|_F\},
\qquad
\|T\|_F^2=\operatorname{Tr}(T^\mathsf T T).
```

The score holds pointwise for the attaining receiver, so a lower-bound promise has value $`P^\star(\delta,T)`$. Immediate Pauli readout achieves the value when $`\|T\|_F\leq1`$. For $`\|T\|_F>1`$, the receiver carries the first qubit across the first gap, makes a Bell measurement when the second qubit arrives, and uses the classical result to choose a one-qubit measurement on the third. The weighted measurement settings depend only on $`T`$.

If the first gap carries only a classical record, the best score is $`1/2+d/12`$ even with unlimited later quantum storage. A noiseless first-gap qubit gives $`1/2+d/(4\sqrt3)`$, which equals the optimum when all three specimens are available for one joint measurement.

## A decision observable

For a binary measurement with outcomes $`+1,-1`$ and effects $`E_+,E_-`$, write the difference of effects as $`D=E_+-E_-`$. Its expected decision is $`\operatorname{Tr}(D\rho)`$. Define the scalar-chirality observable in the Pauli convention

```math
\chi=\sum_{i,j,k\in\{x,y,z\}}\varepsilon_{ijk}\,
\sigma_i\otimes\sigma_j\otimes\sigma_k.
```

Its product-state expectation is the signed volume $`v`$. The exact receivers realize observables proportional to $`\chi`$ on the original input. For $`D=\alpha\chi`$, their probability of a correct decision is $`(1+\alpha|v|)/2`$ at each eligible triple. In the spin-operator convention $`S=\sigma/2`$, the conventional scalar-spin-chirality observable is $`\chi/8`$. See [related work](../references/RELATED_WORK.md) for the known spectral and measurement identities.

The [converse](converse.md) derives the upper bound over quantum instruments. The [receiver](receiver.md) gives the attaining measurements, settings, and timing. The [channel examples](memory-channels.md) interpret the threshold and exhibit a weak-measurement protocol for amplitude damping.
