# Kickoff Prompt — Collatz R# RL-7 Denominator Divisor / Endpoint-Cocycle Attack

Continue the dedicated RL/nontrivial-loop branch from RL-6.

Read first:

1. `RL6_BOUNDARY_GOOD_ROTATION_AND_DENOMINATOR_DEFECT_2026-08-19.md`
2. `RL6_CANONICAL_REGISTER_DELTA_2026-08-19.md`
3. `RL6_ROADMAP_UPDATE_2026-08-19.md`
4. `parent_rl5/RL5_PLATEAU_ANCHOR_RETURN_AND_RIGIDITY_2026-08-19.md`

Run:

```bash
python3 tools/verify_rl6_boundary_good_rotation.py
python3 parent_rl5/tools/verify_rl5_anchor_grammar.py
```

## Frozen RL-6 facts

- Every admissible height word `h_j=n_j-mu_(j+1)` has a good rotation with all nonempty suffix sums positive.
- At a good rotation, `v3(C_good)=M` is automatic even with exact saturation-boundary exits.
- From an `M`-unit rotation numerator, every non-boundary edge propagates the `M`-unit signature automatically.
- An exact boundary `r=n`, `mu'=n+c` preserves the signature iff one finite-depth congruence has cancellation depth exactly `c`.
- Therefore an arbitrary admissible cyclic word realizes a positive periodic integer anchor orbit iff `D|C_good` and all boundary gates pass.
- Generic RL-L41 is the no-boundary special case.
- At the minimum rational anchor candidate, `e_close/W_* < D/2^A < E_mu/W_* < P/W_*`; for k=0, `W_*=R#+1` and `e_close=1-2^-t_close`.

## Primary mission

Attack `D|C_good` itself. Insert the least-root endpoint gates into the affine cocycle modulo divisors of `D`:

- forced-low first departure;
- strict-high odd final return;
- exact final-return root discrete-log class;
- RL-L45 denominator near-resonance interval.

Seek a prime-divisor obstruction or a denominator lift/descent theorem. If compatible residue families survive, characterize them explicitly and identify the next invariant.

Do not spend the session re-solving boundary all-rotation valuations; RL-L42--L44 already reduce them to finite local gates.
