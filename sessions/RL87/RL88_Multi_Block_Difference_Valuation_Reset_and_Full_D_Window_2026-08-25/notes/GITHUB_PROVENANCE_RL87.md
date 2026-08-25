# Selective GitHub provenance used in RL87

Repository:

`jfairfaxball-348/Proof-that-non-trivial-cycles-cannot-exist-in-Collatz`

GitHub connector usage was read-only.  No repository files, branches, issues, pull requests, or commits were modified.

Selectively consulted sources:

1. RL73 commit `454c828d3f9d9961a868737542de4422e07d12e6`
   - exact global skew floor;
   - post-first-mismatch `00` lower bound;
   - partition into maximal height-one synchronized blocks;
   - exact low-`k` giant block count `40,249,491,324,522,944`.

2. RL81 commit `86be41e05a3d5c8966a843539df8a722ff39775c`
   - exact physical lift `J=3A-B+1`;
   - common-mode warning;
   - exact terminal physical state `B_j=2^(k-2)N`.

3. RL79 commit `347a8408646dd39156c5b805bb45f62056125617`
   - canonical generalized-increment cycles;
   - homogeneity/unit-increment red team.

4. `sessions/RL20/RL20_GLOBAL_COPRIME6_PACKING_AND_CF_GATE.md`
   - physical state packing discipline;
   - exact odd-step product identity interface;
   - warning that address/count data need a genuine physical consumer.

The authoritative RL86/RL85 mathematics was already present in the incoming handover and was not recursively re-audited.
