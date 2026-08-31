# RL194 candidate-component portability audit

Status: **PASS**.  CLOSEOUT_LOCK-only review, 2026-08-31.
BASE_HEAD: `4ded9b73d84cd3f9101c9eaef81d783e14390914`.

Scope: the four packaged proof notes and six Python verifiers under
`.rl-work/RL194/candidate/authoritative/`.  The main worker is separately
assembling and auditing the root report, ledgers, target and package
envelope; this note does not claim that those separate duties are complete.
No candidate file was edited by this audit.  No new mathematics, scan range,
route or historical review was introduced.

## 1. Proof-note comparison with frozen scratch

All four packaged notes were compared with their corresponding frozen
scratch notes using complete unified diffs.

- **Rank/corridor:** mathematical formulas, four exact endpoint enclosures,
  rank exclusions, 22 retained deletions, cardinality and signed prefix
  bounds are unchanged.  The header/status and verifier path are updated
  for packaging.  Section 4 now explicitly labels phases 73/78 as
  *intermediate corridor-only* floors, superseded by the separate weighted
  chronological proof.  The closing reference delegates the final
  combined rank refinement to the root ledger.
- **Weight/window/occupation:** all analytic identities and certified
  constants are unchanged.  The local notation Q in the moment section is
  explicitly identified as weighted q mass, called **Q_mass** in the root
  handover, not terminal-rank split `Q=88514772733`.  The bound
  `43742681439` still counts actual height-zero phases under the physical
  assumptions, not H21 terminals, clean starts or ownership.  Changes are
  limited to header/status, that notation clarification, and portable
  verifier/proof paths.
- **Owned prefix:** exact `C=3^37`, common word `212`, all 42 initial pairs,
  transition formulas, counts, two immediate-zero interfaces and the
  no-consecutive-successor-zero result are unchanged.  The narrowly scoped
  depth-3 parity-filter barrier and non-realization/H21 qualifications are
  preserved.  Changes are only the closeout header and package-root command.
- **Chronological weighted speed:** all proof mathematics, finite counts,
  ten survivor ranks and endpoint claims match the frozen reviewed note.
  Header and verifier invocation are made portable.  The resolved final
  scope paragraph explicitly preserves inherited spacing **>=1001** between
  distinct extremal terminals and claims no improvement.  It also retains
  the canonical-origin restriction, unchanged H21 charging, and open branch
  and global gates.

No proof formula, physical premise, inequality direction, inherited
classification or certificate range was strengthened during packaging.

## 2. Executable comparison

- The rank verifier differs only in its module description and printed
  labels.  The old rank count and phase floors are now labelled
  `corridor_only`, with an explicit reference to the separate speed filter.
  All executable mathematical checks are unchanged.
- The weight verifier differs only in the module description, packaged
  proof path and final scope print.  Its exact arithmetic and checks are
  unchanged.
- The owned-prefix verifier differs only in its module description and
  PASS output wording.  Its state transition and complete finite domain
  are unchanged.
- The speed verifier's only executable parameter change is
  `LIMIT=2_000_000` to **`LIMIT=1_826_035`**.  The frozen scratch program
  already broke at 1,826,035 and asserted that exact tested endpoint.
  Therefore this change trims an unused ceiling to the already-certified
  domain; it neither omits an audited phase nor extends the range.
  All survivor, eligible/rejected-count, interval-width and endpoint
  assertions are unchanged.  Other changes are description/diagnostic text,
  including the accurate label `outside_claimed_scan_after`.
- Both inherited scripts, RL178 early-window and RL193 physical debt, are
  **byte-for-byte identical** to current incoming authority (diff exit 0).

The new verifiers use only the Python standard library and contain no
scratch-file imports or runtime dependencies outside the package.  Their
documented commands run from the package root.  Historical paths in proof
provenance remain source references, not required runtime file reads.

## 3. Portable replay

Executed from `.rl-work/RL194/candidate/authoritative/`:

- `python3 verification/verify_rl194_rank_order.py` — **PASS**, exit 0.
- `python3 verification/verify_rl194_weight_order.py` — **PASS**, exit 0.
- `python3 verification/verify_rl194_owned_prefix.py` — **PASS**, exit 0.
- `python3 verification/verify_rl194_chronological_speed.py` — **PASS**, exit 0.
- `python3 verification/verify_rl178_inherited_early_window.py` — **PASS**, exit 0.
- `python3 verification/verify_rl193_physical_debt.py` — **PASS**, exit 0.

The speed replay covered every start `1..1826035`, reproduced lower/upper
terminal floors **190574 / 1826072**, all ten necessary survivors, 359245
additional deletions, and combined necessary-rank cardinality **27057465824**.
No post-1826035 phase was evaluated or represented as complete.  Earlier
coarse and unit-speed diagnostic hits remain labelled as intermediate
tests, not the final weighted endpoint.

The weight replay reproduced actual `N_0>=43742681439`, strict weighted-mass
enclosure `67236063233<Q_mass<80336439250`, 256 toy arrays and all 1024 toy
rank-prefix boundaries.  The toy checks remain algebraic regression tests,
not physical-state coverage.

## 4. Audited packaged SHA256 identities

Paths below are relative to candidate `authoritative/`.

- `proofs/RL194_CHRONOLOGICAL_WEIGHTED_SPEED.md`:
  `8911e4d964d3d6a312120b985384b78da1976243e347a9cce17a5d634c925cf3`
- `proofs/RL194_OWNED_PREFIX_INTERFACE.md`:
  `44d6a2ee7c91ddccea97a8b8798831d96fe931fdc59a1e63ca6ed31644813569`
- `proofs/RL194_RANK_ORDER_AND_CORRIDOR.md`:
  `bee7e0c5d50364e3cad3ef7e0f7812c2d9fa38f85c540985651dc4fee49a06c4`
- `proofs/RL194_WEIGHT_ORDER_AND_ZERO_HEIGHT_OCCUPATION.md`:
  `5337c89f40cb287ce9a2208d70248dd33012d615d23d7eba354079a9ba3930bc`
- `verification/verify_rl178_inherited_early_window.py`:
  `a98da59a9186cdf9b2644da0def069e660586c56eec89a912aabfaac06413136`
- `verification/verify_rl193_physical_debt.py`:
  `b363c261c033ed52dc9303e4981868d3ec96e31a9f77a8beae03831e08a7cca8`
- `verification/verify_rl194_chronological_speed.py`:
  `a18625ce8b779ee308de8194fa7729020b1982088165726dbd1ccdf5e5a8b24b`
- `verification/verify_rl194_owned_prefix.py`:
  `cd10cf58f792f772c91f3fc2c9cdfab3b88805f4e947596044ed7263443260cf`
- `verification/verify_rl194_rank_order.py`:
  `29fff56589778f3d83bcf4c756bf240bd1b7e4537b18dffe73103884bec8de40`
- `verification/verify_rl194_weight_order.py`:
  `bc13c0daf0f2a2bbc25af9dd2527f77de727b61eece18787e549b5008b44d968`

## Verdict

**PASS for the ten audited component files.**  Only the intended packaging,
notation, intermediate-result labels and already-resolved spacing wording
changed.  No repair is required by this component audit.  Root-ledger,
manifest/bundle, fresh-unpack, authority-snapshot, atomic promotion and
remote-readback checks remain the main worker's separate closeout duties.
