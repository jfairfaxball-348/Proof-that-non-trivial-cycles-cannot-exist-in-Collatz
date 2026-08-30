# RL186 red-team report

Date: 2026-08-30

Result: **PASS with no closure claim**.

## Checks

1. **Incoming authority — PASS.** `main` and the authoritative tree were frozen at `ee97900471b6477b567daf4506fdc9ca2b363f1a` / `0d2280edc957e3d89eac46b50ad4bb159ff0ffff`; RL185 recorded manifest, clean verification, fast-suite, and red-team PASS were accepted under verification economy.
2. **First-defect parity — PASS.** `C_tau` is odd only at the first nonzero ordinary defect; this is what permits `D=v_2(C_0)`. No parity claim is extended across carry.
3. **Starting numerator range — PASS.** A zero-prefix start has equal endpoint heights `h_0 in {0,1}`, and the strict RL181 normalized-gap corridor is applied after multiplying by `2^h_0`.
4. **Late enumeration completeness — PASS.** For each `tau=28,...,39`, every multiple of `2^tau` in both shallow starting intervals is enumerated, its exact 2-adic valuation removed, and every terminal H satisfying both the strict gap corridor and mechanical envelope is retained.
5. **Necessary versus physical — PASS.** Surviving enumerated `(C_0,H)` possibilities are necessary candidates only; none is asserted physically realized.
6. **Coverage multiplicity — PASS.** The selected object is the first defect, so a physical first-defect phase can receive at most one start for each admissible offset `tau`.
7. **Tau-39 isolation — PASS.** The inherited extremal rigidity gives `C_1=3*2^38`; a shallow successor would violate the exact normalized-gap upper bound. With `d_j=1`, common height is nondecreasing thereafter.
8. **Zero-block density — PASS.** In a block ending at a nonzero defect, potential `tau>=37` shallow starts occupy only distances 37, 38, 39. A distance-39 shallow start excludes later shallow positions; otherwise there are at most two, and two require at least 39 phase positions. The cyclic density is therefore at most `2/39`.
9. **Weighted charging — PASS.** Low (`H<=22`) and high (`H>=23`) selected defects are partitioned before charging, so their separate capacity constants add without double counting. The worst case assigns the maximum permitted start mass to the cheaper high-height class.
10. **Signed consumer — PASS.** Carry is added separately and remains positive `>1/2`; the exact total flow is independently enclosed in `(0,1/2)`.
11. **Variation versus excursion — PASS.** `>59` in each K direction is not promoted as a prefix excursion or corridor contradiction.
12. **Historical barriers — PASS.** No arbitrary residue count, generic rank/lattice capacity, or unconstrained long local-template enumeration is revived.
13. **No false closure — PASS.** The high type, preferred branch, Gate A/B, non-trivial-cycle exclusion, and Collatz remain open.

## Remaining quantitative barrier

The improvement is genuine but still many orders of magnitude below the K-corridor scale. The next useful consumer must bound long zero prefixes at several scales, not merely sharpen the last two or three offsets.
