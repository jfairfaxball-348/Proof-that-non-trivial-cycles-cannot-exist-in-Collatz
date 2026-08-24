# RL51 — z=29 terminal proximity and the exact next barrier

Date: 2026-08-22

## Status

**EXACT TERMINAL-POWER CERTIFICATE + RIGOROUS METHOD BARRIER.**

After the stable `z=27` elimination, parity upgrades the sole stable continued-fraction survivor to `z>=29`. This note tests the same terminal-power mechanism at the first remaining odd value `z=29`.

It does not eliminate `z=29`; instead it proves exactly what the current one-zero terminal-proximity invariant buys and identifies the minimum strengthening needed next.

## 1. Terminal all-x-one suffix at z=29

For `z=29`, there are 28 internal x-zeros and 28 internal y-zeros, and

`k=q-z+3=q-26`.

Starting from terminal

`Q_1=J+1=2^k+1`,

the same exact all-x-one backward grammar applies:

- backward `11`: `Q -> 2Q/3`, allowed iff `3|Q`;
- backward `10`: `Q -> 2Q+1`, consuming one y-zero.

An exact residue BFS with at most 28 backward `10` steps proves

`maximum all-x-one terminal suffix length = 67`.

Therefore the final x-zero must lie within 68 columns of the terminal state.

## 2. The final x-zero is terminal-negligible

If `c<=67` all-x-one columns follow the final x-zero, then with `g_end=27 zeta / 2^(k+1)`,

`w_last = (g_end/2)(3/2)^c`.

Even the very weak `zeta<2` and the enormous stable-survivor value of `k` imply

`w_last < 2^-1000`.

So terminal power really does force the last zero's phase weight into a negligible regime.

## 3. Why one-zero proximity is not enough

The stable survivor still requires

`Zx > 143/12 = 11.916666...`.

Under the relaxed safe cap `w<17/30`, the exact greedy maxima are

- 27 zero weights: `12.4578427234...`;
- 26 zero weights: `11.9250209414...`;
- 25 zero weights: `11.5254046049...`.

Therefore:

- forcing only the last x-zero negligible leaves 27 potentially large zeros, far too much room;
- even forcing the last **two** x-zeros negligible still leaves the 26-zero maximum `11.9250209...`, slightly above the required `143/12` threshold;
- forcing the last **three** x-zeros negligible would leave only 25 potentially large zeros, whose exact maximum is already below the required mass.

This is a sharp method threshold.

## 4. Exact next target

To eliminate `z=29` by the same terminal-power/phase-mass mechanism, it is enough to prove a bounded terminal predecessor length when at most **two x-zero edges** are allowed after the third-from-last x-zero.

Equivalently:

> prove that every terminal suffix containing at most two x-zero edges has a denominator-independent bounded length.

Then the third-from-last x-zero is forced into a constant-size terminal window. Since the last three zero weights are then exponentially small in the enormous terminal exponent `k`, the remaining 25 zero weights cannot reach `Zx>143/12`, and `z=29` would be excluded.

This is materially narrower than the original Gate-A problem: the next finite automaton needs only terminal `Q`, height, y-zero count, and an x-zero budget of two.

## Verification

Run:

`python3 rl51_research/verify_rl51_z29_terminal_proximity_barrier.py`
