# RL339 closeout verification

Date: 2026-09-16. Status: GREEN FOR THE PROMOTED SCOPED CLAIMS after candidate checks and fresh-unpack transport verification.

Incoming BASE_HEAD `1d21ed6023b9e129cfdf4f8450a8b956a58c6eab`; incoming committed authoritative tree `cfbc3e1a14e85199035ef7b4f0fa87b17617f9ff`. The candidate is a physical ZIP at top-level successor `authoritative/`, with an outer `.zip.sha256` sidecar and internal `SHA256SUMS.txt`. The ZIP root carries the RL339 handover package, one live RL340 target, portable fast verifier, independent red team, and exact reproduction scripts. Fresh-unpack, manifest, and fast-suite checks were performed before atomic promotion. The outer checksum is given by the sidecar and must be checked on each startup.

## Exact finite scans

Primary reconstruction commands (run from the package root):

- `python3 -I verification/reconstruct_total43.py 8 20`
- `python3 -I verification/reconstruct_total43.py 21 21`
- `python3 -I verification/reconstruct_large_singletons.py`
- `python3 -I verification/reconstruct_q35_critical.py`

Independent commands:

- `python3 -I verification/reproduce_total43.py`
- `python3 -I verification/reproduce_large_singletons.py`
- `python3 -I verification/reproduce_q35_critical.py`

All pass with the exact counts and escape maxima in `RL339_EXACT_CERTIFICATE.md`. Complete observed output is frozen in `sessions/RL339/verification/`.

## Portable fast checks

- `python3 -I verification/verify_rl339_fast.py`: `PHASE42_CAP_GREEN`, endpoint floor 32,537,248,343, optimal h 24,281,914, all-rho monotonic checks green.
- `python3 -I verification/red_team_rl339.py`: `PHASE42_RED_TEAM_GREEN`, 29 zero-slack pair labels, the same cap floor independently.

The candidate ZIP was fresh-unpacked in an isolated temporary directory. Its internal SHA256 manifest and fast verifier passed; the red team passed from the clean unpack. No inherited expensive history was rerun beyond current live dependencies. The incoming authority snapshot and live remote HEAD were checked before staging; the intended successor has one live target and one ZIP/sidecar pair. Knowledge catalogues are `stale/deferred` unless a separate successful refresh is recorded; they are not mathematical authority.
