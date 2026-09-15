# RL325 proof ledger — global ownership telescope, carry contraction, and two-ended zero budget

Date: 2026-09-15
Status: FROZEN CANDIDATE FOR RL325 CLOSEOUT
Incoming BASE_HEAD: `e12cbd171fd9b4920c32ba10f1066faea77ad1b1`
Successor: RL326

## Scope retained

Work remains in the ordered genuine `g=2` late-row branch inherited from RL315–RL324.

At the conditional first external survivor,

`(a,ell)=(217976794617,137528045312)`,

put

`X=2^a`, `Y=3^ell`, `D0=X-Y`, `H=X+Y`,
`d=a-ell=80448749305`, `lambda=X/Y`.

The inherited external least-state window remains conditional:

`2^71 <= m < 2^75`.

Internal-only frontier: `ell>=190537`.
External-certificate-conditional frontier: `ell>=49547666544`.

Gate A remains OPEN. Gate B remains OPEN. Global positive non-trivial-cycle exclusion remains OPEN. `g=1` remains separate.

The live canonical regime inherited from RL324 is

`Z0>0`, `K<0`, `c0=-n<=-1`, `M=m-n<m`, `1<=n<2^35`,

and the canonical least-root matched rank `k` lies after the unique RL324 crossing transition `j -> j+1`.

RL324's exact local counterfamily remains binding: no theorem below is a rank-by-rank displacement propagation claim.

## RL325.1 — exact global full-ownership telescope

For genuine consecutive matched ranks write

`d_i=u_i-v_i`,
`a_i=u_(i+1)-u_i`,
`b_i=v_(i+1)-v_i`,
`p_i=a-d_i`,
`Delta_i=2^(d_i)P_i-Q_i`.

Let `A_i,C_i` be the genuine complementary `ell`-odd ordinary numerators. The complementary prefix recurrences are

`2^(a_i) A_(i+1) = 3 A_i + 2^(p_i) - Y`,

`2^(b_i) C_(i+1) = 3 C_i + 2^(a+d_i) - Y`.

Define

`S_i=(2^(u_i)A_i+2^(v_i)C_i)/3^i`,

`T_i=(2^(v_i)C_i-2^(u_i)A_i)/3^i`.

Then exact subtraction gives

`S_(i+1)-S_i = D0(2^(u_i)+2^(v_i))/3^(i+1)`,

`T_(i+1)-T_i = H(2^(u_i)-2^(v_i))/3^(i+1)`.

The frozen proper-factor identity `2^(d_i)A_i-C_i=-H Delta_i` gives pointwise

`T_i = H 2^(v_i) Delta_i / 3^i`.

With normalized defect

`e_i=Delta_i/2^(d_i)`,

one obtains for every genuine **linear** matched-rank interval `l..k`

`2^(u_k)e_k/3^k - 2^(u_l)e_l/3^l`
` = sum_(i=l)^(k-1) (2^(u_i)-2^(v_i))/3^(i+1)`.

Equivalently the exact normalized recurrence is

`2^(a_i)e_(i+1)=3e_i+1-2^(-d_i)`.

Unrolling gives

`e_k = [3^(k-l)/2^(u_k-u_l)] e_l`
`    + sum_(i=l)^(k-1) [3^(k-i-1)/2^(u_k-u_i)](1-2^(-d_i))`.

At the live starting rank `l=j+1`, RL324's small positive defect gives `e_l<1/2`.
At the canonical rank in the `K<0` branch,

`e_k=n-eta/2^r`, hence `n-1<e_k<n`.

A coarse consequence is that if `K_+` denotes the number of strict matched ranks in the interval, then

`K_+ >= 3n-4`.

Classification: **proved analytic genuine-ownership telescope, support-uniform on linear matched intervals**.

## RL325.2 — least-root mechanical / Beatty contraction

For `i<k` set

`t=k-i`, `U_i=u_k-u_i`.

The complementary segment from the least-root canonical phase back around the full `2a` word to `P_i` has length `2a-U_i` and odd count `2ell-t`. The frozen RL319 least-root mechanical defect therefore gives

`ell U_i - a t >= 0`.

