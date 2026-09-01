# RL224 candidate-coupled height closure and e=16 rank deletion

Date: 2026-09-01.

**Classification: exact recurrence theorem plus gap-free finite certificates.**

## 1. Candidate coupling

The inherited e=16 phase-16 coordinate is

`eta=eta_*+3^17 k`,

`y_16=2^34 eta-1-3^16*2^13`, `h_16=1`.

For a fixed candidate `(eta_*,k)`, define recursively

`a_i=v2(3y_i+1)`,

`y_(i+1)=(3y_i+1)/2^a_i`,

`h_(i+1)=b_(i+1)-b_i+h_i-a_i`.

The recurrence uses the exact current odd integer, so later parity/valuation data are not free choices. This is the candidate-to-continuation coupling required by RL224.

The inherited H21 interface requires every physical height to be a nonnegative integer. Hence

`a_i>b_(i+1)-b_i+h_i`

is an exact contradiction for that candidate.

## 2. Exact finite input

The portable reconstruction freezes the inherited two-sided e=16 candidate family from the exact prefix recurrence and root-window/Hensel conditions. Before the already-certified RL216 complete-prefix deletion it reproduces:

- 45,046 H21-compatible exact prefixes;
- 331,935,455 candidates in the two-sided window;
- 170 terminal-Hensel deletions;
- 331,935,285 post-Hensel candidates.

Removing RL216's `Q=43,013,953` prefix leaves the current base family of **45,045 prefixes and 331,927,916 candidates**. RL217's phase-51 consumer is a necessary filter of this same family and left the incoming **139,581,280**.

The reconstructed-record SHA256 is pinned in `certificates/rl224_reconstructive_summary.json`; the portable verifier regenerates this exact source table before rerunning the full finite scan.

## 3. Gap-free phase-200 scan

Nine contiguous chunks cover prefix indices

`1..5000`, `5001..10000`, `10001..15000`, `15001..20000`,
`20001..25000`, `25001..30000`, `30001..35000`, `35001..40000`,
`40001..45045`.

There are no omitted or duplicated prefix indices in the source closeout. Their aggregate hashes are retained only as provenance. The promoted reconstructive verifier independently regenerates all 45,045 prefix records and reruns the complete finite family directly, so no stored chunk or aggregate TSV is load-bearing.

The result at transition index 200 is exactly **4,242 candidates in 4,054 prefixes**.

## 4. Residual direct closure

The portable reconstructive verifier finds every phase-200 survivor during the full scan and immediately replays each from phase 16 through transition 346, requiring a first mandatory-height failure for all 4,242.

Every residual candidate fails by transition index 346. The last failure has `(idx,Q,k)=(44955,153134585,31480)` and forces `h_347<0`.

Therefore the exact necessary e=16 candidate set is empty.

## 5. Rank consequence

The inherited above-p small-offset transport assigns `e=16` to terminal rank `34,124,151,203`. Since every physical e=16 realization would have to lie in the exhausted finite family and obey nonnegative height, no such realization exists. This removes exactly that rank from the necessary-rank ledger.

The global frontier count is therefore **13,415,865,870**.

No other terminal rank, H21 charge, Gate, or global Collatz conclusion is changed.
