# RL195 candidate component portability audit

Date: 2026-08-31. **PASS — candidate component audit, not promotion.**
Incoming job RL195; BASE_HEAD `df980ce3df6fa3e8906a934692221917af25644a`.
Reviewer: independent mechanical-zero-geometry worker.
`CLOSEOUT_LOCK` was active throughout. No new mathematics, route exploration,
history audit or phase-range extension was performed.

## 1. Audited scope and result

Candidate package:
`.rl-work/RL195/candidate/authoritative/`.
Scratch paths below are relative to `.rl-work/RL195/`; packaged paths are
relative to the candidate package. Inherited source paths are relative to
the current incoming `authoritative/` at the stated BASE_HEAD.

Completed:

- full unified-diff comparison of all4 new proof notes and4 new verifiers
  against their audited scratch sources;
- byte-for-byte `cmp` and SHA256 agreement for all4 inherited RL194 proof
  notes and all6 inherited Python verifiers;
- comparison of all3 auxiliary review scripts;
- inspection of the complete10-script wrapper and its README;
- successful execution of the complete wrapper from the candidate package,
  followed by all3 optional auxiliaries with `python3 -B`;
- post-execution SHA256 readback of every audited candidate component,
  with unchanged identities and no candidate bytecode artifacts.

**No discrepancy, proof-logic change, numerical change, unreviewed range
extension or unresolved finding was found.** Differences listed below are
only the authorized status/path, notation and completed-review wording.
The owned seed helper is the repaired, independently accepted source; the
old initial-mod3 restriction has not reappeared.

This audit does not substitute for root-document integration, final bundle
construction, sidecar/manifest verification, clean fresh unpack, authority
snapshot, atomic commit/ref advancement or remote readback. Those remain
the main worker's separate closeout gates. The reviewer did not edit the
candidate, authority or Git state; only this scratch audit was written.

## 2. New proof notes: exact mappings, hashes and all diff categories

### Moment-to-adjacency proof

Source: `artifacts/MOMENT_TO_ZERO_ADJACENCY.md`.
Candidate: `proofs/RL195_MOMENT_TO_ZERO_ADJACENCY.md`.

Source SHA256: `eed5185d8313e9366e6d749cfa506392a6e9742501656da2e91fb389f8d14bac`.
Candidate SHA256: `4c8e53722e93e81f9a8f3418bdd3f00ffd2e516aa219cbfd5d25158779b44141`.

Exactly3 unified-diff hunks: candidate status becomes reviewed closeout
status; the verifier command uses the packaged path; the final review status
is completed and J is identified as root-report J00 rather than branch J=23.
No formula, number, inequality, proof step or scope obligation changes.

### Mechanical zero geometry proof

Source: `agent_zero_geometry/ZERO_GEOMETRY.md`.
Candidate: `proofs/RL195_ZERO_GEOMETRY_AND_RELAXATION_BARRIERS.md`.

Source SHA256: `44b45350557bce9972c6d9fa1f3cf2258068c806fe53809bb1f26a2e1bb1cf71`.
Candidate SHA256: `4bcac24ebcec52fe566b22b2c25e8e73bb61e2e4c51fd3b8a64b2ea1a9cf85ef`.

Exactly3 hunks: research status becomes reviewed closeout status; the now-
completed companion numerical review replaces its pending wording and the
J/J00 distinction is explicit; the verifier command uses the packaged path.
The matching, boundary exception, doublets, capacity inequalities and both
height-only countermodels are unchanged, including their missing physical
moment/odd-state/early-signature assumptions.

### Window reconstruction proof

Source: `agent_window_physical/PHYSICAL_WINDOW_RECONSTRUCTION_AND_DENOMINATOR.md`.
Candidate: `proofs/RL195_PHYSICAL_WINDOW_RECONSTRUCTION_AND_DENOMINATOR.md`.

Source SHA256: `8d37a75f7dffc097115c4af94cc0421a1bf2b834a38dc24a0ef6624f2b31eb2f`.
Candidate SHA256: `1b5dba449540778a5a607749c106c9afa870241a0f265487c65dd65db8f19bb8`.

Exactly2 hunks: reviewed-status wording and the packaged verifier command.
All reconstruction, denominator, integrality, arc identities and scope
qualifications are byte-identical outside those lines.

### Owned local realizability proof

Source: `agent_owned_realizability/OWNED_LOCAL_REALIZABILITY.md`.
Candidate: `proofs/RL195_OWNED_LOCAL_REALIZABILITY.md`.

