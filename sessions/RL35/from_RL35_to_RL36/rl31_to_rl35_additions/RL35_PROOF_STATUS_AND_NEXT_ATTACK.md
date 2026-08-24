# RL35 proof status and next attack

Date: 2026-08-21

## Frozen new results

1. **RL34 type-II continuation / induced-superblock theorem**
   - analytic for `R>=800`;
   - exact finite verifier passes;
   - coefficient `0.246297537816914843649...`;
   - CF floor under inherited `R>=2^71`: `57,641,137,625`.

2. **RL35 anchor-run charging theorem**
   - analytic for `R>=10000`;
   - exact finite verifier passes;
   - global inequality
     `lambda Q^L <= T^(12A-19L) S^(8L-5A)`,
     `Q=1+1/(2000R)`;
   - coefficient `0.245797537816914843649...`;
   - CF floor under inherited `R>=2^71`: `57,699,734,483`.

3. **Verifier coverage repair**
   - RL34 now explicitly checks the `II3,h=13` base before using the period-12 extension on the residue class `h==1 mod12`.
   - RL35 likewise has explicit `h=13` bases for anchor/paired residue classes.

## What the stronger denominator floor buys

It does **not** cross the next continued-fraction denominator `65,470,613,321`, so no branch of the audited RL30 dependency DAG is eliminated merely by the new floor.

In an exact order-3 balanced branch `L=3e`, it raises the inherited lower bound on `e`, but only quantitatively. It does not convert the RL29 `Omega(e/log e)` transport theorem into positive density, and it does not supply the missing sparse radius-3 bridge.

## Best next attack

Do not continue shaving the same local support constant indefinitely.

The highest-value continuation is to export the **anchor-run charging paradigm** to a genuinely branch-closing arithmetic resource:

1. **Order-2 / `g=2` simultaneous-factor branch.** Combine the exact state-gap synchronization (`v2(G)` common prefix and first-divergence blow-up) with repeated induced low/high block ownership. Seek a charging theorem where repeated resynchronization forces either a positive density of high corrections or a proper-factor quotient cost in both `X-Y` and `X+Y` equations.

2. **Strict-excursion/no-balanced-return branch.** Build an induced-state potential on canonical block imbalance rather than parity synchronization. RL35 shows that finite support slack plus deterministic successor dynamics can yield a fixed global gain even when individual extremizers exist.

3. **Algebraic bridge only if sparse.** For order 3 or higher cyclotomic returns, require a genuinely low-support relation in the rotation phase or a proper-factor resultant. Dense exact factor recovery alone remains insufficient.

## Evidence discipline

- `R>=2^71` remains explicitly external.
- Older radius-3 leaves that use Laurent–Mignotte–Nesterenko remain dependent on that published theorem.
- `(G,H)=(12,4)` remains only the exceptional extremal order-3 subbranch, not the global RL problem.
- RL remains open.
