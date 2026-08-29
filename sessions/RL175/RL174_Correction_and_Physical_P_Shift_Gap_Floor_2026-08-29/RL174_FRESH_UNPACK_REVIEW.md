# RL174 fresh-unpack review

Verify the outer ZIP sidecar, unpack into a new empty directory, verify
`SHA256SUMS.txt`, then run:

`python3 verify_rl174_report.py .`

Confirm that the RL173 correction/demotion ledger is present and that the
report distinguishes the auxiliary `F3` functional from the corrected
physical `F2` functional.
