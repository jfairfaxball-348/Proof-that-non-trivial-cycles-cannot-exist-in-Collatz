# RL200 Certified Facts and Proof Ledger

Date: 2026-08-31. All physical statements remain conditional on the sole high branch `(37,0,23,-1)`.

## Newly proved analytic mathematics

- The inherited H21 terminal normalized p-gap is
  `Delta_H21=(7*3^35)/2^21`, independent of the RL199 oriented-lift class and terminal sign.
- Writing the canonical terminal mechanical rank as `r`, with inverse phase
  `i=pr mod L`, `Ai=nL+r`, the terminal corrected potential is exactly
  `K_H21(r)=Delta_H21*2^n/3^i`.
- `K_H21(r)` is strictly decreasing in canonical mechanical rank.  The proof uses
  `delta=A ln2-L ln3`, `0<delta<2^-40`, and
  `ln rho(r)-ln rho(s)=((i_r-i_s)delta+(s-r)ln2)/L>0` for `r<s`.
- Intersecting the exact terminal K value with the inherited global corridor
  `128081997553 < K < 146795909391` sharpens the H21 terminal-rank core from
  `[23369453298,41775866136]` to
  **`[25583192106,41775866136]`**.
- Of the inherited 14 H21 isolated rank deletions, 12 lie in the refined interval.  The resulting
  necessary-rank count is **16,192,674,019**, removing **2,213,738,806**
  previously surviving necessary ranks.
- Over the refined core, the `tau=34` start rank is in
  `[40886621976,57079296006]`, the source one step before the `tau=35` start is in
  `[17517168678,33709842708]`, and the next earlier source is in
  `[74596464685,90789138715]`.  Hence the first two extra prehistory mechanical bits are
  exactly `1,2`.
- For any positive odd unit `y mod 3`, target height `h>=0`, and prescribed mechanical bit
  `c in {1,2}`, there are infinitely many positive odd unit predecessors
  `x=(2^a y-1)/3` with nonnegative source height.  Modulo 9, exactly two exponent classes
  modulo 6 satisfy both integrality and unit conditions.
- Consequently any finite **uncoupled** oriented reverse prehistory using only prescribed
  mechanical bits, independent odd-integrality/unit conditions, and nonnegative heights can be
  extended for every one of RL199's four `eta mod 18` classes.  Such a consumer cannot select
  terminal sign or H21 state.

## Exact certificate

`verification/verify_rl200_h21_k_rank_and_prehistory.py` checks the rigorous logarithmic
enclosures, strict rank monotonicity, exact K-corridor crossing, inherited deletion accounting,
rank-shift intervals, the modulo-9 reverse-prehistory theorem, and representative arithmetic in
all four surviving oriented-lift classes.

## Inherited state retained

RL199's exact oriented lift, mod-9 state selector, parity/sign selector, four classes
`eta=0,8,9,17 mod 18`, Hensel exclusions, and common-pair information-loss theorem remain
unchanged.  The H21 `{33,34,35}` charging family remains binding.  All prior finite-cutoff,
canonical-lift, physical-versus-necessary, rank-versus-time, and variation-versus-excursion
guardrails remain in force.

## Open obligations

RL200 does not remove an `eta mod 18` class, decide `e35`, decide terminal sign, prove physical
H21 incidence, release the H21 charging budget, close the sole branch or Gate A/Gate B, exclude
non-trivial cycles, or prove Collatz.
