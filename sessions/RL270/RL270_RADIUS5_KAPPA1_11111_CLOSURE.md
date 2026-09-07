# RL270 — Radius-5 determinant-one `[1,1,1,1,1]` closure

Date: 2026-09-07  
Classification: **RADIUS5_KAPPA1_11111_CLOSED**

## 1. Scope

RL270 works only the inherited positive-domain Radius-5 determinant-one sector `|kappa|=1`, and only the final flat topology `[1,1,1,1,1]`.

Inherited unchanged from RL269:
- `D=2^A-3^L>1`;
- `qA-mL=1` after orienting to `kappa=+1`;
- the exact zero-flow-cut five-edge identity and full-`D` divisibility test;
- the exact finite determinant cover of **2,234 pairs**, maximum `A=690`;
- no primitivity filter is required for the finite certificate;
- no proper divisor of `D` may replace the complete positive `D`.

Previously closed determinant-one topologies are `[3,2]`, `[3,1,1]`, `[2,2,1]`, and `[2,1,1,1]`.

## 2. Exact singleton reconstruction

Orient to `kappa=+1`. Let `g` have five isolated nonzero entries, three `+1` and two `-1`. Put

`X_t = x_(tm mod A)`,  `H_t = g_(tm mod A)`.

Since `qA-mL=1`,

`(t+L)m = tm-1 (mod A)`.

The reconstruction equation `x_i-x_(i+m)=g_i-g_(i-1)` becomes

`X_t-X_(t+1)=H_t-H_(t+L)`.

Define the cyclic signed length-`L` window

`F_t = sum_{j=0}^{L-1} H_(t+j)`.

Then `F_t-F_(t+1)=H_t-H_(t+L)`, so `X_t-F_t` is constant. Summing over one period gives

`sum X_t=L`,
`sum F_t=L*sum H_t=L`,

hence the constant is zero:

> `X_t = F_t` for every `t`.

Thus the binary word is uniquely reconstructed from the five signed singleton positions. Structural realizability is equivalent to every cyclic length-`L` signed window having value `0` or `1`.

## 3. Ten alternating boundary events

Let

`delta_t=H_t-H_(t+L)`.

Because the five physical nonzero flow entries are singleton components, a singleton and its physical predecessor cannot both be nonzero. Under `(t+L)m=tm-1`, each singleton therefore contributes two distinct boundary events. Hence `delta` has exactly ten nonzero entries, each `+1` or `-1`.

Since `F_t-F_(t+1)=delta_t` and `F` is binary, those ten signs must alternate cyclically. Conversely, if the ten signs alternate, `F` takes two adjacent integer levels; its average is `L/A` with `0<L/A<1`, so those levels are exactly `0` and `1`.

Therefore:

> `[1,1,1,1,1]` is structurally realizable iff its ten boundary-event signs alternate cyclically.

Each singleton pairs two opposite boundary events separated by exactly `L` in `m`-cycle coordinates.

## 4. Four complete cyclic matching families

Translation by `L` preserves cyclic order. After anchoring a positive singleton at event `0` and quotienting only by the five allowed even cyclic rotations, the order-preserving `L`-pairing equations have exactly four positive-gap solution families.

Writing the ten positive boundary gaps as `r0,...,r9` and using positive free parameters `a,b,c,d`:

### Antipodal-5
Singleton event set `(0,1,2,3,4)`:

`r = [L-a-b-c-d, a, b, c, A-2L+d, L-a-b-c-d, a, b, c, d]`.

### Long 5/7
Singleton event set `(0,1,2,5,6)`:

`r = [2L-A-a-c-d, A-L+a-b, A-2L+b+c+d, 2L-A-a-c-d, a, c, A-L-b-c, b, c, d]`.

### Short 3/5
Singleton event set `(0,1,2,6,7)`:

`r = [L-c-d, c, A-2L-a-b-c, a, b+c+d, L-a-b-c-d, a, b, c, d]`.

### Interlaced-5
Singleton event set `(0,1,4,7,8)`:

`r = [L-a-b-c-d, A-2L+a, b, -A+2L+c, A-2L+d, L-a-b-c-d, a, b, c, d]`.

The verifier imposes strict positivity of every displayed gap. No fifth cyclic matching family is feasible.

Across the inherited 2,234 determinant pairs these four families contain exactly:

