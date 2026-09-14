# RL320 fresh-unpack verification

Date: 2026-09-14
Status: PASS

The candidate `RL320_to_RL321_Handover.zip` was unpacked into clean temporary
storage at
`/var/folders/8w/bg8m169j4_x795b3ltzvtbyr0000gp/T/tmp.3VWpNnahEj`.

Verified:

1. outer SHA-256 equals
   `24acb32ffd36899760f63b0f477df78b78eb3f855e4dd94a90b4877f0cec5756`;
2. all nine internal manifest entries match;
3. `verify_rl320_weighted_factors_and_clocks.py` passes;
4. `verify_rl320_late_row_bounded_surrogate.py` passes;
5. the unpack contains the frozen incoming target, closeout, proof ledger,
   red-team report, verifier output, session handover, successor target, and
   both portable verifiers.

The bounded loops are regression evidence. The first-survivor logarithmic
comparison is an exact rational-interval certificate in the scope stated by
the proof ledger.
