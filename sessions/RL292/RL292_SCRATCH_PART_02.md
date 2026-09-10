This is FINITE EVIDENCE ONLY. It is not promoted and does not contract Gate A by itself.

Its strategic meaning is sharper than a generic shifted valuation: t(J) records the deep boundary phase *before* the J-2 reset occurs. For the analytic family above, t(J_N)=N+4, so t<=mu would force mu(J_N)>=N+4 and would prepay the arbitrary phase reset.

### D. Finite-template closure still fails

The two-phase endpoint reserve

Phi(J)=max(nu_2(J-2)+2, nu_2(3J+2))

also survives the H<=22 physical-state inequality Phi(J)<=mu(J), but it is not edge-Lipschitz. Exact reachable cost-one macros in the certificate can increase Phi by 12 beyond their unit cost. This is consistent with RL283's unbounded shifted-template barrier: a finite family of endpoint templates does not close under arbitrary retained boundary phase.

Thus the new candidate t(J)<=mu(J) is useful only as one ancestry-pricing lemma, not as a standalone Bellman potential.

### E. Rank-1 minimal-arrival finite signal

On the same exact H<=22 scan, among targets whose minimum historical height is realized by a cost-one positive-checkpoint macro, every nontrivial target observed satisfies a strong Gate-A margin; the worst minimum-height examples have nu_2(J)-mu(J) <= -5 (e.g. 8192 at H=18). This is FINITE EVIDENCE ONLY.

It motivates a controlled Rank-1 theorem target:

"a minimum-area fixed-seed history whose final positive-checkpoint macro has height one cannot be a Gate-A violator."

If proved analytically, every minimum-area Gate-A counterexample would have final excursion height at least two, giving exactly the minimal controlled kernel extension permitted by RL292.

### Next intended attack

Prioritize the ancestry-pricing theorem for the stripped-unit label

positive even reachable checkpoint (J,H) => nu_2(3J+2) <= H,

while treating it as a sublemma rather than a full Bellman potential. In parallel, seek an analytic proof that a minimum-area cost-one arrival is Gate-A safe; if successful this removes the complete height-one kernel and forces the next controlled extension to excursion height h=2.

No authoritative repository state changed. Gate A remains open with exact residual k>=25 odd, H_can<k.

## Fourth checkpoint — first-positive Bellman reduction and pulled-back hazard-cylinder bridge

Status: ANALYTIC REDUCTION + ANALYTIC BRIDGE + STRATEGIC CORRECTION / NOT PROMOTED.

### A. Exact first-positive Bellman reduction

Let a genuine canonical path start at the fixed seed `(d,J,H)=(1,-13,0)`, and let `s_*` be its first state with `J>0`. Positive `J` is forward invariant, so every later positive-even balanced checkpoint lies in the future cone of `s_*`.

For a physical state `s`, retain RL290's full-state Bellman future threat

`Bcal(s)=sup_sigma [nu_2(J_end)-Delta H_sigma]`

over legal future segments ending at a positive even `d=1` checkpoint.

Then the global positive-checkpoint theorem is equivalent to the restricted root theorem

`for every globally reachable first-positive state s_*: Bcal(s_*) <= H(s_*)`.

Proof: if a later checkpoint `e` violates `nu_2(J_e)<=H_e`, its suffix from `s_*` has `Delta H=H_e-H_*`, hence

`Bcal(s_*) >= nu_2(J_e)-(H_e-H_*) > H_*`.

Conversely `Bcal(s_*)>H_*` supplies a legal future checkpoint with

`nu_2(J_e)-Delta H > H_*`, hence `nu_2(J_e)>H_e`.

Thus all fixed-seed historical complexity before the first sign crossing can be compressed to the first-positive state and its already-paid height. The remaining theorem is a future-threat theorem on this sign-crossing root family.

This meshes directly with RL288's promoted first-positive structure: at such a root, with `M=J+2^d-2` and `A=H+d-1`, one has `0<M<3^d` and `nu_2(M)<=A`, with the recorded unique equality state `(3,2,1)`.

### B. Minimum-area checkpoint-geodesic version

