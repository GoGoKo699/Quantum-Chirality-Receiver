# Chirality with a flagged polarization memory

One four-carrier polarization-loss block improves the minimax score of a three-arrival handedness test exactly when both polarization transmissivities are positive. At unequal transmissivities $`x=0.490,\ y=0.509`$, retaining the Schur spin tag gives a staged receiver a higher score than a receiver that keeps every labeled loss mask, discards the tag, and can make a joint final measurement. The link has zero orientation-independent quantum capacity at this spectrum.

## First-gap resources

One product triple arrives in order, one specimen per slot. The three Bloch vectors have an unknown common proper orientation and scalar triple product of magnitude $`d\gt 0`$. The receiver guesses its sign and scores every trial. The first instrument can retain an arbitrary classical record and encode one logical qubit into one fixed four-carrier spin-zero block. The common filter has unknown axes and known squared transmissivities $`x,y`$. All four carriers count, including losses. The fixed Schur decoder finishes by the second arrival, discards the spin gauge, and returns the labeled survival mask. The staged receiver measures any recovered qubit with specimen two and carries a classical record to specimen three. The relaxed receiver may keep those systems through the second gap. The model supplies no quantum bypass, extra specimen, environment access or postselection.

The [source model](model.md) supplies the handedness promise and [converse](converse.md) supplies the rotational prior and singlet–triplet norm identity. The physical channel and the fixed Schur decoder are defined in [Quantum Polarization Loss Coding](https://github.com/GoGoKo699/Quantum-Polarization-Loss-Coding/blob/bb539ea2307da5c17a91d1d9976a99c8521f8fbb/science/schur_receiver.md). Its [capacity theorem](https://github.com/GoGoKo699/Quantum-Polarization-Loss-Coding/blob/bb539ea2307da5c17a91d1d9976a99c8521f8fbb/science/capacity.md) gives the robust quantum capacity threshold.

## Exact scores

Let $`p_B=2xy(x+y)-3x^2y^2`$ be the probability of at least three survivors, $`p_E=2(1-x)(1-y)(2-x-y)-3(1-x)^2(1-y)^2`$ the probability of at most one survivor, and $`q=1-p_B-p_E`$ the probability of exactly two. Set $`a=\sqrt{1-t^2}`$ for $`0\le t\le 1`$. The factors for the recovered quantum branch are

```math
m(t)=\sqrt{1+a+a^2},\qquad
g(t)=\frac{\sqrt{3-t^2+2t}+\sqrt{3-t^2-2t}}{2}.
```

Use $`h=m`$ for a classical second gap and $`h=g`$ for joint access at the final slot. Each score equals $`1/2+dH/12`$. For a lower-bound promise on the magnitude of the scalar triple product, use the promised lower bound as $`d`$.

| Decoder information | Exact coefficient |
|---|---|
| Loss mask and spin tag | $`H=\max_t[p_B h(t)+p_Et+q]`$ |
| Loss mask, with the spin tag discarded | $`H=\max_t[p_B h(t)+p_Et+\sqrt{q^2t^2+(x-y)^4(1-t^2)}]`$ |

The staged tagged score exceeds the immediate-readout coefficient of 1 exactly when $`xy\gt 0`$. Retaining the spin tag strictly improves either timing model when $`0\lt x,y\lt 1`$. For boundary filters, a two-survivor mask already determines the spin outcome whenever that mask has positive probability.

### The unequal-transmissivity example

For $`x=0.490,\ y=0.509`$, one has $`x+y=0.999`$, so the robust quantum capacity is zero. Both decoders receive every labeled survival mask. The extra bit says singlet or triplet when exactly two carriers survive.

| Decision strategy | Coefficient | Correct probability at $`d=1`$ |
|---|---:|---:|
| Immediate first-specimen readout | 1 | 58.3333% |
| Spin tag discarded, classical second gap | 1.0241053 | 58.5342% |
| Spin tag discarded, joint final measurement | 1.0347550 | 58.6230% |
| Spin tag retained, classical second gap | **1.0621340** | **58.8511%** |
| Spin tag retained, joint final measurement | 1.0716898 | 58.9307% |

The strict separation also follows without trusting those numerical maxima. At $`t=1/\sqrt2`$, the staged tagged coefficient exceeds $`1.05963`$. From $`g(t)\le1+\sqrt{1-t}`$ and the bound $`qt+(x-y)^2`$ on the contribution of the masks, the relaxed mask-only coefficient is at most $`1+p_B^2/[4(1-p_B)]+(x-y)^2\lt 1.03566`$. Maximizing the resulting quadratic in $`\sqrt{1-t}`$ gives this upper bound.

## Proof

### The decoded first-gap channel

At least three survivors return the logical qubit by a label-dependent fixed identification, with state-independent branch weights. Zero or one survivor gives state-independent flags. For each two-survivor mask $`S`$, the tag effects are $`w_0P_S`$ and $`w_1(I-P_S)`$, where $`P_S`$ is the logical projector for a product of pair singlets, $`w_0=xy(1-x)(1-y)`$ and $`w_1=w_0+(x-y)^2/3`$. The three pairings have squared overlap $`1/4`$ and each occurs twice. Their Bloch axes lie in the logical $`XZ`$ plane. The three pairings have Bloch inner product $`-1/2`$ and the axes sum to zero. Consequently the twelve rank-at-most-one tag effects sum to $`qI`$, with $`q=3(w_0+w_1)`$. Discarding the tag leaves the mask effect $`w_0P_S+w_1(I-P_S)`$, which retains logical dependence for unequal transmissivities.

The Schur channel identity holds with a reference. The comparison uses the decoded interface after gauge discard. Keeping the gauge or obtaining the spin tag by another physical measurement changes the available outputs.

### Arbitrary first instruments and the mask-only comparison

For equally likely mirror triples with the same Gram matrix, average each sign over common proper rotations. This gives a hypothesis difference $`d\chi/24`$, where $`\chi=\sum_{ijk}\varepsilon_{ijk}\sigma_i\otimes\sigma_j\otimes\sigma_k`$. The resulting Bayes performance bounds the worst-case score from above.

Refine the first record to one Kraus operator per branch. Write that operator as $`K=\sqrt{s(I+tn\cdot\sigma)}\,U`$, where $`s=\mathrm{Tr}(K^\dagger K)/2`$, $`\lVert n\rVert=1`$, and the $`s`$ weights sum to one. Absorb $`U`$ into simultaneous rotations of the later specimens using invariance of $`\chi`$. For a classical effect $`E`$ on the first specimen, the largest decision trace against the corresponding branch of $`\chi`$ is $`4\lVert\mathrm{Tr}(E\sigma)\rVert_2`$ by the singlet–triplet identity. The staged receiver attains it by measuring specimens two and three along two orthogonal axes in the plane perpendicular to the effect's Bloch vector and reporting the signed product.

Each retained spin effect remains rank at most one after filtering, so its Bloch-vector length equals its trace. Those traces sum to $`2sq`$. The pure erasure effects give length $`2sp_Et`$. For a two-survivor mask with tag omitted, put $`\beta=(w_0-w_1)/(w_0+w_1)`$ and write $`P_S=(I+n_S\cdot\sigma)/2`$. If $`q=0`$, this term vanishes. Otherwise, the filtered mask effect has trace $`s(w_0+w_1)(1+\beta t\,n\cdot n_S)`$ and determinant $`s^2(w_0+w_1)^2(1-t^2)(1-\beta^2)/4`$. Its Bloch-vector length is the square root of the squared trace minus four times the determinant. Since $`u\mapsto\sqrt{u^2-k}`$ is concave for $`u\ge\sqrt{k}`$ and $`k\ge0`$, the sum is bounded by its value at the average $`n\cdot n_S=0`$. Equality is attainable with $`n`$ normal to the tag plane. The total normalized mask contribution is $`q\sqrt{\beta^2+(1-\beta^2)t^2}`$, which equals the entry in the table because $`q|\beta|=(x-y)^2`$.

### Optimal staged measurement of the recovered qubit

Rotate the branch axis to $`Z`$ in the measurement description, remove the factor $`s`$, and write $`F=\sqrt{I+tZ_1}`$ on pair one and two. In this pair let $`|s_0\rangle`$ be the real singlet and $`|t_i\rangle=-i(\sigma_i\otimes I)|s_0\rangle`$ its Cartesian triplets. The coefficient $`A_i`$ of the third specimen's Pauli $`\sigma_i`$ in $`\chi`$ equals $`2(|s_0\rangle\langle t_i|+|t_i\rangle\langle s_0|)`$.

Refine the slot-two POVM to rank-one effects. Write each effect after congruence by $`F`$ as a projector on $`\psi_\ell=b_\ell s_0+\sum_i(u_{\ell i}+iv_{\ell i})t_i`$, with $`b_\ell\ge0`$. The vectors include the effect weights. The best last-slot Pauli direction is along $`u_\ell`$, giving contraction $`8b_\ell\lVert u_\ell\rVert`$. The projectors sum to $`I+tZ_1`$, imposing

```math
\begin{aligned}
\sum_\ell b_\ell^2&=1,& \sum_\ell b_\ell v_{\ell z}&=t,\\
\sum_\ell (u_{\ell z}^2+v_{\ell z}^2)&=1,\\
\sum_\ell(\lVert u_{\ell,\perp}\rVert^2+\lVert v_{\ell,\perp}\rVert^2)&=2,\\
\sum_\ell(u_{\ell x}v_{\ell y}-u_{\ell y}v_{\ell x})&=t.
\end{aligned}
```

Cauchy–Schwarz gives $`\sum_\ell v_{\ell z}^2\ge t^2`$. For $`V=\sum_\ell\lVert v_{\ell,\perp}\rVert^2`$, the last identity similarly gives $`V(2-V)\ge t^2`$ and hence $`V\ge1-a`$. It follows that $`\sum_\ell\lVert u_\ell\rVert^2\le 2-t^2+a`$. A further Cauchy–Schwarz bounds the normalized contraction by $`m(t)`$.

For attainment at $`t\lt 1`$, take three equally spaced angles $`\phi`$ and both signs independently, and form the six vectors $`\psi=s_0+\sum_i(u_i+iv_i)t_i`$ using

```math
\begin{aligned}
u&=(\sqrt{1+a}\cos\phi,\sqrt{1+a}\sin\phi,\pm a),\\
v&=(-\kappa u_y,\kappa u_x,t),\qquad \kappa=\frac{t}{1+a}.
\end{aligned}
```

The average of their projectors is $`I+tZ_1`$, and each $`u`$ has length $`m(t)`$. Use effects $`F^{-1}|\psi\rangle\langle\psi|F^{-1}/6`$ in slot two and measure the third along the corresponding $`u`$. At $`t=1`$, direct first-specimen readout attains the endpoint. The relaxed receiver reaches $`g(t)`$ by the [singlet–triplet trace-norm identity](converse.md#the-singlet-and-triplet-blocks), applied to the coherent branch with an ideal qubit channel. Its optimum may require storing both the recovered qubit and specimen two through the second gap.

For each first outcome, add its coherent, erasure, and two-survivor contributions and multiply by its weight $`s`$. The weights sum to one, so their average is bounded by the maximum of the single-strength coefficient in the table. A normalized coefficient $`H`$ gives a decision trace $`\mathrm{Tr}(D\chi)=8H`$. Against the twirled difference $`d\chi/24`$, this means success probability $`1/2+dH/12`$.

### Pointwise attainment and thresholds

Use two first outcomes with effects $`(I\pm tn\cdot\sigma)/2`$, both at the maximizing strength, and condition the later measurements on the outcome. For the mask-only receiver, both axes are normal to the tag plane. Each retained tag and erasure branch uses the staged classical rule. Mix the resulting protocol with its complex-conjugate controls and flip the latter's reported sign. The real logical channel allows this operation on the apparatus. It does not require conjugating an unknown specimen. Apply a common uniformly random proper signed-axis permutation to the three specimens as they arrive. The resulting binary decision observable is $`H\chi/6`$. The signed-axis twirl removes the one-body terms, the sign-flipped conjugation removes the rotation-invariant even terms, and the only invariant three-body component is $`\chi`$. This converts Bayes attainment into pointwise attainment.

At $`t=1`$, each decision class achieves the classical value. If $`p_B\gt 0`$, moving slightly below 1 increases the quantum contribution by order $`\sqrt{1-t}`$ at a classical cost of order $`1-t`$. If $`p_B=0`$, all accessible first-gap outputs are classical. The formula for $`p_B`$ gives $`p_B\gt 0`$ exactly when $`xy\gt 0`$. In fact, when $`xy=0`$ each physical filter channel is entanglement breaking, since its surviving polarization ray is fixed and its other output is an erasure flag. This rules out a gain from alternative block encodings for that boundary, while the exact score formulas concern the fixed Schur interface.

In the interior, a mask-only optimizer has strength below 1 and its mask contribution is strictly less than $`q`$. Evaluating the tagged strategy at that same strength proves strict tag utility with equal gap resources. Maximizers can be found by a scalar search. For $`0\lt t\lt 1`$, $`g(t)\gt m(t)`$, so relaxing the second gap can increase the score.

## Related work and checks

The ingredients include rotation twirling and multiplicity encodings, exact logical recovery after one carrier is lost, and polarization-dependent erasure. Joint measurements of scalar chirality and weak instruments before noisy storage address different timing or source models. The new decision theorem optimizes the first instrument and the staged readout at the decoded Schur interface, while holding the labeled survival masks fixed in the tag comparison. [Related work](../references/RELATED_WORK.md#polarization-loss-and-spin-tags)

The [matrix verifier](../verification/verify_flagged_polarization.py) checks the decoded branches, staged readout, and score comparison. The [reading bridge](../learning/BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) connects the twirling and spin decompositions to the review literature.
