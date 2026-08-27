# RL129 authoritative-package integrity repair

## Trigger

The RL130 incoming gate, run from commit
`2d34a4e7b4746eaa3e32688c3d24bf6cdea7c4d5`, found that the outer
sidecar for `RL129_Quotient_Descent_L13_to_L40_and_L41_Frontier_2026-08-27.zip`
asserted a SHA-256 different from the tracked archive's actual SHA-256.

## Investigation

- The archive extracted successfully into a clean temporary directory.
- Every extracted package file passed the package's internal `SHA256SUMS.txt`.
- The extracted package directory was byte-for-byte identical to the tracked
  package directory (excluding the ignored Finder metadata file).
- The complete RL129 fresh-unpack fast verifier suite passed from that clean
  extraction.

Thus the mathematical package and its internal manifest are unchanged and
verified.  The defect is confined to the stale outer sidecar value.

## Repair

The sidecar is corrected to the actual SHA-256 of the unchanged tracked
archive:

`f1aabe6afed1b69619cdd52f7400c66b99e6c089ecb9d529ccc7a3f3647c0d83`

No theorem, finite certificate, scope statement, verifier, archive payload,
or promoted frontier is modified.  This is an integrity repair, not an RL
research-state promotion.

## Required post-repair gate

Run the outer sidecar check, fresh unpack, internal-manifest check, and
`verification/run_fast_rl129_verifiers.sh` before beginning RL130 research.
