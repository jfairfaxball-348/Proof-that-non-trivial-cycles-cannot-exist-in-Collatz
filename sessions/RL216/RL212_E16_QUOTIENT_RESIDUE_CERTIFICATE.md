# RL212 exact e=16 quotient-residue certificate

Date: 2026-09-01. Classification: **exact finite arithmetic certificate** supporting
the scoped RL212 theorem. All physical implications remain conditional on a physical
H21 realization of the inherited sole high branch `(37,0,23,-1)`.

For `e=16`, the inherited RL210 lock gives `h_t=h_(p+t)` through the source and
`K_0=...=K_17=2^37`. The H21 source has height one, so the root recurrence has
`h_0=h_1=0`, `h_16=1` and
`a_i=c_i+h_i-h_(i+1)>=1`.

Exact propagation gives **108,950** root prefixes. Every one has total exponent
`S_16=b_16-h_16=24`. With
`y_(p+16)=2^34 eta-1` and flat K,

`y_(p+16)-y_16 = 3^16*2^13`.

Writing `2^24 y_16=3^16 y_0+Q`, integrality gives

`eta = (2^24+Q) * (2^58)^(-1) (mod 3^16)`.

The 108,950 prefixes give 108,950 distinct eta residues modulo `3^16`. Their
mod-9 counts are:

- `eta=0 mod9`: 29,286;
- `eta=8 mod9`: 15,760;
- all other residues: 63,904.

Thus the inherited H21 state filter leaves **45,046** abstract arithmetic prefixes,
with both state011 and state111 still present.

Compressing the recurrence to `(height,Q mod 3^k)` gives complete H21-compatible
coverage through `k=6`. The first informative level is `k=7`:

- modulus `3^7=2187`;
- H21-compatible universe: 486 residues (`eta mod9` equal to 0 or 8);
- reachable: 469;
- forbidden: **17**.

The forbidden eta residues modulo 2187 are

`[0, 53, 431, 891, 917, 972, 1160, 1295, 1458, 1493, 1565, 1620, 1701, 1862, 2060, 2088, 2106]`.

State011 (`eta=0 mod9`) contributes the eight forbidden residues

`[0, 891, 972, 1458, 1620, 1701, 2088, 2106]`,

and state111 (`eta=8 mod9`) contributes the nine forbidden residues

`[53, 431, 917, 1160, 1295, 1493, 1565, 1862, 2060]`.

At modulus 2187 the compressed automaton has phase-1 through phase-16 state counts

`[1,2,3,7,12,30,85,173,401,586,1071,1912,2308,3416,3655,4950]`;

at phase 16 and height one there are only 1,243 `Q mod2187` states. This is the
canonical compressed object; no raw 45,046-prefix list is promoted.

For every H21-compatible exact prefix, the root relation `y_p-y_0=2^37` gives
exactly one lift of eta from modulo `3^16` to modulo `3^17` for which both root
states are units modulo 3. This unique lift does **not** alter eta modulo 2187,
so it creates no further low-level hole and excludes neither H21 state.

Finally, the ordinary H21 terminal-valuation condition is 2-adic: it excludes one
odd `s` residue modulo `2^22`. Since `gcd(2187,2^22)=1`, CRT shows that this filter
alone cannot turn a surviving ternary residue into an empty arithmetic class.
It therefore does not delete the e=16 terminal rank.

No physical incidence, rank deletion, terminal sign, H21 charge, branch
contradiction, Gate closure or global nontrivial-cycle exclusion is certified.
