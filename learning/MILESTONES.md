# Project understanding map

These 30 milestones trace a three-arrival handedness decision from single-qubit measurements to the exact scores for unital noise and for a flagged polarization memory. The [Bartlett–Rudolph–Spekkens bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) introduces the common source and connects its rotation twirl and spin decompositions to both receivers.

| Phase | Milestones | Scientific connection |
|---|---|---|
| Background/preliminaries | [M01](#m01-a-qubit-as-a-bloch-vector)–[M05](#m05-proper-rotations-and-mirrors) | Inputs and geometric handedness |
| Background/preliminaries | [M06](#m06-classical-records-and-feed-forward)–[M12](#m12-the-full-receiver-model) | Measurement, noise, symmetry, and the receiver model |
| Narrative/innovation | [M13](#m13-the-chirality-operator)–[M16](#m16-the-first-gap-matters) | Observable, ideal reference score, and first-gap separation |
| Narrative/innovation | [M17](#m17-principal-memory-axes)–[M22](#m22-cyclically-aligning-the-principal-axes) | Timed Bell receiver for arbitrary known unital noise |
| Narrative/innovation | [M23](#m23-refining-the-first-slot-instrument)–[M26](#m26-the-exact-minimax-score) | Bound for every first-slot instrument and the exact score |
| Narrative/innovation | [M27](#m27-interpreting-the-threshold)–[M30](#m30-the-complete-result) | Channel thresholds, storage schedules, and spin tags |

## Phase I · Background and preliminaries

### M01 A qubit as a Bloch vector

**Central question.** What does a vector say about one qubit?

**Understanding target.** Read $`\rho=(I+r\cdot\sigma)/2`$ as a density operator. The three coordinates of $`r`$ are Pauli expectations and positivity constrains $`\lVert r\rVert\le1`$.

**Prerequisites.** None within this map.

**Conceptual connection.** Recognize what is physically accessible from a single shot and what is a property of the preparation.

**Source pointers.** [Unital background notes](WATROUS_BRIDGE.md) · [Worked example](WATROUS_BRIDGE.md#a-complete-first-example)

### M02 Measuring a spin component

**Central question.** What can the detector return on a single arrival?

**Understanding target.** Distinguish an axis $`n`$ from the random outcome $`s=\pm1`$. A measurement of $`n\cdot\sigma`$ has mean $`n\cdot r`$.

**Prerequisites.** [M01](#m01-a-qubit-as-a-bloch-vector).

**Conceptual connection.** Use the same language for a Cartesian Pauli measurement and a later measurement along a weighted axis.

**Source pointers.** [Unital background notes](WATROUS_BRIDGE.md) · [Worked example](WATROUS_BRIDGE.md#a-complete-first-example)

### M03 Ordered product states

**Central question.** What does one run of the apparatus receive?

**Understanding target.** Represent the three preparations by $`\rho_1\otimes\rho_2\otimes\rho_3`$ and attach each tensor factor to its arrival slot. Product expectations factor into three single-input expectations.

**Prerequisites.** [M01](#m01-a-qubit-as-a-bloch-vector), [M02](#m02-measuring-a-spin-component).

**Conceptual connection.** Use order to distinguish the roles of the first and second temporal gaps.

**Source pointers.** [Unital background notes](WATROUS_BRIDGE.md) · [Model](../science/model.md)

### M04 Oriented volume

**Central question.** What binary label is encoded in the triple?

**Understanding target.** Read the determinant with the Bloch vectors in its columns. Its magnitude $`d`$ measures volume, and its sign reverses under an exchange of two columns.

**Prerequisites.** [M01](#m01-a-qubit-as-a-bloch-vector), [M03](#m03-ordered-product-states).

**Conceptual connection.** Connect the determinant expansion to a sum of products of three measurable Pauli expectations.

**Source pointers.** [Model](../science/model.md) · [Worked example](WATROUS_BRIDGE.md#a-complete-first-example)

### M05 Proper rotations and mirrors

**Central question.** Which change of axes preserves the label?

**Understanding target.** Explain why a common proper rotation preserves the determinant and why a mirror reverses it while preserving dot products. Equal lengths and pairwise dot products leave the sign unresolved.

**Prerequisites.** [M04](#m04-oriented-volume).

**Conceptual connection.** Identify the nuisance orientation and the matched alternative used in the converse.

**Source pointers.** [Model](../science/model.md)

### M06 Classical records and feed-forward

**Central question.** How can an early measurement change a later one?

**Understanding target.** Distinguish an early measurement outcome, the stored record of it, and the later measurement it selects. Use a list of outcomes to define the receiver's final decision.

**Prerequisites.** [M02](#m02-measuring-a-spin-component), [M03](#m03-ordered-product-states).

**Conceptual connection.** Give a causal description of an adaptive measurement even when no quantum register crosses a gap.

**Source pointers.** [Unital background notes](WATROUS_BRIDGE.md) · [Receiver](../science/receiver.md)

### M07 A noisy qubit channel

**Central question.** What can happen to a retained qubit between arrivals?

**Understanding target.** Interpret a unital channel as a physical map preserving the maximally mixed state. Its Bloch matrix $`T`$ acts on polarization by $`r\mapsto Tr`$.

**Prerequisites.** [M01](#m01-a-qubit-as-a-bloch-vector), [M03](#m03-ordered-product-states).

**Conceptual connection.** Relate the length and direction of a stored Bloch vector to the memory's action.

**Source pointers.** [Unital background notes](WATROUS_BRIDGE.md) · [Memory channels](../science/memory-channels.md)

### M08 A measurement with a retained output

**Central question.** What information can leave the first slot together?

**Understanding target.** An instrument yields a classical outcome and a conditional quantum output. Use a Kraus representation for each branch and a trace-preserving sum over outcomes.

**Prerequisites.** [M06](#m06-classical-records-and-feed-forward), [M07](#m07-a-noisy-qubit-channel).

**Conceptual connection.** Include weak measurements and classical-only and retain-only strategies in one operational model.

**Source pointers.** [Unital background notes](WATROUS_BRIDGE.md) · [Converse](../science/converse.md)

### M09 Trace and Frobenius norms

**Central question.** Why do the proof and theorem use different norms?

**Understanding target.** Read the trace norm as a sum of singular values and the Frobenius norm as their root-sum-square. Distinguish the object being measured in each expression.

**Prerequisites.** [M01](#m01-a-qubit-as-a-bloch-vector), [M07](#m07-a-noisy-qubit-channel).

**Conceptual connection.** The trace norm limits discrimination of the two reachable states. The Frobenius norm of the memory Bloch matrix determines the final threshold.

**Source pointers.** [Unital background notes](WATROUS_BRIDGE.md) · [Converse](../science/converse.md)

### M10 Averaging a common rotation

**Central question.** How can we reason about a source orientation the receiver does not know?

**Understanding target.** Use the same random proper rotation on all three vectors. A worst-case guarantee cannot exceed the score averaged over this family.

**Prerequisites.** [M05](#m05-proper-rotations-and-mirrors), [M06](#m06-classical-records-and-feed-forward).

**Conceptual connection.** Keep the geometry of the triple intact while removing the arbitrary lab orientation in the upper-bound calculation.

**Source pointers.** [Collective twirling](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md#reading-the-review) · [Model](../science/model.md)

### M11 Binary state discrimination

**Central question.** How does a state difference constrain a guessing probability?

**Understanding target.** For equal prior weights, relate the optimal success to $`1/2+\lVert \rho_+-\rho_-\rVert_1/4`$. Interpret the positive and negative spectral subspaces as a measurement rule.

**Prerequisites.** [M06](#m06-classical-records-and-feed-forward), [M09](#m09-trace-and-frobenius-norms).

**Conceptual connection.** Apply the same bound to a classical record together with an unmeasured quantum system.

**Source pointers.** [Unital background notes](WATROUS_BRIDGE.md) · [Converse](../science/converse.md)

### M12 The full receiver model

**Central question.** Which inputs, operations, and resources define the comparison?

**Understanding target.** State the one-visit-per-qubit promise, unknown common frame, determinant sign, known first-gap channel, and availability of local controls. Locate every retained classical and quantum system between arrivals.

**Prerequisites.** [M03](#m03-ordered-product-states), [M04](#m04-oriented-volume), [M06](#m06-classical-records-and-feed-forward), [M07](#m07-a-noisy-qubit-channel), [M08](#m08-a-measurement-with-a-retained-output), [M10](#m10-averaging-a-common-rotation), [M11](#m11-binary-state-discrimination).

**Conceptual connection.** Assemble the model for comparing classical processing, first-gap memory, and an unrestricted final measurement in the converse.

**Source pointers.** [Model](../science/model.md) · [Converse](../science/converse.md)

## Phase II · Narrative and innovation

### M13 The chirality operator

**Central question.** Which term retains the mirror difference after averaging?

**Understanding target.** Derive the third-order Pauli sum $`\chi`$ from the determinant expansion. In the orientation-averaged density difference, the one- and two-body terms cancel and the coefficient is $`d/24`$.

**Prerequisites.** [M04](#m04-oriented-volume), [M05](#m05-proper-rotations-and-mirrors), [M10](#m10-averaging-a-common-rotation), [M12](#m12-the-full-receiver-model).

**Conceptual connection.** Reduce an unknown-orientation classification task to measuring a specified operator on three qubits.

**Source pointers.** [Model](../science/model.md) · [Converse](../science/converse.md)

### M14 The unrestricted ideal benchmark

**Central question.** How much could a joint measurement on all three inputs reveal?

**Understanding target.** Use the spectrum of $`\chi`$ and the Holevo–Helstrom theorem to obtain the ideal joint score $`1/2+d/(4\sqrt3)`$.

**Prerequisites.** [M09](#m09-trace-and-frobenius-norms), [M11](#m11-binary-state-discrimination), [M13](#m13-the-chirality-operator).

**Conceptual connection.** Set the reference value that the timed receiver with ideal first-gap storage will attain.

**Source pointers.** [Model](../science/model.md) · [Converse](../science/converse.md)

### M15 A receiver with classical storage

**Central question.** What can be learned without a retained qubit?

**Understanding target.** Choose a uniformly random Pauli-axis permutation and return the product of three measurement signs times its parity. The resulting decision observable is $`\chi/6`$.

**Prerequisites.** [M02](#m02-measuring-a-spin-component), [M04](#m04-oriented-volume), [M06](#m06-classical-records-and-feed-forward), [M13](#m13-the-chirality-operator).

**Conceptual connection.** Translate an observable identity into the pointwise classical success $`1/2+d/12`$.

**Source pointers.** [Worked example](WATROUS_BRIDGE.md#a-complete-first-example) · [Receiver](../science/receiver.md)

### M16 The first gap matters

**Central question.** Can later joint operations recover the ideal score after the first qubit is measured?

**Understanding target.** A first-slot effect selects a Bloch vector weighting the remaining two-qubit operator. Positivity bounds its length by the trace of the effect, giving the classical score as an upper bound even with unrestricted later storage.

**Prerequisites.** [M08](#m08-a-measurement-with-a-retained-output), [M11](#m11-binary-state-discrimination), [M13](#m13-the-chirality-operator), [M15](#m15-a-receiver-with-classical-storage).

**Conceptual connection.** Locate the lost discrimination power across the first gap by optimizing over every first measurement.

**Source pointers.** [Converse](../science/converse.md)

### M17 Principal memory axes

**Central question.** How can local controls express arbitrary unital memory in a usable form?

**Understanding target.** Write the real Bloch matrix in signed singular-value coordinates using proper rotations. Keep track of which rotation is applied before and after the first-gap use.

**Prerequisites.** [M07](#m07-a-noisy-qubit-channel), [M09](#m09-trace-and-frobenius-norms), [M12](#m12-the-full-receiver-model).

**Conceptual connection.** Reduce channel-dependent construction to three real weights whose squared sum is $`\lVert T\rVert_F^2`$.

**Source pointers.** [Unital background notes](WATROUS_BRIDGE.md) · [Memory channels](../science/memory-channels.md) · [Receiver](../science/receiver.md)

### M18 One Bell measurement on the first pair

**Central question.** How can the second slot supply three signed correlations at once?

**Understanding target.** Show that the three pair observables for one permutation parity commute and that their product fixes the third sign. Their simultaneous eigenbasis is a rotated Bell basis with four outcomes.

**Prerequisites.** [M02](#m02-measuring-a-spin-component), [M03](#m03-ordered-product-states), [M06](#m06-classical-records-and-feed-forward), [M17](#m17-principal-memory-axes).

**Conceptual connection.** Read the pair into two independent classical bits before the third qubit arrives.

**Source pointers.** [Unital background notes](WATROUS_BRIDGE.md) · [Receiver](../science/receiver.md)

### M19 The last measurement axis

**Central question.** How does the pair result determine the last measurement?

**Understanding target.** Combine the measured signs with the relevant axis weights to form the direction for the final qubit. Normalize by the length of the weight vector, which is independent of the Bell outcome.

**Prerequisites.** [M02](#m02-measuring-a-spin-component), [M17](#m17-principal-memory-axes), [M18](#m18-one-bell-measurement-on-the-first-pair).

**Conceptual connection.** Realize a weighted three-body correlation through a classical Bell record and one single-qubit measurement.

**Source pointers.** [Receiver](../science/receiver.md)

### M20 Combining the two Bell settings

**Central question.** Why are two permutation classes used?

**Understanding target.** With equal probability use either the even or the odd class, and reverse the output sign for the odd class. The resulting observable has the alternating signs of $`\chi`$.

**Prerequisites.** [M04](#m04-oriented-volume), [M13](#m13-the-chirality-operator), [M18](#m18-one-bell-measurement-on-the-first-pair), [M19](#m19-the-last-measurement-axis).

**Conceptual connection.** Achieve a properly signed statistic for every orientation of the input, with the two Bell settings used on different runs.

**Source pointers.** [Receiver](../science/receiver.md)

### M21 Tracking the observable back through memory

**Central question.** How do the memory weights enter the decision on the input states?

**Understanding target.** Apply the adjoint memory map to the receiver observable. The circuit intentionally uses the signed gains once in the readout, and channel back-propagation multiplies by those gains once more.

**Prerequisites.** [M07](#m07-a-noisy-qubit-channel), [M17](#m17-principal-memory-axes), [M19](#m19-the-last-measurement-axis), [M20](#m20-combining-the-two-bell-settings).

**Conceptual connection.** Find the squared gains contributed by the three principal axes before their roles are averaged.

**Source pointers.** [Receiver](../science/receiver.md) · [Memory channels](../science/memory-channels.md)

### M22 Cyclically aligning the principal axes

**Central question.** How does the score become independent of input orientation under anisotropic noise?

**Understanding target.** Use calibrated rotations to cycle the three memory gains through the three chosen lab axes. This gives each axis the same mean square gain and makes the resulting observable proportional to $`\chi`$.

**Prerequisites.** [M05](#m05-proper-rotations-and-mirrors), [M17](#m17-principal-memory-axes), [M20](#m20-combining-the-two-bell-settings), [M21](#m21-tracking-the-observable-back-through-memory).

**Conceptual connection.** Distinguish the physical random choice of memory alignment from the common source-rotation average in the converse.

**Source pointers.** [Receiver](../science/receiver.md)

### M23 Refining the first-slot instrument

**Central question.** What must the upper bound allow before the memory is used?

**Understanding target.** Reveal Kraus labels as extra classical data and express each branch using its trace weight, strength, and axis. The extra labels can only help a receiver, and the branch weights sum to one.

**Prerequisites.** [M08](#m08-a-measurement-with-a-retained-output), [M12](#m12-the-full-receiver-model), [M16](#m16-the-first-gap-matters).

**Conceptual connection.** Account for arbitrary weak and strong measurements before retention in a single calculation.

**Source pointers.** [Converse](../science/converse.md)

### M24 The singlet and triplet blocks

**Central question.** What makes each branch's trace norm computable?

**Understanding target.** Write the difference operator in off-diagonal singlet–triplet form on the later pair. For such a block matrix the trace norm is twice the sum of the singular values of the coupling block.

**Prerequisites.** [M09](#m09-trace-and-frobenius-norms), [M13](#m13-the-chirality-operator), [M23](#m23-refining-the-first-slot-instrument).

**Conceptual connection.** Reduce the full three-qubit spectrum to a two-dimensional positive matrix on the memory output.

**Source pointers.** [Converse](../science/converse.md) · [Spin decomposition](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md#reading-the-review)

### M25 Bounding every branch

**Central question.** Can an intermediate-strength measurement outperform both endpoint strategies?

**Understanding target.** Use the branch formula and physical contraction of $`T`$ to bound the trace norm by the same channel expression for every strength and axis. Add the trace norms over the labeled blocks.

**Prerequisites.** [M17](#m17-principal-memory-axes), [M23](#m23-refining-the-first-slot-instrument), [M24](#m24-the-singlet-and-triplet-blocks).

**Conceptual connection.** Explain why no instrument can beat the higher of the two endpoint scores for unital memory.

**Source pointers.** [Converse](../science/converse.md)

### M26 The exact minimax score

**Central question.** Where do the receiver and converse meet?

**Understanding target.** Combine the two constructive strategies with the upper bound to obtain $`P^\star(d,T)=1/2+(d/12)\max\{1,\lVert T\rVert_F\}`$. Use the pointwise success to interpret a promise $`d\ge\delta`$.

**Prerequisites.** [M14](#m14-the-unrestricted-ideal-benchmark), [M15](#m15-a-receiver-with-classical-storage), [M16](#m16-the-first-gap-matters), [M22](#m22-cyclically-aligning-the-principal-axes), [M25](#m25-bounding-every-branch).

**Conceptual connection.** Identify both the worst-case guarantee and the corresponding strategy for any known unital first-gap channel.

**Source pointers.** [Model](../science/model.md) · [Receiver](../science/receiver.md) · [Converse](../science/converse.md)

### M27 Interpreting the threshold

**Central question.** What does it mean for a noisy memory to help?

**Understanding target.** Explain why depolarizing visibility must exceed $`1/\sqrt3`$ and why residual dephasing can help. Compare unital channels with the same average fidelity by calculating their different Frobenius norms.

**Prerequisites.** [M07](#m07-a-noisy-qubit-channel), [M09](#m09-trace-and-frobenius-norms), [M17](#m17-principal-memory-axes), [M26](#m26-the-exact-minimax-score).

**Conceptual connection.** Use the three stored-axis gains to diagnose a unital memory. In the spin-zero block, compute the probability of recovering the full logical qubit and determine when that probability is positive.

**Source pointers.** [Memory channels](../science/memory-channels.md) · [Decoded first-gap channel](../science/flagged-polarization-memory.md#the-decoded-first-gap-channel)

### M28 The storage schedule

**Central question.** What has to remain coherent at each stage of an optimal run?

**Understanding target.** Trace the first specimen through each memory. The Bell receiver uses a parity setting and signs after the second arrival. The flagged-loss receiver uses the tag or a six-outcome measurement of the recovered qubit and the second specimen. Both records select a Pauli measurement on specimen three.

**Prerequisites.** [M12](#m12-the-full-receiver-model), [M16](#m16-the-first-gap-matters), [M18](#m18-one-bell-measurement-on-the-first-pair), [M19](#m19-the-last-measurement-axis), [M26](#m26-the-exact-minimax-score).

**Conceptual connection.** Translate the score separation into a specific requirement on when storage is useful and what may be discarded.

**Source pointers.** [Model](../science/model.md) · [Receiver](../science/receiver.md) · [Optimal staged measurement](../science/flagged-polarization-memory.md#optimal-staged-measurement-of-the-recovered-qubit)

### M29 Amplitude damping and weak measurement

**Central question.** What changes when the memory moves the center of the Bloch ball?

**Understanding target.** Interpret amplitude damping as an affine Bloch map. A weak measurement supplies a recorded branch and lets its output align with that translation. Explain the constructive improvement for survival probabilities between one third and one.

**Prerequisites.** [M07](#m07-a-noisy-qubit-channel), [M08](#m08-a-measurement-with-a-retained-output), [M21](#m21-tracking-the-observable-back-through-memory), [M25](#m25-bounding-every-branch), [M27](#m27-interpreting-the-threshold).

**Conceptual connection.** Locate the dependence of the exact endpoint optimization on the unital assumption, and distinguish the demonstrated construction from an optimum for general nonunital noise.

**Source pointers.** [Memory channels](../science/memory-channels.md)

### M30 The complete result

**Central question.** How can the spin tag help when both receivers see the same losses?

**Understanding target.** Compare the two exact flagged-memory scores with the loss mask held fixed. Explain why a refined rank-one effect preserves more first-specimen information and check that the staged tagged receiver beats the joint mask-only receiver at the stated example.

**Prerequisites.** [M12](#m12-the-full-receiver-model), [M13](#m13-the-chirality-operator), [M26](#m26-the-exact-minimax-score), [M27](#m27-interpreting-the-threshold), [M28](#m28-the-storage-schedule), [M29](#m29-amplitude-damping-and-weak-measurement).

**Conceptual connection.** Separate finite decision utility from asymptotic quantum capacity. Give the charged carrier count and the quantum storage used at each gap.

**Source pointers.** [Exact scores](../science/flagged-polarization-memory.md#exact-scores) · [Mask-only comparison](../science/flagged-polarization-memory.md#arbitrary-first-instruments-and-the-mask-only-comparison) · [Worked loss example](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md#two-survivors-and-one-classical-bit)