Since `gcd(a,ell)=1` and `1<=t<ell`,

`U_i >= ceil(a t/ell)`.

Thus the telescope coefficient

`rho_i=3^t/2^(U_i)`

satisfies

`rho_i <= 3^t/2^(ceil(a t/ell))`.

Writing `r_t = a t mod ell`, the exact identity is

`3^t/2^(ceil(a t/ell))`
` = exp(-t(a log 2-ell log 3)/ell) 2^(r_t/ell-1)`
` < 2^(r_t/ell-1)`.

Because `gcd(a,ell)=1`, the residues `r_t` permute `1,...,ell-1`. Therefore every initial interval obeys

`sum rho_i < ell/(2 log 2) - 1/2`.

With `e_(j+1)<1/2`,

`e_k < 1/3 + ell/(6 log 2)`,

and hence

`n < 4/3 + ell/(6 log 2)`.

The exact 280-term rational `2 atanh(1/3)` lower enclosure for `log 2` certifies the initial integer cap

`n <= 33068504827`.

Classification: **proved analytic contraction plus exact finite rational constant certificate**.

## RL325.3 — exact full-row gap partition and canonical tail ownership

The full fixed-weight numerator gap is

`Q(u)-Q(v)=H G`.

Splitting its rank sum at the canonical rank and using the normalized telescope gives, with

`sigma_k=2^(u_k)/3^k`,

`(1/Y) sum_(i<k) 3^(ell-1-i)(2^(u_i)-2^(v_i))`
` = G + sigma_k e_k`,

and

`(1/Y) sum_(i>=k) 3^(ell-1-i)(2^(u_i)-2^(v_i))`
` = lambda G - sigma_k e_k`.

The canonical tail has weight `s>=1`. Its first `s` matched ranks are strict, so

`lambda G - sigma_k e_k`
` >= (sigma_k/2)(1-(2/3)^s)`.

The genuine prefix from the row boundary to the least state gives `sigma_k>R/m>=1`. Consequently

`e_k + (1/2)(1-(2/3)^s) <= lambda G/sigma_k`,

and therefore

`n - 5/6 < lambda G`.

This is the valid live-branch carry-to-physical-gap inequality.

**Scope warning.** No absolute bound `G<2^35` is available in this live late-row-root branch. The RL319 `G<2^35` theorem is root-aligned only. The scratch-only attempted corollary `n<=G<2^35` is explicitly rejected in the correction ledger.

Classification: **proved analytic global ownership partition and tail inequality**.

## RL325.4 — crossing-prefix physical gap bound

At the RL323/RL324 first crossing rank `j`, let

`z=u_j-j`.

Thus `z` is the number of zero phases in the late-row prefix before the crossing. The first-difference / ordered-prefix crossing calculation gives the strict physical-gap bound

`G < 2^z`.

This is a prefix-length-dependent statement, not the invalid absolute root-aligned cap.

Combining with RL325.3 yields

`n < 5/6 + lambda 2^z`.

Classification: **proved analytic crossing-prefix bound in the live ordered branch**.

## RL325.5 — two-ended zero-budget theorem

Let

`h=ell-k`,
`rho=j+h=j+ell-k`,
`L=a-u_k`.

The physical suffix from the canonical least state `m=P_k` to the late-row boundary has `h` one-bits and therefore `L-h` zero-bits. The prefix before the crossing has `z=u_j-j` zero-bits.

Apply the least-root mechanical inequality between matched ranks `j` and `k`:

`u_k-u_j >= ceil(a(k-j)/ell)`.

Since `k-j=ell-rho` and

`u_k-u_j=(a-L)-(j+z)`,

this rearranges exactly to

`(L-h)+z <= floor(d rho/ell)`.

Hence

`z <= floor(d rho/ell)`

and, because `v_j>=j`,

`d_j=u_j-v_j <= z <= floor(d rho/ell)`.

Together with RL325.3–RL325.4,

`n < 5/6 + lambda 2^(floor(d rho/ell))`.

This theorem is genuinely global: it consumes the least-root mechanical word between the crossing and canonical rank and is absent from the RL324 local counterfamily.

Classification: **proved analytic global two-ended zero-budget theorem**.

