# RL92 SESSION STATE AND RL93 KICKOFF

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

## Incoming RL92 gate

- outer RL92 SHA-256: PASS;
- fresh internal RL92 manifest: PASS;
- supplied RL92 fresh-unpack verification: PASS;
- RL91 fast verifier suite: PASS.

Verification economy applied. No recursive historical expensive verification was performed.

## Frozen RL92 results

### Wide inherited exact tier

Modulo `2^5,000,056`:

`d<=5,000,030`, `r<=7,000,000` + minimal reset => `n_next<=5,000,053`.

### Extended deep exact tier

Modulo `2^10,000,056`, the complete exact scan over

`0<=r<=1,100,000`

has global minimum balanced inverse-residue bit length `10,000,034`, attained at `r=378,722`.

Therefore:

`boxed: d<=10,000,032 and r<=1,100,000 + minimal reset => n_next<=10,000,053.}`

### Updated weighted staircase cover

With

`mu=1/7,000,001`,

`lambda=5,900,000/35,000,222,000,031`,

every block outside the union of the two certified rectangles pays

`lambda*d+mu*r>=1`.

Every survivor must satisfy

`b-floor(lambda D_b+mu R_b^max)`

`<= (k-1-b)+floor(D_b/(C-10,000,053)).`

### Top block count is worst

`floor(lambda*C)=7,105>2`, so the contradiction margin strictly decreases as `b` rises. It is enough to test `b=k-1`.

### Odd interval eliminated

Every odd

`boxed: 2,921,630,975 <= k <= 2,921,652,721}`

is impossible on the exact first-Farey/full-phase Gate-A branch.

This removes `10,874` additional consecutive odd values.

Updated branch-specific surviving odd window:

`boxed: 2,921,652,723 <= k <= 42,150,931,559.}`

At `k=2,921,652,721`, margin `+4,796`.

At the next odd `k3=2,921,652,723`, margin `-17,013`.

### Ultra-deep exploratory tier

Exact non-load-bearing probe modulo `2^15,000,056`, `r=0..1,000`:

- minimum balanced bit length `15,000,048` at `r=88`;
- local consequence `d<=15,000,046 => n_next<=15,000,053`.

The present wide-to-deep support line already clears the later depth corners, so this ultra-deep tier does not improve the current one-line cover. The current deep depth-axis relaxation cannot activate before approximately `R_d=3,499,990`.

## Authoritative RL93 live obligation

Attack `k3=2,921,652,723` using the continuing multiscale 2-adic frontier.

Priority:

1. extend `2^10,000,056` beyond `r=1,100,000` using completed exact chunks only;
2. recompute the global deep minimum and supporting weights after each meaningful extension;
3. if `k3` closes, propagate immediately to the exact next failure point;
4. compare pure 10M extension with a fresh smaller-modulus middle tier when scan work becomes competitive;
5. revisit three-tier/ultra-deep convexification only when the staircase geometry makes its extra corner active;
6. do not promote tier-specific successor charging without a rigorous nontrivial lower bound on the stronger-tier population;
7. preserve first-Farey scope and all inherited red-team constraints.

## Sustained attack rule

A theorem, endpoint elimination, or improved bound is a checkpoint rather than a close trigger. Continue through case propagation, constant sharpening, adjacent frontier tiers, and red-team while the route remains productive.

Verification economy remains mandatory.