- antipodal-5: **7,097,775,603**;
- long 5/7: **3,117,265,503**;
- short 3/5: **6,563,699**;
- interlaced-5: **538,629,405**;
- total: **10,760,234,210** structural states.

The inherited raw two-necklace five-gap count was **618,391,058,390**, so this is an exact structural compression rather than a sample.

## 5. Sparse full-D residue formula

Choose the anchored positive singleton at physical index zero and let `P_t=sum_{u<t}H_u`. For `i_t=tm mod A`, the exact physical one-prefix count is

`R_(i_t)=1+tq-L*floor(tm/A)-P_t`.

Set the unit

`z = 2^m * 3^(-q) (mod D)`.

Because `qA-mL=1` and `2^A=3^L (mod D)`, one has

`z^L=2^(-1)` and `z^A=3^(-1)` modulo `D`.

After removing a common invertible power of `3`, the exact five-edge numerator is the sparse sum

`P(z)=sum c_s z^(b_s)`,

where `b_s` is the `m`-cycle location of a singleton event and, scanning singleton events in cyclic order with prefix sum `P`,

- a `+1` singleton contributes coefficient `3^(P+1)`;
- a `-1` singleton contributes coefficient `-3^P`.

Thus full-`D` divisibility is exactly a five-term modular equation; no word of length `A` has to be reconstructed in the certificate.

For the four parameterizations, multiplication by an invertible monomial gives the following equivalent zero tests used by the verifier:

- antipodal:
  `2 z^(a+b+c+d)-1+z^a-z^(a+b)+z^(a+b+c)=0`;
- long:
  `4 z^(a+b+c+d)-3z^b+2z^a-2z^(a+b)+2z^(a+b+c)=0`;
- short:
  `2 z^(a+b+c+d)-z^(a+b)+z^(a+b+c)+2-2z^a=0`;
- interlaced:
  `6 z^(a+b+d)-3-2z^a+5z^(a+b)=0`.

All congruences are modulo the complete positive `D`.

## 6. Complete meet-in-the-middle certificate

Each sparse equation separates into at most two free variables on each side. The complete verifier builds exact residue tables subject to the family positivity constraints.

Across all 2,234 determinant pairs it generates:

- antipodal: `4,489,399 + 4,489,399` side residues;
- long: `2,798,156 + 1,107,046`;
- short: `72,715 + 150,525`;
- interlaced: `53,541 + 1,378,850`.

Total residue entries examined: **14,539,631**.

There are **zero valid left/right residue matches** in every family. Therefore:

> full-`D` hits over all **10,760,234,210** structural states = **0**.

## 7. Orientation and independent red team

The independent direct-word replay through `A<=18` gives exactly:

- 8,996 positive-domain `[1,1,1,1,1]`, `|kappa|=1` instances;
- 4,498 with `kappa=+1`, 4,498 with `kappa=-1`;
- positive orientation family split `3522 / 718 / 204 / 54` for antipodal/interlaced/short/long;
- the identical split after exact source/target reversal for `kappa=-1`;
- zero full-`D` hits;
- 714 proper-factor-only instances;
- zero determinant mismatches;
- zero source/target-orientation mismatches;
- zero sparse-polynomial versus direct numerator mismatches.

For `kappa=-1`, if `y=rotate(x,m)` and `m'=A-m`, then source/target reversal gives determinant `+1` with the numerator difference negated, so the positive-orientation certificate covers both signs exactly.

The permanent negative-domain sentinel `A=11,L=7,D=-139,Q=18904` remains outside the promoted `D>1` scope. Primitivity is not used as a filter.

## 8. Promoted result

> In the inherited positive-domain primitive/full-`D` Radius-5 setting, no exact-distance-5 self-rotation with `|kappa|=1` and topology `[1,1,1,1,1]` exists.

Classification: **RADIUS5_KAPPA1_11111_CLOSED**.

Together with RL266-RL268, this closes the complete Radius-5 determinant-one `|kappa|=1` sector.

Radius 5 itself is **not** yet proved. The inherited `|kappa|=3` and `|kappa|=5` sectors remain open. Gate A, Gate B, the fifth selector, selector enumeration, the general Radius-n programme and global non-trivial-cycle exclusion remain open/frozen as previously recorded.