## RL325.6 — exact omitted-Beatty mass

Retaining the omitted tail of the Beatty sum gives the sharper exact inequality

`n < B_* - [1/(3 lambda)] sum_(r=1)^rho 2^(floor(a r/ell))/3^r`,

where

`B_* = 4/3 + ell/(6 log 2)`.

For certification use the exact rational lower enclosure

`L_280 = 2 sum_(q=0)^279 (1/3)^(2q+1)/(2q+1) < log 2`

and the frozen exact first-survivor bound

`lambda < 1+2^-40`.

The portable verifier uses

`B_upper = 4/3 + ell/(6 L_280)`

and replaces `1/lambda` by the smaller exact `1/(1+2^-40)`, producing a rigorous upper bound on the right side.

Classification: **proved analytic identity/inequality plus exact rational certification mechanism**.

## RL325.7 — self-consistent carry contraction

The two independent `rho` inequalities now meet.

The exact floors are

`floor(59d/ell)=34`,
`floor(60d/ell)=35`,
`floor(61d/ell)=35`,
`floor(62d/ell)=36`,
`floor(63d/ell)=36`.

For `rho<=59`, RL325.5 gives a carry upper bound below `33068504812` (in fact below `17179869185`).

At `rho=60`, the exact omitted-Beatty certificate gives a strict upper bound below `33068504813`.

Therefore an integer `n>=33068504813` would have to satisfy both `rho>=60` and `n<33068504813`, impossible. Hence

`n <= 33068504812`.

For the maximal surviving carry

`n=33068504812`,

`rho<=59` is impossible by RL325.5, while the exact omitted-Beatty certificate at `rho=63` gives

`n < 33068504812`.

Monotonicity of the omitted positive sum therefore excludes every `rho>=63`, leaving

`rho in {60,61,62}`.

Classification: **exact integer contraction from two proved analytic inequalities plus exact rational finite certificate**.

## RL325.8 — finite physical endgame at maximal carry

For `n=33068504812`, the inequality

`n < 5/6 + lambda 2^z`,

with frozen `lambda<1+2^-40`, forces `z>=35`.

If `rho=60` or `61`, RL325.5 and the exact floor `35` give

`(L-h)+z<=35`.

Thus

`z=35`, `L=h`, `d_j<=35`.

The canonical-to-boundary suffix contains no zero phases: it is exactly `1^h`.

If `rho=62`, the zero budget is `36`, so

`L-h<=1`, `d_j<=36`.

Thus the canonical-to-boundary suffix contains at most one zero phase.

Since `j>=1`, one has `h<=rho-1`, so in all maximal-carry cases

`L<=62`.

Therefore

`n=33068504812`

forces the finite physical endgame

- `rho in {60,61,62}`;
- `d_j<=36`;
- `L<=62`;
- the canonical-to-boundary suffix has at most one zero.

For `rho=60,61`, the suffix is all ones and therefore

`x+1=(3/2)^h(m+1)`, `2^h | (m+1)`.

This is a finite-support collapse only for the maximal surviving carry; it is not a closure of all remaining `n`.

Classification: **proved analytic finite-endgame contraction plus exact certified integer thresholds**.

## RL325.9 — binding barriers and non-results

1. RL324.6 remains binding: local matched-defect recurrence, positivity, unit-minus-one geometry, and least-state lower bounds do not propagate displacement bounds.
2. The exact telescope is linear; no cyclic-wrap theorem is claimed.
3. `G<2^35` is not available in the live late-row-root branch.
4. `n<=G` is not promoted.
5. The `rho in {60,61,62}`, `L<=62`, at-most-one-zero conclusion applies only to the maximal remaining carry `n=33068504812`.
6. R1 remains OPEN: the three maximal-carry endgames have not been eliminated, and lower carries remain to be consumed.

## Final scope

R1 — Parent Bridge remains OPEN.

Gate A remains OPEN.
Gate B remains OPEN.
R2 — g=2 Closure has not started as a closed-stage claim.
Global positive non-trivial-cycle exclusion remains OPEN.
`g=1` remains separate.

`PARENT_DIFFICULTY_DELTA = EASIER`.
