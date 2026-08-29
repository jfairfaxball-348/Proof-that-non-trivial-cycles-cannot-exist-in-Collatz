# RL176 certified facts and proof ledger

## New proved analytic mathematics

- **RL176.1:** in the physical preferred `h_p=0` branch, the least and
  unique second-smallest odd states satisfy `a_0=a_p=1`.
- **RL176.2:** `m == y_p == 3 (mod 4)` and therefore `4 | g_p`.
- **RL176.3:** using the RL175 half-barrier and inherited certified
  `Delta > 1/1,116,000,000,000`,
  `0 < g_p < 186,000,000,000`; hence
  `4 <= g_p <= 185,999,999,996`.
- **RL176.4:** a first shifted exponent mismatch exists with
  `1 <= J <= 36`.
- **RL176.5:** at that first mismatch,
  `v2(g_p)=S_J+min(a_J,a_{p+J}) <= 37`.  Hence the first nonzero corrected
  p-shift defect occurs in the carry-free prefix window, with
  `G_{J+1}=a_{p+J}-a_J != 0`.
- **RL176.6:** if `v2(g_p)` is 36 or 37, then the global upper bound forces
  `g_p=2^36` or `g_p=2^37`, respectively.

## Exact finite / arithmetic certificates

- `A*p-L*u=1`.
- `p+37<L`.
- `186,000,000,000 < 2^38`.
- The largest positive multiple of four below
  `186,000,000,000` is `185,999,999,996`.
- The associated lattice index satisfies
  `1 <= k <= 46,499,999,999` for `g_p=4k`.
- The external-assisted lower transform from
  `3*2^71*Delta>6,365,000,000` gives the next admissible multiple of four
  `10,608,333,336`.

## Inherited correction/demotion state

- The corrected physical p-shift defect remains
  `G_i=S_{p+i}-S_p-S_i`.
- The physical accelerated functional remains
  `F2=sum q_i(2^(G_i)-1)=3(lambda-1)g_p`.
- RL173's older `sum q_i(3^(-G_i)-1)` remains auxiliary only.
- The RL175 sparse-resultant exclusion is inherited, but **is not used**
  as the independent source of the new `4 | g_p` restriction.

## External qualification

- Only the lower band
  `g_p >= 10,608,333,336` uses the inherited external computational
  minimum `m>=2^71`.
- All RL176.1--RL176.6 core statements are independent of that minimum.

## Global status

No cycle construction or exclusion.  Gate A and Gate B remain open.
The preferred `h_p=0` branch is narrowed to an integer 4-lattice and an
early first-mismatch 2-adic interface, but it is not closed.  Global
non-trivial-cycle exclusion and Collatz remain open.
