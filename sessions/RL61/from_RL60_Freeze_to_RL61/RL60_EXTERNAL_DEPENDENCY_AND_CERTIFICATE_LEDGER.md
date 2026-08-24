# RL60 external dependency and certificate ledger

Date: 2026-08-23

## 1. Purpose

This file prevents external computations and session-local finite searches from being silently upgraded into analytic theorems during the RL61 whole-tree audit.

## 2. Stable inherited external floor

RL50 retained Barina's peer-reviewed verification through `2^71` as the safe accepted computational floor for relevant cycle-state arguments.

Classification: **external peer-reviewed computational certificate**.

The audit should still confirm the exact theorem/interface used by the RL proof, but this is the stable external input retained after RL50.

## 3. Demoted Ansari extension

RL50 explicitly demoted the earlier use of Ansari 2025 to extend the floor to `4*3^44+2`, after an exact residue audit found the printed induction identity used in the relevant lemma already fails at `n=1 mod 36`.

Classification: **do not use as an accepted dependency** unless independently repaired from a different valid theorem.

## 4. Live Barina project status

Earlier sessions observed a live verification status around `2075*2^60` on 2026-08-22/23.

Classification: **live external computation / not part of the stable proof ledger** unless freshly re-audited and archived.

Do not confuse this with the peer-reviewed `2^71` result.

## 5. RL60 path-record-envelope reduction

RL60 used Barina's published path-record table as a complete record-peak envelope below `2^71` and derived the provisional result

`K <= 129`.

Classification: **external computational certificate, interface audit required**.

Required audit items:

- source identity and publication/version date;
- exact definition of the shortcut map / path record used;
- completeness range (`all starts below 2^71`, not merely sampled records);
- exact record-envelope row used near the K131 terminal target;
- correct conversion from target peak to a lower bound on starting value;
- correct use of the RL59 terminal-mass inequality;
- exact first contradictory odd exponent.

Until these are checked, keep the stronger interval

`25 <= K <= 129`

and its huge coupled `z` interval in a separate **external/audit-pending** box.

## 6. RL60 residue/minimal-counterexample finite certificates

Source preserved:

`verification/residue_interval_cert.cpp`.

It encodes a residue-class/minimal-counterexample descent over the shortcut map and can certify large intervals of starting values without scanning each start independently.

During the session it was used to reproduce/extend thresholds through K39.

Classification in this handover: **exact finite computation, replay required for publication-grade reproducibility because raw per-chunk logs were not preserved**.

The next audit may promote these once the supplied source is independently inspected and replayed.

## 7. Analytic versus finite boundary

The following distinction must remain explicit:

- The terminal hit predicate and the conversion from a certified `N(K0)` to a `z` lower bound are analytic/arithmetic consequences of the RL59 framework.
- The numerical value of `N(K0)` for a given threshold is a finite certificate unless a separate analytic lower-envelope theorem is proved.
- The 3-adic reverse-grammar observations are analytic local structure, but they do not yet prove all threshold values uniformly.

## 8. External-source freeze note

This bundle records the source names/roles rather than embedding a web snapshot. The RL61 audit should fetch the current authoritative sources, record exact URLs/version dates, and archive whatever finite data are actually used in a promoted theorem.
