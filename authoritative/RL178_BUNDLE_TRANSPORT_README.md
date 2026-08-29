# RL178 lossless bundle transport

The authoritative RL178 handover ZIP is transported as checksummed base64 text parts for atomic connector promotion.

1. Verify transport files with `sha256sum -c PART_SHA256SUMS.txt`.
2. Run `python3 reconstruct_rl178_bundle.py`.
3. The reconstructed file must match `RL178_Negative_Compensation_and_Height_Return_2026-08-29.zip.sha256`.
4. Unpack it, verify `SHA256SUMS.txt`, then run the portable and consolidated RL178 verifiers.

The transport is lossless and changes no mathematical or proof-state content.
