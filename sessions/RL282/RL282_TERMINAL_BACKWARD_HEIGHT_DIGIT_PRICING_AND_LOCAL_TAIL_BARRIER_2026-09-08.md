# RL282 — terminal-backward height-digit pricing and local-tail barrier

Date: 2026-09-08

## Classification

Primary:

`TERMINAL_BACKWARD_HEIGHT_DIGIT_PRICING_AND_LOCAL_TAIL_BARRIER_PROVED`

Promoted subordinate results:

- `ONE_ZERO_MOD3_OUTPUT_SHELL_PROVED`
- `ARBITRARY_POSITIVE_BOUNDARY_SUFFIX_AFFINE_COMPRESSION_PROVED`
- `TERMINAL_ONE_ZERO_HEIGHT_DIGIT_PRICING_PROVED`
- `BOUNDARY_INVERSE_RUN_RECURRENCE_PROVED`
- `PURE_ZERO_FINAL_TAIL_LOCAL_REALIZABILITY_FAMILY_PROVED`
- `POSITIVE_TAIL_MASS_AND_F_BARRIER_PROVED`
- `UPSTREAM_CHECKPOINT_REACHABILITY_IDENTIFIED_AS_GATE_A_OBSTRUCTION`

All promoted mathematical items are analytic. The verifier supplies finite regression checks only; no finite sample is promoted as a global theorem.

Gate A remains open. Gate B remains separate/open/frozen. The fifth selector was not scanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## 1. Incoming exact state

RL282 starts from RL281 with:

- terminal state `d=1, J=2^k`;
- every terminal exponent `k` is odd;
- every positive `d=1` state has `H_can>=3`, so `k=3` is Gate-A safe;
- every hypothetical Gate-A violator satisfies
  `k>=5`, `k` odd, `H_can<k`;
- the inherited dangerous-zero condition
  `H_can<k => m0>=8`, equivalently `z>=k+6`;
- the one-zero first-return law
  `3^h(J_in+4)=2^h(2J_out+3)`;
- for `J_in!=-4`,
  `h=nu_2(J_in+4)`;
- the reachability invariant
  `J mod 3 in {0,(-1)^d}`;
- every positive multi-zero excursion is fully priced by the positive checkpoint `F` inequality;
- total positive-phase zero mass satisfies `S_positive<15`;
- terminal scale is
  `Q_T=X/2^(k+1)`;
- the positive checkpoint Lyapunov quantity is
  `F=Q(J+3)`.

The RL282 mission was a scalable height-escalation theorem for residual odd `k>=5`.

## 2. One-zero output shell

Consider a reachable positive one-zero first return
from an even positive `d=1` checkpoint `J_in`
to a positive `d=1` return state `J_out`.

The exact one-zero law is

`3^h(J_in+4)=2^h(2J_out+3)`.

For `J_in!=-4`, write

`J_in+4=2^h M`

with `M` odd. Then

`2J_out+3=3^h M`.

If `h>=2`,

`J_out = 3(3^(h-1)M-1)/2`,

and the parenthesized factor is nonzero modulo `3`. Hence

`nu_3(J_out)=1`.

If `h=1`, then

`J_out=3(M-1)/2`.

At `d=1`, reachability gives `J_in mod 3 in {0,2}`. Therefore
`M=(J_in+4)/2 mod 3` is respectively `2` or `0`, so `(M-1)/2`
is nonzero modulo `3`. Again

`boxed: nu_3(J_out)=1`.

Thus every reachable positive one-zero output lies on the exact shell

`boxed: J_out == 3 or 6 (mod 9)`.

Equivalently, for `A=J+1`, every such output satisfies

`A == 4 or 7 (mod 9)`.

This is a global consequence of the inherited one-zero law plus the inherited mod-3 reachability invariant, not a finite observation.

## 3. Exact positive boundary affine compression

