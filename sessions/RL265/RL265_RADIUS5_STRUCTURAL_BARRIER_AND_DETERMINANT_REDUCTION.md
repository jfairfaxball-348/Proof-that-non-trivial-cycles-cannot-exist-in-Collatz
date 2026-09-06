# RL265 — Radius-5 structural barrier and determinant reduction

Date: 2026-09-06
Classification: **RADIUS5_EXACT_BARRIER_FOUND**

Incoming authoritative head: `ad4e7afe3520670f2960e44b57c3cdfc0184d543` (RL264).

## 1. Scope and frozen work

This session follows the RL264 user-directed pivot exactly.

Frozen and not touched:
- Gate A;
- the fifth retained arithmetic selector;
- selector-by-selector enumeration.

Radius 4 remains a promoted local theorem. Gate B remains open. No global non-trivial-cycle exclusion is claimed.

The RL265 objective is the literal Radius-5 local-theorem upgrade. The general Radius-n programme is secondary and may be pursued only if Radius 5 exhibits a genuine uniform mechanism.

## 2. Recovered Radius-4 / Radius-5 provenance

The authoritative chain recovered before new work was:

- RL238: literal exact-distance-4 local theorem proved for the audited primitive/full-`D` self-rotation setting; the exact Radius-4 flow topologies are the height-two `(1,2,1)` case plus the flat connected/component partitions `[4]`, `[3,1]`, `[2,2]`, `[2,1,1]`, `[1,1,1,1]`.
- RL239: independent Radius-4 audit passed. Radius 5 was assessed as a moderate new project. It proved the exact area-5 flow classification into nine topology families and promoted only a finite `A<=18` certificate: 181,542 raw exact-distance-5 word/shift instances; 10 full-`D` hits; all ten are the nonprimitive alternating `A=10,L=5,D=781` repetition; zero primitive hits.
- RL247: positive-domain scope audit passed. The exact negative regression `d=00011110111`, `A=11,L=7,D=-139,Q=18904,n=-136` is an exact-Radius-4 negative-cycle example but lies outside the written `D>1` theorem scope. No Radius-3/4 demotion was required.
- RL264: Radius 4 remains promoted locally; Radius 5 is activated; Gate A and the fifth selector are explicitly frozen.

No later Radius-4 demotion was found in the live history through RL264.

The literal Radius-5 target is therefore: take the exact audited RL238 local theorem statement and replace exact cyclic distance `4` by exact cyclic distance `5`, retaining every other admissibility hypothesis (primitive, full-`D`, positive-domain and any explicit RL238 strict/equality side conditions) unchanged. This session does not weaken those hypotheses by analogy.

## 3. Independent reconstruction of the audited metric

For a binary word `d=(d_0,...,d_{A-1})`, let

`L=sum d_i`,
`D=2^A-3^L`,

and use the promoted parity-word numerator convention

`Q(d)=sum_{i:d_i=1} 2^i 3^(L-r_i)`

where `r_i` is the ordinal number (starting at 1) of the one at position `i`.

This convention exactly reproduces the promoted root-crossing identity

`2 Q(tau d) = 3^(d_0) Q(d) + d_0 D`

for the left cyclic rotation `tau`.

For two equal-mass binary words `x,y`, define prefix discrepancy

`c_i=sum_{j=0}^i (x_j-y_j)`.

The cyclic adjacent-transposition distance is the cyclic earth-mover value

`dist_cyc(x,y)=min_{t in Z} sum_i |c_i-t|`.

An optimal integer `t` is any median of the `c_i`. The corresponding optimal integer flow is

`g_i=c_i-t`.

For `y=tau^m x`, the exact distance is `sum_i |g_i|`.

This reconstruction is independently checksumed by the RL239 finite count: exhaustive positive-domain enumeration through `A<=18` gives exactly 181,542 distance-5 word/shift instances and exactly the ten RL239 full-`D` hits described above.

## 4. Exact Radius-5 topology theorem

Let `g` be an optimal transport flow with

`sum_i |g_i|=5`.

Because `x_i-y_i=g_i-g_{i-1}` and `x_i-y_i in {-1,0,1}`, adjacent flow heights differ by at most one.

Therefore:

