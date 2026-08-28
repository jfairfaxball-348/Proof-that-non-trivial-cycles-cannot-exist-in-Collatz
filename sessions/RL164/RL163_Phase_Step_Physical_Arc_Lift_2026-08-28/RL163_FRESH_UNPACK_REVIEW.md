# RL163 fresh-unpack review checklist

1. Verify the outer ZIP sidecar before unpacking.
2. Unpack to a new empty directory.
3. Run `shasum -a 256 -c SHA256SUMS.txt`.
4. Run `python3 verify_rl163_report.py .`.
5. Confirm the report retains its `g=1` and non-closure limitations.
