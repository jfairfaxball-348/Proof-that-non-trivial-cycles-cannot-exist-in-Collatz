# RL107 — odd-core collision ownership classification and basin-equality barrier

## Outcome

RL107 closes the stated odd-core-collision candidate with an exact physical
classification, but the route does **not** produce the required growing odd
product population or an ordinary full-ownership contradiction.

For the maximum-rooted first-Farey boundary states

`x_p, x_(2p), ..., x_((g-1)p)`, 

equal odd cores occur exactly across aligned all-even block runs.  Combining
this with the RL106 exclusion of runs of `ceil(g/2)` or more bounds each
collision class, but the resulting guaranteed number of distinct boundary
odd cores is only constant: it is `1` for `g=2,3` and `2` for every `g>=4`.
Thus raw multiplicity is not converted into a growing population of distinct
odd product phases.

A secondary exact ordinary-basin test identifies the equality-level interface
that would suffice for a blue contradiction: if the physical maximum were a
power of two, its two-odd-step roof predecessor would be a depth-two LTE
blue-comb node.  However, roof grammar, raw counts, and bare least
inverse-cylinder minimality do not force that dyadic equality.

No raw multiplicity, Gate, nontrivial cycle, or global Collatz statement is
closed by RL107.

## 1. Exact boundary odd-core collision classification

Let `1 <= h < k < g` and suppose

`oddcore(x_(hp)) = oddcore(x_(kp)) = y`.

Write

`x_(hp)=2^a y`,  `x_(kp)=2^b y`.

Because the states are distinct members of a simple cycle, `a != b`.  The
larger 2-adic exponent state reaches the smaller by the unique consecutive
halving chain on the common odd core.

The maximum-rooted physical placement now fixes the relevant cyclic arc.  The
complementary arc between two internal prefix boundaries passes through the
physical maximum `M`; it cannot be an all-even path, because an all-even path
is strictly decreasing at every step while both internal boundary states are
below `M`.  Therefore the all-even halving chain is the direct maximum-rooted
prefix arc

`x_(kp) -> ... -> x_(hp)`, 

whose length is `(k-h)p`.  Hence

`a-b=(k-h)p`,

and every step on that segment is even.  Equivalently:

> `oddcore(x_(hp)) = oddcore(x_(kp))` if and only if the `k-h` aligned blocks
> between those boundaries form an all-even (zero-odd-input) run.          (107.1)

The reverse implication is immediate: an all-even run consists only of
halvings and therefore preserves odd core.

This maximum-rooted argument is essential.  Directed-cycle simplicity alone
does not identify which cyclic arc is the halving chain.

## 2. Consequence of RL106

RL106 excludes aligned all-even runs of length at least `ceil(g/2)`.  Thus an
odd-core collision class among the `g-1` internal boundary indices has index
diameter strictly below `ceil(g/2)` and therefore at most `ceil(g/2)` members.
Consequently

`# distinct boundary odd cores >= ceil((g-1)/ceil(g/2)).`             (107.2)

Exactly,

- the lower bound is `1` for `g=2,3`;
- the lower bound is `2` for every `g>=4`.

The interval-class construction in the finite verifier shows the pure
combinatorial class-count bound is sharp under only this diameter restriction.
It is not asserted to realize a Collatz cycle.

Therefore the odd-core injection candidate fails its intended quantitative
purpose: RL106 forbids long collisions, but permits enough short local
collisions that no growing odd-product population follows.

## 3. Exact ordinary roof/blue-comb implication

Let `M` be the actual physical maximum of a hypothetical ordinary nontrivial
cycle, and let its two-odd-step roof predecessor be

`Q=(4M-5)/9`.

If `M=2^k`, the roof integrality condition gives `9 | 2^k+1`, hence
`k == 3 (mod 6)`.  Then

`Q=(4*2^k-5)/9 = 4(2^k+1)/9 - 1 = B(2,k)`,

