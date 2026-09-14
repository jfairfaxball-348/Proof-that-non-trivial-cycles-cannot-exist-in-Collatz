# RL316 closeout — exact row energy and dual-shadow ownership frontier

Date: 2026-09-14
Status: CLOSED AND FROZEN
Incoming authoritative HEAD: `edadf26ae0ee53d60037960a8226fc5fbfd5de79`
Successor: RL317

## 0. Executive conclusion

RL316 does not prove Gate A, Gate B, global positive non-trivial-cycle
exclusion, or the Collatz conjecture.

It completes the first prescribed row/layer attack on the RL315 canonical
interface.  The unsigned row energy admits a closed exact formula, but the
formula telescopes to the inherited full numerator ownership identity.  This
is a decisive method barrier: future work must use layer support, signs,
physical path legality, or another genuinely independent input.

For `g=2`, RL316 identifies the canonical reduced shadow as a rankwise late
envelope, constructs a dual early envelope, proves an exact rational-shadow
bracketing theorem around the two physical boundary states, and turns the
RL315 positive cofactor quotient into a deterministic row-decoding coordinate.

The frozen RL21 countermodel saturates all new `X+Y`-side identities while
failing only the `X-Y` state-sum factor.  The exact successor frontier is
therefore absolute `D0=X-Y` ownership of the dual-shadow bracket.

## 1. Prefix-potential identity

For a binary word `w` of length `a` and weight `n`, let `P_j` count its ones
strictly before position `j`, and put

`Q(w)=sum_(j:w_j=1)2^j 3^(n-1-P_j)`.

Define

`Phi(w)=sum_(j=0)^(a-1)2^j 3^(n-P_j)`.

Then

`Phi(w)=4Q(w)+2^a-3^n`.

Proof.  Set `U_j=2^j3^(n-P_j)`.  Since
`P_(j+1)=P_j+w_j`, direct checking for `w_j=0,1` gives

`U_j=(U_(j+1)-U_j)+4w_j2^j3^(n-1-P_j)`.

Sum over `j`; the first term telescopes from `U_0=3^n` to `U_a=2^a`.

## 2. Exact general row energy

Write the full word as `g` rows `w_k` of length `a`, with

`A=ga`, `L=g ell`.

Choose the cyclic row cut so that its discrepancy levels satisfy

`E_0=min_k E_k=0`,

`E_(k+1)=E_k+n_k-ell`, where `n_k=|w_k|`.

Let `P_(k,j)` be the row prefixes.  The RL315 canonical lower envelope and
interface are

`T_j=min_k(E_k+P_(k,j))`,

`tau_j=T_(j+1)-T_j`,

`f_(k,j)=E_k+P_(k,j)-T_j`.

Put

`X=2^a`, `Y=3^ell`, `D0=X-Y`,

`q=Q(tau)`, `q_k=Q(w_k)`,

`s_k=sum_(h>k)n_h=(g-k-1)ell-E_(k+1)`.

After factoring `X^k` from row `k`, its positive energy is

`R_k=sum_j2^j3^(L-(kell+T_j)-f_(k,j))(3^(f_(k,j))-1)`.

Expanding `3^f-1` and applying the prefix-potential identity to `tau` and
`w_k` gives

`R_k=Y^(g-k-1)(4q+D0)-3^(s_k)(4q_k+X-3^(n_k))`.

Now

`Q(d)=sum_kX^k3^(s_k)q_k`,

and the constant terms telescope to

`X^g-Y^g=D0H`,

where

`H=(X^g-Y^g)/(X-Y)`.

Therefore

`sum_kX^kR_k=4(qH-Q(d))`.

Under full ownership `Q(d)=D0Hx_0`, and with `n=q-D0x_0`, this is exactly

`4nH`.

Thus row-total regrouping alone contributes no constraint beyond the inherited
ownership identity.  This does not invoke or strengthen RL206; it is a direct
closed telescope compatible with the RL206 barrier.

## 3. `g=2` meet/join envelope theorem

Use the universal balanced length-`a` cut.  Both rows `w_0,w_1` have weight
`ell`.  Let their `h`-th odd positions be `p_(0,h),p_(1,h)`.

Because the canonical prefix is

`T_j=min(P_(0,j),P_(1,j))`,

its `h`-th one occurs at

`p_(tau,h)=max(p_(0,h),p_(1,h))`.

Define the dual word `sigma` by

`p_(sigma,h)=min(p_(0,h),p_(1,h))`.

Both coordinatewise sequences are strictly increasing.  Rankwise expansion of
`Q` gives

`q_0+q_1=q_tau+q_sigma`.

The late-envelope deficits

`delta_k=q_tau-q_k`

are nonnegative and satisfy

`delta_0+delta_1=q_tau-q_sigma`,

