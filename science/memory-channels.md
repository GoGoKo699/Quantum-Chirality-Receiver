# Which memory channels help?

For a known unital qubit memory, usefulness is determined by the squared Frobenius norm $`F=\|T\|_F^2`$. The threshold is strict: coherent storage improves the score exactly when $`F>1`$.

## Depolarization, dephasing, and unitarity

A depolarizing memory with Bloch visibility $`v`$ has $`T=vI_3`$ and $`F=3v^2`$. Its visibility must exceed $`1/\sqrt3`$ for a gain. A dephasing memory with protected $`X`$ axis and transverse visibility $`v`$ has $`T=\operatorname{diag}(1,v,v)`$. Its $`F=1+2v^2`$ gives a gain for any positive transverse visibility. Complete dephasing lies at the threshold.

For a unital qubit channel, the standard channel unitarity is $`u(\mathcal N)=F/3`$. This follows by averaging $`\|Tr\|_2^2`$ over unit Bloch vectors. The exact receiver criterion is therefore $`u(\mathcal N)>1/3`$. The average fidelity to the identity is $`1/2+\operatorname{Tr}(T)/6`$. The table evaluates two channels with the same average fidelity and different optimal decisions.

| Memory map in Bloch coordinates | Average fidelity | Squared Frobenius norm | Optimal success at magnitude $`d`$ |
|---|---:|---:|---:|
| $`\operatorname{diag}(1/2,1/2,1/2)`$ | $`3/4`$ | $`3/4`$ | $`1/2+d/12`$ |
| $`\operatorname{diag}(1,1/4,1/4)`$ | $`3/4`$ | $`9/8`$ | $`1/2+(d/12)\sqrt{9/8}`$ |

Unitarity diagnoses usefulness in this model. Constructing the attaining receiver also uses the signed principal weights and axes of the memory map. See [related work](../references/RELATED_WORK.md) for the benchmarking definition.

## Amplitude damping rewards a weak first measurement

Unitality removes affine offsets from the Pauli blocks in the [converse](converse.md). In a nonunital memory the affine term can interact with information gained at the first arrival. Consider amplitude damping with survival probability $`\eta\in[0,1]`$. Its Bloch action is $`r\mapsto Tr+c e_z`$, where $`T=\operatorname{diag}(\sqrt\eta,\sqrt\eta,\eta)`$ and $`c=1-\eta`$.

For strength $`t\in[0,1]`$, first apply the two-outcome instrument

```math
K_+=P,\quad K_-=P X,\qquad P=\sqrt{(I+t Z)/2}.
```