Source SHA256: `5ec3d6e89432ed7af95dd55b9abac3b13e3f2a74e3c0090f623d068f2357420c`.
Candidate SHA256: `9d7896252518f35f590068d33f95c76dbc99abb5e735b89d921c9e535271bca3`.

Exactly4 hunks: reviewed status; packaged verifier invocation; classification
status with explicit retention of the defined relaxation; completed red-team
wording and its review pointer. The finite-word proof, compatibility modulus,
CRT restriction to compatible initial conditions, infinite local families,
all42 roots, all3 depths, all34,039 paths, all44 patterns and missing global
p/L/phase/prehistory/ownership conditions are unchanged. The documented
helper-interface repair is preserved.

## 3. New verifiers: exact mappings and hashes

All4 complete diffs were inspected. No executable arithmetic, assertion,
range, transition rule, loop, branch, constant or repaired helper changed.
Only module docstrings and, in three scripts, printed research-status text
were normalized.

1. `artifacts/verify_moment_adjacency.py`
   -> `verification/verify_rl195_moment_adjacency.py`.
   Source: `b84e93f5e5f065321b7ae760a1e6833313ec5a139fe87b6ddc35b0ec2fd90bc1`.
   Candidate: `c72679f3378fee1113bb8a6ffde6ff355daaff65d0c1948708aa1bb087735eb5`.
   Exactly1 hunk: remove research-status wording from the module docstring.

2. `agent_zero_geometry/verify_zero_geometry.py`
   -> `verification/verify_rl195_zero_geometry.py`.
   Source: `d9b9db907e6f5d91e06ead5a1bf12a27e4113b21365650661017610103abafdd`.
   Candidate: `e632d84f494c366d09293aa37499c387b3b2129f383b9f16c23498a9305cdb26`.
   Exactly2 hunks: module docstring and printed classification status only.

3. `agent_window_physical/verify_rl195_window_reconstruction.py`
   -> `verification/verify_rl195_window_reconstruction.py`.
   Source: `f7959a2a7ae9c4c6575f6619da3ef0c928566d42549ee593a52db0606e2c7858`.
   Candidate: `8707bd2396bb6565246ebac4f56a4c9604aa317e930144b987a2adfff5eb50bf`.
   Exactly2 hunks: module docstring and final printed status prefix only.

4. `agent_owned_realizability/verify_owned_local_realizability.py`
   -> `verification/verify_rl195_owned_local_realizability.py`.
   Source: `502fa58d660d72711fa07e5fda110b84f6d5802abd043c67453e5714ba282389`.
   Candidate: `8fa17fc20c7ac3d7c064226f464a7e7c9a4c9ec89908f5d5465ab47600e714fc`.
   Exactly2 hunks: module docstring and printed research-status prefix only.

## 4. Inherited components: byte-preservation PASS

For each path below, the current incoming source and candidate have the
same SHA256 and `cmp` exited0. There are no changed bytes.

```text
bee7e0c5d50364e3cad3ef7e0f7812c2d9fa38f85c540985651dc4fee49a06c4  proofs/RL194_RANK_ORDER_AND_CORRIDOR.md
8911e4d964d3d6a312120b985384b78da1976243e347a9cce17a5d634c925cf3  proofs/RL194_CHRONOLOGICAL_WEIGHTED_SPEED.md
5337c89f40cb287ce9a2208d70248dd33012d615d23d7eba354079a9ba3930bc  proofs/RL194_WEIGHT_ORDER_AND_ZERO_HEIGHT_OCCUPATION.md
44d6a2ee7c91ddccea97a8b8798831d96fe931fdc59a1e63ca6ed31644813569  proofs/RL194_OWNED_PREFIX_INTERFACE.md
a98da59a9186cdf9b2644da0def069e660586c56eec89a912aabfaac06413136  verification/verify_rl178_inherited_early_window.py
b363c261c033ed52dc9303e4981868d3ec96e31a9f77a8beae03831e08a7cca8  verification/verify_rl193_physical_debt.py
29fff56589778f3d83bcf4c756bf240bd1b7e4537b18dffe73103884bec8de40  verification/verify_rl194_rank_order.py
bc13c0daf0f2a2bbc25af9dd2527f77de727b61eece18787e549b5008b44d968  verification/verify_rl194_weight_order.py
cd10cf58f792f772c91f3fc2c9cdfab3b88805f4e947596044ed7263443260cf  verification/verify_rl194_owned_prefix.py
a18625ce8b779ee308de8194fa7729020b1982088165726dbd1ccdf5e5a8b24b  verification/verify_rl194_chronological_speed.py
```

Original RL labels and intermediate historical outputs are preserved as
provenance, not substituted for later combined-frontier statements. In
particular the inherited speed verifier still covers exactly1..1826035.

