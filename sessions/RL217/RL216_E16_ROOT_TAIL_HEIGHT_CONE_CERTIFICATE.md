# RL216 exact e=16 root-tail height-cone certificate

Date: 2026-09-01. Classification: **exact finite modular arithmetic certificate** supporting the scoped RL216 theorem.

The verifier reconstructs the 45,046 inherited e=16 H21-compatible prefixes and selects the unique minimum-Q prefix:

- `Q=43,013,953`;
- `eta_*=119,416,283 mod3^17`;
- `eta=1709 mod2187`, state111;
- RL215 interval `28,812<=k<=36,180`;
- 7,369 candidates after the inherited terminal Hensel filter (zero Hensel deletions in this prefix).

For every residue branch `k=r+2^m t`, the verifier propagates the exact affine odd state `y_i=A_i t+B_i`, derives `a_i=v2(3y_i+1)`, and enforces

`h_(i+1)=b_(i+1)-b_i+h_i-a_i >= 0`.

When the valuation depends on t, the branch is split by parity; branch populations inside the finite RL215 k interval are counted algebraically. No 331-million-candidate enumeration is used.

Through phase 174 the sieve produces 6,219 disjoint failure residue branches with total population exactly **7,369**. No branch survives. The latest first negative-height failure is phase 174.

Failure-class digest:
`b7f03ca354275de4e4d9aaa0698ab6e39d088232331a3f2f9b111a01df96d972`.

Exact promoted consequence:

- prefixes deleted: **1**;
- arithmetic candidates removed vs RL215: **7,369**;
- conservative targeted e=16 remainder: **331,927,916** candidates across **45,045** prefixes;
- all 469 reachable eta classes modulo2187 remain represented;
- no terminal rank deletion; global frontier remains **13,415,865,871**.

No physical incidence/charge, branch contradiction, Gate closure or global nontrivial-cycle exclusion is certified.
