# Kickoff Prompt — Collatz R# RL-3 Relative Height / Rotation / Xi-Probe Attack

Continue the dedicated RL/nontrivial-loop branch. Do not resume RO XCORL/HVE and do not restart a general audit.

Read:

1. `RL2_SUFFIX_CODE_OBSTRUCTION_AND_XI_PROBE_ATTACK_2026-08-19.md`
2. `RL2_CANONICAL_REGISTER_DELTA_2026-08-19.md`
3. `RL2_ROADMAP_UPDATE_2026-08-19.md`
4. `parent_snapshot/RL_CANONICAL_LEMMA_RESULT_REGISTER_2026-08-19.md`
5. `parent_snapshot/RL_PROOF_DEPENDENCY_GAP_MAP_2026-08-19.md`

Run:

```bash
python3 tools/verify_rl2_suffix_xiprobe.py
```

## Frozen new facts

- `Phi_h` is exactly an inverse-integrality code for histories into a common endpoint.
- Same-endpoint tail/cycle `Phi_h` equality is automatic and cannot be the primary pruning invariant.
- The cycle may be unwrapped backwards, extending that equality through every `h<=k` in the strict-preperiod case.
- There are analytic infinite inverse towers satisfying ordinary legality, the least-red floor and local xi, so a local suffix/xi automaton cannot close RL.
- In `k>0`, the immediate tail and cycle predecessor exponents are distinct but have the same parity.
- Backward height defect `delta=x-R#` is contracted only by exponent 1; every exponent `>=2` expands it.
- Xi side-branch probes `q_d(y)=v3(2^(d-1)y+1)` provide an infinite family of exact least-red constraints.
- The initial forward exponent-1 neutral run has exact length `v2(R#+1)-1`.

## Primary mission

Attack the **relative height/rotation/xi-probe automaton**, not raw `Phi_h` matching.

### k>0

Compare the actual tail inverse branch from `c0` to `R#` against the periodically unwrapped cycle inverse branch. Seek an exact finite state that can track the tail height defect to zero while the cycle branch remains periodic. Fuse this with prefix slack and a small set of justified xi probes.

### k=0

Use the root-side xi valuation ceilings together with the minimum rotation, exact neutral-run length, common cycle denominator and inherited residue restrictions. Seek either an extension theorem for the xi-probe sieve or a proof that it remains too sparse.

A successful session should produce either a genuine exclusion, a finite recurrent survivor class with a proved lift theorem, or another precise obstruction that identifies the next indispensable invariant.
