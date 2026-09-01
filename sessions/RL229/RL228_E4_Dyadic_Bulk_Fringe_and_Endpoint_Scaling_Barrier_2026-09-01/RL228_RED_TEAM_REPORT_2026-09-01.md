# RL228 red-team report

Date: 2026-09-01.

## RT1 — reproduce RL226 through transition 43

**PASS.** The verifier exactly reproduces all RL226 state counts, transition-failure counts, height survivors, terminal-Hensel disjointness, and combined survivors through transition 43.

## RT2 — preserve finite-window endpoint information

**PASS.** The theorem writes every cylinder count as `floor(N/2^m)+epsilon`, explicitly preserving the endpoint bit. No residue-independent merge is asserted when `epsilon` matters.

## RT3 — exact common failure modulus

**PASS.** `cap=E_(i+1)-m`, so every failure extension has total precision `m+cap=E_(i+1)`.

## RT4 — exact phase-44 state count

**PASS.** Since `E_44=31` and `N>2^31`, every admissible phase-44 residue cylinder intersects the window. A separate precision dynamic programme gives **7,743,281**, while its phases 36..43 match the full cylinder traversal.

## RT5 — endpoint-dominance boundary

**PASS.** `E_45=33` and `2^33>N`, so the transition-44 bulk coefficient is exactly zero. The next exact count is pure endpoint-residue incidence.

## RT6 — anti-merge witness

**PASS.** Two exact phase-44 singleton representatives are replayed directly. Both have precision 31 and height 0, but one has next valuation 1 and the other 4 against cap 2. Current cardinality does not determine future fate.

## RT7 — no scope inflation

**PASS.** No transition-44 deletion, rank deletion, e=28/33/40/45 transfer, physical H21 charge, Gate closure, or global exclusion is claimed. The barrier does not purport to rule out all future compressors.

## Verdict

**PASS — RL228 meets success class C and must pivot rather than deepen the e=4 endpoint traversal.**
