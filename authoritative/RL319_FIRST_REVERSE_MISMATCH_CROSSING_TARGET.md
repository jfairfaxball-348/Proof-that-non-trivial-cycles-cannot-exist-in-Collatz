# RL319 — first reverse-mismatch crossing target

Date prepared: 2026-09-14
Status: PREPARED, NOT STARTED
Session type: DIRECT CROSS-CONTENT CROSSING ATTACK

## Absolute objective

Continue toward excluding positive non-trivial Collatz cycles.

## Authoritative starting point

Begin from the RL318 closeout and proof ledger. Do not repeat the RL318 historical survey.

Maintain two distinct frontiers:

- internal-only reduced frontier: `ell>=190537`;
- conditional external-certificate reduced frontier: `ell>=49,547,666,544`.

On the external-conditional track, the first above-side survivor is

`(a,ell)=(217,976,794,617,137,528,045,312)`.

## Primary target: exact first reverse mismatch

Use the RL317 nonzero-residue branch.

Let

`X=2^a`, `Y=3^ell`, `H=X+Y`,
`d=gcd(H,epsilon)`, `h=H/d>1`, `E=epsilon/d`.

Over one balanced row compare:

- the physical content-`h` `T_h` trajectory, starting at `hR` and ending at `hx`;
- the coprime-content shadow trajectory, starting at `hR-E` and ending at `hx+E`.

For the signed gap `delta=P-S`:

`delta_0=E>0`,
`delta_a=-E<0`.

At every phase, physical states are divisible by `h` and shadow states are coprime to `h`, so `delta!=0`.

Same-parity updates are

- even/even: `delta -> delta/2`;
- odd/odd: `delta -> 3delta/2`.

The inherited first mismatch has orientation physical odd / shadow even and gives

`delta' = P + (delta+h)/2 >0`.

Hence the first mismatch cannot cross. A later physical-even / shadow-odd mismatch is mandatory. At such a step

`delta'=(delta-2S-h)/2`.

The first crossing therefore satisfies

`0<delta<2S+h`,
`delta'<0`.

### Required attack

Derive a genuinely non-homogeneous consequence from this crossing. Preferred outcomes:

1. force `h=1`, contradicting the nonzero-residue branch;
2. force a forbidden zero gap or impossible divisibility/coprimality condition;
3. combine pre-crossing and post-crossing evolution to obtain a bounded carry independent of support;
4. connect the crossing to the complementary full-D remainders `D0r` and `D0(H-r)`;
5. derive a support-independent finite certificate.

Do not replace this with standalone normalized `T_h` invariants: RL79 blocks that route.

## Quantitative first-survivor input

At the first external survivor,

`Delta=a log(2)-ell log(3)`

is approximately `8.986548708617925e-13`.

For a genuine balanced return with `x=R+G`, positivity gives

`G/R < exp(Delta)-1`,

hence

`x/R<exp(Delta)`.

Historical RL134--RL137 additionally give for `g=2`:

- all accelerated-prefix mechanical defects are nonnegative;
- positive prefixes are confined to canonical contact geometry;
- `m<2^75` internally;
- conditional on the external least-state floor, `2^71<=m<2^75`.

Use these only if they enter the crossing proof directly. Do not restart broad historical archaeology.

## Secondary target: ordered-row zero branch

If the crossing route fails cleanly, attack `epsilon=0`.

Then `tau=u`, `sigma=v`, and the rows are rankwise ordered. Use simultaneously:

- genuine `D0 | U+V`;
- `H | U-V` and physical state swap `R<x`;
- integer parity ownership;
- first-survivor nonnegative-defect geometry.

Target a theorem forcing `u=v`. RL21 remains the negative control showing that `H`-side order alone is insufficient.

## Explicit barriers already checked

Do not spend a session retrying:

- bare continued fractions/product inequalities;
- fixed-depth complete residue-prefix descent;
- count-only gcd restrictions;
- generic RL310 segment packing at `g=2` on this fibre;
- standalone homogeneous `T_h` moments/products/permutations;
- RL140 multiplicity-two contact obstruction without first proving a `<=3` changed-contact theorem;
- RL141/RL142 bounded-interface machinery without verifying their hypotheses at `g=2`;
- support-by-support grammar or the RL316 `a<=22` scan.

## Scope

Gate A remains open.
Gate B remains open.
Global positive non-trivial-cycle exclusion remains open.
No Collatz conjecture claim is made.
Lean formalisation remains separate.
