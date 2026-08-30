# RL191 — Universal Carry-Completed Gap Transport, Spacing 1001, and Flow 480

Date: 2026-08-30  
Authoritative branch: sole high branch `(v,H,J,d)=(37,0,23,-1)`  
Incoming authority: RL190 at commit `69bffb574ff185d927e7ed1128bca7a44e228b4e`

## Executive result

RL191 removes the two phase-46 exceptional ranks without assuming a common-mechanical step across the switch/carry seam.  The replacement is an exact carry-completed normalized-gap transport law inherited from the full-period `K/rho` identities:

\[
2^{c_i}\Delta_{i+1}=3\Delta_i+\varepsilon_i,\qquad |\varepsilon_i|<2.
\]

The bound is universal for the physical source transition: ordinary noncarry sources have `|epsilon_i|<1`, while the unique carry source has `epsilon_i=2-2^{-h_i}`, hence still `<2`.  The mechanical switch is not an exception because the law uses the actual source bit `c_i`.

Using that universal law, an exact finite rank/word certificate excludes every necessary extremal-triple terminal separation from 46 through 1000.  Therefore consecutive extremal `{35,36,37}` triple terminals have chronological spacing at least 1001.

That spacing improves the exact `N35` density bound to

\[
N_{35}\le \left\lfloor\frac{57L}{1037}\right\rfloor
       =7,559,400,754.
\]

Re-optimising the inherited RL187 safe charging families at this new population crossover yields ordinary absolute corrected flow

\[
> \frac{24,171,310,097}{50,331,648}>480.
\]

The inherited signed/carry conversion then gives each signed flow mass `>240` and each directional `K` variation `>80`.  These are total-variation statements, not chronological excursion statements, and they do not close the branch.

The dangerous H21 early core
`D=[23,369,453,298,41,775,866,136]`
remains open.  Its `{33,34,35}` charging family is still exactly binding; RL191 does not relax that budget.

## 1. Incoming certified state

RL190 supplied:

- `A=217,976,794,617`;
- `L=137,528,045,312`;
- `B=A-L=80,448,749,305`;
- `R=L-B=57,079,296,007`;
- extremal terminal-rank interval
  `E=[72,797,034,370,103,818,202,602]`;
- extremal triple spacing at least 46;
- exact separation-46 overlap
  `[85,411,789,764,103,818,202,602]`;
- two exceptional necessary ranks
  `90,789,138,715` and `101,129,528,126`;
- `N36=7,238,318,174`;
- `N37=7,052,720,272`;
- clean-start total `10,075,174,499`;
- dangerous H21 `{33,34,35}` core
  `D=[23,369,453,298,41,775,866,136]`.

RL191 accepts these under verification economy and does not recursively reopen their derivations.

## 2. Universal carry-completed normalized-gap transition

Use the RL181 full-period identities

\[
\rho_i=\frac{2^{b_i}}{3^i},\qquad
q_i=\frac{2^{S_i}}{3^i},\qquad
h_i=b_i-S_i,\qquad
c_i=b_{i+1}-b_i\in\{1,2\},
\]

and

\[
K_{i+1}-K_i=\frac13 q_i(2^{G_i}-1),\qquad
\rho_{i+1}=\frac{2^{c_i}}3\rho_i.
\]

Define the carry-completed normalized pair gap

\[
\Delta_i:=K_i/\rho_i.
\]

On a noncarry source this is the physical pair gap `x_{i+p}-x_i`; at the unique `p`-shift carry source it is the carry-completed gap `2m-x_i`.  Dividing the `K` increment by the next `rho` gives exactly

\[
2^{c_i}\Delta_{i+1}
 =3\Delta_i+2^{-h_i}(2^{G_i}-1).
\]

Thus

\[
\varepsilon_i:=2^{-h_i}(2^{G_i}-1).
\]

For an ordinary noncarry `p`-edge, `G_i=h_i-h_j`, so

\[
\varepsilon_i=2^{-h_j}-2^{-h_i},
\]

and `|epsilon_i|<1`.

At the unique carry source the inherited carry relation gives `G_i=h_i+1`, so

\[
\varepsilon_i=2-2^{-h_i},
\]

hence `1<=epsilon_i<2`.

Therefore the conservative physical law

\[
\boxed{2^{c_i}\Delta_{i+1}=3\Delta_i+\varepsilon_i,\quad
|\varepsilon_i|<2}
\]

holds across ordinary sources, the mechanical switch, and the carry source.  No common-mechanical hypothesis is required.

## 3. Phase-46 exceptional ranks

At separation 46 there are `n=9` source transitions.  The two RL190 exceptional ranks are fed directly into the universal law with their actual mechanical source words.  Starting from the inherited terminal gap

\[
\Delta_0=3^{37}/2^{21},
\]

the exact conservative affine error ball misses both permitted later `tau=37` start gaps, `2^37` and `2^38`, at each exceptional rank.

Thus the two necessary phase-46 ranks

- `90,789,138,715`;
- `101,129,528,126`

are excluded.  Together with RL190's safe phase-46 atoms, separation 46 is fully excluded.

## 4. Exact finite resonance scan: separations 46 through 1000

