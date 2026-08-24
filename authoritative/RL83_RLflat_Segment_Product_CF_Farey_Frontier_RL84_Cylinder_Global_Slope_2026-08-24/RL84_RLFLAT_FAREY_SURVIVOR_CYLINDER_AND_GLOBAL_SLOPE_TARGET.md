# RL84 target — RL♭ first Farey survivor, cylinder ownership, and local/global slope dichotomy

Date: 2026-08-24

## Purpose

Continue from RL83's segment-product first-surplus theorem and exact frozen-floor Farey frontier.

For a hypothetical primitive nontrivial positive shortcut-Collatz cycle, let

`M=RL♭=max C`, `R#=min C`.

RL83 proves that, conditional on the inherited external input `R#>=2^71`, no backward prefix from `M` can be multiplicatively surplus before depth

`114,208,327,604`.

At that earliest arithmetically possible depth, the reduced count pair is uniquely

`(p*,q*)=(114208327604,72057431991)`.

The primary RL84 question is:

# Can the first Farey survivor be coupled to the exact 3-adic word cylinder and the full-cycle denominator strongly enough to exclude it or force a new structural dichotomy?

Do not revert to blind residue expansion or generic continued-fraction enumeration.

---

## 1. Mandatory inherited interface

Use without re-deriving unless a verifier fails:

1. RL82 backward affine law
   `x_i=(2^i M-B_i)/3^{o_i}`;
2. unique word cylinder
   `M==2^{-i}B_i (mod3^{o_i})`, with even `M` giving one class modulo `2*3^{o_i}`;
3. ceiling
   `(2^i-3^{o_i})M<=B_i`;
4. exact top residue
   `M==26,80,152 (mod162)`;
5. prefix-balanced finite cylinders survive arbitrarily deep;
6. full denominator
   `(2^A-3^L)M=B_A`;
7. RL83 segment product
   `Delta_i<=o_i/(3R#)`;
8. reduced surplus tube
   `0<p log2-q log3<=q/(3R#)`;
9. exact frozen-floor Farey frontier
   `q>=72057431991`, `p>=114208327604`;
10. proper first-surplus overshoot ordering
    `2^j/3^o<2^A/3^L`;
11. distinct-slope branch
    `qQ>3R#log2`;
12. equal-slope branch
    `gcd(D_j,D)=2^{pd}-3^{qd}`, `d=gcd(g,G)`;
13. first-surplus count optimization does not improve the fixed-count `B` envelope;
14. the envelope maximizer `O^oE^e` is compatible with the `80 mod162` top branch.

Retain the RL20 warning that a naive CF-class -> final-return 3-adic address splice decouples without ownership/divisibility.

---

## 2. Required investigations

### 2.1 Exact cylinder/interval collision at the first Farey pair

At the earliest arithmetic pair

`j=p*=114208327604`, `o=q*=72057431991`, `e=j-o`,

all proper prefixes are balanced and the final symbol is `E`.

For a word `w`, combine exactly:

- its cylinder `M==m_w (mod2*3^o)`;
- its first-surplus ceiling `D_j M<=B_j`;
- positivity and `R#<=x_i<=M`;
- top branch `M==26,80,152 (mod162)`.

Seek a compressed theorem deciding emptiness of the interval/cylinder intersection without enumerating `~10^11` symbols or numerical maxima.

A useful invariant may be a normalized cylinder representative, a recurrence for the quotient of `B_i` by the surplus defect, or a monotone residue-height coordinate.

### 2.2 Use the actual Farey-neighbor structure, not a generic CF list

The first survivor is the mediant between

`103768467013/65470613321 < beta`

and

`10439860591/6586818670 > beta`.

Exploit this exact neighboring geometry.  Determine whether first-surplus word data can force the reduced slope onto a *different* Farey branch, or whether the mediant imposes congruences on `j,o,e` that interact with the 3-adic cylinder.

Do not spend the session merely generating later convergents.

### 2.3 Split proper first surplus from full-return first surplus

Handle separately:

- `j<A`: then `x_j<M`, local raw overshoot is strictly smaller than global overshoot, and the complementary count block is also surplus;
- `j=A`: the first surplus is the full return, so every proper maximum prefix is balanced.