At `d=1` with odd `J`, both zero-height boundary choices have the affine form

`J'=(3^x J+1)/2`,  `x in {0,1}`.

Let a legal positive zero-height boundary suffix be

`w=x_1...x_L`

and let

`r=sum_i x_i`.

Define

`C_w = sum_(j=1)^L 2^(j-1) 3^(sum_(i=j+1)^L x_i)`.

Exact composition gives

`boxed: 2^L J_T = 3^r J_0 + C_w`.

At a retained terminal `J_T=2^k` this becomes

`boxed: 2^(k+L)=3^r J_0+C_w`.

If `J_0` is the output of a reachable positive one-zero excursion, Section 2 yields `nu_3(J_0)=1`, hence

`boxed: nu_3(2^(k+L)-C_w)=r+1`.

Thus an arbitrary final positive boundary suffix is compressed exactly to `(L,r,C_w)`.

## 4. Exact height-digit pricing for the preceding one-zero excursion

Define

`N_w(k)=2^(k+L+1)-2C_w+3^(r+1)`.

Using the suffix identity,

`N_w(k)
 = 2(3^r J_0)+3^(r+1)
 = 3^r(2J_0+3)`.

Therefore

`boxed:
 nu_3(N_w(k))
 = r + nu_3(2J_0+3)`.

If a one-zero excursion of actual height `h` precedes the suffix, its exact equation implies

`3^h | (2J_0+3)`,

so

`boxed:
 h <= nu_3(N_w(k))-r`.

Equivalently, height at least `h` forces

`boxed:
 2^(k+L+1)
 == 2C_w-3^(r+1)  (mod 3^(r+h))`.

For `n>=1`, `2` has exact order `2*3^(n-1)` modulo `3^n`.
Indeed LTE gives

`nu_3(2^(2*3^m)-1)
 = nu_3(4^(3^m)-1)
 = 1+m`,

so the order lifts by a factor `3` at every level.

Consequently, whenever the right side is a unit, each additional allowable one-zero height unit selects exactly one of the three lifts of the previous exponent class. For a fixed suffix, cheap height is therefore priced by successive ternary digits of the terminal exponent.

This is an exact arithmetic thinning theorem. Section 7 proves that it is not by itself a Gate-A closure mechanism.

## 5. Boundary inverse-run recurrence

Put

`A=J+1`.

On the positive odd boundary,

- `x=1` gives `A -> 3A/2`;
- `x=0` gives `A -> (A+2)/2`.

A forward block `0 1^t` therefore has the exact inverse

`boxed:
 R_t(A)=2(2^t A/3^t - 1)`,

defined precisely for

`0<=t<=nu_3(A)`.

Every positive boundary suffix can be reconstructed backwards by iterating these inverse blocks.

Write a target as

`A=3^v U`,  `3 not| U`.

Then the leftmost inverse block has three valuation regimes.

### Deep undershoot: `t<=v-2`

The predecessor shell state satisfies

`nu_3(R_t(A)-1)=1`

and

`nu_3(2R_t(A)+1)=1`.

Since `R_t(A)-1` is the predecessor `J`, the preceding one-zero excursion, if present, has available 3-adic height exactly `1`. No high-height branch is hidden here.

### Near-full consumption: `t=v-1`

This is one exceptional branch. Shell admissibility is controlled by
`nu_3(2^v U-1)`, and extra one-zero height is controlled by the next exact 3-adic valuation.

### Full consumption: `t=v`

This is the second exceptional branch. Let

`c=nu_3(2^v U-1)`.

The leading run length before the zero is forced by this valuation, and further available height is again controlled by the next exact 3-adic valuation.

Thus arbitrary boundary tails reduce to a valuation automaton: deep undershoots force height one, and all possible larger cheap height is confined to the near-full/full branches.

## 6. A zero-count/mass route barrier

The positive neutral boundary loop at `J=3` has word `10` and scale multiplier `4/3`.

