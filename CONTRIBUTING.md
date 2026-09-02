# Contributing

Contributions, corrections, verifier improvements, and mathematical observations are welcome.

Please clearly distinguish between:

- proved analytic results;
- exact machine-verifiable results;
- computational evidence;
- conjectures;
- heuristic observations; and
- corrections or counterexamples to existing claims.

A result appearing in a research-session document should not be treated as established solely because it appears in the repository.

Please include enough information for mathematical or computational claims to be independently checked.

When modifying an existing claim, please preserve the research record where practical by stating whether the claim is being strengthened, weakened, corrected, or withdrawn rather than silently replacing its historical status.

By contributing, you agree that code contributions may be distributed under the repository's MIT code licence and documentation or research-text contributions may be distributed under the repository's CC BY 4.0 documentation licence, unless a different licence is explicitly agreed for a particular contribution.

## Infrastructure contributions

Repository tooling supports Python 3.9 and later and currently uses only the Python standard library. Run the complete local checks from the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 tools/rl_conveyor.py index-validate
```

If an infrastructure change alters catalogue inputs or generation, rebuild the three generated files, stage the complete intended change, and validate the exact staged tree:

```sh
python3 tools/rl_conveyor.py index-build
git add knowledge/session_catalog.jsonl knowledge/result_catalog.jsonl knowledge/index_metadata.json
python3 tools/rl_conveyor.py index-validate --staged
git diff --cached --check
```

Stage other intended source changes before `index-validate --staged`; the check is designed to reject catalogue pointers whose inputs are absent from or differ in the Git index. Do not hand-edit generated catalogue files.

Infrastructure maintenance consumes no RL number and must use a separate commit from a numbered mathematical transition. It must not alter `authoritative/`, frozen `sessions/`, targets, handovers, or recorded proof classifications unless the task is an explicitly authorized mathematical or conveyor-state transition.