The full-return branch may have a cyclic/Christoffel or maximum-rotation characterization that the proper branch lacks.

### 2.4 Equal local/global reduced slope branch

If

`j/o=A/L=p/q`,

write `(j,o)=g(p,q)`, `(A,L)=G(p,q)` with `g<G` for a proper prefix.

Use

`D_j=(2^p)^g-(3^q)^g`,

`D=(2^p)^G-(3^q)^G`,

and

`gcd(D_j,D)=2^{p gcd(g,G)}-3^{q gcd(g,G)}`.

Investigate whether

- `g|G` and hence `D_j|D`;
- the word-cylinder congruence;
- `D|B_A` / `M=B_A/D`;
- primitive rotation ownership

can be made incompatible.

A real result here would be the requested local-to-global divisibility bridge.

### 2.5 Distinct local/global reduced slope branch

If the slopes differ, use

`qQ>3R#log2`.

Try to combine this with

- `q,Q>=72057431991`;
- RL19/RL20 odd-state packing;
- any available bound on `L`, `A`, or `M/R#`;
- two-rational Farey separation;
- strict local/global overshoot ordering.

Do not treat the denominator-product inequality by itself as a contradiction.

### 2.6 First-survivor least-state window

At the exact earliest pair, RL83 proves

`R#<=4,358,487,209,795,430,953,242`.

Together with the inherited floor this gives a factor-`<1.846` window for `R#` if the first surplus occurs at the earliest pair.

Test whether inherited RL root congruences, phase packing, or ownership can exploit this *only if their hypotheses genuinely apply to the same RL object*.  Do not identify unrelated RL48 auxiliary states with `R#` or `M`.

### 2.7 Cylinder compatibility red team

Use the analytic family `O^oE^e` as the adversary:

- it is first-surplus prefix-balanced;
- it attains the count envelope;
- its cylinder is `M==-1 (mod3^o)`;
- for `o>=4` it lands in `M==80 (mod162)`.

Any proposed theorem relying only on prefix balance, count envelope, or the current top residue must survive this test.

### 2.8 Ordinary `+1` sensitivity

Preserve the additive `B_i` / `+1` product information.  A purely homogeneous slope theorem is unlikely to couple the Farey survivor to ownership.

---

## 3. Computational role

Small exact programs are encouraged for:

- symbolic recurrence discovery for cylinder representatives;
- exact modular experiments on compressed word families;
- Farey-neighbor / rational-interval checks;
- low-depth falsification of proposed cylinder invariants;
- equal-slope defect-gcd experiments.

Do **not** enumerate all words to the RL83 frontier, and do not scan numerical Collatz maxima to an enormous bound.

A finite experiment is evidence or an exact finite certificate only over its declared finite domain.

---

## 4. Stop / pivot conditions

Freeze the RL♭ first-surplus route if a serious attack shows that:

- the Farey slope and 3-adic cylinder remain independent under all available full-cycle identities;
- equal-slope defect gcd reduces to a standard difference-of-powers tautology with no ownership consequence;
- distinct-slope denominator separation yields only ever-larger length lower bounds;
- the interval/cylinder problem becomes unrestricted Collatz stopping-time analysis;
- progress becomes another residue ladder rather than a global consumer.

If so, return to the RL75 ranked **hybrid owned-macro periodicity-or-packing route**, preserving RL83 as a strong independent global lower-bound theorem and method barrier.

---

## 5. Desired outcome

Prefer, in order:

1. an analytic exclusion of the first Farey survivor cylinder for every legal word;
2. a local-to-global divisibility theorem that eliminates either the equal- or distinct-slope branch;
3. a finite structured family of Farey/cylinder survivors plus exact exclusion;
4. a sharp analytic no-go theorem proving the cylinder and slope data decouple, followed by an explicit pivot to the RL75 hybrid route.

Do not claim RL or Collatz closure without a complete chain.

---

## 6. Close-out requirements

Freeze separately:

- proved analytic mathematics;
- exact finite certificates;
- externally inherited certificates/input;
- computational evidence;
- conjectures;
- method barriers/dead routes;
- corrections/demotions;
- verifier status.

Create the next numbered authoritative bundle and matching sidecar, verify its internal manifest, and run a fresh-unpack fast suite.
