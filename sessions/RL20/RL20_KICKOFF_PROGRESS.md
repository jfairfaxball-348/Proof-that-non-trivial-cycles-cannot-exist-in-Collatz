# RL20 kickoff progress

Date: 2026-08-20

RL remains **OPEN**. Exact radius 3 remains **CLOSED for the inherited proof chain** after fresh verifier checks.

## Fresh baseline gate

All eight RL19 kickoff verifiers passed freshly in this session:

- `verify_rl18_repairs.py` — PASS
- `verify_rl18_global_orbit_identity.py` — PASS
- `verify_rl18_cubic_norm_reduction.py` — PASS
- `inherited/verify_rl12_same_direction_canonical.py` — PASS
- `inherited/verify_rl13_p3_j0_interior.py` — PASS
- `verify_rl19_cubic_skew_closure.py` — PASS
- `verify_rl19_global_weighted_population.py` — PASS
- `verify_rl19_global_odd_step_product.py` — PASS

No radius-3 repair was triggered.

## New RL20 result 1 — bounded-radius bridge formally falsified at the local-grammar level

`RL20_BOUNDED_RADIUS_BRIDGE_COUNTERMODEL.md`

The previously unfrozen length-184 session countermodel has been reconstructed and made exact. It is a primitive `(A,L)=(184,116)` word satisfying the RL-L54 proper-suffix envelope, the first-183 external-floor prefix envelope, the hard `s=2,t_exit=1` root bit grammar, and an endpoint-compatible `n_close=t_close=1` final-return residue witness.

Natural root/post-neutral/final-anchor rotation distances are `20,48,28`; a wider endpoint neighborhood has minimum distance `20`.

The word has `D∤Q`, so it is not an RL object. Evidence label: **EXACT FINITE CERTIFICATE** against the local-grammar-only bridge, not against RL.

## New RL20 result 2 — coprime-6 packing and continued-fraction gate

`RL20_GLOBAL_COPRIME6_PACKING_AND_CF_GATE.md`

Analytically, every phase of a nontrivial positive cycle is nonzero mod 3. In the k=0 least-root branch `R#≡1 mod6`, sorted odd states satisfy

`y_j >= R# + 3j + (j mod2)`.

Hence the RL19 odd-step product sharpens to

`log lambda <= 1/(3R#) + (1/9) log(1+3(L-1)/R#)`.

More generally, with `g=gcd(A,L)`, `p=A/g`, `q=L/g`, the crude product bound gives

`0 < p/q-log_2 3 <= 1/(3R# log2)`.

If `2q^2<3R#log2`, Legendre forces `p/q` onto the continued-fraction spine of `log_2 3`.

Using rigorous rational log intervals and the inherited **EXTERNAL COMPUTATIONAL INPUT** `R#>=2^71`, the exact verifier excludes every above-`log_2 3` convergent through

`q=49,547,666,543`.

Therefore

`L/gcd(A,L) >= 49,547,666,544`.

Evidence label: **ANALYTIC + EXACT FINITE CERTIFICATE + EXTERNAL COMPUTATIONAL INPUT**. No LMN is used.

## New RL20 result 3 — canonical higher-block polynomial is a coboundary

`RL20_CANONICAL_BLOCK_COBOUNDARY.md`

For `A=ga,L=gell`, at the canonical block scale let `E_j` be cumulative block imbalance and `x_j` the block-start states. Setting `y_j=3^{-E_j}x_j` gives the exact coefficient identity

`3^{-E_(j+1)}Q(B_j)=2^a y_(j+1)-3^ell y_j`.

Thus the whole canonical block polynomial telescopes exactly to `Q=RD`. The RL-L55 proper-factor cancellation is therefore a state coboundary, not an independent obstruction.

Evidence label: **ANALYTIC**.

Strategic effect: raw higher-block/proper-factor divisibility should be pruned unless combined with state inequalities, ownership, a rotation difference, or an independently sparse coefficient pattern.

