# A receiver that uses one Bell measurement

The receiver consumes each specimen once. When the memory provides a gain, the receiver retains one qubit across the first gap and releases all quantum information at the second arrival. The last specimen is measured locally using settings computed from the Bell outcome.

## Receiver with no coherent storage

Choose one of the six ordered permutations $`(i,j,k)`$ of $`(x,y,z)`$ uniformly before the first arrival. Measure $`\sigma_i,\sigma_j,\sigma_k`$ as the corresponding qubits arrive. Report the product of the three signs times $`\varepsilon_{ijk}`$. The decision observable is $`\chi/6`$ because each term occurs with probability one sixth. Its correct-decision probability at magnitude $`d`$ is $`1/2+d/12`$.

## A weighted Pauli measurement via two Bell settings

For a nonzero real weight vector $`w=(w_x,w_y,w_z)`$, define

```math
\chi_w=\sum_{i,j,k}\varepsilon_{ijk}w_i\,
\sigma_i\otimes\sigma_j\otimes\sigma_k.
```

The following receiver implements $`\chi_w/(2\lVert w\rVert_2)`$ as a binary decision observable on its measurement inputs, where the first input to this measurement is the first qubit after storage.

1. Independently select parity $`p\in\{+1,-1\}`$ with equal probabilities. For the three permutations satisfying $`\varepsilon_{ijk}=p`$, jointly measure the three operators $`\sigma_i\otimes\sigma_j`$ on the first and second registers. Write their outcomes as $`s_{ij}\in\{+1,-1\}`$.
2. On arrival of the third qubit, measure the one-qubit observable

```math
B_{p,s}=\frac{p}{\lVert w\rVert_2}
\sum_{(i,j,k):\,\varepsilon_{ijk}=p}s_{ij}w_i\sigma_k .
```

3. Report that measurement's sign. Each of the three output axes $`k`$ appears exactly once. Thus $`B_{p,s}^2=I`$ for every Bell outcome.

In step 1 the three pair observables commute. The product of any two is minus the third, so the joint measurement is a four-outcome projective measurement. They are the usual Bell observables $`X\otimes X,Y\otimes Y,Z\otimes Z`$ in rotated axes. A cyclic Pauli-axis rotation on the second qubit aligns the axes. The usual Bell circuit then uses a CNOT from the first qubit to the second, a Hadamard on the first, and two computational-basis measurements. This reads $`X\otimes X`$ and $`Z\otimes Z`$, with $`Y\otimes Y`$ obtained from their negative product. Afterward only the parity and two signs are retained.

If $`P_s`$ are the Bell projectors for the chosen parity, then $`\sum_s s_{ij}P_s=\sigma_i\otimes\sigma_j`$. Substituting into $`\sum_s P_s\otimes B_{p,s}`$ and averaging over the two settings gives $`\chi_w/(2\lVert w\rVert_2)`$. This identity holds on all three-qubit states, regardless of the unknown source orientation.

## Match the receiver to a unital memory

A signed singular-value decomposition of the known Bloch matrix has the form

```math
R^{\mathsf T} T S=\mathrm{diag}(\mu_x,\mu_y,\mu_z),
\qquad R,S\in SO(3).
```

Allowing signed entries $`\mu_i`$ keeps both coordinate changes proper. Implementing $`S`$ before storage and $`R^{\mathsf T}`$ after storage realizes the diagonal map. The second rotation can be part of the Bell measurement. Put $`F=\sum_i\mu_i^2`$. When $`F>1`$, choose weights $`w_i=\mu_i`$. In the Heisenberg representation the effective diagonal channel maps $`\sigma_i`$ to $`\mu_i\sigma_i`$, so the observable on the source inputs is $`\chi_{\mu^2}/(2\sqrt F)`$, where $`(\mu^2)_i=\mu_i^2`$.

The receiver uses the three cyclic placements of these axes with equal probabilities. If $`C`$ is a cyclic permutation matrix and $`a\in\{0,1,2\}`$ is the choice, use $`S C^a`$ before storage and $`C^{-a} R^{\mathsf T}`$ after storage. The effective diagonal entries and the weights are permuted together. Each coefficient of $`\chi_w`$ then averages to the same value, giving

```math
D=\frac{\sqrt F}{6}\chi .
```

This is a pointwise symmetrization of the decision observable. It uses three choices of channel orientation, a parity coin, one Bell circuit, and a final one-qubit measurement. On each run the channel still acts once on a single qubit. The retained data after the second slot are entirely classical.

| Time | Quantum operation | Information retained at the next gap |
|---|---|---|
| First arrival | Rotate the first specimen and send it through the calibrated memory | One qubit and the chosen settings |
| Second arrival | Read the memory output and second specimen in the prescribed Bell basis | Bell outcome and settings |
| Third arrival | Measure the one-qubit observable specified by the Bell outcome | Decision sign |

For $`F\leq1`$ use the immediate-readout receiver. Together with the [instrument converse](converse.md), the two choices establish the [exact minimax value](model.md).

