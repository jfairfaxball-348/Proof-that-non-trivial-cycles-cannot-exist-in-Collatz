# RL131 verification

Run `./run_fast_rl131_verifiers.sh`. It checks the inherited rotation algebra,
the exact L=56..57 quotient table, then reruns a self-contained consecutive
odd-start induction certificate through `23,506,639,475`. The final trajectory
that crosses `uint64_t` is handled exactly by the verifier's local base-`2^32`
arbitrary-precision implementation.
