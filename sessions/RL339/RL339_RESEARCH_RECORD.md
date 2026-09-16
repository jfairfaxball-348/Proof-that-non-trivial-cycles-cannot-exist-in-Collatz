# RL339 research progress — NOT AUTHORITATIVE, NOT PROMOTED

BASE_HEAD `1d21ed6023b9e129cfdf4f8450a8b956a58c6eab`; committed
`authoritative/` tree `cfbc3e1a14e85199035ef7b4f0fa87b17617f9ff`.
Scope throughout: the ordered genuine `g=2`, `Z0>0`, `K<0` parent at
`(a,ell)=(217976794617,137528045312)`, with the externally conditional
least-state floor `m>=2^71`. R1 and the global proof remain OPEN.

## Exact singleton escape (new finite certificate candidate)

Retain the inherited q=0 odd-state band `2^71<=P<2^76+2^36`, the exact
rational-mechanical factor grammar, and the singleton profile `(1)`. For each
ordered adjacent zero pair with `1<=z,z'<=35` and `43<=z+z'<=70`, enumerate
every admissible length-`z+z'` template, every odd residue lift in the band,
and every integral odd backward reconstruction. No high-carry ownership filter
is imposed, so the population is a superset of live physical rows at every
lower bootstrap.

For total 43: 28 ordered pairs, 721 templates, 80,403 candidate rows. For
totals 44..70: 378 ordered pairs, 11,865 templates, 39,361 candidate rows.
Every one of the 119,764 candidate sources reaches below `2^71` under the
deterministic forward odd Collatz map, in at most 186 odd steps (185 for
totals 44..70). A state on the assumed cycle cannot do so. Thus every live
singleton has adjacent zero total at most 42. The scan is gap-free over the
stated finite ranges and is independently reconstructed by the two red-team
scripts below. Classification: exact finite candidate certificate, conditional
on the inherited state band and external floor. **NOT PROMOTED.**

Primary and independent checks:

```
python3 .rl-work/RL339/artifacts/neutral_singleton_escape.py 8 20
python3 .rl-work/RL339/artifacts/neutral_singleton_escape.py 21 21
python3 .rl-work/RL339/artifacts/all_large_singleton_escape.py
python3 .rl-work/RL339/artifacts/red_team_total43.py
python3 .rl-work/RL339/artifacts/red_team_large_singleton.py
```

## Density and phase theorem candidate

Let `q_0,...,q_T` be the inherited genuine linear mechanical excess word,
`q_0=0`, `T=ell-rho`, `Z` its number of zero positions, and `K` its positive
positions. RL336 gives every zero run length at most 35 in the high-carry
conditional branch. A complete positive run of length `p` between zero runs
`z,z'` satisfies `z+z'<=42p`: for `p=1` use the new singleton exclusion;
for `p>=2`, use `z+z'<=70<=42p`. A terminal positive tail only strengthens
the count. Summing over all complete returns and bounding the two endpoint
zero runs by 35 gives

`2Z<=42K+70`, hence `K>=ceil((T+1-35)/22)`.

Define each complete-return slack `sigma=42p-z-z'`; a terminal positive tail
may be assigned `sigma=42p-z` with a dummy zero target. Then `sigma>=0`, and
every positive-slack edge has `p<=sigma`. Let `S42` be their total slack.
Every zero-slack edge is a singleton with `z+z'=42`. Within a zero-slack
block, labels either alternate `z <-> 42-z` or stay at `21 -> 21`.

Let `B` be the number of zero-slack blocks, `K0` the positive ranks on their
edges, and `P` a collection of disjoint pairs of low target anchors separated
by 44 physical ranks. Since defect edges cost at least their positive length,
`K0>=K-S42` and `B<=S42+1`. Every full group of four zero-slack edges
contains such a pair: in an alternating block use its two low targets; in a
`21->21` block use the first and third low targets. Therefore

`4P>=K0-3B>=K-4S42-3`.

The step-44 fractional phase is

