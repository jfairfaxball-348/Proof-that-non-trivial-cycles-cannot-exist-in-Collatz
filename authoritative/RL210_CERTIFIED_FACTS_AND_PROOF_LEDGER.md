# RL210 certified facts and proof ledger

Date: 2026-08-31. Canonical current classification record.

## New proved analytic mathematics

**RL210-T1 — global 56-bit p-shift overlap.** For `0<=t<z=L-p`, the lifted
p-shift has no epsilon carry and `b_(p+t)=u+b_t`. For an above-p tau34 source
`a=p+e`, source height one gives an exact normalized endpoint valuation
`v2(F_e)=b_e-1`, where

`F_e=3*2^37-P_p+(3^p-2^u)R_(p,p+e)/2^u`.

For every `e>=56`, positivity of all acceleration exponents truncates the actual
word modulo `2^56` to the two p-separated 56-step cumulative-exponent prefixes:

`sum_(t=0)^55 (2^(S'_t)-2^(S_t))3^(-t) = -3*2^37 mod2^56`,

with `S_t=b_t-h_t` and `S'_t=S_(p+t)-u=b_t-h_(p+t)`. This is a genuine global
prefix/cancellation restriction, not a reflected below-p theorem.

**RL210-T2 — first-divergence selector.** The two prefixes are strictly
increasing. If m is their first mismatch, the exact valuation of their first
non-cancelling difference is `min(S_m,S'_m)`. Hence every physical current
above-p source with `e>=56` must satisfy

`24<=m<=37` and `min(S_m,S'_m)=37`.

All heights agree at p-separated phases before m. At m one height is exactly
`b_m-37` and the other is smaller. If `m=24`, only
`S'_24=37<S_24=38` survives the exact finite orientation check, so
`h_(p+24)=1` and `h_24=0`.

**RL210-T3 — short-offset prefix locking.** Reducing the exact endpoint at
`e<56` shows that whenever `n_e=b_e-1<37` and `b_(e-1)<n_e`, exact valuation
forces `S_t=S'_t` for `0<=t<=e`. On the current necessary small-offset frontier
this applies exactly at `e=4` and `e=16`. Thus a physical source at either rank
has `h_t=h_(p+t)` through the source and, by the noncarry K increment identity,
`K_0=...=K_(e+1)=2^37`.

Complete proofs are in `proofs/RL210_GLOBAL_P_SHIFT_PREFIX_OVERLAP_THEOREM.md`.

## New exact finite certificates

**RL210-CERT1 — exact small-offset frontier.** Among all source offsets
`1<=e<56`, exactly six current necessary above-p ranks survive: e equal to
`4,16,28,33,40,45`, with the terminal phases/ranks and endpoint depths recorded
in `RL210_GLOBAL_PREFIX_OVERLAP_CERTIFICATE.md`. Therefore exactly
**7,091,831,278** of the **7,091,831,284** current above-p necessary ranks have
`e>=56` and are subject to RL210-T2.

**RL210-CERT2 — m=24 orientation obstruction.** Exhaustive integer DP modulo
`2^40`, over every strictly increasing continuation bounded by `b_t`, proves
that the orientation `S_24=37<S'_24=38` cannot satisfy the RL210-T1 overlap.
The opposite orientation remains arithmetically possible at this certificate's
scope; no physical occurrence is asserted.

Portable verifier: `python3 verification/verify_rl210_global_prefix_overlap.py`.

## Inherited mathematics and corrections

RL209-T1/T2/CERT1/CERT2, RL208-T1/CERT1, RL206-T1/T2/T3, all inherited H21
identities, RL202's absolute root theorem, RL206-C1 and RL206-C2 retain their
exact scopes. Corrected below-p constants remain 37 / 60 / 97. Eta classes remain
`0,8,9,17 mod18`. The current necessary predicate is exactly the RL209 predicate.

RL195 complete-word denominator equivalence and RL201 real-mass/coupled-reverse
barriers remain binding. RL210 uses an absolute actual-word p-shift overlap,
which RL201 explicitly left outside its local translation barrier.

## Frontier and open obligations

RL210 deletes **zero** terminal ranks. The exact frontier remains:

- total necessary terminals: **13,415,865,871**;
- canonical source `a>p`: **7,091,831,284**;
- canonical source `a<p`: **6,324,034,587**.

RL210 proves a global prefix/height selector but no eta/state/sign/valuation
selector. It proves no physical H21 incidence or charge and no contradiction of
`(37,0,23,-1)`. Gate A globally open; Gate B globally open; nontrivial-cycle
exclusion open.

The main successor obligation is to combine the 24..37 first-divergence cases,
the m=24 orientation restriction, and the e=4/16 K-flat locks with genuinely
absolute complete-word closure/K/height information. Merely enumerating longer
unanchored exponent prefixes is lower priority and is not independent closure
information.
