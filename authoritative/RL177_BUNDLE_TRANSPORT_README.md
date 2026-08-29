# RL177 lossless bundle transport

The authoritative RL177 handover ZIP is transported as checksummed base64 text
parts because this connector worker cannot atomically upload the binary ZIP
blob directly.

1. Verify the transport files with `sha256sum -c PART_SHA256SUMS.txt`.
2. Run `python3 reconstruct_rl177_bundle.py`.
3. The reconstructed file must match
   `RL177_Early_P_Shift_Mismatch_Compensation_and_Height_Split_2026-08-29.zip.sha256`.
4. Unpack it and verify the internal `SHA256SUMS.txt`, then run the portable
   and consolidated RL177 verifiers.

The transport is lossless; it changes no mathematical or proof-state content.