1. `max |g_i| <= 2`. A height three point would require at least the mass profile `1,2,3,2,1`, already of mass 9.
2. If `max |g_i|=1`, every nonzero component is a constant-sign run of unit height. The component lengths are therefore one of the seven integer partitions of 5:
   `[5]`, `[4,1]`, `[3,2]`, `[3,1,1]`, `[2,2,1]`, `[2,1,1,1]`, `[1,1,1,1,1]`.
3. If `max |g_i|=2`, any height-two component contains a `1,2,1` core of mass four. The fifth unit either extends one shoulder of that component, giving the connected height-two family `(1,1,2,1)` / `(1,2,1,1)` up to reflection, or forms a separate unit component, giving the height-two `4+1` family.

Thus the exact distance-5 transport classification has precisely nine topology families, independently reproducing RL239 without an orientation/cyclic omission.

## 5. New exact determinant lemma

Define the signed transport skew

`kappa=sum_i g_i`.

Since `|z| == z (mod 2)` for every integer `z`,

`kappa == sum_i |g_i| == 5 (mod 2)`.

Hence `kappa` is odd and in particular nonzero. Also

`|kappa| <= sum_i |g_i| = 5`,

so

`|kappa| in {1,3,5}`.

For `y=tau^m x`, summing the prefix discrepancy and reducing modulo `A` gives

`kappa == -m L (mod A)`.

Therefore there is an integer `q` such that the exact determinant identity holds:

`q A - m L = kappa`.

Consequences:

- Radius 5 has **no zero-skew sector** for the elementary parity reason above.
- `gcd(A,L)` divides `kappa`, hence every exact Radius-5 self-rotation satisfies

  `gcd(A,L) in {1,3,5}`.

- The Radius-5 arithmetic naturally splits into three determinant sectors `|kappa|=1,3,5`.
- If `gcd(A,L)=3` or `5`, dividing by the common gcd turns the corresponding `|kappa|=3` or `5` equation into an exact determinant-one approximation for the reduced pair. Any continued-fraction use must nevertheless preserve the RL238/RL239 reduced-denominator/multiple correction: a reduced convergent denominator is not automatically the original denominator.

The exhaustive `A<=18` replay checks this determinant identity on all 181,542 exact-distance-5 instances.

## 6. Topology-specific skew possibilities

Writing the sign of each unit-height component explicitly gives:

- `[5]`: `|kappa|=5`;
- `[4,1]`: `|kappa| in {3,5}`;
- `[3,2]`: `|kappa| in {1,5}`;
- `[3,1,1]`: `|kappa| in {1,3,5}`;
- `[2,2,1]`: `|kappa| in {1,3,5}`;
- `[2,1,1,1]`: `|kappa| in {1,3,5}`;
- `[1,1,1,1,1]`: `|kappa| in {1,3,5}`;
- connected height-two mass 5: `|kappa|=5`;
- height-two `4+1`: `|kappa| in {3,5}`.

This is a sharper arithmetic partition than the unsigned nine-family list and supplies the natural successor proof organisation.

## 7. Exact lower-radius irreducibility barrier

A tempting Radius-n strategy would be to prove that an exact distance-5 self-rotation necessarily gives some other self-rotation at distance 3 or 4 and then invoke the existing local theorem.

That strategy is false in every Radius-5 topology family.

The verifier contains the following primitive positive-domain witnesses. For each row:

- the displayed shift has exact cyclic distance 5;
- the word is primitive;
- `D>1`;
- **no nontrivial cyclic rotation of the word has distance 3 or 4**.

| Radius-5 topology | A | L | D | word | shift m | set of all nontrivial rotation distances |
|---|---:|---:|---:|---|---:|---|
| `[5]` | 10 | 5 | 781 | `1111100000` | 1 | {5,8,11,12,13} |
| `[4,1]` | 10 | 5 | 781 | `1111010000` | 1 | {5,6,9,10,11} |
| `[3,2]` | 10 | 5 | 781 | `1110110000` | 9 | {5,6,7,8,9} |
| `[3,1,1]` | 10 | 5 | 781 | `1101010100` | 3 | {2,5} |
| `[2,2,1]` | 11 | 5 | 1805 | `11011010000` | 1 | {5,7,8,9} |
| `[2,1,1,1]` | 10 | 5 | 781 | `1101010100` | 1 | {2,5} |
| `[1,1,1,1,1]` | 13 | 6 | 7463 | `1101100100100` | 2 | {5,6,7,8} |
| height-two connected | 13 | 7 | 6005 | `1101101101000` | 3 | {5,6,8,9} |
| height-two `4+1` | 12 | 5 | 3853 | `111001001000` | 3 | {5,6,7,8} |

