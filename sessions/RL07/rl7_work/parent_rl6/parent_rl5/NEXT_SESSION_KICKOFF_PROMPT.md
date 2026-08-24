# Kickoff Prompt — Collatz R# RL-6 Denominator Divisibility and Boundary Cancellation

Continue the dedicated RL/nontrivial-loop branch from RL-5.

Read first:

1. `RL5_PLATEAU_ANCHOR_RETURN_AND_RIGIDITY_2026-08-19.md`
2. `RL5_CANONICAL_REGISTER_DELTA_2026-08-19.md`
3. `RL5_ROADMAP_UPDATE_2026-08-19.md`
4. `parent_rl4/RL4_CROSSING_SLACK_AND_CYCLE_EXIT_2026-08-19.md`

Run:

```bash
python3 tools/verify_rl5_anchor_grammar.py
```

## Frozen RL-5 facts

- Physical exponent-1 plateaus are suffixes of canonical red-anchor neutral runs; compressed xi levels form a deterministic orbit `u -> F(u)`.
- `mu_next=0 iff t` is odd; saturation forces `2*3^(n-1)|t`.
- Any xi non-rise satisfies `2t>=n`; xi direction is forced except on one critical integer per effective depth.
- Final return to `R#` realizes an exact root xi probe with a nested 3-adic discrete-log address.
- Every transition is the exact ceiling `W'=ceil(3^h W/2^(h+t))`.
- For a cyclic compressed word, every rotation has `W_r=C_r/[6^M(2^A-3^L)]`; the word determines a unique rational candidate orbit.
- `v2(C_r)=M+n_r` is automatic. If no exit has `v3(2^t-1)=n`, then `v3(C_r)=M` is automatic too.
- For generic admissible words with no exact saturation-boundary exit, `D=2^A-3^L` dividing one rotation numerator is necessary and sufficient for the full periodic integer anchor orbit; all other rotations and exact local exit valuations then follow automatically.
- Nontrivial 3-adic numerator cancellation is confined to exact saturation-boundary exits.
- For k>0, nonzero cumulative exponent difference fixes physical order through reverse depth `2R#`.

## Primary mission

Attack `D=2^A-3^L` divisibility of the rotation numerators `C_r` using the low root departure gate and the high/discrete-log final-return gate. In parallel, derive the finite 3-adic cancellation grammar for exact boundary exits `v3(2^t-1)=n`.

Do not spend the session on another root-only sieve, scalar xi telescoping, blind expansion of the finite search domain, or multiplication of local Haar costs without a dependence theorem.
