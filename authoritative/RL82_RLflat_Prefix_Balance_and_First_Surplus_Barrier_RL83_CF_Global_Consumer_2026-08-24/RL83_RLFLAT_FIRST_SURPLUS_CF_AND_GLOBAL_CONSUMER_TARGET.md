# RL83 target — RL♭ first-surplus prefix, continued-fraction gate, and global consumer

Date: 2026-08-24

## Purpose

Continue from the RL82 maximum-state architecture without reverting to blind residue-tree expansion.

For a hypothetical nontrivial positive shortcut-Collatz cycle, let

`M=RL♭=max C`.

Along the backward cycle from `M`, let `o_i` be the number of odd predecessors among the first `i` steps and define the first multiplicative-surplus index

`j=min{i>=1 : 2^i>3^{o_i}}`.

The full cycle satisfies `2^A>3^L`, so `j` exists.

RL82 proves that every finite prefix has an exact affine/cylinder description and that only surplus prefixes contain nontrivial maximum-ceiling information. The first 183 prefixes are forced balanced conditional on the inherited external floor `R#>=2^71`.

The primary RL83 question is:

# Can the first-surplus prefix be consumed by the global cycle denominator / continued-fraction / packing structure strongly enough to exclude it?

Do not make deeper modulus enumeration the primary attack.

---

## 1. Mandatory inherited RL82 interface

Use without re-deriving unless a verifier fails:

1. `x_i=(2^i M-B_i)/3^{o_i}`;
2. word cylinder `2^i M==B_i (mod3^{o_i})`;
3. ceiling `(2^i-3^{o_i})M<=B_i`;
4. prefix-balanced words have unbounded finite cylinders;
5. fixed-count envelope
   `B_i<=2^{e_i}(3^{o_i}-2^{o_i})`;
6. surplus bound
   `M<=2^e(3^o-2^o)/(2^i-3^o)`;
7. near resonance
   `0<i log2-o log3<2^e/M`;
8. full cycle
   `(2^A-3^L)M=B_A`;
9. maximum-rotation inequalities
   `(2^i-3^{o_i})B_A<=B_i(2^A-3^L)`;
10. local CF gate: for `g=gcd(i,o)`, `p=i/g`, `q=o/g`, if
    `2^(e+1)q^2<M o log2`, then `p/q` is an above-`log_2 3` convergent;
11. exact top residue
    `M==26,80,152 (mod162)`;
12. pure finite-depth residue pruning is barrier-limited.

---

## 2. Required investigations

### 2.1 First-surplus optimization, not all-word enumeration

The first surplus has

`2^(j-1)<=3^{o_j}<2^j`

and its last symbol is `E`.

Exploit this special first-crossing geometry. Seek an exact optimization of `B_j` **subject to all previous prefixes being balanced and to the unique 3-adic cylinder**, rather than the coarse unrestricted fixed-count bound.

The coarse count envelope first loses the `2^71` contradiction at `(j,o,e)=(184,116,68)`, but this is not a word-level survivor. Determine the true first word-level frontier if it is compressible.

### 2.2 Merge the cylinder residue with the ceiling bound

For a word with odd count `o`, the maximum lies in one class modulo `2*3^o` but also satisfies a finite upper bound once surplus occurs.

This gives a finite interval/residue collision problem:

`M == m_w (mod 2*3^o)`

and

`M <= B_j/(2^j-3^o)`.

Seek an analytic or finite-state criterion deciding when that intersection is empty without enumerating all words.

### 2.3 Continued-fraction consumer

For every surviving first-surplus prefix reduce

`j/o=p/q`.

Apply the RL82 local CF gate and compare with the exact continued-fraction spine of `beta=log_2 3` already used by RL20.

Look for one of:

- an index parity restriction;
- a denominator/gcd incompatibility;
- a clash between the 3-adic cylinder and convergent numerators/denominators;
- a large-next-partial-quotient requirement that can be certified away;
- a coupling to the global reduced ratio `A/L`.

Do not merely restate that the ratio is close to `log_2 3`.

### 2.4 Couple local first surplus to the full cycle

Use

`(2^A-3^L)M=B_A`

and

`(2^j-3^o)B_A<=B_j(2^A-3^L)`.

Seek a relation between the local defect

`D_j=2^j-3^o`

and the full defect

`D=2^A-3^L`.

Potential consumers include divisibility, gcd, rotation, and state packing. A useful theorem should make the first surplus more restrictive because it lives inside the *same* closed cycle, not just inside an arbitrary capped excursion.

### 2.5 Top/bottom coupling

Use the inherited least state `R#` only through audited interfaces. Since `R#<=x_i<=M`, ask whether the first-surplus state can be squeezed simultaneously by

- the RL82 affine formula;
- the `R#>=2^71` floor;
- coprime-6 state packing;
- odd-step product bounds;
- the fact that `M` is the unique global maximum.

A ratio bound on `M/R#`, even weak, could materially sharpen the local surplus inequality.

### 2.6 Critical balanced ray red-team

The minimal-density balanced mechanical word begins

`OOEOOEOOEOEOO...`

and every finite prefix has an unbounded cylinder. Any proposed first-surplus theorem must explain why a genuine closed cycle cannot simply shadow this ray for a very long time and then exit.

Use it as the adversarial test case.

### 2.7 Ordinary `+1` sensitivity

Preserve the additive `B_i` / cylinder data. A purely homogeneous count argument will not distinguish the ordinary `+1` map from generalized `+s` maps and is unlikely to close the route.

---

## 3. Computational role

Small exact programs are encouraged for:

- dynamic optimization over balanced prefixes;
- exact interval/residue collision checks;
- continued-fraction reconstruction with rational interval arithmetic;
- falsifying proposed induction rules;
- finding the first word-level frontier beyond the coarse depth-183 certificate.

Do not enumerate numerical candidate maxima to a huge bound as the main method.

A finite frontier must be labelled an exact finite certificate, not an analytic infinite proof.

---

## 4. Fast stop / pivot conditions

Freeze the route if:

- first-surplus survivors merely move to larger depth without a compressible invariant;
- the 3-adic cylinder and CF spine remain independent;
- the maximum-rotation inequalities collapse to the standard full-cycle denominator with no extra content;
- the critical balanced ray defeats every proposed local induction;
- the attack becomes unrestricted Collatz stopping-time analysis rather than maximum-specific cycle analysis.

If that happens, return to the ranked RL72/RL75 global route map. The deferred unit-lattice/content route remains available.

---

## 5. Desired outcome

Prefer, in order:

1. an analytic contradiction for every possible first-surplus prefix;
2. a theorem forcing first-surplus count pairs onto a finite/structured CF spine plus an exact exclusion of that spine;
3. a nontrivial local-to-global divisibility/gcd bridge between `D_j` and `D`;
4. a sharp analytic barrier theorem explaining why first-surplus information cannot couple to closure.

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

Create the next numbered authoritative bundle and sidecar and verify its internal manifest and fresh-unpack fast suite.
