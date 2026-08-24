# RL60 session freeze and proof state

Date: 2026-08-23

## 1. Scope of this freeze

This note records the state at the end of the RL60 terminal-tail session. It is intentionally conservative: it distinguishes inherited audited results, exact finite/session computations that should be replayed, external computational dependencies, and still-open statements.

No result in this file should be interpreted as a proof of RL or of the Collatz conjecture.

## 2. Exact live safe-CF survivor parameters

The rigorous safe continued-fraction stress point inherited from RL50 is

`a   = 123,139,092,617,126,647,266`

`ell =  77,692,117,359,936,589,403`

`q   =  45,446,975,257,190,057,863`.

For the terminal parameterization used in RL59/RL60,

`R = z-27`,

`K = q-z+3`,

hence the exact affine coupling

`K+z=q+3 = 45,446,975,257,190,057,866`.

The terminal exponent `K` is odd.

## 3. Inherited audited RL59 baseline

Retain unless an inherited verifier fails:

- the sole safe-CF survivor is still open;
- `Zx>143/12` strictly;
- `E<5/3` strictly;
- each x-zero weight `w<17/30`;
- terminal `J_end=2^K`, `Q_end=2^K+1`;
- `K` odd and `K>=25`;
- the positive terminal potential `J*g <= zeta*3^(4-d)/2` on positive post-cut states embeddable in the endpoint;
- the repeatable RL58 `J=3 <-> 5` synchronized pump is terminally neutralized;
- after the last `10` return the final positive height-one tail is synchronized and deterministic;
- final aligned zero mass satisfies `M_final>23/4`;
- the shortcut coordinate `n=(J-1)/2` evolves by
  - even `n -> n/2`,
  - odd `n -> (3n+1)/2`;
- a terminal hit occurs exactly when either
  - `n+1=2^K`, or
  - `3n+2=2^K`,
  for admissible odd `K`;
- Gate A remains open;
- no valid global Gate-B/RL→radius-3 bridge is proved.

## 4. RL59 finite thresholds inherited into RL60

The RL59 handover records:

| threshold | first start `N(K0)` | derived survivor lower bound on `z` |
|---|---:|---:|
| `K>=25` | 11,184,810 | 9,457,747 |
| `K>=27` | 13,256,071 | 11,209,181 |
| `K>=29` | 125,687,199 | 106,279,619 |

The RL59 prose correction `11,209,179` refers to the forced final-`00` count at `K>=27`; the resulting odd `z` lower bound is `11,209,181`.

## 5. RL60 finite-threshold extension

During RL60 the same terminal-tail logic was extended to:

| threshold | first start `N(K0)` | `Jmin=2N+1` | derived odd lower bound on `z` |
|---|---:|---:|---:|
| `K>=31` | 715,827,882 | 1,431,655,765 | 605,295,637 |
| `K>=33` | 1,908,874,353 | 3,817,748,707 | 1,614,121,697 |
| `K>=35` | 10,180,663,219 | 20,361,326,439 | 8,608,649,047 |
| `K>=37` | 45,812,984,490 | 91,625,968,981 | 38,738,920,711 |
| `K>=39` | 122,167,958,641 | 244,335,917,283 | 103,303,788,559 |

The conversion used is the inherited RL59 bootstrap:

`Amin(K0)=floor(115*Jmin/272)+1`,

then `z >= next_odd(Amin+1)` under the hypothesis `K>=K0`.

### Audit status of these RL60 thresholds

- The session independently rechecked the inherited K25/K27/K29 boundaries with a different strong-induction design.
- K31/K33/K35 were extended and later rechecked with the residue/minimal-counterexample method.
- K37/K39 were certified during the session with the residue/minimal-counterexample implementation whose source is preserved as `verification/residue_interval_cert.cpp`.
- The raw per-chunk output logs were not preserved in the active workspace. Therefore the next skeptical audit should replay the supplied source before treating K31–K39 as publication-grade bundled certificates.

This is a **reproducibility warning**, not evidence that the numerical claims failed.

## 6. 3-adic reverse-grammar observation

For the even terminal predecessor

`B_K=(2^K-2)/3`,

the reverse grammar observed in RL60 has a clean 3-adic structure:

- if `K ≡ 1 (mod 6)`, then `B_K` is divisible by 3, so this inverse branch has no odd predecessor at that node; doubling preserves divisibility by 3;
- if `K ≡ 3 (mod 6)`, the initial consecutive inverse-D run is governed by `v_3(K)`;
- if `K ≡ 5 (mod 6)`, after one doubling the consecutive inverse-D run is governed by `v_3(K+1)`.

This explains the observed K33/K35 reverse ancestors and is a structural lead, not yet a global lower-envelope theorem.

## 7. External path-record reduction obtained in RL60

The session used Barina's published path-record table, described as complete for starting values below `2^71`, as a global peak envelope for that verified range.

Comparing terminal targets against that envelope gave the provisional contradiction for every odd `K>=131`; therefore the survivor was compressed to

`25 <= K <= 129`, `K` odd.

Equivalently

`22 <= t=K-3 <= 126`, `t` even.

Using the exact coupling `K+z=q+3`, this external-certificate reduction would sharpen the survivor location to

`45,446,975,257,190,057,737 <= z <= 45,446,975,257,190,057,841`.

The lower endpoint corresponds to `K=129`; the upper endpoint corresponds to `K=25`.

### Classification

**External computational certificate / audit-pending interface.**

Before promotion, independently verify:

1. the path-record table is indeed complete for every start below `2^71` under the same shortcut convention needed here;
2. the record envelope comparison is made against the smaller of the two admissible terminal targets for each `K`;
3. the starting-value lower bound extracted from the record table is correct;
4. the terminal mass inequality is applied with the correct strict/non-strict rounding;
5. the contradiction with `z=q+3-K` first occurs at `K=131` and covers all larger odd `K`.

## 8. What this does NOT close

Even if the sole safe-CF survivor is eventually eliminated:

- the full uniform Gate-A theorem is not automatically proved for all denominator regimes;
- the failed RL48 direct half-period radius-3 match does not revive;
- a valid Gate-B/global-to-radius-3 bridge would still need to be proved unless the whole-tree audit finds that later reductions changed the logical architecture;
- RL and Collatz remain open.

## 9. Freeze point

Do not extend `K=41,43,...` before the whole-tree audit/roadmap reset. The current survivor attack is frozen at this point so the next session can decide whether it remains the highest-leverage branch.
