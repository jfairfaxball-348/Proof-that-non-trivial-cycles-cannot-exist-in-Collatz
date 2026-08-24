# START HERE — RL43

## 1. Read these first

1. `RL42_PROOF_STATUS_AND_RL43_ATTACK.md`
2. `RL42_REPRODUCIBILITY_LEDGER.md`
3. `RL42_DEPENDENCY_MAP.md`
4. `NEXT_SESSION_KICKOFF_PROMPT_RL43.md`

## 2. Verify before extending

Run:

```bash
bash verification/run_all_rl42_verifiers.sh
```

Then verify bundle hashes:

```bash
sha256sum -c SHA256SUMS.txt
```

Treat any verifier or hash failure as a stop-and-repair event.

## 3. Current theorem/certificate state

The retained chain is:

- exact ordered-rank identities + prefix cap -> transport-efficiency inequality;
- analytic consequence `rho > (45/4)G`;
- inherited `4|G` -> `rho >= 46`;
- bounded exact certificate: no physical positive-to-negative crossing of excursion excess `e<=3` in the contradiction range `rho<=47`;
- sharpened transport pricing -> `rho >= 48`;
- exact reduced `rho=48` boundary DP -> `rho != 48`;
- therefore **`rho >= 49`**.

RL remains open. The `g=2` branch remains open.

## 4. Primary RL43 target

Do **not** return to the old billion-scale area tables.

Attack `rho=49` using the excess decomposition. The only total moved-mass/excess layers currently needing consideration are

`(P,E) = (45,4), (44,5), (43,6)`,

with the refined efficiency bound forcing `P_+ >= 43` and therefore at most two units of negative moved mass.

Prefer a symbolic/parametric classification of crossing-capable `e=4,5,6` local families, followed by a safe-superset boundary DP. Do not brute-force all large-`p` `e=6` words unless a much smaller representation has first been exhausted.

## 5. Strategic track beyond rho=49

The main scalable quantity is

`M_eff = sum_(positive moved ranks) (1-2^(-delta_m))`.

The exact numerator equation gives

`M_eff >= 3(z+1)G/z^2`,

while displacement/excess bounds control `M_eff` from above. Feed the stronger binary-deficit form

`P_+ - sum 2^(-delta_m) >= 3(z+1)G/z^2`

back into the inherited endpoint-loss / packing / correction-product machinery. The goal is to close the distortion-versus-concentration loophole globally, not merely increase the low-`rho` floor one integer at a time.