For a candidate terminal separation `s`, let `n=s-37`.  The necessary terminal-rank overlap is

\[
E\cap(E-sB\bmod L).
\]

For each nonempty overlap, RL191 partitions the integer rank interval at every preimage of:

- the modular wrap `0`;
- the mechanical threshold `R`;

for every source offset `j=0,...,n-1`.  Each resulting integer atom therefore has one exact constant source-bit word

\[
c_j\in\{1,2\}.
\]

For a fixed word, propagate the conservative error ball from
`Delta_0=3^37/2^21`.  If the accumulated source sum is `S`, the centre is

\[
3^s/2^{21+S}.
\]

Writing the radius as `radnum/2^S`, the exact recurrence under
`|epsilon|<2` is

\[
\text{radnum}\leftarrow 3\,\text{radnum}+2\cdot2^S,\qquad
S\leftarrow S+c.
\]

The verifier then checks, using integer arithmetic only, that for both targets
`T in {2^37,2^38}`,

\[
|3^s-T2^{21+S}|>\text{radnum}\,2^{21}.
\]

Certificate totals:

- separations scanned: 46 through 1000 inclusive;
- nonempty necessary separations: `432`;
- exact constant-word atoms: `24,173`;
- minimum affine safety margin: `>5,999,580`;
- worst certified atom:
  `(s,a,b,T,S)=(665,103606717628,103809541145,2^37,996)`.

Therefore:

\[
\boxed{\text{consecutive extremal triple terminal spacing}\ge 1001.}
\]

This is a finite theorem through 1000, not a claim that all larger separations are impossible.

## 5. Exact `N35` density consequence

An extremal triple block has span 38 and owns three `N35` starts.  Spacing at least 1001 forces the following nontriple span to satisfy

\[
S\ge1001-38=963.
\]

Use the inherited nontriple capacity

\[
K\le \lfloor 2S/37\rfloor.
\]

Write `S=37q+r`, `0<=r<37`.  Then
`K<=2q+1_{r>=19}`.  Exact cross multiplication shows

\[
\frac{3+K}{38+S}\le\frac{57}{1037}.
\]

For fixed `r`, the slack

\[
57S-945-1037K
\]

increases by 35 when `q` increases, so it is enough to check the least
`q` allowed by `S>=963` for each residue.  The verifier checks all 37 residues.  Arithmetic equality occurs at `S=999,K=54`; no physical-realisation claim is made.

Hence

\[
N_{35}\le\left\lfloor\frac{57L}{1037}\right\rfloor
=7,559,400,754,
\]

with remainder 886.

Population consequences:

- clean starts with `tau<=34`: at least `2,515,773,745`;
- `tau=35` population cap boundary: `321,082,580`;
- inherited `tau=36` population: `185,597,902`;
- inherited `N37=7,052,720,272`.

## 6. Reweighted safe charging and corrected-flow floor

Reuse RL187's exact terminal-height vocabulary and all inherited low/high co-ownership families.  Set

\[
U=2^{-25}.
\]

RL191 uses the safe schedule

- `tau<=34`: `10U/3 = 5/(3*2^24)`;
- `tau=35`: `4U/3 = 1/(3*2^23)`;
- `tau=36`: `4U/3 = 1/(3*2^23)`;
- `tau>=37`: `U`.

The verifier rechecks every conservative low-height family and every inherited high co-ownership family:

- H18 `{28,29,30,31,32,33,34,35}`;
- H19 `{30,31,32,33,34}` or `{31,32,33,34,35,36}`;
- H20 `{31,32,33,34,35,36}`;
- H21 `{33,34,35}` or `{34,35,36,37}`;
- H22 `{35,36}`;
- H23 `{37,38}`;
- H24 `{39}`.

Two families bind exactly:

- H20 `{31,32,33,34,35,36}` equals `2^-21`;
- H21 `{33,34,35}` equals `2^-22`.

Thus the H21 early core remains a genuine binding object.

Using the exact new populations, ordinary absolute corrected flow is

\[
>
2,515,773,745\frac{10U}{3}
+321,082,580\frac{4U}{3}
+185,597,902\frac{4U}{3}
+7,052,720,272U
\]

which equals

\[
\boxed{>\frac{24,171,310,097}{50,331,648}>480.}
\]

By the inherited RL187 signed-total/carry conversion:

\[
\text{each signed flow mass}>
\frac{24,171,310,097}{100,663,296}>240,
\]

and

\[
\boxed{\text{each directional }K\text{ variation}>
\frac{24,171,310,097}{301,989,888}>80.}
\]

These are aggregate variation bounds only.

## 7. What remains open

RL191 does **not** prove:

- nonexistence of the sole high branch;
- nonexistence of isolated/extremal triples;
- a spacing theorem beyond 1000;
- a chronological `K` excursion of size 80;
- an incidence/sign/recurrence law for the H21 early core `D`;
- any Gate A, Gate B, or global Collatz closure.

The next useful problem is no longer the phase-46 seam.  It is to consume the universal transport theorem structurally: either replace the bounded 46..1000 scan by an analytic resonance obstruction, or turn the strengthened >480/>80 aggregate flow into a valid chronological/phase-order contradiction without confusing total variation with excursion.
