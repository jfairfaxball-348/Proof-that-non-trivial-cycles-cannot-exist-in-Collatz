# RL91 SESSION STATE AND RL92 KICKOFF

Date: 2026-08-25

## Frozen global status

- radius-3 primitive/full-`D`: closed local theorem;
- Gate A even terminal `k`: closed analytically;
- Gate A terminal `k<=25`: closed by inherited exact finite certificate;
- Gate A odd `k>=27`: open globally;
- Gate A globally: open;
- Gate B globally: open;
- RL/nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

The first-Farey/full-phase branch is narrowed further but remains branch-specific.

## Incoming RL91 gate

- outer RL91 SHA-256: PASS;
- fresh internal RL91 manifest: PASS;
- supplied RL91 fresh-unpack verification: PASS;
- RL90 fast verifier suite: PASS.

Verification economy applied. No recursive historical expensive verification was performed.

## Frozen RL91 results

### Wide exact 2-adic tier

Modulo `2^5,000,056`, the complete exact GMP scan over

`0<=r<=7,000,000`

has global minimum balanced inverse-residue bit length `5,000,032`, attained at `r=2,595,446`.

Therefore:

`boxed: d<=5,000,030 and r<=7,000,000 + minimal reset => n_next<=5,000,053.}`

### Deep low-r exact tier

Modulo `2^10,000,056`, the complete exact GMP scan over

`0<=r<=300,000`

has global minimum balanced inverse-residue bit length `10,000,037`, attained at `r=33,524`.

Therefore:

`boxed: d<=10,000,035 and r<=300,000 + minimal reset => n_next<=10,000,053.}`

### Weighted staircase cover

With

`mu=1/7,000,001`,

`lambda=6,700,000/[7,000,001*5,000,031]`,

every block outside the union of the two certified rectangles pays

`lambda*d+mu*r>=1`.

Hence the number outside the union is at most

`floor(lambda D_b + mu R_b^max)`.

Every survivor must satisfy

`b-floor(lambda D_b+mu R_b^max)`

`<= (k-1-b)+floor(D_b/(C-10,000,053)).`

### Top block count is worst

For fixed `k`, the weighted bad-block floor rises by at least

`floor(lambda*C)=8,068`

per added block, while the explicit block-count contribution gains only `2` and the short-successor capacity is nondecreasing.

Hence it is enough to test `b=k-1`.

### Odd interval eliminated

Every odd

`boxed: 2,921,406,841 <= k <= 2,921,630,973}`

is impossible on the exact first-Farey/full-phase Gate-A branch.

This removes `112,067` consecutive odd values.

Updated branch-specific surviving odd window:

`boxed: 2,921,630,975 <= k <= 42,150,931,559.}`

At `k=2,921,630,973`, the top-stratum contradiction margin is `+586`.

At the next odd

`k2=2,921,630,975`,

the frozen two-tier margin is `-23,150`.

## Authoritative RL92 live obligation

Attack `k2=2,921,630,975` using the **multiscale 2-adic frontier**.

Priority:

1. extend the `10,000,056`-bit deep tier beyond `r=300,000`;
2. update the exact supporting-line weights after each extension;
3. compare deep-tier extension against widening the `5,000,056`-bit tier beyond `r=7,000,000`;
4. introduce a third modulus tier if its frontier corner improves the convex cover;
5. test tier-specific successor charging rather than conservatively charging every covered block at `10,000,053`;
6. close `k2` if possible, then propagate immediately through the next odd interval;
7. freeze the exact last positive and first nonpositive margins.

Do not brute-force all cofactors below `2^D`. Do not restart independent full-`D` midpoint congruence accumulation. Do not infer primitivity from repeated differences or cofactors.

## Sustained attack rule

A theorem, endpoint elimination, or improved bound is a checkpoint rather than a close trigger. Continue through case propagation, constant sharpening, adjacent frontier tiers, and red-team while the route remains productive.

Verification economy remains mandatory.
