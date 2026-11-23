# Upper bound for every first-stage instrument

The receiver may measure weakly before storing its first qubit, keep an unlimited classical record, and then perform an arbitrary joint measurement using its memory output and both later specimens. The bound below includes that entire class. It starts with a pair of rotationally mixed sources and reduces each first-stage branch to a two-dimensional singular-value calculation.

## A rotational prior

Fix two mirror triples with the same Gram matrix and volume of magnitude $`d`$. For each sign, draw a proper rotation uniformly from $`SO(3)`$ and apply it to all three vectors. This gives two density matrices $`\bar\rho_+,\bar\rho_-`$. Assign prior probability one half to each sign. A strategy's worst-case success is at most its average under this prior.

The averaged Bloch terms of degree one vanish. The degree-two terms depend only on the Gram matrix. The third-order rotation moment is

```math
\int_{SO(3)} R_{ia}R_{jb}R_{kc}\,dR
=\frac16\varepsilon_{ijk}\varepsilon_{abc}.
```

Indeed, a proper-rotation-invariant real tensor of rank three is proportional to the Levi-Civita tensor. Invariance on the left and right imposes this form on both index triples. Contracting with $`\varepsilon_{ijk}`$ gives the coefficient, since a proper rotation preserves $`\varepsilon`$. Subtracting the two averaged density matrices then gives

```math
\Delta=\bar\rho_+-\bar\rho_-=\frac d{24}\chi.
```

For any fixed strategy up to the final joint decision, the binary Helstrom bound gives the equal-prior success probability $`1/2+\lVert \Delta_{\mathrm{out}}\rVert_1/4`$. Classical records are orthogonal blocks of the output matrix.

## The singlet and triplet blocks

On the second and third registers define $`A_i=\sum_{j,k}\varepsilon_{ijk}\sigma_j\otimes\sigma_k`$, so $`\chi=\sum_i\sigma_i\otimes A_i`$. Let $`|s\rangle=(|01\rangle-|10\rangle)/\sqrt2`$ be their singlet and set $`|t_i\rangle=-\mathrm i(\sigma_i\otimes I)|s\rangle`$. These three vectors are orthonormal and lie in the triplet space. Each $`A_i`$ changes sign under swap, hence it maps the singlet to the triplet and the triplet to the singlet. Direct Pauli multiplication gives $`A_i|s\rangle=2|t_i\rangle`$. Consequently,

```math
A_i=2\bigl(|t_i\rangle\langle s|+|s\rangle\langle t_i|\bigr).
```

For three Hermitian qubit blocks $`B_i`$, the norm of $`\sum_i B_i\otimes A_i`$ follows by writing the operator on the singlet and triplet sectors. Its off-diagonal block is twice the vertical stack of $`B_x,B_y,B_z`$, and its positive singular values appear twice:

```math
\left\lVert \sum_i B_i\otimes A_i\right\rVert_1
=4\mathrm{Tr}\sqrt{\sum_i B_i^2}.
```

In particular, $`\lVert \chi\rVert_1=8\sqrt3`$. This gives the fully joint optimum $`1/2+d/(4\sqrt3)`$ under the rotational prior.

## A classical first gap

Let $`E_y`$ be the effect of the first measurement for outcome $`y`$ and define $`(v_y)_i=\mathrm{Tr}(E_y\sigma_i)`$. Positivity gives $`\lVert v_y\rVert_2\leq\mathrm{Tr}E_y`$. On the remaining pair the unnormalized branch of $`\Delta`$ is $`(d/24)\sum_i(v_y)_iA_i`$, whose trace norm is $`(d/6)\lVert v_y\rVert_2`$. The total trace norm is at most $`d/3`$ because $`\sum_y\mathrm{Tr}E_y=2`$. Thus the success probability is at most $`1/2+d/12`$ even when the two later qubits become available for a joint measurement. The same argument applies to continuous records by integration.

## An arbitrary instrument before a unital memory

Refine the first-stage classical record to reveal one Kraus operator $`K`$ per branch. This gives the receiver additional classical information and can only increase its performance. A branch that chooses classical-only storage can be represented as preparing a fixed state for the memory input. In a nonzero branch, write the polar decomposition $`K=P U`$ in output coordinates, where $`U`$ is unitary and

```math
P=\sqrt{s(I+t\,n\cdot\sigma)},\qquad
s=\tfrac12\mathrm{Tr}K^\dagger K,\quad
0\leq t\leq1,\quad \lVert n\rVert_2=1.
```

The instrument obeys $`\sum s=1`$. Since $`\chi`$ is invariant under a common proper rotation, conjugating its first register by $`U`$ is equivalent to conjugating the last two by $`U^\dagger`$. Those unitary conjugations preserve the trace norm after the first-stage operations. We may therefore calculate each branch with $`P`$ alone.

Define $`M=\sqrt{1-t^2}\,I_3+(1-\sqrt{1-t^2})nn^{\mathsf T}`$. The component along $`n`$ is preserved by $`M`$ and the perpendicular components are multiplied by $`\sqrt{1-t^2}`$. Inserting $`P`$ on both sides of each Pauli matrix gives

```math
P\sigma_iP=s\bigl(t n_i I+(Me_i)\cdot\sigma\bigr).
```

Unitality preserves the scalar term. The normalized first-register blocks after memory are therefore

```math
B_i=t n_i I+(TM e_i)\cdot\sigma.
```

Set $`F=\lVert T\rVert_F^2`$ and $`b=\lVert Tn\rVert_2^2`$. A Bloch matrix of a unital channel is a contraction on the unit ball, so $`0\leq b\leq\min(1,F)`$. Because $`M n=n`$ and $`M^2=(1-t^2)I_3+t^2 nn^{\mathsf T}`$,

```math
\sum_i B_i^2=aI+2t(Tn)\cdot\sigma,\qquad
a=F+(1-F+b)t^2.
```

The norm contributed by the branch before the factor $`d/24`$ is

```math
4s\left(\sqrt{a+2t\sqrt b}+\sqrt{a-2t\sqrt b}\right).
```

Let $`L=\max(1,F)`$. Since $`a`$ interpolates between $`F`$ and $`1+b`$, it obeys $`a\leq 2L`$. With that condition, squaring the desired inequality gives

```math
\sqrt{a+2t\sqrt b}+\sqrt{a-2t\sqrt b}\leq 2\sqrt L
\quad\Longleftrightarrow\quad
a-L-\frac{bt^2}{L}\leq0.
```

For $`F\leq 1`$, the last expression is $`(F-1)(1-t^2)`$. For $`F\geq1`$, it is $`(F-1)(b/F-1)t^2`$. Both are nonpositive. Summing with $`\sum s=1`$ bounds the classical-quantum output difference by $`d\sqrt L/3`$ in trace norm. The Helstrom formula gives the claimed $`1/2+d\sqrt L/12`$ upper bound. When only a positive lower bound on $`|V|`$ is specified, use a pair of mirror triples at that boundary.

The [staged receiver](receiver.md) attains the bound on each input orientation. The [channel examples](memory-channels.md) show how unitality enters the optimization.

