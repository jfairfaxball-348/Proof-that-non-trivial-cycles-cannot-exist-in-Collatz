# RL195 portable verifier suite

Run from any directory:

`sh /path/to/package/verification/run_fast_rl195_verifiers.sh`

The wrapper locates itself and runs all10 standalone Python3 verifiers
using only the standard library. No network, repository checkout, giant
2^A/3^L integers, generated catalogue, or conversation state is required.
It disables bytecode artifacts. Every load-bearing numerical comparison
uses integers/Fraction enclosures; display decimals are not evidence.

## New components

- `verify_rl195_moment_adjacency.py`: complete symbolic boundary/partition
  checks and rigorous constant rounding J00>=9719139553;256 toy arrays,
  7 admissible,3 strict-case regressions. No actual phase enumeration.
- `verify_rl195_zero_geometry.py`: matching, doublets, exact capacity,
  all4 mechanical cells/all7 relaxed-witness cells and both height-only
  countermodels;256 toy arrays/7 admissible words. Not physical realization.
- `verify_rl195_window_reconstruction.py`: symbolic actual Bezout input,
  positive rational/denominator/arc identities for256 toy arrays/7
  admissible words,35 gaps and175 arcs, plus the trivial integral one-cycle.
- `verify_rl195_owned_local_realizability.py`: every path from all42
  roots under212 through depth3, counts540/4517/34039,44 sign patterns,
  two local seed witnesses per path under t=1mod3^5, unchanged digest and
  all336 repaired-helper cases. No global p/L compatibility is inferred.

## Inherited live components

The6 earlier Python scripts are byte-preserved from incoming RL194. They
verify the RL178 early signature, RL193 physical-debt constants, RL194
rank corridor, weight/moment/occupation, depth3 owned parity graph and the
complete chronological range1..1826035. Their original RL labels are
correct provenance. No later start or transition depth is silently covered.

## Independent auxiliary reviews

Optional reproducible review commands from the package root:

`python3 -B reviews/verify_adjacency_independent.py`

`python3 -B reviews/verify_owned_seed_red_team.py`

`python3 -B reviews/verify_window_independent.py`

These respectively use128 logarithm terms/degree12 exponentials;85 small
word/27931-residue checks and all34039 final paths at t=0mod3; and an
independent affine-composition denominator replay. The owned checker has
only its import path mechanically adapted to the packaged verifier.
Historical NOT_PROMOTED wording in auxiliary audit artifacts describes
their research-stage provenance, not the final root proof classification.

Proofs are in proofs/; reviews record original source hashes. The component
portability audit checks allowed status/path changes and preserved logic.
Mathematical PASS does not replace bundle/manifest/fresh-unpack/Git gates.
