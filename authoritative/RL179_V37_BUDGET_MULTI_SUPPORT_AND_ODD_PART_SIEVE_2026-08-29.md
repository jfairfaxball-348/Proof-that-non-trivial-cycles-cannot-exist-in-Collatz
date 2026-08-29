# RL179 — V37 budget, multi-support, and odd-part sieve

Date: 2026-08-29

## Outcome and classification

RL179 works the authoritative `RL179_V37_NEGATIVE_RETURN_AND_ZERO_HEIGHT_TRANSITION_TARGET.md` in the preferred `h_p=0` branch.  The sole surviving zero-height high-valuation type

`(v,H,J,d)=(37,0,23,-1)`

is **not excluded**.  The session nevertheless produces three exact advances:

1. an all-path signed budget theorem through phase 29 that forces multiple later positive-flow phases;
2. an exact pair-state sharpening of the three phase-29 positive interfaces through phase 30;
3. a general mod-8 odd-part sieve for ten of the fourteen inherited zero-height mismatch indices.

No inherited theorem is corrected or demoted.  No external `m>=2^71` minimum is used.  Surviving necessary states are not promoted as physical existence.

## 1. Frozen inherited state

Use

`A=217976794617`, `L=137528045312`,
`p=65470613321`, `u=103768467013`, `Ap-uL=1`,
`t=L-p=72057431991`.

Let

`b_i=floor(Ai/L)`, `c_i=b_(i+1)-b_i`, `h_i=b_i-S_i`,
`q_i=2^(S_i)/3^i`, `rho_i=2^(b_i)/3^i`, and

`G_i=S_(p+i)-S_p-S_i=h_i-h_(p+i)` for carry-free `i<t`.

The corrected physical flow is

`F2=sum_i q_i(2^G_i-1)=3(lambda-1)g_p`.

RL178 supplies, for the surviving high type,

- `g_p=2^37`;
- `y_(p+24)-2y_24=3^24`;
- `(h_24,h_(p+24))=(0,1)`;
- `a_24=a_(p+24)=1` and `G_25=-1`;
- `G_i<0` for `24<=i<=28` on every physical continuation;
- phase 29 is the earliest necessary positive reversal;
- phase-29 zero return is impossible;
- the positive phase-29 height pairs are `(1,0),(2,0),(2,1)`;
- the exact pair-state second-transition law;
- residue-ordered mechanical weights satisfy `rho_i<1` for every `1<=i<L`.

The common prefix has `G_i=0` through phase 23, so phases before 24 contribute zero to `F2`.

## 2. A rigorous lower bound `F2>1/3` in the high branch

Put

`Delta=A ln 2-L ln 3`, so `lambda=e^Delta`.

The exact verifier bounds `ln 2` and `ln 3` with rational intervals from

`ln x = 2 sum_(n>=0) z^(2n+1)/(2n+1)`, `z=(x-1)/(x+1)`,

using 100 terms and a rational geometric tail bound.  It proves

`Delta > 1/(9*2^37)`.

Since `e^Delta-1>Delta`, the high branch satisfies

`F2=3*2^37*(e^Delta-1) > 3*2^37*Delta > 1/3`.

### Theorem RL179.1 — high-branch positive-flow floor

For `(v,H,J,d)=(37,0,23,-1)`,

`F2>1/3`.

Classification: analytic inequality with exact rational arithmetic certificate.

## 3. Exact signed budget through phase 29

RL178's exact transition law is propagated from

`(h_24,h_(p+24),C_24)=(0,1,3^24)`,

where for negative defect `C=Z-2^e X`.

There are exactly 10 necessary path histories at phase 29.  For a state `(h,hp,C)`, the exact corrected-flow term is

`T_i = q_i(2^G_i-1)
     = (2^(b_i-hp)-2^(b_i-h))/3^i`.

The best (least negative) cumulative value through phase 29 is

`sum_(i=24)^29 T_i = -6734508720128/7625597484987 < -7/8`.

The most negative path gives

`-55387898249216/22876792454961`.

Thus every necessary high path must obtain later net flow

`sum_(i>=30) T_i = F2-sum_(i=24)^29 T_i > 1/3+7/8 = 29/24 > 1`.

For every positive corrected-flow term,

`T_i=rho_i(2^(-h_(p+i))-2^(-h_i))`,

and RL178's residue ordering gives `0<rho_i<1`; hence every individual positive term obeys `0<T_i<1`.

Therefore no single later positive phase can repair the high-branch budget.

Four of the ten phase-29 histories already have cumulative flow below `-5/3`; they end at

- `(0,3,2144699292645)`;
- `(0,3,2144699292643)`;
- `(0,1,536174823161)`;
- `(0,2,1072349646321)`.

For each of these,

`sum_(i>=30) T_i > 1/3+5/3 = 2`,

so at least three later positive phases are mandatory.

### Theorem RL179.2 — multi-support compensation

Every physical continuation of the surviving high type must contain at least **two** positive corrected-flow phases after phase 29.  Four of the ten exact necessary phase-29 histories require at least **three** such later positive phases.

In particular, even any phase-29 positive reversal is only the beginning of the required compensation; it cannot be the sole post-window positive support.

Classification: exact finite certificate plus inherited analytic envelope inequality.

## 4. Exact phase-29 pair-state sharpening

