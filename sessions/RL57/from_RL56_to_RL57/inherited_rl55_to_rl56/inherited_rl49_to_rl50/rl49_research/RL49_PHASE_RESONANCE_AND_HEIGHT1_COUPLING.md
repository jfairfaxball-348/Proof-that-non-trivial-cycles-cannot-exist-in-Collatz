# RL49 — phase-resonance squeeze and height-one synchronized-mass coupling

Date: 2026-08-22

## Status

Two new analytic identities/inequalities for the retained one-excursion/full-phase branch. They do **not** close RL by themselves.

The first uses the inherited external computational floor `R# >= 2^71` only for its numerical continued-fraction consequence. The algebraic phase bound itself is unconditional within the live RL48 conventions.

## 1. Full phase gives a much stronger resonance squeeze

Write

- `X=2^a`, `Y=3^ell`, `M=X-Y`,
- `zeta=X/Y`, with `1<zeta` and retained window `zeta^2<16/15`,
- `k=t+3`,
- `D=Qx-Qy >= 0`.

RL48 gives

`Q(v)=75*3^(ell-3)+2X-2^(a-k+1)-12D`.

Since `Y=27*3^(ell-3)`, under full phase

`N=(Q(v)+4Y)/M`

satisfies the exact identity

`N(zeta-1)=2zeta+61/9-zeta/2^(k-1)-12D/Y`.

Therefore, because `D>=0` and the terminal power term is positive,

`N(zeta-1) < 2zeta+61/9`.

The retained window gives `zeta<31/30`: indeed `(zeta-1)^2>=0` implies `2zeta<=zeta^2+1<31/15`. Hence

`boxed: N(zeta-1) < 398/45.`

This is phase-specific; the old RL19/RL20 global product bounds do not contain this constant-size quotient constraint.

Every state of a hypothetical nontrivial positive cycle is at least its least state. Conditional on the inherited external verified floor `R#>=2^71`,

`boxed: zeta-1 < 398/(45*2^71) ~= 3.746e-21.`

Thus a full-phase RL object is forced into an ultra-near-resonant branch.

## 2. Continued-fraction consequence

Let `beta=log(3)/log(2)`. Since `gcd(a,ell)=1` in the retained branch,

`a/ell-beta = log(zeta)/(ell log 2)`.

Using `log(zeta)<zeta-1`, the phase bound gives

`0<a/ell-beta < 398/(45*2^71*ell*log 2)`.

Whenever

`ell < 2^71 log 2 / (2*(398/45))`,

Legendre forces `a/ell` to be an above-`beta` continued-fraction convergent.

The exact rational-interval verifier gives the rigorous gate

`ell <= 92,524,042,457,747,860,050`.

Among all above-`beta` convergents below that gate, every one is excluded by the phase bound except exactly

`a = 123,139,092,617,126,647,266`,

`ell = 77,692,117,359,936,589,403`,

`q=a-ell = 45,446,975,257,190,057,863`.

So, conditional on `R#>=2^71`, any full-phase solution with denominator below the Legendre gate is reduced to one explicit enormous coprime pair.

This is a narrowing theorem/certificate, not a global contradiction: above the Legendre gate non-convergent approximants are not ruled out by this argument alone.

## 3. Exact coupling that removes the RL48 height-one mass relaxation

RL48 proved that the old separable Gate-A relaxation fails because it treats arbitrarily many synchronized height-one ranks independently. The requested missing object was an exact telescoping identity for that mass.

Use local internal-column coordinates. Before an edge at local column `i`, let

`p = number of x-ones already used`,

`g = 2^i/3^p`.

At height `d=1`, a same-bit edge is either `00` or `11`.

For `00`,

`T'=T/2`, `g'=2g`, hence

`g'T' = gT`.

For `11`,

`T'=(3T+2)/2`, `g'=2g/3`, hence

`g'T'-gT = 2g/3`.

At height one the x/y rank counts are aligned. On an `11` edge the moved rank has zero displacement `delta=0`, its rank weight is

`w = 2^i/3^(p+1)=g/3`,

and its exact RL47 rank-transport contribution is

`w(3-2^0)=2w=2g/3`.

Therefore on **any maximal height-one synchronized segment**,

`boxed: sum_(11 on segment) 2w = (gT)_exit-(gT)_entry.`

All `00` edges disappear from this identity and arbitrarily long zero-area `11/00` pumping is compressed to two boundary values.

This is exactly the kind of coupling missing from the RL47/RL48 separable envelope.

## 4. Why this changes the attack order

The best next Gate-A proof attempt is no longer to optimize independent rank positions. Instead:

1. decompose the exact one-excursion path into maximal height-one synchronized segments plus skew/higher-height excursions;
2. replace every synchronized segment by the boundary term `(gT)_exit-(gT)_entry`;
3. charge only skew/higher-height pieces against the true area `H` and prefix cap;
4. combine this with the exact terminal valuation `T+1=2^(t+3)`;
5. for actual full-phase objects, also impose the phase-resonance squeeze above, which makes `zeta` essentially 1 and supplies an additional rank-defect/state-size constraint.

The goal is a **phase-aware Gate-A theorem for genuine RL objects**, not the stronger and unnecessary statement for every path in the relaxed automaton.

## 5. Strategic closure target

A proof-ready target is:

> **Coupled height-one/full-phase lemma.** No retained one-excursion path satisfying the exact prefix cap, full-phase quotient condition, and terminal value `T+1=2^(t+3)` can have `H<=t+2`.

This would close the required Gate-A inequality on the actual phase branch while simultaneously rejecting the fake structural paths responsible for the RL48 method barrier.

After that, attack the remaining full-phase branch with the exact quotient/four-swap arithmetic, not with the invalid radius-3 metric shortcut.

## Verification

- `phase_squeeze/verify_rl49_phase_resonance_squeeze.py`: exact rational log intervals, continued-fraction prefix, and the unique surviving sub-gate convergent.
- `phase_squeeze/verify_rl49_height1_mass_telescoping.py`: exact column-by-column regression of the synchronized-mass telescoping identity on the audited RL47 `(65,41), t=2` structural witness.