If its entry scale is `q`, the `x=0` zero in the loop has weight `2q/3`.
After `N` loops,

`q_N=q(4/3)^N`.

The total zero mass inserted by all `N` loops is exactly

`sum_(i=0)^(N-1) (2/3)q(4/3)^i
 = 2(q_N-q)
 < 2q_N`.

Hence an arbitrarily large count of positive boundary zeros can have bounded total mass relative to the post-loop scale.

Therefore neither positive boundary-zero count nor `S_positive<15` can by itself force increasing canonical height. This is compatible with the inherited neutral-family barrier and does not produce a Gate-A counterexample.

## 7. Exact pure-zero final-tail local family

The ternary thinning of Section 4 is not subcritical against legal boundary tails.

Fix any odd terminal exponent

`k>=3`

and any prescribed one-zero height

`h>=2`.

Because `2` generates the units modulo `3^(h+1)`, there is one residue class

`q (mod 2*3^h)`

satisfying

`boxed:
 2^(q+1)(2^k-1)
 == -5 + 2^h 3^h
    (mod 3^(h+1))`.

Choose any sufficiently large positive representative in that class and set

`J_0=2^q(2^k-1)+1`.

Then

`2J_0+3
 =2^(q+1)(2^k-1)+5`

has exact 3-adic valuation `h`. In particular

`J_0==3 (mod 9)`.

Put

`M=(2J_0+3)/3^h`

and

`J_in=2^h M-4`.

The defining congruence gives:

- `M` odd and `3 not| M`;
- `J_in>0` for sufficiently large `q`;
- `J_in` is even;
- `J_in==0 (mod 3)`;
- `nu_2(J_in+4)=h`;
- `3^h(J_in+4)=2^h(2J_0+3)`.

Therefore the genuine positive one-zero word

`0 1^h`

takes `J_in` to `J_0` with exact height `h`.

Now append `q` boundary zeros. For `0<=t<=q`,

`T_0^t(J_0)
 =2^(q-t)(2^k-1)+1`.

Every intermediate state with `t<q` is positive odd, and at `t=q`

`T_0^q(J_0)=2^k`.

Hence

`boxed:
 J_in --0 1^h--> J_0 --0^q--> 2^k`

is an exact locally legal positive terminal block for every odd `k>=3` and every `h>=2`.

Increasing `q` by multiples of `2*3^h` preserves the exact height condition, so there are infinitely many such local blocks.

Crucial scope:

This theorem does **not** assert that `J_in` is globally reachable from the original state `J=-13` at low accumulated height. It is a local positive-phase realizability/barrier theorem only.

## 8. Exact scale, zero-mass, and F cost of the pure-zero family

Let `Q_T` be the terminal scale.

The `q` boundary zeros give

`Q_0=Q_T/2^q`.

The one-zero excursion satisfies

`Q_0=2(2/3)^h Q_in`,

so

`boxed:
 Q_in=Q_T 3^h/2^(q+h+1)`.

The excursion contributes one zero of weight `Q_in`.
The boundary zeros have total weight

`Q_0(2^q-1)=Q_T(1-2^(-q))`.

Therefore

`boxed:
 S_block
 =Q_T[1-2^(-q)+3^h/2^(q+h+1)]`.

Along the infinite admissible progression in `q`,

`boxed: S_block -> Q_T`.

For the checkpoint Lyapunov quantity `F=Q(J+3)`, direct substitution gives

`boxed:
 F_T-F_in
 =Q_T[4
      -5/2^(q+1)
      +3^h/2^(q+h+1)]`.

Hence

`boxed: F_T-F_in -> 4Q_T`.

On a retained terminal,

`Q_T=X/2^(k+1)`.

For residual `k>=25`, the inherited `X<160/3` gives

`Q_T < (160/3)/2^26 < 7.95*10^(-7)`.