`alpha=(44a mod ell)/ell=101543836620/137528045312>1/2`.

For every starting phase, two weights at phase separation `alpha` sum to at
least `1+2^(1-alpha)`. A rational log/exponential lower certificate proves
`2^(1-alpha)-1>198849/1000000=:c`. The inherited weighted-support theorem
therefore gives the all-length candidate

`W_struct >= K + c*max(0,(K-4S42-3)/4)`.

Classification: analytic density and phase-pair candidate theorems consuming
the exact finite singleton certificate. **NOT PROMOTED.**

At fixed `rho`, set `Kbase=ceil((ell-rho+1-35)/22)`, `K=Kbase+h`, and
`s=44Kbase-2(ell-rho+1)+70` (so `0<=s<=43` while `Kbase>0`). Then
`S42<=44h+s`. Intersect the displayed structural bound with the inherited
arbitrary-support residue envelope `W(Kbase)+h`. At `rho=60` the exact
integer minimax occurs at `h=24,281,914`, with certified gain
`24,281,914.2845...` and upper carry RHS `32537248343.41877...`.

For every `rho>=60` the RHS is strictly decreasing: when `rho` increases by
one, `Kbase` stays or falls by one. An omitted ideal term removes more than
`1/(6 Lambda)` from the RHS. With no K drop, endpoint slack increases by two,
so optimized phase gain falls by at most `2c`, restoring less than
`2c/(12 Lambda)`. With a K drop, endpoint slack falls by 42; the structural
positive-part argument rises by 167, and the weighted residue step is at
least one, so optimized gain cannot fall. The restored residue step is less
than `(22/21)/(12 Lambda) < 1/(6 Lambda)` since `Kbase<ell/22` and the
quartic weight increment is less than `22/21`. The inherited `rho<=59`
companion bound is below `17,179,869,185`. Thus the conditional candidate cap
is `n<=32537248343`, improving RL338 by 9,023,656, while leaving R1 OPEN.

Arithmetic and independent checks:

```
python3 .rl-work/RL339/artifacts/verify_density42_cap.py
python3 .rl-work/RL339/artifacts/red_team_density42_cap.py
python3 .rl-work/RL339/artifacts/phase42_candidate.py
python3 .rl-work/RL339/artifacts/red_team_phase42.py
```

## q=35 physical critical layer (separate exact candidate)

Across every high-to-high p=5..8 pair with q=35 reduced charge at least zero,
the relaxed in-band reconstruction has, respectively by p,
`(pairs,templates,candidates)=(196,64120,299),(168,140992,20),
(112,209938,2),(56,271326,0)`. All 321 candidate sources escape below
`2^71` in at most 39 odd steps, without any high-carry filter. Thus the
RL338 positive exceptions and high-to-high zero-charge baselines cannot
occur on the assumed cycle. The exact scan and an independently written
reconstructor both pass. This strengthens the physical interpretation of
RL338 but is not needed for the density-42 cap.

```
python3 .rl-work/RL339/artifacts/critical_q35_escape.py
python3 .rl-work/RL339/artifacts/red_team_q35_critical.py
```

## Direct route barrier and open work

At `rho=60`, the inherited q=35 consumer gives RHS `32546271992.519...`.
Hypothetical q=36 with the same boundary 43 gives `32546270036.602...`,
and even formal `2H>=K` in that same consumer gives
`32546200590.019...`; q=36 is not the smallest missing direct-closure
theorem. Even with every one of the `T+1` ranks positive and every phase
weight at its strict upper limit 2, the inherited linear telescope RHS at
`rho=60` exceeds `10,147,163,936`. This is a method barrier for direct
`n<1` closure through that telescope, not a contradiction for the parent.

The new cap remains 12,146,996,285 above the fixed high-carry ownership
threshold `20,390,252,058`; no R1 parent closure is claimed. The next attack
must consume exact physical identity across the remaining negative-charge
return layer or find another absolute obstruction. Do not turn the next
step into a blind total-42 singleton or q=36 census.
