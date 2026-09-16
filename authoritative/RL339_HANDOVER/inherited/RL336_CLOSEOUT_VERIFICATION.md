# RL336 closeout verification

Date: 2026-09-16. Status: GREEN FOR ATOMIC PROMOTION once ZIP/sidecar fresh-unpack and authority snapshot checks pass. Incoming BASE_HEAD: `496325dd80bf220c99ef9292d14ce66ec2b954d1`.

The strict flat-authority startup adapter preserved the incoming committed tree identity `fa2cd895e4d515a5bbefdd04f5d66f6d0bf4ecca`; local HEAD matched live `origin/main`. Incoming `verify_rl335_physical_and_q28.py`, `verify_rl335_consumer.py`, and `red_team_rl335_q28.py` all passed in isolated Python. The parser mismatch was mechanical and did not change mathematical authority.

Candidate checks from the frozen proposed successor authority:

- `verification/verify_rl336_q32_prefix.py`: GREEN; p=5 178 pairs / 63,234 templates / 4,886 distinct 60-prefixes, p=6 36 pairs / 35,590 templates / 5,778 distinct 58-prefixes; 2,242 graph edges, q=32 potential range 0..43.
- `verification/verify_rl336_q32_consumer.py`: GREEN; exact rational finite maximum rho=60, uniform bridge cap `32546278588`, ordinary Q256 handoff below cap.
- `verification/verify_rl336_zero37_part1.py` through `part3.py`: GREEN; exact disjoint factors 0..36, 5,343,788 owned candidates, maximum escape 229.
- `verification/verify_rl336_zero36_part1.py` through `part5.py`: GREEN; exact disjoint factors 0..35, 15,512,438 owned candidates, maximum escape 234.
- `verification/red_team_rl336.py`: GREEN; independent three-way residue lifting, reversed-edge q=32 relaxation, maximum-escape witness checks.

An independent C++ scan agreed with the portable Python zero-run counts and maxima for every factor of both lengths. No certificate range gap or inherited mathematical contradiction was found. Knowledge catalogues are stale/deferred unless separately rebuilt and validated during this closeout.

The ZIP contains an internal `SHA256SUMS.txt` and is paired with the top-level `.zip.sha256` sidecar. A clean fresh unpack, internal-manifest check, complete portable fast suite, exact candidate tree comparison, atomic commit/push, and remote readback are required before RL336 is complete.