## 5. Auxiliary review scripts

`agent_owned_realizability/verify_adjacency_independent.py`
-> `reviews/verify_adjacency_independent.py`: byte-identical, SHA256
`8c5861885357da0ff24cc7ac0cf17f1ad14f62eedec7257dc757654436468e7d`.

`agent_owned_realizability/verify_window_independent.py`
-> `reviews/verify_window_independent.py`: byte-identical, SHA256
`87b25aaed52379a05ec3fdd4e21fd2cbf17bc54de4e665c061a7df635c3c0813`.

`agent_zero_geometry/verify_owned_seed_red_team.py`
-> `reviews/verify_owned_seed_red_team.py`:
source SHA256 `0762600e6f0ea68b14d73c1f44edb43593ce9dd61513b4dc6b44de95032e2603`;
candidate SHA256 `22c0856be165f007b72f357e7b9d38c9bbb2185b6c61a8ca8778a0547b09abb6`.
Exactly one changed line is the required import-path adaptation:

```diff
-SOURCE = Path(__file__).resolve().parents[1] / "agent_owned_realizability" / "verify_owned_local_realizability.py"
+SOURCE = Path(__file__).resolve().parents[1] / "verification" / "verify_rl195_owned_local_realizability.py"
```

All other bytes are unchanged. The target exists and the adapted script
executes successfully from the package. Retained NOT_PROMOTED text in the
audit script is research-stage provenance, explicitly explained in the
packaged README; it is not a conflicting root proof classification.

## 6. Wrapper, actual execution and outcomes

Wrapper: `verification/run_fast_rl195_verifiers.sh`, SHA256
`14502a07601323b6c5d24a8653f83a9d57bf16b2c9ca22cfe0d7c8929ddd95a5`.
README: `verification/README.md`, SHA256
`f910cbf1d74bc55f8087adb210a33a9a5aa16dd958045fe63f4b523a2ddf96da`.

The wrapper uses `set -eu`, locates its own verifier directory, disables
bytecode, and invokes all10 expected standalone scripts exactly once. The
verification directory contains precisely those10 Python files, the wrapper
and README. All listed imports are standard-library imports. The auxiliary
owned checker imports only its packaged verifier through the adapted path.

Executed from `.rl-work/RL195/candidate/authoritative/`:

```sh
sh verification/run_fast_rl195_verifiers.sh
python3 -B reviews/verify_adjacency_independent.py
python3 -B reviews/verify_owned_seed_red_team.py
python3 -B reviews/verify_window_independent.py
```

The complete command chain exited0. All10 primary scripts and all3
auxiliaries reported PASS. Recorded outcome checks:

- inherited early signature, debt constants, rank corridor, occupation,
  owned depth3 graph and complete1..1826035 speed certificate: PASS;
- RL195 adjacency: `J00>=9719139553`, with strict threshold for J00-1
  inside `(9719139551,9719139552)`;256/7/3 toy counts: PASS;
- RL195 geometry: all4 mechanical cells, all7 relaxed-witness cells,
  N0=57079296007/J=1 witness and zero-free p-window witness,
  256 tested/7 admissible toy arrays: PASS;
- RL195 window reconstruction:256 toy arrays/7 admissible words,
  35 gaps/175 arcs, no integral nontrivial toy word, trivial integral
  one-cycle only, and no actual high-branch phase scan: PASS;
- repaired owned local replay:42 roots, paths540/4517/34039,44 patterns,
  336 helper regressions including126 initial mod3-zero cases: PASS;
- original owned replay digest remains
  `34837dc796e7637e7044c1ad3393a31a2baef7129ea9b9154d7775928810277f`;
- independent adjacency128-term/degree12 check and all4 binary assignments:
  PASS, threshold enclosure width below1e-40;
- independent owned85-word/27931-residue and all34039 final t=0 mod3
  local-path checks: PASS;
- independent affine-composition window/denominator replay: PASS.

These outputs retain the reviewed physical/relaxation distinctions. They
do not establish H21 ownership, new pair spacing, additional speed coverage,
global p/L compatibility, an atom realization/exclusion or branch closure.

## 7. Final readback and conclusion

Every candidate hash listed above was recomputed after the executions and
matched its pre-execution value. No `__pycache__` or `.pyc` file was created
in the candidate proof/verification/review directories. The tracked worktree
was clean at the final check. The reviewer changed no candidate component.

**Component portability gate: PASS.** There are no remaining component
findings. Root integration and subsequent final sealing/fresh-unpack/Git
gates are explicitly outside this report. The next permitted work remains
the locked closeout transaction, not new mathematics.
