# RL73 — Ownership-forced zero-area macro and low-k localization

Date: 2026-08-24

## 0. Status

RL73 continues from the checksum-clean authoritative RL72 global audit. It does **not** prove Gate A, Gate B, RL closure, nontrivial-cycle exclusion, or the Collatz conjecture.

The new result is an analytic synthesis, conditional only on the already-retained full-phase one-excursion architecture and the stable accepted external nontrivial-cycle state floor `N>=2^71`. It proves that every hypothetical low-`k` Gate-A violation must contain an astronomically large **post-first-mismatch height-one synchronized macro**. This is the first theorem in the RL63–RL72 ownership programme that converts global full phase into a quantitative zero-area-depth localization.

The result is a localization theorem, not a contradiction: height-one synchronized motion is shortcut-Collatz-conjugate, so a new endpoint/ownership theorem is still required to eliminate the forced macro.

---

## 1. Frozen inherited notation

Use RL64/RL65 full-phase extendability. A full-phase one-excursion datum has

- internal length `m=a-k-1`;
- internal words `x,y` of common weight `r`;
- full half-word weight `ell=r+3`;
- `M=2^a-3^ell>0`;
- terminal `J=2^k`;
- full phase quotient `N>0`, `N==3 (mod8)`;
- stable accepted external state floor `N>=2^71`;
- rank defect `mathcalD>=0`;
- area `H=sum_j delta_j`.

RL65 proves the exact quotient identity

`(N-2)M = 237*3^r - 12*mathcalD - 2^(a-k+1)`.     (1.1)

RL72 proves every terminal Gate-A violation has odd `k>=27` and `H>=25`; RL71 supplies the exact nested `delta_*=c162` conclusion inside a hypothetical nested violation with odd `k<=165`.

---

## 2. New full-phase phase squeeze from the exact RL65 quotient

Put

`zeta=2^a/3^ell>1`.

Since `mathcalD>=0` and `2^(a-k+1)>0`, (1.1) gives

`(N-2)M < 237*3^r`.

But `ell=r+3`, so

`M=3^(r+3)(zeta-1)`.

Therefore

`boxed: zeta-1 < 79/[9(N-2)] <= 79/[9(2^71-2)].`     (2.1)

Classification: **analytic theorem** under full-phase extendability plus the retained stable `2^71` external floor.

This slightly strengthens the older RL49 bound used in the safe phase-resonance certificate.

---

## 3. Safe reduced-denominator floor and global exponent-skew floor

Let

`beta=log_2(3)`.

If `a/ell=p/q` in lowest terms, then

`0 < p log 2 - q log 3 < 79/[9(2^71-2)]`.

The exact RL49 continued-fraction method, rerun in the lightweight RL73 verifier with the stronger bound (2.1), gives the Legendre gate

`q <= 93,226,756,704,262,400,759`

and exactly one surviving above-`beta` convergent below that gate:

`p0 = 123,139,092,617,126,647,266`,

`q0 =  77,692,117,359,936,589,403`.

The next above-`beta` convergent denominator is

`205,632,218,873,398,596,256`,

well above the gate. Hence every retained full-phase datum satisfies

`boxed: ell >= q0 = 77,692,117,359,936,589,403.`     (3.1)

This is a global denominator floor: if the reduced denominator is below the Legendre gate it must be `q0`; otherwise it is larger than the gate.

Now define the integer exponent skew

`Delta=2a-3ell`.

Because `a/ell>beta`,

`Delta > (2beta-3)ell`.

The exact rational log interval in the verifier proves

`(2beta-3)q0 > Delta0-1`,

where

`Delta0 = 2p0-3q0 = 13,201,833,154,443,526,323`.

Since `Delta` is an integer and `ell>=q0`,

`boxed: Delta >= Delta0 = 13,201,833,154,443,526,323.`     (3.2)

Classification: **analytic + exact arithmetic/continued-fraction certificate**, using the stable `2^71` external floor.

Important correction to the exploratory RL73 scratch work: (3.2) is not justified merely by naming the RL50 stress convergent. Its uniformity comes from the reduced-denominator dichotomy plus `a/ell>log_2(3)`. The bundled verifier checks this exact logical chain.

---

## 4. Internal column count identity

Let the internal pair-column counts be

- `c00` for `00`;
- `c11` for `11`;
- `e` for `01`;
- `e` for `10`.

The equality of the internal x/y weights forces the two mismatch counts to agree. Thus

`m=c00+c11+2e`,

`r=c11+e`.

Using `a=m+k+1` and `ell=r+3`,

`boxed: Delta-2k+7 = 2c00-c11+e.`                    (4.1)

Every `10` occurs with pre-height at least two and contributes at least one unit to the area, so

`boxed: 1<=e<=H`

in every terminal path containing a mismatch.

Classification: **analytic identity/corollary**.

---

## 5. Canonical synchronized grammar before the first mismatch

Before the first mismatch the path stays at height one and is synchronized. Starting from canonical `J=-13`, the unique synchronized choice that keeps `J` odd cycles

`-13 --11--> -19 --00--> -9 --11--> -13`.

The alternative synchronized choice exits to the first even height-one state. Therefore the entire synchronized prefix immediately before the first mismatch is exactly one of

`(101)^q 0`,

`(101)^q 11`,

`(101)^q 100`,

where `1` denotes `11` and `0` denotes `00`. The corresponding first-mismatch entry states are respectively

`-6, -28, -4`.

For the skew contribution `P=2c00_pre-c11_pre`, every complete `101` cycle contributes zero, while the three exits give

`boxed: P in {2,-2,3}.`                               (5.1)

Classification: **analytic canonical-start theorem**, already implicit in RL67 but used here in a new counting splice.

