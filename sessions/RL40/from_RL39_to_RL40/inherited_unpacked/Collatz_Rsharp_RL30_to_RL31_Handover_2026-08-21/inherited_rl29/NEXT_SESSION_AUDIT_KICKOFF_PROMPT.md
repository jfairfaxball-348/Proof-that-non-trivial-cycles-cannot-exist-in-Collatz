# RL30 audit/review session kickoff

Audit the attached `Collatz_Rsharp_RL29_to_RL30_Audit_Handover_2026-08-21.zip` as a skeptical research mathematician before extending the Collatz/RL work.

Do not begin by searching deeper residues. First establish the exact proof state and whether the new RL29 bridge claims are correct and useful.

## Mandatory verification

1. Read `START_HERE.md`, `RL29_AUDIT_LEDGER.md`, `RL29_SESSION_RESULTS_TO_AUDIT.md`, and `RL29_BRIDGE_DISTANCE_AND_CLOSURE_MAP.md`.
2. Run all 20 inherited verifiers under `inherited_rl27/` plus:
   - `rl29_additions/verify_rl29_exact_ownership_and_lifts.py`
   - `rl29_additions/verify_rl29_transport_scaling.py`
3. Treat any verifier failure as stop-and-repair.
4. Keep the external `R>=2^71` input explicitly external.

## Audit track A — referee the new mathematics

Independently prove or reject each of these:

1. `R==667 mod4608`, `R>=5275`, and the forced nine-bit prefixes.
2. Exact absolute ownership:
   `gcd(A0,A2,A6)=B-Y` and the displayed integer Bezout extraction.
3. Exact relative Eisenstein ownership:
   `gcd(F0,F6)=B w^2-Y` up to a unit and the displayed Eisenstein Bezout identity.
4. The `e>=67` correction-product argument.
5. The universal orbit-sum identity and the claim that synchronized columns contribute zero to the relative mode.
6. The pairwise transport identity and the “at least 47 positive-imbalance times before first synchronized u/v sign reversal” conclusion.
7. The scaled-state interval and the proposed theorem
   `H=Omega(e/log e)` distinct aligned columns containing a phase `>2.9R`.

Actively look for off-by-one errors in synchronized runs, orientation errors in rotated blocks, hidden uses of the cycle endpoint, cancellation problems, and accidental reliance on the external lower bound.

## Audit track B — reconstruct the global proof DAG

From the inherited RL20--RL27 documents, reconstruct a dependency diagram answering:

- what exactly has radius 3 proved;
- what global reduction leads to the order-3 balanced sector;
- which sectors are analytically closed versus only finitely certified;
- whether eliminating `R==91 mod288,(G,H)=(12,4)` would actually close the current RL theorem;
- if not, list every remaining bridge/case precisely.

Do not assume the answer from handover prose.

## Audit track C — quantify the remaining bridge gap

The inherited supporting-line coefficient is

`457841/1843200 = 1/4 - 2959/1843200`.

Determine quantitatively what extra product/packing gain is required to cross the contradiction threshold.

Then test the RL29 scaling theorem against that requirement:

1. Does `Omega(e/log e)` help at all with the existing coefficient argument?
2. Can the long-synchronized-run alternative be assigned a gain growing with run length, producing `Omega(e)` total weighted gain even if the raw number of high columns is only `Omega(e/log e)`?
3. Can high even phases be converted, injectively or with bounded multiplicity, into useful high odd phases/odd correction factors?
4. Is there a sharper way to use the 47-positive-imbalance transport threshold?

## Audit track D — assess the algebraic bypass

The forced rotations now recover both coprime factors of `B^3-Y^3`:

`B-Y` and `B^2+BY+Y^2`.

Check whether this can genuinely interface with the already-closed radius-3 sparse/resultant machinery. In particular, look for forced cancellation, proper-factor divisibility, low support, or resultant nonvanishing. Do not call the bridge successful merely because the factors are exactly recoverable; the natural rotated numerators are dense.

## Deliverable

Before doing new research, write an audit report with:

1. **Proof-state table:** proved / external / finite certificate / exploratory / false or needs repair.
2. **Dependency DAG:** what would have to be proved to get from the current exceptional sector to RL.
3. **Distance-to-closure assessment:** identify the smallest plausible missing theorem(s), and whether one successful theorem could close the bridge or multiple layers remain.
4. **Quantitative target:** the exact packing/product improvement needed.
5. **Recommended next attack:** choose between weighted synchronization packing, algebraic sparsification, or another route, with reasons.

Only after that audit should you continue the attack. Preserve any repaired verifier and package a new handover at session end.
