# RL152 bundle transport

Lossless text transport for `RL152_Global_Depth_Budget_and_Reciprocal_Width_Bridge_2026-08-28.zip`.

Run:

`python3 reconstruct_rl152_bundle.py`

The script verifies `PART_SHA256SUMS.txt`, concatenates the Base64 part(s),
decodes the ZIP, and verifies the expected ZIP SHA-256.
