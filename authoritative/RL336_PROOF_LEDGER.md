# RL336 proof ledger — prefix obstruction, q=32 charge, and zero-run contraction

Date: 2026-09-16. Status: candidate for verified atomic promotion. Incoming BASE_HEAD: `496325dd80bf220c99ef9292d14ce66ec2b954d1`. Successor: RL337.

## Exact scope

All new results concern only the ordered genuine `g=2`, `Z0>0`, `K<0` parent branch at `(a,ell)=(217976794617,137528045312)`. The inherited least-state floor `m>=2^71` is externally conditional. The physical state band is `2^71<=P<2^76+2^36`; the fixed high-carry regime and owned-state lower bound are inherited. Gate A, Gate B, the other `g=2` branches, `g=1`, R1, and the global positive non-trivial-cycle theorem remain open.

Incoming carry cap was `n<=32546289530` and zero-run bound was `z<=37`. All RL335 singleton, p2, p3, and p4 physical exclusions remain inherited certificates under verification economy.

## RL336.1 — uniform modular prefix obstruction

For a mechanical factor word of length `L`, let its gaps be `g_1,...,g_L`. Define `C_0=0` and `C_j=2^{g_j} C_{j-1}+3^{j-1}`. A physical odd start `P` realizing the first `j` gaps must satisfy

`P ≡ C_j (2^{g_1+...+g_j})^{-1} (mod 3^j)`.

The exact mechanical words are obtained by partitioning phases `0<=r<ell` at the cutpoints `(- (a-ell) j) mod ell` and sampling the cutpoint and its immediate successor. The admissible positive profiles have `q_p=1` and `1<=q_i<=q_{i+1}+1`; their gap perturbations are `q_{i+1}-q_i` at the specified adjacent-zero interface. The verifier enumerates the complete finite template sets and deduplicates prefixes.

- For p=5, every one of the 178 ordered pairs with `22<=z,z'<=37` and `z+z'>=56` is excluded. The 63,234 exact templates yield 4,886 distinct 60-gap prefixes. Their least required residue is `1244028314838852758759941`, exceeding the strict state upper bound `75557863725983042895872`.
- For p=6, every one of the 36 ordered pairs with `30<=z,z'<=37` and `z+z'>=67` is excluded. The 35,590 exact templates yield 5,778 distinct 58-gap prefixes. Their least required residue is `1330277458523593058251285`, also above the state band.

Since the relevant moduli `3^60` and `3^58` also exceed the upper bound, no allowed physical start can realize any of these prefixes, regardless of later gaps or endpoints. This is a uniform prefix obstruction, with an exact finite certificate for its complete template ranges. It removes the RL335 five-positive `N37->N37` obstruction and the adjacent high-pair q=32 cycle supports. It is conditional only through the inherited physical-state band and branch assumptions.

## RL336.2 — all-length q=32 charge theorem

Retain the inherited density potential `d(z)=max(0,2z-43)` and true edge slack `s=d(z')-d(z)-(2z'-43k)`. A conservative graph has states `N(1),...,N(37)` and 2,242 edges: singleton k=1 when `z+z'<=43`, plus a fallback k=5 for each ordered pair. Replace fallback k=5 by k=6 in the excluded p=5 pair region, and by k=7 in the excluded p=6 pair region. The latter is nested in the former.

Exact relaxation supplies a second potential of range `0..43`; direct verification of every edge proves

`32(K-2H)-S<=43`, equivalently `2H>=K-S/32-43/32`.

The extension is all-length: each additional positive raises true slack by 43 while q=32 charge rises by only 32. Thus the displayed fallback edge is worst for every longer anonymous positive return. This is an exact finite-state theorem plus analytic monotonicity, not a finite-depth p catalogue.

## RL336.3 — exact zero-run certificates

Using the inherited owned-state lower threshold `22689747442693040208618`, the state upper bound above, and deterministic odd Collatz continuation to below `2^71`:

- A run of 37 zeros has 37 mechanical factors and exactly 5,343,788 owned candidates. Every candidate descends below `2^71`; maximum escape is 229 odd steps. Hence `z<=36` in this conditional branch.
- A run of 36 zeros has 36 mechanical factors and exactly 15,512,438 owned candidates. Every candidate descends below `2^71`; maximum escape is 234 odd steps. Hence `z<=35` in this conditional branch.

The ranges are gap-free: the verifier enumerates each complete factor and every odd start in its exact congruence class within the state band, subject to the affine owned-state threshold. Independent C++ and portable Python implementations agree factor by factor on counts and maxima. The portable zero-run-36 check is split into disjoint factor ranges `[0,12)`, `[12,24)`, `[24,30)`, `[30,36)`, with a checked aggregate. Classification: exact finite certificates under the explicitly conditional least-state floor.

## RL336.4 — exact rational consumer and cap

The inherited phase/telescope machinery consumes the q=32 anchor as

`W_struct >= K + C*(K/2 - (65/64)S - 107/64)`, `C=25120009946627/10^14`.

The exact rational verifier checks rho 60..2894, the uniform bridge 2895..21,999,999, and the inherited ordinary Q256 handoff at rho=22,000,000. The finite maximum is at rho=60, with `K=6112357564`, endpoint slack 3, optimal h=59,232,591 and RHS `32546278582.35252...`. The bridge upper RHS is `32546278588.09747...`, giving the self-consistent cap

`n<=32546278588`.

This improves the incoming cap by 10,942. Classification: exact rational conditional branch consumer, not R1 closure.

## Boundary and open obligation

No correction or demotion of inherited authoritative mathematics is needed. A q=33 diagnostic on the new `z<=35` graph encountered a physical p=5 row for pair `(24,27)` and did not yield the short uniform prefix theorem used above; it is not promoted as a q=33 result. The next theorem must supply a genuinely all-length affine/exact-state owned-descent or support obstruction that closes the ordered parent branch, rather than a continuing p-by-p or zero-run scan.
