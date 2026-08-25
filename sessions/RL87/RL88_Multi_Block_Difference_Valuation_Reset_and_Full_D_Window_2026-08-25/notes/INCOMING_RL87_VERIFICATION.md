# Incoming RL87 verification — 2026-08-25

Supplied files:

- `RL87_Aperiodic_Quotient_Complexity_Physical_Packing_2026-08-25.zip`
- matching `.sha256` sidecar
- supplied `RL87_FRESH_UNPACK_VERIFICATION_2026-08-25.txt`

Current-session checks:

- outer SHA-256: PASS;
- fresh unpack: PASS;
- internal `SHA256SUMS.txt`: PASS;
- `bash verification/run_fast_rl86_verifiers.sh`: PASS.

The fast verifier reproduced:

- first Farey pair `(114208327604,72057431991)`;
- `h=27021536997`;
- pure-odd re-entry depth/index bounds;
- RL85 fallback return span `<=43234459194`;
- RL85 spaced-distinct quotient count `>=930959`.

No historical expensive verifier was rerun.
