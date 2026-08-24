# RL27 method evidence and no-go experiments

Date: 2026-08-21

## Status warning

Everything in this note is **exploratory/session evidence**, unless it simply restates an analytic theorem cited from the proof-status note. These experiments guide strategy; they are not proof certificates and must not be promoted to unconditional mathematics.

Scripts are retained in `rl27_experiments/` for reproduction and extension.

---

## 1. Simultaneous three-start least-state lifting does not collapse locally

The experiment lifts `R==27 mod32` through deeper powers of two while simultaneously enforcing least-state inequalities for the three starts

`R`, `R+12`, `R+4`.

Session runs found many viable classes rather than a dying tree, including:

- depth 20: 109 viable classes;
- depth 25: 794 viable classes;
- depth 30: 6,458 viable classes;
- depth 35: 43,996 viable classes.

The observed survivors also satisfied the stronger prefix growth test `3^(#odd) >= 2^j` on all three starts, so they were not surviving merely because of a small additive affine term.

### Strategic conclusion

A finite-prefix least-state lift by itself is not currently a plausible closure mechanism. A theorem would need a genuinely nonlocal invariant or a proof that all infinite continuations eventually violate some additional cycle condition.

Primary script: `test_three_start_lifts.py`.

---

## 2. Raw 3-adic tail-density recursion is too weak by itself

From the exact identity

`U-V=8B+12Y`,

one can write terminal valuation-tail congruences modulo `3^m` involving cumulative valuations of the adjacent blocks. The attractive hope was that these congruences might force a combined terminal valuation average above the balanced budget `2b/e ~= 2 log_2(3) ~= 3.17`.

The exploratory DP did not support that. It found admissible tails with combined average as low as approximately

`33/12 = 2.75`

in the tested depth range, well below what would be needed for the desired contradiction.

The three-block version with the exact endpoint classes likewise did not immediately force the needed density penalty.

### Strategic conclusion

The 3-adic congruence needs extra phase ownership, crossing information, or sparse-factor structure. Do not continue it as a bare average-valuation argument.

Scripts: `test_3adic_tail_dp.py`, `test_3block_3adic_tail_dp.py`.

---

## 3. Synchronized gap experiment — useful lead, not invariant

At equal-odd-count synchronization times, the three trajectory gaps become exact numerator-difference objects. A depth-30 exploration found 365 distinct synchronized gap pairs. The endpoint target

`(-8,-12)`

was not observed in that finite search, and sampled synchronized pairs kept the `R` trajectory below the other two.

This is **not** proof of sign preservation: a genuine cycle in the exceptional geometry must eventually reach the negative endpoint pair, so any true invariant of that form would itself exclude the sector and therefore requires proof.

### Strategic conclusion

Study the **first synchronized sign reversal**, not a finite catalogue of synchronized residues. It is the first point where an exact numerator difference defeats the initial positive affine gap.

Scripts: `search_sync_invariants.py`, `analyze_sync_excursions.py`.

---

## 4. Countermodel searches

The scripts `search_negative_countermodel.py` and `search_periodic_2adic_countermodel.py` explore whether long or periodic 2-adic-style continuations can satisfy the prefix growth constraints. These are diagnostic tools only. They should be used to falsify proposed purely local invariants before investing in an analytic proof.

---

## 5. Research discipline for RL28

A productive proposed lemma should survive the following adversarial tests before being elevated:

1. Can the simultaneous lift scripts construct arbitrarily deep finite countermodels to it?
2. Does the raw 3-adic tail DP admit a low-valuation witness?
3. Does the lemma actually use the endpoint permutation / synchronized sign reversal, or is it only another one-block prefix bound?
4. Does its gain scale with `e` or another global size parameter?
5. Does it preserve the exact distinction between analytic proof, finite certificate, and external computational input?