The effects sum to identity because $`XZX=-Z`$. Send the resulting qubit through the damping channel. In the negative branch apply $`X`$ to each subsequent specimen at its arrival. On the pair and then the final qubit, apply the [weighted Bell receiver](receiver.md#a-weighted-pauli-measurement-via-two-bell-settings) with

```math
w=\left(\sqrt{\eta(1-t^2)},\sqrt{\eta(1-t^2)},\eta+ct\right),
\qquad
F_\eta(t)=\|w\|_2^2=2\eta(1-t^2)+(\eta+ct)^2 .
```

Take any $`t,\eta`$ with $`F_\eta(t)>0`$ for this implementation. The positive branch's measurement difference pulls back through the channel and the filter as

```math
D_+=\frac{\chi_{w^2}+ w_z(c+\eta t)I\otimes A_z}
{4\sqrt{F_\eta(t)}}.
```

Indeed, the channel adjoint maps $`X,Y`$ to $`\sqrt\eta X,\sqrt\eta Y`$ and maps $`Z`$ to $`\eta Z+cI`$. The filter multiplies the first two by $`\sqrt{1-t^2}/2`$ and gives $`P(\eta Z+cI)P=[(\eta+ct)Z+(c+\eta t)I]/2`$. The negative branch is conjugation of $`D_+`$ by $`X^{\otimes3}`$. This preserves the diagonal weighted chirality and flips $`I\otimes A_z`$, so the affine terms cancel when the two effects are summed. Uniformly apply one of the three common cyclic axis rotations to all three inputs as they arrive. The averaged decision observable on the original inputs is

```math
D=\frac{\sqrt{F_\eta(t)}}{6}\chi .
```

The implementation carries one channel qubit across the first gap and no quantum register across the second. Its pointwise success at magnitude $`d`$ is $`1/2+d\sqrt{F_\eta(t)}/12`$.

At $`t=1`$ the protocol has $`F_\eta(1)=1`$, the classical score. At $`t=0`$ it has $`F_\eta(0)=2\eta+\eta^2`$. This last value determines the optimal score for storage with no state-dependent first outcome: the affine offset acts on the identity and drops out of the twirled difference $`\Delta`$. If first-slot preprocessing has Bloch linear part $`S`$, its contraction property gives $`\|TS\|_F\leq\|T\|_F`$. The singlet-triplet norm calculation with no first-slot outcome then gives the upper bound $`1/2+d\|T\|_F/12`$. The $`t=0`$ receiver attains it with input-independent axis choices and feed-forward.

For $`1/3<\eta<1`$, maximizing this family gives

```math
t_\star=\frac{\eta(1-\eta)}{2\eta-(1-\eta)^2}\in(0,1),
\qquad
F_\eta(t_\star)=1+\frac{(3\eta-1)^2}{2\eta-(1-\eta)^2}.
```

The expression is a strictly concave quadratic in $`t`$ over this range. Its interior maximum is larger than both endpoint scores. For example, at $`\eta=2/5`$, the best no-outcome storage has $`F_\eta(0)=24/25`$, while the staged weak-measurement receiver reaches $`F_\eta(6/11)=12/11`$. For $`\eta\leq1/3`$, this family reaches its maximum $`1`$ at the classical endpoint. To see the boundary, factor $`F_\eta(t)-1=(1-t)[(2\eta-(1-\eta)^2)t+2\eta+\eta^2-1]`$. The bracket is nonpositive throughout $`[0,1]`$ in that survival range.

These formulas establish an achievable family for amplitude damping, including a strict advantage over both endpoints.

## Allowing coherent storage across the second gap

The same first instrument gives a stronger comparison when the receiver may retain its memory output and the second specimen until the third arrives. After the negative-branch rotations, each branch of the twirled difference is proportional to

```math
H=w_x X\otimes A_x+w_y Y\otimes A_y+
(tI+bZ)\otimes A_z,\qquad b=\eta+ct .
```

Branchwise Helstrom readout is now available as a joint measurement. The [singlet-triplet identity](converse.md#the-singlet-and-triplet-blocks) gives a success probability $`1/2+df(t)/24`$ under the rotational prior, with

```math
f(t)=\sqrt{a+2tb}+\sqrt{a-2tb},
\qquad a=2\eta(1-t^2)+t^2+b^2 .
```

The decision effect of this readout may be chosen as the sign of $`H`$, with zero assigned to its kernel by a fair coin. It is odd under complex conjugation because $`\overline{H}=-H`$ in the computational basis. The channel, first-stage Kraus operators, and negative-branch rotations are real in that basis, so the decision observable pulled back to the original inputs is also odd. Common proper-rotation averaging preserves the success under the rotational prior and projects this observable onto a multiple of $`\chi`$. Indeed identity and pair correlations are the invariant terms of degrees zero and two in the Pauli expansion, and all are even under conjugation. This yields the same score pointwise.

For $`\eta>0`$, choose $`t<1`$ sufficiently close to one. Then

```math
a-1-t^2b^2=(1-t^2)(2\eta+b^2-1)>0
```

since $`b\to1`$ as $`t\to1`$. This implies $`f(t)>2`$. If $`a>2`$ the implication follows from $`f(t)^2\geq2a`$. If $`a\leq2`$ the positive expression gives $`a^2-4t^2b^2>(2-a)^2`$, and squaring $`f(t)`$ again proves the claim. Thus this relaxed receiver improves on the classical score at every positive survival probability. The exact nonunital tradeoff between the two arrival gaps remains open.
