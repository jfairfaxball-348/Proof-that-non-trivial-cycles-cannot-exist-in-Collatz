# RL308 scratch freeze

Date: 2026-09-13
Status: FROZEN SUPPORTING SCRATCH. `RL308_REPORT.md` and `RL308_PROOF_AND_SCOPE.md` control theorem status.

## 1. Exact owner witness data for the promoted X cut

Source:

`X=(4,43)`.
Owner:

`N=(2,-17)`.

The ten owned leaves are:

- `X:010 -> (3,23)` cost 8.
  Owner word `01000111100000100` reaches `(3,23)` cost 18.
  Under `Bcal(N)<=1`, branch bound = 11.

- `X:011 -> (3,44)` cost 8.
  Owner word `010001111011011111001000` reaches `(3,44)` cost 13.
  Branch bound = 6.

- `X:100 -> (5,216)` cost 10.
  Owner word `010000010000` reaches `(5,216)` cost 17.
  Branch bound = 8.

- `X:101 -> (5,347)` cost 10.
  Owner word `010000010001` reaches `(5,347)` cost 17.
  Branch bound = 8.

- `X:110 -> (4,90)` cost 8.
  Owner word `0100011110100100` reaches `(4,90)` cost 14.
  Branch bound = 7.

- `X:111 -> (2,18)` cost 8.
  Owner word `01000111101011100` reaches `(2,18)` cost 13.
  Branch bound = 6.

- `X:0010 -> (4,81)` cost 13.
  Owner word `0100011110110101111110000000` reaches `(4,81)` cost 20.
  Branch bound = 8.

- `X:0011 -> (4,153)` cost 13.
  Owner word `01000111101101011111101101100000` reaches `(4,153)` cost 17.
  Branch bound = 5.

- `X:00001 -> (5,326)` cost 20.
  Owner word `010001111011010111111011011110111011101111010011101101111110011110001010100100000000`
  reaches `(5,326)` cost 27.
  Branch bound = 8.

- `X:00011 -> (5,495)` cost 20.
  Owner word `01000111101101011111101101111011101110111101001110110111111001111000001101110111111011010110111010001101110000000000`
  reaches `(5,495)` cost 26.
  Branch bound = 7.

Residuals:

- `X:00000 -> (7,2039)` cost 20.
- `X:00010 -> (7,2546)` cost 20.

These twelve words are the complete promoted cut.

## 2. Early broad same-state owner exploration

Initial Dijkstra closures compared X and Y to the known scalar sources

`(4,39), (2,-17), 8, P, R3, D0, (2,-84)`.

This showed many shallow X states were already same-state owned, motivating a small exact cut instead of a global pointwise theorem.

Restricting X to owners `(2,-17)` and `(4,39)` gave early safe branches but left the two eventual deep-zero residuals. The final promoted cut deliberately uses only `(2,-17)` for its ten owned leaves, making the conditional dependency cleaner.

## 3. Common-state minimizer diagnostics

For divisibility shells k=6..13, exact shortest paths found:

- checkpoint 8 costs: `9,10,11,12,13,13,15,15`;
- X costs: `16,17,18,19,20,20,22,22`;
- Y costs: `22,23,24,25,26,26,28,28`.

At k=6 the shortest words share a long suffix after exact merger states:

`8 --011010--> (2,19)` cost 4,
`X --11101--> (2,19)` cost 11.

Likewise

`X --1110111--> (1,15)` cost 13,
`Y --1111111100--> (1,15)` cost 19.

This suggested potential ingress-offset relations, but no forcing theorem was established.

## 4. Incomplete X cylinder-exclusion computation

The experiment excluded every future beginning with the complete prefix `11101` and searched for high Bellman score.

At cost caps 30, 40, 50, and 60, the best score encountered was `-6`, realized by a path to checkpoint 8, but every run hit the imposed `1,000,000` state cap.

Therefore:

- the result is incomplete;
- no coverage claim is made;
- it must not be used as a certificate;
- it may be resumed only if a later roadmap gives this cylinder-forcing question priority.

## 5. Y-by-X owner grammar proliferation

A direct attempt used the X reachable cone as an owner for Y with target `Bcal(Y)<=12` and provisional `Bcal(X)<=11`.

The unresolved frontier counts after state merging were:

depth 5: 30 unresolved;
6: 46;
7: 80;
8: 153;
9: 283;
10: 531;
11: 1008;
12: 1890;
13: 3504;
14: 6421;
15: 11459.

At depth 15 only 310 of 11,769 frontier states were certified safe.

This was treated as a depth/proliferation warning, not as a route to continue automatically.

## 6. Naive Bellman-potential failure

The exploratory potential

`phi(d,J)=ceil(log2(K+1))+d`

fails an edge-Lipschitz condition required of a Bellman dual.

Exact counterexamples include:

- `(1,2) --0,cost0--> (2,6)`, with phi `2 -> 4`;
- `(1,4) --0,cost0--> (2,9)`, with phi `3 -> 4`;
- `(1,5) --1,cost0--> (1,8)`, with phi `3 -> 4`.

Do not reuse this potential as a proof device without substantial modification.

## 7. Live frontier at interruption

The intended next local step before the strategic pivot would have been to test whether the two X residuals

`(7,2039)`, `(7,2546)`

could be cheaply extinguished under the loose ceiling 31, before attacking Y.

Direct user instruction superseded that plan.

No work on those residuals was performed after the checkpoint.

Y remains mathematically untouched by any promoted RL308 result.

## 8. Strategic freeze

The complete current Gate-A/Bellman/scalar programme remains preserved across RL305–RL308 and older frozen sessions.

This scratch file is not an argument that the route is bad mathematics. The reason for stopping is architectural: local sophistication must no longer determine project priority without a clear end-to-end global dependency shortening.
