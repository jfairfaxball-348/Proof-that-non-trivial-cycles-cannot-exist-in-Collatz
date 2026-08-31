# RL203 proof — dyadic prefix information boundary

## 1. Exact normalization

Use the inherited RL201 endpoint identity at an H21 tau34 source phase a:
`3(alpha-1)rho_a(2^33 eta-1/2)
 =3K_0-alpha P_p+(alpha-1)P_a`,
where `alpha=3^p/2^u`, `K_0=2^37`, and `rho_a=2^b_a/3^a`.

Put `d=3^p-2^u`. Multiplying by `2^u` and defining
`E_a=3*2^u*K_0-3^p P_p+d P_a` gives
`E_a=3d rho_a(2^33 eta-1/2)
    =d*2^(b_a-1)*3^(1-a)*(2^34 eta-1)`.

The H21 source has height one, so `S_a=b_a-1`. Hence the normalized 2-adic unit
`U_a=E_a/2^S_a` is exactly
`U_a=d*3^(1-a)*(2^34 eta-1)`.
All denominators here are odd and therefore units in `Z_2`.

It follows immediately that for `m<=34`,
`U_a = -d*3^(1-a) (mod 2^m)`.
Modulo `2^35`, after multiplication by the inverse odd factor,
`U_a/[d*3^(1-a)] = -1+2^34(eta mod2)`.
Thus the first eta-sensitive dyadic bit is parity and nothing earlier.

## 2. The forced H21 tail contains exactly the same bit

For the lower tau34 endpoint let `A_t` be the cumulative chronological
acceleration exponent from the source to offset t. The inherited H21 tail gives
`A_t=t` for `0<=t<=33`.

Modulo `2^35`,
`sum_(t=0)^33 2^t/3^t
 =3-2^34/3^33
 =3-2^34`,
because the inverse of every odd number is odd.

If eta is even, the lower endpoint is the H21 terminal endpoint and its final
exponent is one, so the t=34 term contributes `2^34/3^34`, equal to `2^34`
modulo `2^35`; the total is `3`.
If eta is odd, the lower final exponent is at least two and the t=34 term has
2-adic valuation at least 35; the total remains `3-2^34`.

These are exactly the two residues of `3(1-2^34 eta) mod 2^35`. Therefore this
truncation is an algebraic restatement of the already inherited terminal
orientation law. It supplies no independent sign selector.

## 3. Hensel precision is 56 bits

The inherited terminal condition excludes one eta residue in each mod-9 state
class modulo `2^22`. To know eta modulo `2^22` from `2^34 eta-1`, the normalized
unit must be known modulo `2^(34+22)=2^56`, because the remaining coefficient is
odd and invertible in `Z_2`.

This observation does not say a 56-bit consumer succeeds. It fixes the first
precision at which the existing Hensel exclusion can consume a newly determined
dyadic eta residue.

## 4. Below-p necessary sources are separated from the root term

Write `a=p-e`, `e>=1`. The positive H21 tail occupies phases a through a+33.
For `e<=33` it hits the inherited zero anchor at p, so such a source is
impossible.

For e=34..38, use `r_a=aB mod L` and `pB=1 mod L`. The exact ranks are:
- e=34: 15303429871
- e=35: 72382725878
- e=36: 129462021885
- e=37: 49013272580
- e=38: 106092568587

Every one lies outside the inherited core
`[25583192106,41775866136]`.
At e=39 the rank is `25643819282`, inside the core. Hence every surviving
necessary source with `a<p` satisfies `p-a>=39`.

The Bezout identity `Ap-uL=1` gives
`b_(p-e)=u-ceil((Ae-1)/L)`.
At e=39,
`61L < 39A-1 <= 62L`, so the ceiling is 62. Since `h_a=1`,
`u-S_a=u-(b_a-1)=63`, and this depth only increases with e.

For a<p, the endpoint moment can be written exactly as
`E_a=3*2^(u+37)-2^u P_a-3^p sum_(j=a)^(p-1)q_j`.
For a physical word, `q_0=1` and every `q_j` for `j>=1` is even in `Z_2`
because `S_j=sum_(k<j)a_k>=1`. Thus `P_a` is an odd 2-adic unit. After division
by `2^S_a`, the `2^u P_a` term therefore begins exactly at depth `u-S_a>=63`;
the first root-normalization term begins at depth at least 100. Both vanish
modulo `2^56`.

Therefore, for every below-p necessary source, the complete truncation at the
existing Hensel-resolution scale is insensitive to those root terms. Any new
exclusion at that scale must come from the remaining post-source/completion tail
or from a different independently global consumer.

## 5. Scope

This is a one-sided information-boundary theorem. It does not analyze `a>p`,
does not prove the complete exact height-word route insufficient, and removes no
rank or eta class. All inherited physical-incidence, ownership, branch, Gate and
global obligations remain open.
