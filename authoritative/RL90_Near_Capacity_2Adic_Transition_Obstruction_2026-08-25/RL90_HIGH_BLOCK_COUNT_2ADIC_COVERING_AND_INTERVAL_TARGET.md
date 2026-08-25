# RL90 target — high-block-count 2-adic covering and interval continuation

Date: 2026-08-25

## Authority

Continue from the frozen RL89 state.

RL89 eliminated the exact first-Farey lower endpoint `k=2,921,384,819`, raised the odd lower endpoint to `2,921,384,821`, and at that next odd value eliminated all block-count cases below `b=k-2`.

Do not restart generic quotient packing, independent midpoint congruence accumulation, or repeated-difference-to-primitivity arguments.

## 0. Frozen constants

- `C=42,150,931,628`;
- `k1=2,921,384,821`;
- `Q_min(k1)=123,139,091,657,887,804,843`;
- surviving first-Farey odd upper bound `42,150,931,559`.

At `k1`, only two block-count strata remain:

### Stratum A: `b=k1-2=2,921,384,819`

- `D_b=106,858,350,489`;
- average deficit `~36.578`;
- at least `33,321,293` blocks have deficit `<=36`;
- `H-b<=1`;
- excursion grammar is minimal `01,10` except at most one plateau/zero-return exception.

### Stratum B: `b=k1-1=2,921,384,820`

- `D_b=149,009,282,117`;
- average deficit `~51.006`;
- `H=b=e=k-1`;
- every complete excursion is minimal `01,10`.

## 1. Primary target: deficit-36 cofactor covering

For a minimal reset,

`3^(s+1)m-1=2^(n_next+2)m_next`.

RL89 exactly certifies that `|m|<2^29` forces `n_next<=63` for the full physical exponent range.

Extend this to the deficit-36 regime

`|m|<2^37`

without a brute scan over all cofactors.

Preferred methods:

1. 2-adic discrete-log bit covering / branch-and-bound;
2. split the exponent and use the special triangular structure
   `3^(2^j)=1 mod 2^(j+2)`;
3. normalize `m=3^q m_*` with `3∤m_*`, since multiplying `m` by `3` simply shifts `s+1`;
4. certify a small finite set of 3-free seed cofactors capable of long reset;
5. it is enough to bound the **number of exceptional transitions** sharply; zero exceptions is not required.

A theorem leaving at most `O(1)` long-reset exceptions among the `33,321,293` deficit-`<=36` blocks will eliminate Stratum A because the total deficit can pay for only about two genuinely short successors and the area grammar contributes at most one exceptional transition.

## 2. Secondary target: deficit-51 stratum

If Stratum A closes, attack `b=k-1`.

Here every excursion is minimal, so there is no area exception. The required cofactor threshold is around deficit 51, i.e. `|m|<2^52` for a direct population theorem.

Do not brute-force `2^52`. Use whatever sparse-seed structure is obtained in Target 1 and scale it.

## 3. Interval propagation

After any `k1` closure, do not stop.

Immediately:

1. recompute `Q_min(k)` and actual `D_b` at the next odd `k`;
2. propagate the covering theorem across all feasible `b` strata;
3. solve exact fixed-stratum exclusion thresholds;
4. identify the first odd `k` where a genuinely new cofactor threshold is required.

Aim for a nontrivial eliminated odd interval, but do not dilute a valid endpoint theorem if the covering threshold changes discontinuously.

## 4. Common-mode selector — only if needed

RL89's successful endpoint theorem avoids common-mode reconstruction.

Only introduce a selector if the 2-adic covering leaves a small exceptional cofactor set whose multiplicity must be controlled. Any selector must pass the RL81 physical-lift barrier and RL20 packing separation.

Candidates remain `J`, `L`, full-`D` content, or primitive phase ownership, but repeated difference alone is never enough.

## 5. Red teams

Every closure candidate must pass:

1. RL81 common-mode freedom;
2. RL79 generalized-increment homogeneity;
3. RL20 physical representative/packing separation;
4. primitivity;
5. first-Farey scope;
6. RL88 arbitrary-reset family;
7. verification economy.

## 6. Sustained attack protocol

Do not close at the first theorem or endpoint elimination.

Treat each result as a checkpoint and continue through:

- all remaining cases;
- constant sharpening;
- next odd parameter values;
- interval propagation;
- red-team;
- strongest adjacent continuation.

Close only for genuine context/compute pressure, stop-and-repair, actual route exhaustion after adjacent tests, or full target closure with immediate consequences propagated.
