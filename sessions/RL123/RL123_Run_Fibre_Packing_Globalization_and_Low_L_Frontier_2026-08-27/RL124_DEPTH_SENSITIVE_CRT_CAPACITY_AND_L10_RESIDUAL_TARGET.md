# RL124 target — depth-sensitive CRT capacity and the `L=10` residual strip

RL123 has globalized run-fibre packing and moved the certified primitive nontrivial low-odd-count frontier to

`L>=10`.

The live `L=10` strip is analytically reduced to

`6<=Z<=24`.

A naive rooted-word scan contains `417,221,532` words and is not the preferred first move.

Work in this order.

## Priority A — depth-sensitive CRT strip capacity

For each physical odd-to-even boundary, retain its full run-depth pair `(o_i,z_i)`.

RL123 proves that the subset

`C_(j,k)={i:o_i>=j,z_i>=k}`

lies in one residue class modulo `2^k3^j`.

Turn the width ceiling

`W <= floor(B/D)`

into capacity inequalities such as

`C_(j,k) <= floor(W/(2^k3^j))+1`,

and combine them with the exact identities

`O_k=sum_i(o_i-k+1)_+`,
`Z_k=sum_i(z_i-k+1)_+`.

Seek an analytic infeasibility theorem or a sharply reduced run-profile family for `L=10`.

Do not replace this with a bulk word scan.

## Priority B — closest-rotation/window coupling

Use RL123.5:

`dist_cyc(w,rot_s(w)) = min_c sum_i |h_i^(s)-c|`.

On the live complement `R_*>=4`, every nontrivial shift has dispersion at least `4`.

Exploit `s=2,3,...` to force run diversity/depth patterns or to eliminate near-periodic profiles. Any `R_*<=3` profile hands directly to the inherited closed local engine.

Do not assume long runs or a run-count bound beyond what the window formula actually proves.

## Priority C — compressed exact ownership certificate

If A/B leave a finite residual profile set, test ordinary ownership through

`D | Q(w)`

using a compressed exact method:

- run-profile enumeration;
- dynamic programming;
- meet-in-the-middle on the ten odd positions;
- or another gap-free exact certificate.

The certificate must enumerate the analytically reduced family exactly and record primitive versus periodic hits.

A raw `417,221,532`-word scan is allowed only if a simpler exact compression genuinely fails and the run remains reproducible.

## Success conditions

Any one of the following is useful:

1. exclude all `L=10` primitive nontrivial candidates and promote `L>=11`;
2. reduce `6<=Z<=24` to a much smaller explicit run-profile family by analytic theorem;
3. strengthen `P_plus` or `H(L,Z)` through multi-depth CRT capacity;
4. prove a new `R_*<=3` producer from the sliding-window formula;
5. produce a reusable compressed exact ownership certificate architecture for subsequent `L`.

## Mandatory red teams

Preserve:

- RL20 ownership discriminator;
- RL79 generalized-increment scaling;
- RL81 physical-state ownership;
- primitivity and periodic-hit separation;
- Raw/Farey scope;
- exact finite-certificate scope.

No Gate closure may be claimed unless the actual global obligation is discharged.