and the ordinary Collatz trajectory is

`Q -> (2^(k+1)-1)/3 -> 2^k -> ... -> 1`.

Thus a physical nontrivial-cycle maximum cannot be dyadic.  This is an exact
ordinary basin identity.  It is also logically weaker than the already direct
observation that a power-of-two cycle state reaches `1`; its value here is to
pin down the precise roof/blue-comb equality interface.

## 4. Local equality-bridge barrier

The remaining question is whether first-Farey word information can force a
physical equality such as `M=2^k`.  The local data tested in RL107 do not.

The length-ten, weight-six inverse words

`1110001011` and `1100001111`

both begin with the same `11` inverse roof grammar and have the same raw
counts.  Their least positive even inverse-cylinder representatives are
respectively

`512=2^9` and `1106`.

These are finite local cylinder witnesses only.  They are **not** asserted to
be first-Farey words, physical cycle segments, or countermodels to the
first-Farey hypothesis.  They establish only the required negative point:
roof grammar plus raw counts plus bare least-cylinder selection do not force a
single dyadic type.  A successful equality bridge must use genuinely
word-sensitive physical ordering/full ownership beyond those data.

## 5. Red-team ledger

- **RL79 / generalized increment:** the odd-core collision classification is
  built from the common even branch and is not itself an ordinary-increment
  discriminator.  The blue-basin consequence is ordinary-specific: for a
  generalized `T_s`, scaling sends the corresponding blue-comb trajectory to
  the generalized `s <-> 2s` cycle rather than to `1`.
- **RL20 / denominator ownership:** no fake denominator divisibility or
  divided-out factor is used.  A future basin contradiction must arise from
  an actual physical equality.
- **RL81 / physical-state separation:** (107.1) concerns actual physical
  maximum-rooted boundary states.  The two cylinder witnesses are explicitly
  non-owned local examples and are never promoted to physical states.
- **Primitivity:** the argument uses a simple primitive orbit only to exclude
  repeated distinct cycle states and to identify the physical cyclic arcs.
- **Raw multiplicity:** `g` remains the raw first-Farey multiplicity.  No
  raw/reduced identification is made.
- **External input:** the application of RL106 in Section 2 remains
  conditional on RL106's inherited external ordinary cycle-minimum floor and
  RL101 maximum envelope.  The collision equivalence (107.1) itself does not
  require that external floor.
- **Scope:** no Gate or global theorem is claimed.

## 6. Corrections and demotions

No inherited authoritative theorem is demoted.

Two defects in the unpromoted Codex checkpoint draft were repaired before
promotion:

1. the checkpoint stated that (107.2) equals `2` for every `g>=3`; the exact
   arithmetic gives `1` at `g=3` and `2` only for `g>=4`;
2. the checkpoint attributed the direction of the all-even arc to simple-cycle
   injectivity alone; the frozen proof now supplies the required
   maximum-rooted physical argument showing the complementary arc passes
   through `M` and therefore cannot be all-even.

The interrupted bounded leading-`11` first-surplus enumeration through length
18 emitted no certified result and remains **NOT PROMOTED**.

## 7. Route decision

Freeze the following as method barriers:

- odd-core collisions + the RL106 run-length bound do not generate a growing
  population of distinct odd product phases;
- roof grammar + raw counts + residue/cylinder minimality do not by themselves
  force a dyadic physical equality.

The live next architecture is a **word-sensitive exact physical equality
bridge** from an actual first-Farey boundary state to a certified ordinary
basin node.  Congruence, quotient proximity, count data, or a non-owned local
cylinder match is insufficient.

## Verification

- `python3 verification/verify_odd_core_collision_geometry.py`
- `python3 verification/verify_roof_blue_alignment.py`

The first verifier checks the exact class-count arithmetic for `g=2..1000`,
including the corrected `g=3` endpoint.  The second checks 500 exact roof/comb
identities and the two same-count inverse-cylinder witnesses.