RL178 promoted only the three positive phase-29 height pairs and their flow quanta.  Keeping the normalized integer `C` gives the exact positive interfaces

1. `(h,hp,C)=(1,0,536174823161)`;
2. `(2,0,1072349646323)`;
3. `(2,1,1072349646323)`.

At phase 29, `c_29=2`.  Applying the exact valuation law gives the complete necessary phase-30 images:

### Interface 1

`(1,0,536174823161)` maps exactly to

- `(1,0,402131117371)`, with `G_30=+1`; or
- `(0,1,402131117371)`, with `G_30=-1`.

Thus immediate sign reversal is allowed but zero return is not.

### Interface 2

`(2,0,1072349646323)` maps exactly to

- `(2,1,804262234743)`, with `G_30=+1`; or
- `(2,0,804262234743)`, with `G_30=+2`.

Thus it remains strictly positive at phase 30.

### Interface 3

`(2,1,1072349646323)` maps exactly to

- `(3,2,1608524469485)`, with `G_30=+1`;
- `(3,1,1608524469485)`, with `G_30=+2`; or
- `(3,0,1608524469485)`, with `G_30=+3`.

Thus it also remains strictly positive at phase 30.

### Theorem RL179.3 — no phase-30 zero return

None of the three phase-29 positive pair-state interfaces can return to `G_30=0`.  Only the `(1,0)` interface can reverse sign immediately; the other two remain positive.

Classification: exact finite arithmetic certificate under the RL178 necessary transition law.  Survival is not physical existence.

## 5. Zero-height odd-part sieve

RL177's exact zero-height mismatch indices are

`J in {1,3,5,6,8,10,11,13,15,17,18,20,22,23}`.

For a zero-height mismatch put `k=J+1` and write

`g_p=2^v w`, with `w` odd.

RL178.1 gives at phase `k`:

- for `d=+1`: `2Z-X=3^k w`, heights `(1,0)`;
- for `d=-1`: `Z-2X=3^k w`, heights `(0,1)`.

Suppose the next mechanical digit is `c_k=1`.

For `d=+1`, the next exponents satisfy `alpha in {1,2}`, `beta=1`, and the relevant valuation is

`nu_+=v2(3^(k+1)w+1)`.

The exact valuation comparison gives:

- `nu_+=1`: unique sign-preserving continuation `(alpha,beta)=(1,1)`;
- `nu_+=2`: impossible;
- `nu_+>=3`: unique zero return `(alpha,beta)=(2,1)`.

For `d=-1`, `alpha=1`, `beta in {1,2}`, with

`nu_-=v2(3^(k+1)w-1)`,

and similarly:

- `nu_-=1`: unique sign-preserving continuation `(1,1)`;
- `nu_-=2`: impossible;
- `nu_->=3`: unique zero return `(1,2)`.

The `c_k=1` condition holds exactly at

`J in {1,3,6,8,11,13,15,18,20,23}`.

Because `w` is odd, the forbidden valuation `nu=2` is a single mod-8 class.

If `J+2=k+1` is odd (`J=1,3,11,13,15,23`):

- `d=+1` forbids `w=1 (mod 8)`;
- `d=-1` forbids `w=7 (mod 8)`.

If `J+2` is even (`J=6,8,18,20`):

- `d=+1` forbids `w=3 (mod 8)`;
- `d=-1` forbids `w=5 (mod 8)`.

### Theorem RL179.4 — mod-8 zero-height sieve

At each of the ten `c_(J+1)=1` zero-height mismatch indices, one full odd residue class modulo 8 is impossible for each sign.  The surviving classes split exactly into sign-preserving valuation `1` and zero-return valuation at least `3` cases.

For `J=23`, `v=37` forces `w=1`.  The positive sign lands in the forbidden class and recovers RL178.3; the negative sign has `v2(3^25-1)=1` and recovers the forced RL178.4 continuation.

Classification: analytic local transition theorem with exact congruence certificate.

## 6. What did not close

The high negative type survives the exact necessary interface.  The multi-support theorem forces more global positive support but, by itself, does not yet convert the residue-deficit identity into a contradiction.  Necessary pair-state propagation beyond the first return branches grows quickly and is not promoted as a physical path catalogue.

The four zero-height indices with `c_(J+1)=2`, namely

`J in {5,10,17,22}`,

are not removed by the mod-8 `nu=2` obstruction; their local valuation pattern admits `nu=1`, `nu=2`, and `nu>=3` branches.  They remain a distinct lifting target rather than a failure of the theorem above.

## 7. Scope locks retained

- No resurrection of RL173's `3^(-G)` functional.
- No use of the RL175 sparse ownership resultant as an independent gap obstruction.
- No silent use of `m>=2^71`.
- No physical-existence inference from necessary automaton survival.
- No move to the secondary `h_p>=1` branch.
- Gate A, Gate B, the preferred branch, global non-trivial-cycle exclusion, and Collatz remain open.

## 8. Next target

RL180 should combine the new mandatory multi-support structure with the residue-ordered deficit identity, while using the exact phase-30 pair states to restrict where the required later positive support can occur.  In parallel, lift the odd-part sieve to mod 16 / mod 32 and explicitly treat the four `c_(J+1)=2` zero-height indices without enlarging the old height-only automaton.