---

## 6. Forced post-first-mismatch `00` mass

Let `c00+` and `c11+` count synchronized columns strictly after the synchronized prefix and hence from the first mismatch onward. All mismatches occur in this post-prefix part. Splitting (4.1) at the prefix gives

`Delta-2k+7 = P + 2c00+ - c11+ + e`.

Since `c11+>=0`,

`boxed: c00+ >= ceil[(Delta-2k+7-P-e)/2].`             (6.1)

Now suppose there is a hypothetical Gate-A violation in the first open low-`k` laboratory

`27<=k<=165`, `k` odd, `25<=H<k`.

Use

`Delta>=Delta0`, `P<=3`, `e<=H<=k-1`.

The right side of (6.1) is minimized at

`k=165`, `H=e=164`, `P=3`, `Delta=Delta0`,

giving

`boxed: c00+ >= 6,600,916,577,221,762,917.`          (6.2)

Thus a hypothetical low-`k` violation contains more than `6.6e18` post-first-mismatch `00` columns.

Classification: **analytic corollary** of Sections 2–5 and the RL72 low-`k` proof state.

---

## 7. Forced giant height-one zero-area macro

Every internal column with pre-height `d>1` contributes at least one to

`H=sum(d-1)`.

Therefore at most `H` of the `c00+` columns can lie above height one. Consequently the number of post-first-mismatch **height-one aligned `00` columns** is at least

`c00+ - H`.

After the first mismatch, each return to height one occurs at a `10`. There are exactly `e` such returns. Hence the post-first-mismatch height-one synchronized motion is partitioned into at most `e` maximal synchronized blocks.

By pigeonhole, one such block contains at least

`ceil[(c00+ - H)/e]`

aligned `00` columns. Minimizing over the entire hypothetical violation window gives

`boxed:`

`some post-first-mismatch height-one synchronized block contains`

`at least 40,249,491,324,522,944 aligned 00 columns.`   (7.1)

The minimum occurs at `k=165`, `H=e=164`; because of the final ceiling division the same block lower bound is attained for all three canonical prefix-skew values `P in {-2,2,3}`. The smallest intermediate `c00+` bound is attained for `P=2` or `P=3`.

Classification: **new RL73 analytic localization theorem + exact finite parameter audit**.

The word “block” here means a maximal height-one synchronized block. The theorem counts at least `40,249,491,324,522,944` `00` columns inside that block; it does **not** claim those `00` columns are consecutive, because `11` columns may interleave.

---

## 8. Relation to the RL71 nested exact-value window

RL71 proves that in any hypothetical nested `g=0` violation with odd `k<=165`,

`delta_*=c162` exactly.

RL73 therefore gives the simultaneous necessary conditions for every nested hypothetical violation with `27<=k<=165`:

1. the last active displacement is exactly the RL71 selected representative `c162`; and
2. somewhere after the first mismatch there is a height-one synchronized block containing at least `40,249,491,324,522,944` aligned `00` columns.

The finite-window/mod-243 selector cannot by itself see this depth: RL72 already showed the all-`00` terminal local state is periodic in the zero-depth modulo 162. RL73 strengthens the diagnosis from “depth may be unbounded” to “a hypothetical violation is forced to exhibit astronomical zero-area depth.”

---

## 9. Why this is not Gate-A closure

RL50 proved that height-one synchronized dynamics are shortcut-Collatz-conjugate. Aligned `00/11` motion costs zero area and zero RL50 defect energy. Therefore the existence of the forced macro is not itself contradictory.

A proof cannot simply say “the block is too long.” It must use information absent from unrestricted height-one dynamics, for example:

- the exact full-phase denominator/quotient;
- a macro endpoint restriction involving `J`, `g`, `W`, or RL50's height-one return coordinate `L`;
- an ownership-sensitive restriction on the entry/exit residue or normalized weight of the giant block;
- a global packing/weighted-difference invariant that remains non-coboundary after synchronized telescoping.

This is precisely the ownership-sensitive zero-area-depth interface identified by RL72.

---

## 10. Failed/rejected stronger interpretations

### F1. “The RL50 stress pair alone gives the uniform skew floor.”

Rejected as an incomplete justification. The uniform theorem needs the reduced-denominator dichotomy plus the log-ratio inequality. RL73 supplies that chain and verifies it exactly.

### F2. “The forced `00` columns are consecutive.”

Not proved. The theorem gives their number inside one maximal synchronized height-one block; `11` columns may interleave.

### F3. “A huge synchronized block contradicts full phase.”

Not yet. This would amount to solving the ownership-sensitive macro problem that remains open.

### F4. “Further q-digits will bound this macro.”

Not supported. RL71's finite-window theorem and RL72's mod-243 periodicity barrier say local fixed-precision digits do not control arbitrary zero-area depth.

---

## 11. Updated live target

The highest-leverage next theorem is now more concrete:

> **Giant owned height-one macro theorem.** Under full-phase extendability, prove that a post-first-mismatch maximal height-one synchronized block cannot contain `>=40,249,491,324,522,944` aligned `00` columns when the surrounding terminal exponent satisfies `k<=165`; or prove an endpoint inequality strong enough to charge such a block to area/active-rank weight.

The preferred coordinates for this attack are RL50's exact height-one normalized quantities (`g`, `J`, `L`, `W`) together with the RL64 full-phase completion condition. Pure local residue lifting is a secondary tool only.

A successful theorem at this threshold would close the entire low-`k` Gate-A band `27<=k<=165`, because RL72 already closes `k<=25` and RL66 eliminates even `k`. It would still leave odd `k>=167` unless the macro theorem is uniform in `k`.
