# RL146 bundle transport

Lossless text transport for `RL146_Contact_Carry_Order_Closure_2026-08-28.zip`.

Reconstruct with:

`python3 reconstruct_rl146_bundle.py`

The script verifies `PART_SHA256SUMS.txt`, concatenates the Base64 parts, decodes the ZIP, and verifies the expected ZIP SHA-256.
