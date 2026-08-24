# RL20 proof status and next attack

Date: 2026-08-20

## 1. Proof-state ledger

### Closed / proved within the inherited chain

- Radius-3 sparse/cyclic-rotation obstruction: **closed**, subject to the inherited stated external dependency ledger.
- RL20 local-grammar bridge countermodel: **exact finite certificate**; all-rotation minimum radius is exactly `4`.
- Coprime-6 state packing: **analytic**.
- Continued-fraction gate: **analytic + exact finite certificate**, with the numerical denominator floor conditional on inherited external `R#>=2^71`; no LMN used for this RL20 bound.
- Canonical gcd-block coboundary identity: **analytic**.
- Final-return/CF endpoint decoupling: **analytic no-go + exact witness**, repaired after phase compatibility.
- Final-return phase compatibility: **analytic**.
- Hard weak-close second-low-or-huge-length dichotomy: **analytic**, numerical huge-length corollary conditional on inherited `R#>=2^71`.
- Hard weak-close global numerator lower bound: **analytic**, clean `L>=92` simplification conditional on inherited accepted RL-E3.
- Near-resonant gcd-block one-sided geometry: **analytic**, with finite `m=195` and huge reduced-block numerical corollaries conditional on inherited `R#>=2^71`.

### Still open

- RL globally.
- Any theorem forcing a genuine RL object into radius `<=3`.
- The balanced-return weighted-difference contradiction.
- The strict-excursion packing contradiction.

## 2. What is definitely dead

Do not spend another session attempting any of these without new hypotheses:

1. local root/final-return grammar alone `=>` radius `<=3`;
2. direct final-return 3-adic address alone `=>` exclusion of large continued-fraction classes;
3. raw canonical proper-factor/block polynomial divisibility `=>` contradiction.

Each has a formal obstruction/countermodel/coboundary explanation in this bundle.

## 3. The key new dichotomy

Let `E_j=K_j-j ell` at canonical gcd-block cuts in the least-state rotation, with `lambda<16/15`.

Then `E_j>=0` for every proper cut.

### Balanced-return branch

If `E_j=0` for some `0<j<g`, then

`R# < x_j < (16/15)R#`

and `x_j` is odd. This gives two distinct odd rotations, both genuine `D`-divisible cycle states, with exact zero block imbalance.

Because the reduced block length is enormous (`a>=78,450,472,029` under the inherited floor), this is not a short local accident.

**Primary theorem target:** derive an exact formula for the numerator/state difference between the least-state rotation and the balanced rotation. Exploit both the zero imbalance and the height interval to obtain either:

- a cyclic adjacent-transposition distance bound `<=3`; or
- a nonzero integer/multiple of `D` trapped strictly between `-D` and `D`; or
- an impossible state-ordering/packing inequality.

A falsifying finite/abstract word model is equally valuable if it shows more structure is needed.

### Strict-excursion branch

If every proper `E_j>=1`, then every proper canonical block state satisfies

`x_j > (45/16)R#`.

Meanwhile the normalized lift `H_j=z^j3^{-E_j}x_j` is monotone and remains inside

`R# < H_j <= lambda R#`.

**Secondary theorem target:** quantify the total increment of this narrow lift against the repeated physical factor-3 excursions. Look for a weighted population lower bound that exceeds the available strip width `(lambda-1)R#`.

## 4. How radius 3 should now be used

Radius 3 is not the object to extend generically. It should be treated as a finished contradiction engine.

Only return to its internals if:

- a bundled verifier fails; or
- the balanced-return/global argument derives a specific radius-3 configuration whose hypotheses need matching against the closed theorem.

Do **not** launch a generic radius-4/5 ladder simply because the local countermodel has minimum radius `4`.

## 5. External-input discipline

Keep these labels explicit:

- `R#>=2^71` is inherited external computational input, not an analytic theorem of RL20.
- `L>=92` is inherited accepted input RL-E3.
- The RL20 continued-fraction denominator floor is conditional on `R#>=2^71` but does not invoke LMN.
- Radius-3 closure retains whatever external dependencies are listed in the inherited RL18/RL19 audit; do not silently upgrade them.

## 6. Recommended first derivation next session

For a balanced cut `r=ja`, compare the least rotation `d` and the rotation `rho^r d` using the existing arbitrary-rotation difference identity. Insert `K_j=j ell` immediately, so every factor `2^r/3^{K_j}` reduces to `z^j` with no imbalance power of `3`.

Then use

`R# < x_j < lambda R#`

and the exact cycle equations for both rotations to seek a signed integer expression divisible by `D` but numerically smaller than `D`.

If the resulting identity still telescopes, record the precise coboundary causing the failure and move to the strict-excursion branch rather than repeating the same algebra in another guise.
