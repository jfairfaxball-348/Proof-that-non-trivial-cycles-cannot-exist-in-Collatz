# Verification status

The root runner recompiles every new C++ program from source before execution.

`33/4` is the independent audit target: the C++ implementation is separate from the inherited RL56 Python implementation and reproduces its decision statistics.

`77/10` and `17/3` are included for reproducibility only. They are new RL57 discovery programs and still require structurally independent implementations.

The target-8 witness replay is included to demonstrate exactly why the old viability-only witness cannot satisfy the inherited defect budget.

The inherited RL56->RL57 verifier suite is preserved unchanged in the inherited handover directory. It is not automatically run by the root script because it is substantially broader and slower; RL58 should run it as a regression check when practical, especially if any inherited interface is questioned.