These are **not** full-`D` cycle candidates and are not counterexamples to Radius 5. Their role is narrower and exact: they falsify every attempted family-wide reduction based only on the existence of a lower-radius self-rotation.

Therefore all nine Radius-5 topology families are genuinely irreducible with respect to a purely cyclic/topological invocation of Radius 3 or Radius 4.

## 8. Exact remaining arithmetic obstruction

Under the full-`D` hypothesis, `D|Q(d)`, every cyclic rotation also has numerator divisible by `D`. Hence for an exact distance-5 rotation

`D | (Q(tau^m d)-Q(d))`.

A five-swap transport expresses this numerator difference, modulo the cyclic `2^A == 3^L (mod D)` relation, as a signed five-unit `2,3`-monomial transport sum subject to one of the nine topology patterns and one of the determinant sectors above.

Primitivity makes a nontrivial rotation a different word; for fixed `(A,L)`, the numerator map is injective (successive 2-adic valuations recover the ordered one positions), so the numerator difference is nonzero.

The Radius-5 theorem therefore requires a new arithmetic exclusion of a nonzero full-`D` multiple in these determinant-constrained five-unit transport sums. RL238's Radius-3/4 theorems do not automatically supply that exclusion, and the witnesses in Section 7 prove there is no topology-only shortcut.

This is the exact barrier promoted by RL265.

## 9. Finite replay and red team

The portable verifier independently checks:

- exact RL239 count `181542` for positive-domain `A<=18`;
- all nine topology counts;
- `|kappa|` counts `{1: 50802, 3: 48254, 5: 82486}`;
- the determinant identity and gcd consequence on all 181,542 instances;
- exactly ten full-`D` hits, all the nonprimitive alternating `A=10,L=5,D=781` repetition;
- 4,590 positive-domain distance-5 words in the same range with a nontrivial proper factor `gcd(Q,D)>1` but not full `D`, demonstrating why proper-factor hits must not be conflated with the theorem hypothesis;
- the nine lower-radius-free topology witnesses above;
- the permanent RL247 negative-domain regression exactly.

No empirical percentage is promoted. The finite replay is a reconstruction/audit and falsification aid only.

## 10. Radius-n verdict

The simple induction hypothesis

> exact distance `n+1` forces some lower exact-distance self-rotation to which Radius `<=n` applies

is decisively false already at `n=4 -> 5`, in every Radius-5 topology family.

Therefore RL265 does **not** launch a general Radius-n theorem.

A Radius-n programme remains conceivable only if the determinant/transport arithmetic can be made uniform in `n` (for example, a uniform exclusion for bounded `2,3`-S-unit transport sums). The present topology alone does not provide such an induction.

## 11. Closeout classification and successor

Classification: **RADIUS5_EXACT_BARRIER_FOUND**.

Promoted:
- exact independent reconstruction of the Radius-5 metric and RL239 finite checksum;
- exact nine-family topology proof;
- exact nonzero odd-skew / determinant lemma;
- `gcd(A,L) in {1,3,5}`;
- topology-specific determinant-sector table;
- explicit primitive positive-domain witnesses proving all nine families are lower-radius irreducible;
- a precise statement of the remaining full-`D` arithmetic obstruction;
- falsification of a purely topological Radius-n shell induction.

Not promoted:
- the Radius-5 local theorem;
- any infinite conclusion from the `A<=18` replay;
- any general Radius-n theorem;
- any Gate A/Gate B/global cycle exclusion.

Successor RL266 should attack only the new determinant-sector arithmetic, beginning with `|kappa|=1` because it gives an exact determinant-one relation and occurs only in flat families. It must preserve the RL238/RL239 reduced-denominator/multiple correction and may use exact computation only after an explicit infinite reduction is proved.