## Best next targets

1. Use the final-return 3-adic address to restrict which continued-fraction convergents or gcd classes can occur.
2. Apply the RL18/RL19 weighted-difference identity at canonical block shifts, where the raw block sum itself is now known to be tautological.
3. Seek a one-sided inequality for the normalized block states `y_j=3^{-E_j}x_j` in the near-resonant branch; this is the missing extra input that could make a cofactor/resultant argument non-tautological.
4. Keep the huge-length branch separate; no contradiction is currently proved there.

## New RL20 result 4 — final-return / continued-fraction direct coupling is structurally insufficient

`RL20_FINAL_RETURN_CF_DECOUPLING.md`

The final-return discrete-log address constrains one closing excess exponent `t_close`, while the continued-fraction gate sees only the totals `(A,L)`. Since `A-L=sum_j t_j`, the only immediate link is `t_close<=A-L`.

This is too weak even in the inherited hard-root class. The explicit external-floor root

`R#=2361183241434822606907 = 91 (mod 144)`

supports both exact endpoint witnesses `(n,t)=(1,1)` and `(2,3)` while retaining the hard `s_root=2,t_exit=1` departure grammar. Hence endpoint address arithmetic alone selects no large CF/gcd class.

Evidence label: **ANALYTIC NO-GO LEMMA + EXACT FINITE WITNESS**.

## New RL20 result 5 — the local bridge countermodel is globally radius-4 packed

The strengthened `verify_rl20_bounded_bridge_countermodel.py` now checks all `184 choose 2 = 16,836` cyclic-rotation pairs. The minimum adjacent-transposition distance is exactly

`4`,

attained for example at shifts `(0,19)`.

Thus RL-L27 + RL-L36 + RL-L54 local endpoint/slope grammar does not even force *some* radius-3 pair somewhere in the rotation orbit. The length-184 model sits exactly one unit outside the closed radius-3 regime.

Evidence label: **EXACT FINITE CERTIFICATE**.

## New RL20 result 6 — hard root + exceptional weak close forces a second low plateau or enormous length

`RL20_HARD_ROOT_SECOND_LOW_EXIT.md`

In the hard root branch `(s_root,t_exit)=(2,1)`, the root plateau contributes slope factor `8/9`. The exceptional weak final return `(n_close,t_close)=(1,1)` necessarily has `(s_close,mu_close)=(1,0)` and contributes `4/3`. Their owned product is therefore `32/27`.

Hence if `lambda=2^A/3^L < 32/27`, at least one additional plateau must satisfy

`2^(s+t) < 3^s`.

If instead `lambda>=32/27`, the RL20 coprime-6 packing inequality gives

`L >= 1+(R#/3)(lambda^9 exp(-3/R#)-1)`.

Conditional on the inherited `R#>=2^71` floor, exact rational arithmetic plus `exp(-x)>1-x` yields

`L > 1+6R#/5`.

So the exceptional hard weak-close branch has a genuine global dichotomy: **a second low-excess plateau exists, or the odd length is larger than `1.2 R#`.**

Evidence label: **ANALYTIC + EXTERNAL COMPUTATIONAL INPUT for the numerical huge-length corollary**.

## Updated best next targets

1. Use the newly forced second low plateau in the hard `(s_root=2,n_close=1)` near-resonant branch: seek canonical ownership, a weighted difference to the root/final rotations, or a repeatable low-block descent.
2. Keep the `lambda>=32/27` branch separate as an explicit huge-length branch; do not hide it inside a generic near-resonance statement.
3. Do not return to the direct final-address/CF sieve without adding `D|Q`, ownership of another plateau, or a constraint on the remaining `t_j`.
4. Do not start a generic radius-4/5 classification ladder merely because the local countermodel has minimum radius 4; the all-rotation radius-4 certificate is a sharp no-go for the local bridge, not evidence that generic radius escalation will close RL.
