# RL271 verification

The full deterministic verifier sources, exact pair CSVs, scripts and frozen outputs are retained in the closeout bundle `RL271_Radius5_Kappa3_Flat_Sector_Closure_2026-09-07.zip`, whose SHA-256 is recorded in this session.

`FAST_SUITE_OUTPUT.txt` is the successful compressed-certificate run from the clean-unpack candidate; `REDTEAM_OUTPUT.txt` is the successful exhaustive direct-word `A<=18` all-flat replay.

The fast suite covers `[4,1]`, both three-component leaves, the four-component leaf with an independent reconstruction, and both primary/alternate singleton modular certificates. The longer direct-word red team is kept separate from the fast suite.

The connector closeout stores the human-readable verification outputs and bundle digest in-repository; the complete source/data bundle is also attached to the closeout response for transport.
