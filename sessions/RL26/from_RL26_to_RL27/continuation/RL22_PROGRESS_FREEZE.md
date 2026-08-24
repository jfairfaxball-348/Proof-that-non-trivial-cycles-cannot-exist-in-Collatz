# RL22 progress freeze — global packing strengthened, cubic ownership sharpened

Date: 2026-08-21

## Current proof state

RL remains open. Exact radius 3 remains closed under the inherited audited hypotheses/dependencies. The live problem is still the global bridge.

This continuation produced two durable advances and one explicitly retired overreach.

## A. Stronger radius-independent odd-state packing

The RL21 low/high injection was refined twice.

1. Maximal short-linked low chains have at most three low states.
2. Using only a coarse extra-high lower bound gives

   `log(lambda)/L <= 29/(108R-27)`

   and, conditional on the inherited external floor `R>=2^71`,

   `L/gcd(A,L) >= 55,204,624,168`.

3. Using the exact terminal odd-state alternatives after a maximal low chain gives the stronger analytic theorem, valid for `R>=160`,

   `log(lambda)/L <= log(1+1/(4R-1)) <= 1/(4R-1)`.

   Under the inherited external floor this yields the new certified gate

   `L/gcd(A,L) >= 57,212,717,233`.

The next continued-fraction denominator remains `65,470,613,321`, so no new convergent threshold is crossed.

Primary files:

- `RL22_LOW_CHAIN_PACKING_AND_CF_GATE.md`
- `verify_rl22_low_chain_cf_gate.py`
- `RL22_TERMINAL_HIGH_PACKING_AND_CF_GATE.md`
- `verify_rl22_terminal_high_cf_gate.py`

The terminal-high theorem supersedes the `29/108` coefficient in the external-floor branch, but the earlier theorem remains correct.

## B. Order-3 balanced returns: explicit cubic lattice with physical state-gap coordinates

For three equal-density macroblocks with

`B=2^b`, `Y=3^e`, `C=B^2+BY+Y^2`,

and block numerators `U,V,W`, the cubic relative condition is equivalent to the lattice

`U-W = kY+nB`,

`V-W = k(B+Y)-nY`.

For an actual integer cycle with balanced states

`R`, `x=R+G`, `y=R+H`,

the lattice coordinates are exactly

`n=G`, `k=H`.

Thus the Eisenstein relative mode is directly the two-dimensional physical state-gap mode.

If the three blocks share `r` parity bits, `2^r` divides both physical gaps. In a primitive cycle the gaps are positive and distinct, which gives the sharpened shortest-vector bound

`max(|U-W|,|V-W|) >= 2^r(2B+Y)`.

In the near-resonant three-way balanced branch, all three balanced states are low enough to begin `11`, so globally

`max(|U-W|,|V-W|) >= 4(2B+Y)`.

This is a genuine integer-ownership consequence, but no universal upper bound on the owned macroblock numerator differences has yet been proved.

Primary files:

- `RL22_CUBIC_PREFIX_LATTICE_OWNERSHIP.md`
- `verify_rl22_cubic_prefix_lattice.py`

## C. Scope correction / retired overreach

An exploratory route tried to use strict supercriticality of every proper macroblock prefix as if it were a universal least-state fact. That is not valid: additive-prefix rescue can keep a phase above the least state even when the raw multiplicative prefix is undercritical.

Therefore:

- the cubic lattice/state-gap results are GLOBAL/ANALYTIC;
- the stronger `Q`-range theorem under strict-supercritical macroblocks is only CONDITIONAL on that additional prefix package;
- the irrational-rotation average idea based on *all* proper prefixes being supercritical is not frozen as a global theorem.

The conditional cubic range lemma remains useful for model testing. It shows that under strict-supercriticality plus a shared prefix of length `r` containing `p` ones, a non-diagonal primitive cubic solution requires

`e-p > 3*2^r(2+Y/B)`.

The exact dynamic-programming verifier records the finite frontier of that conditional criterion, but those finite frontiers are not global cycle exclusions.

## D. Verification status

All current verifier scripts in `rl21_continuation` pass:

- all seven RL21 verifiers;
- `verify_rl22_low_chain_cf_gate.py`;
- `verify_rl22_terminal_high_cf_gate.py`;
- `verify_rl22_cubic_prefix_lattice.py`.

## E. Best next attacks

1. **Push integer high-run packing beyond the `1/4` coefficient.** The current terminal-high proof leaves additional high states individually bounded by the threshold `H`; their transition ownership should permit another block pairing refinement.
2. **Order-3 cubic global upper bound.** Seek an upper bound on `|U-W|,|V-W|` from suffix domination / full block ownership that can meet the new lower bound `4(2B+Y)` without assuming every macroblock prefix is supercritical.
3. **g=2 simultaneous factor problem.** Continue attacking the coupled `X-Y` absolute mode and `X+Y` gap mode; the gap factor alone is already formally insufficient.

Do not revive:

- second-rotation full-`D` divisibility as an independent constraint;
- bounded transport radius from local slope geometry alone;
- the uncorrected RL20 coboundary increment;
- universal all-prefix supercriticality.
