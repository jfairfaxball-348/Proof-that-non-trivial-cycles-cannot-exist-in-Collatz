# RL177 certified facts and proof ledger

## New proved analytic mathematics

- **RL177.1:** for the RL176 first mismatch `J`, the carry-free prefix obeys
  `G_i=h_i-h_{p+i}` and `E_{p+i}=E_i+1` for `0<=i<=J`.  The paired states are
  consecutive in lifted-defect/value order.  At `J+1`, `d=G_{J+1}>0`
  reverses the pair order, while `d<0` preserves it.
- **RL177.2:** with `v=v2(g_p)`, the first nonzero corrected-flow term is
  `T=sgn(d)*(2^|d|-1)*2^v/3^(J+1)`.  Hence
  `|T| >= (2/3)^37 > 3/10^7`, and the total magnitude `N` of negative
  corrected-flow terms satisfies `N>3/10^7`.
- **RL177.3:** if the common mismatch height `H=h_J=h_{p+J}` is zero, then
  `c_J=2`, `{a_J,a_{p+J}}={1,2}`, `|d|=1`, and `v=b_J+1`.  There are exactly
  28 signed local types at 14 certified indices.  In every such type
  `|T|>1/3` and `N>1/3`.
- **RL177.4:** if `H>=1`, at least three distinct global height phases are
  positive and
  `R-Q > 3/2 - 2^(-H) - 2^(-|d|-1) >= 3/4`.  Therefore
  `F2 < rho_t-(q_p^-1-1)*(3/2-2^-H-2^(-|d|-1))`, and uniformly
  `F2 < 1/2-11*Delta/16`.

## Exact finite / arithmetic certificates

- The local automaton identifies 15,872 legal tuples
  `(J,H,a_J,a_{p+J},d,v)` under the stated local certified rules and `v<=37`.
- Every valuation `v=2,...,37` appears with both signs of `d`; this is a
  local-method barrier, not a physical existence statement.
- Every legal tuple has `|d|<=21`.
- The zero-height mismatch indices are exactly
  `1,3,5,6,8,10,11,13,15,17,18,20,22,23`, with two signs at each index.
- The smallest zero-height first-flow magnitude is
  `134217728/387420489 > 1/3`.
- The global first-flow lower quantum is
  `2^37/3^37 = 137438953472/450283905890997363 > 3/10^7`.
- `v=36` has no zero-height local type.
- The only zero-height `v=37` local types are `J=23`, `d=+/-1`, with
  `|T|=2^37/3^24`.

## Inherited correction / scope state

- The authoritative corrected p-shift remains
  `G_i=S_{p+i}-S_p-S_i`.
- The physical functional remains
  `F2=sum q_i(2^G_i-1)=3(lambda-1)g_p`.
- RL173's old `3^(-G)` weighted functional remains auxiliary only.
- The RL175 sparse ownership resultant is not used as an independent gap
  obstruction in RL177.
- The inherited external `m>=2^71` floor is not used in any new core RL177
  theorem.

## Global status

No physical cycle is constructed or excluded.  Gate A and Gate B remain
open.  The preferred `h_p=0` branch is split into a finite zero-height
interface with a `>1/3` negative-flow requirement and a positive-height
three-support branch with a stronger mechanical-loss barrier.