`delta_1-delta_0=q_0-q_1`.

For a genuine cycle,

`D0 | q_0+q_1=q_tau+q_sigma`,

`H=X+Y | q_0-q_1`.

If `q_0=q_1`, inherited fixed-weight injectivity modulo `X` forces the rows to
agree, contradicting primitivity.  Hence

`q_tau-q_sigma>=|q_0-q_1|>=X+Y`.

## 4. Exact dual-shadow bracket

Label the physical boundary states

`R<x=R+G`.

Let row `u` map `R` to `x`, row `v` map `x` to `R`, and put
`U=Q(u)`, `V=Q(v)`.  The row equations are

`U=D0R+XG`,

`V=D0R-YG`,

so `U-V=(X+Y)G>0`.

Set

`epsilon=q_tau-U>=0`.

Using the envelope sum identity,

`q_tau=D0R+XG+epsilon`,

`q_sigma=D0R-YG-epsilon`.

Both shadows have positive numerators.  Their rational fixed states

`r_tau=q_tau/D0`, `r_sigma=q_sigma/D0`

satisfy

`r_tau-x=R-r_sigma=(YG+epsilon)/D0>0`.

Therefore

`0<r_sigma<R<x<r_tau`,

and

`r_tau+r_sigma=R+x`.

This is a strict, exactly symmetric bracket at the balanced cut.  It does not
make either rational shadow a genuine integer cycle.

## 5. Cofactor quotient and row decoding

The RL315 positive quotient at the lower boundary is

`n=q_tau-D0R`.

Section 4 gives the exact complementary identities

`n=XG+epsilon`,

`n+q_sigma=D0x`.

In particular

`XG<=n<=D0x-1`.

Modulo `X`,

`U == q_tau-n (mod X)`.

For fixed `tau`, the inherited injectivity of `Q(w) mod X` on weight-`ell`
words therefore makes `n mod X` a deterministic outgoing-row decoder.

More precisely, if `s<a` is the first position where `u` and `tau` differ,
then the fixed-weight first-difference lemma and `X|XG` give

`v2(n)=s`.

If `u=tau`, then `epsilon=0` and `X|n`.

## 6. Exact saturation and route barrier

The frozen RL21 `X+Y`-factor countermodel has

`(a,ell)=(65,41)`,

`U-V=4(X+Y)`.

RL316's verifier reconstructs its envelopes and finds

`epsilon=0`,

`q_tau-q_sigma=4(X+Y)`,

`n=4X`.

Thus it saturates the envelope gap, exact bracket, and quotient lower edge.
It also has RL21's positive unique-least rational orbit and near-minimum
geometry.  But

`X-Y` does not divide `U+V`.

RL38's unique area-seven local crossing similarly gives
`q_tau-q_sigma=X+Y` at `(6,2)`.

Therefore `X+Y` ownership plus binary interface legality, envelope geometry,
and dyadic row decoding still does not close `g=2`.  The missing resource is
genuine absolute `D0` ownership.

## 7. Verification and evidence

Portable commands:

```sh
python3 -I verification/verify_rl316_row_energy.py
python3 -I verification/verify_rl316_g2_dual_shadow.py
```

They check:

- 2,645 general canonical words;
- 224,325 balanced two-row pairs;
- 111,350 ordered dual-shadow pairs;
- the exact frozen RL21 and RL38 saturation witnesses.

These are regressions for the analytic proofs and exact replays of inherited
certificates.  An exploratory simultaneous-factor scan through `a<=22` found
no distinct pair, but it is not promoted and is irrelevant to the internal
frontier `ell>=190537`.

## 8. Corrections and scope

No inherited mathematical claim was corrected or demoted.

Binding qualifications:

1. The dual shadows are rational, not integer cycles.
2. `r_sigma<R` does not contradict physical leastness.
3. No local denominator ownership is inferred.
4. Unsigned row energy is a rewrite, not an independent constraint.
5. The RL21 witness blocks every `H`-only closure claim.
6. `g=1` remains separate.

Gate A remains open.
Gate B remains open.
Global positive non-trivial-cycle exclusion remains open.
No Collatz conjecture claim is made.

## 9. Successor frontier

RL317 should attack the absolute dual-shadow ownership problem:

> Can genuine `D0 | q_tau+q_sigma`, positivity of both rational shadows, and
> integer path ownership obstruct the exact bracket or reduce it to a
> support-independent finite certificate?

If the analytic `D0` route proves equivalent to the old simultaneous-factor
problem, independently replay the first reduced fibre before using any RL315
numerical scratch.

`PARENT_DIFFICULTY_DELTA = SAME`

Reason: RL316 produced a cleaner exact object and eliminated unsigned row/H-only
variants, but the remaining `D0` consumer is the genuine unresolved ownership
barrier.