On RL290's positive-even checkpoint macro graph every edge has strictly positive height cost `h>=1`. Let `mu(J)` be minimum fixed-seed historical height to checkpoint `J`, and let `V(J)` be the checkpoint Bellman threat.

If a minimum-area history reaches `J'` from predecessor `J` by a macro of cost `h`, then

`mu(J')=mu(J)+h`

and Bellman gives

`V(J)>=V(J')-h`.

Therefore

`V(J)-mu(J) >= V(J')-mu(J')`.

So Bellman deficit cannot first appear at a non-root checkpoint along a minimum-area history. Every global violation propagates backward to a positive-phase root with at least the same deficit.

Strategic correction: the previous proposed programme "prove minimum-area height-one arrivals safe, then extend the kernel to h=2" is unnecessary as a principal Bellman strategy. A minimal Bellman violation is already a root regardless of the height of its final incoming macro. Kernel-by-kernel extension is relevant only insofar as it helps estimate root future threat.

### C. Exact pulled-back future-template center identity for `t=nu_2(3J+2)`

At a balanced checkpoint let the paired parity words `x,y` have common length `n`, common weight `r`, and affine numerators `Q_x,Q_y`:

`C_x(z)=(3^r z+Q_x)/2^n`,
`C_y(z)=(3^r z+Q_y)/2^n`.

Use RL289's fixed affine pairing `A(z)=3z+14`.

Define the two 2-adic pullback centers

`p_x = C_x^{-1}(-2/3)
     = (-2^(n+1)-3Q_x)/3^(r+1)`,

`p_y = A^{-1}(C_y^{-1}(-1/3))
     = (-2^n-14*3^(r+1)-3Q_y)/3^(r+2)`.

Using the exact checkpoint identity

`3Q_x-Q_y = 14*3^r + 2^n(J-1)`,

direct subtraction gives

`boxed: p_x-p_y = -2^n(3J+2)/3^(r+2)`.

Hence

`boxed: nu_2(p_x-p_y)=n+nu_2(3J+2)`.

Interpretation: `t(J)=nu_2(3J+2)` is exactly the *extra common 2-adic cylinder depth beyond the already-fixed n-bit prefix* between two pulled-back future templates. The templates are precisely the 2-adic half-step itineraries of `-2/3` (`01000...`) and `-1/3` (`10000...`), i.e. the stripped-unit height-one suffix pair.

This proves that `t` is a genuine fixed-pair cylinder-overlap quantity, not an arbitrary shifted valuation.

### D. But `t<=H` is not a principal Rank-1 solution

Even if the finite candidate

`nu_2(3J+2)<=mu(J)`

were proved globally, it would not control recursive Rank-1 Bellman threat. The homogeneous `010` danger towers from the earlier checkpoint have

`nu_2(3M_j+2)=3`

at every nonterminal level while `V(M_R)>=k-R` is arbitrarily large.

Thus the stripped-unit label can prepay particular phase-reset mechanisms, but it cannot be the missing global Bellman regularizer by itself. Deprioritize it from principal theorem status.

### E. New principal theorem target exposed by the reduction

Attack directly:

`FIRST_POSITIVE_BELLMAN_DOMINATION:
 every globally reachable first-positive state (d,J,H) satisfies Bcal(d,J)<=H.`

This is equivalent to the global checkpoint/Bellman target by Section A, but the root family carries RL288 sign-crossing structure unavailable at arbitrary later checkpoints.

Exact H<=22 falsification support:

- stopping the canonical search at the first `J>0` produces 314 first-positive `(d,J,H)` root occurrences;
- these collapse to 41 physical `(d,J)` roots after minimizing H;
- minimum-H roots begin `(2,1,1)`, `(2,3,1)`, `(3,2,1)`;
- within the inherited total-height window, a direct finite-horizon Bellman scan found no root violation among every root for which a positive-even checkpoint is reachable within the remaining H<=22 budget;
- the worst observed finite-horizon equality is `(d,J,H)=(2,3,1)`, with threat `1`, witnessed by future checkpoint `8` at added height `2`.

This is FINITE EVIDENCE ONLY. It is not a proof of the root theorem.

Regression support:

