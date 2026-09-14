# RL319 proof ledger — crossing contraction and root-aligned carry cap

Date: 2026-09-14
Status: FROZEN WITH RL319 CLOSEOUT

## A. Newly proved analytic mathematics

1. **Phase residue and coprimality.** In the nonzero-residue branch,
   `2^j delta_j == 3^(t_j)E (mod h)` and
   `gcd(delta_j,h)=1` at every phase.
2. **First-crossing decomposition.** At the first reverse crossing,
   `h(2p+1)=3delta+2q`, where `p` is even and
   `gcd(delta,h)=gcd(q,h)=1`.
3. **Rankwise suffix dominance.** For the post-crossing suffixes,
   `Q(beta)>=Q(alpha)`, with equality exactly for zero outstanding lead and
   identical suffixes.
4. **Support-independent crossing contraction.** If `(n,B)` are the remaining
   shadow suffix counts, `3^B q<=2^n E`.
5. **Half-step least-root transport.** RL135.2 is equivalent to
   `F(n)=aC(n)-ell n>=0` for every binary phase rooted at the least odd state.
6. **Ordered-row dichotomy.** The `epsilon=0` branch either places the least
   state in the late row or admits a least-rooted reduced balanced return.
7. **Late-row scaled contact.** In the first alternative, for interface height
   `s>=1`, the antipodal state has form `3^s m+K`, with
   `0<|K|<3^s2^35` and `3` not dividing `K`.

## B. Exact rational-interval consequences

At the first external survivor, a least-rooted balanced return satisfies

`0<G<2^35`, `v2(G)<=34`.

If its recomputed envelope residue is nonzero and
`epsilon=kappa H+r`, `0<r<H`, then

`0<=kappa<2^34`.

The verifier proves the load-bearing comparisons

`Delta<log(1+2^-40)` and `D0/H<2^-41`

using exact rational atanh-series enclosures.

## C. New method barriers and red teams

1. Local reverse-mismatch parity, positivity, divisibility, and coprimality
   admit an exact family for every `h>1` coprime to `6`; they cannot close the
   branch without global coupling.
2. The suffix inequality does not bound a dyadic-dominant suffix.
3. Re-cutting an ordered return at the least root need not preserve
   `epsilon=0` or row order.
4. The late-row contact band grows with unbounded interface height `s`; the
   present least-state input does not produce a finite certificate there.
5. The bounded verifier enumerations are regression evidence, not theorem or
   certificate.

## D. Preserved scope

- Internal-only reduced frontier: `ell>=190537`.
- Conditional external-certificate frontier: `ell>=49,547,666,544`.
- `g=1` remains separate.
- RL79, RL206, RL233, and RL263--RL264 remain binding.
- RL140--RL142 may be used only after proving their interface hypotheses.

Gate A: OPEN.
Gate B: OPEN.
Global positive non-trivial-cycle exclusion: OPEN.
No Collatz-conjecture claim is made.