Thus arbitrarily long, arbitrarily 3-adically precise local final tails can fit inside exponentially tiny positive zero-mass and `F` budgets.

The present combination of:

- terminal 3-adic thinning;
- positive boundary-zero mass;
- `S_positive<15`;
- terminal scale;
- positive `F` ceiling;

cannot by itself close Gate A.

## 9. Local valuation monotonicity is also insufficient

The experimentally attractive checkpoint statement

`nu_2(J)<=H`

is not preserved by individual positive excursions.

For example, the legal height-one first return

`J=30 -> J=24`

raises

`nu_2(J)` from `1` to `3`.

Therefore any proof of the global checkpoint inequality, if true, must use reachability information carried from the original trajectory rather than a naive block-by-block valuation budget.

RL282 also observed strong finite evidence for the stronger relation `J<=2^H` at reachable positive `d=1` states, but no gap-free analytic proof was obtained. Neither statement is promoted.

## 10. Supporting finite exploration — explicitly unpromoted

During RL282, an exact height-capped checkpoint automaton was explored in scratch computation.

The session reported:

- exhaustive positive-checkpoint search through `H<=26`;
- no positive even checkpoint with `nu_2(J)>H`;
- power-of-two Gate-A safety observed through odd `k=27`.

This large finite computation is **not part of the promoted RL282 theorem set** because the closeout fast suite intentionally does not reproduce the multi-million-state height-capped closure.

It is preserved here as successor evidence only. A future session may rerun and package it as a separate exact certificate if that becomes useful.

No authoritative residual bound is narrowed using this exploratory computation.

## 11. Exact remaining obstruction

Gate A remains

`H_can>=k`

at terminal `d=1,J=2^k`.

The authoritative residual remains

`boxed:
 k>=5, k odd, H_can<k`.

RL282 shows that the final positive boundary tail is not where a uniform proof can come from:

- arbitrary final tails compress exactly to a 3-adic valuation condition;
- every extra cheap one-zero height unit consumes one ternary digit for a fixed tail;
- nevertheless pure-zero tails provide an infinite exact locally legal family for arbitrary odd `k` and prescribed `h>=2`;
- their positive mass and `F` costs can be arbitrarily small at fixed terminal scale;
- local `nu_2(J)` monotonicity fails across excursions.

Therefore the missing theorem must constrain **upstream global reachability of positive checkpoints as a function of accumulated height**.

A sufficient target would be

`d=1, J>0, J even, globally reachable at height H
 => nu_2(J)<=H`.

At a terminal `J=2^k` this immediately gives `k<=H`.

This is a target, not an RL282 theorem.

A stronger experimentally observed target is `J<=2^H`, but it is also unproved.

## 12. Verification

Portable verifier:

`verification/verify_rl282_terminal_backward.py`

checks directly from the exact normalized recurrence:

- positive one-zero output shell;
- exact boundary affine compression;
- terminal shell valuation;
- height-digit identity;
- inverse-run recurrence and deep-undershoot valuation;
- exact order of `2` modulo sampled powers of `3`;
- the pure-zero local family for 114 `(k,h)` pairs;
- complete replay of those 114 positive terminal blocks;
- exact zero-mass and `F` formulas;
- positive neutral-loop mass barrier.

Clean verifier output is frozen in

`verification/RL282_FAST_VERIFIER_OUTPUT.txt`.

The finite checks are regression support only. The promoted claims are the analytic identities/proofs in this report.

## 13. Scope and non-claims

RL282 does not:

- close Gate A;
- claim the locally constructed `J_in` states are globally reachable;
- promote the `H<=26` scratch search as a theorem;
- classify positive boundary Collatz cycles;
- reopen completed first-return excursion interiors;
- merge Gate B into Gate A;
- scan the fifth selector;
- start Radius 6+;
- claim global non-trivial-cycle exclusion.

The successor should work upstream, not spend another session refining the final-tail 3-adic classification.
