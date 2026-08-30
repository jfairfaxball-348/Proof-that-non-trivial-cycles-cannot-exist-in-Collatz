# RL183 certified facts and proof ledger

## New proved analytic mathematics

- **RL183.1 — successor height-rise law.** With `c_i=b_(i+1)-b_i in {1,2}` and accelerated exponent `k_i>=1`,
  `h_(i+1)=h_i+c_i-k_i<=h_i+1`.
  Therefore an ordinary p-shift edge with both endpoint heights at most k has its j-th chronological successor at endpoint heights at most `k+j`.
- **RL183.1a — physical 25-edge owned-corridor floor.** At least `10,075,174,553` ordinary `h<=1` p-shift starts have all 25 edges `i,...,i+24` ordinary. Every numerator on each corridor is uniquely ternary-owned; the required ownership depth rises from 25 at cutoff 1 to at most 40 at cutoff 25.
- **RL183.2 — binary/ternary defect sensor.** On consecutive ordinary p-edges,
  `2|C_i` iff `G_i=0`, while `3|C_(i+1)` iff `G_i` is even.
  Thus current numerator parity plus successor ternary divisibility determines whether the current defect is zero, nonzero even, or odd. For an `h<=1` edge,
  `2|C_i` iff `3|C_(i+1)`.
- **RL183.3 — common-mechanical numerator successor law.** Except at the unique ordinary mechanical-switch p-rank and the unique p-shift carry, source and p-shift target share `c_i`. Then
  `2^d C' = 3C + 2^(M-b) - 2^(M-a)`,
  with `d=c+M-M'>=1`.
- **RL183.4 — mechanical-bit phase location.** If `c_i=1`, then `x_i<4m/3`; if `c_i=2`, then
  `x_i>=(4m-2^-h_i)/3>=(4m-1)/3`.

## Analytic results with exact integer certificates

Inside the surviving `(37,0,23,-1)` high branch only:

- ownership depths for endpoint cutoffs `k=1,...,25`:
  `25,26,26,27,28,28,29,30,30,31,31,32,33,33,34,35,35,36,37,37,38,38,39,40,40`;
- exact mechanical rank split:
  - `c=1`: `57,079,296,007` ranks;
  - `c=2`: `80,448,749,305` ranks;
- after removing carry/switch crossings, at least `10,075,174,571` clean four-edge corridors remain;
- necessary local height/mechanical template counts:
  - 1 transition: 34,
  - 2 transitions: 342,
  - 3 transitions: 3,884;
- the three-transition templates collapse to 357 composite affine numerator maps;
- some three-transition template is physically used at least `2,594,021` times;
- some composite three-transition affine map is physically used at least `28,221,778` times;
- forced shallow `c=2` populations:
  `16,722,313,938`, `24,526,523,999`, `27,725,426,287`, `29,184,838,817`
  for `h<=1,2,3,4`;
- after removing the possible width-1/3 overlap around `4m/3`, forced shallow `c=2` states at `x>=4m/3`:
  `16,722,313,937`, `24,526,523,997`, `27,725,426,284`, `29,184,838,811`.

## Exact verifier output

`verification/verify_rl183_owned_successor_corridors.py`: PASS.

## New method barrier

Longer unconstrained forward-template enumeration is not a physical capacity theorem. The 25-edge corridors, defect sensor, repeated short affine maps, and phase-location split now require a global consumer tying them to corrected-flow drift, defect sign/parity, ternary reset, or width.

## Inherited correction / scope state

- Corrected `G_i=S_(p+i)-S_p-S_i` remains authoritative.
- The physical corrected-flow functional remains the `2^G` functional; RL173's `3^-G` quantity remains auxiliary only.
- Necessary automata/templates remain one-way filters, not physical existence certificates.
- RL175's sparse ownership resultant is not revived as a generic independent gap obstruction.
- RL168-RL171 rank/chain/inverse-rank barriers remain in force.
- All RL180-RL183 high-branch population, m, pair-gap, suffix, corridor, map, and phase-location statements remain internal to `(37,0,23,-1)`.

## Global status

The sole zero-height `v=37` negative-sign high type survives. The preferred `h_p=0` branch, the positive-height branch, Gate A, Gate B, global non-trivial-cycle exclusion, and Collatz remain open.
