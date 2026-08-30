# RL185 — signed defect drift and phase-weighted corridor capacity

Date: 2026-08-30

## 0. Outcome and classification

RL185 continues the sole surviving zero-height high type

`(v,H,J,d)=(37,0,23,-1)`.

It does **not** exclude that type, close the preferred `h_p=0` branch, close Gate A or Gate B, exclude all non-trivial cycles, or prove Collatz.

RL184 proved that at least `10,075,174,499` clean 40-edge physical successor corridors exist and that every such corridor contains a nonzero corrected p-shift defect. RL185 converts that incidence theorem into a genuinely signed and phase-weighted global restriction.

The main new point is that the forced defect cannot be treated as an arbitrarily cheap late event. Height growth inside a clean corridor is controlled by the exact mechanical word: height can rise only on a `c=2` step. Through offset 39 there are at most 23 such steps, so every defect used to discharge an RL184 corridor has p-endpoint heights at most 24. More strongly, a defect at high endpoint height can serve fewer possible corridor starts. This height-versus-coverage trade gives a universal `2^26` charging constant.

Promoted results:

1. **RL185.1 — mechanical height localization of forced defects** (analytic + exact integer certificate). In a clean RL184 corridor starting from a p-edge with both endpoint heights at most one, the p-edge at chronological offset `j`, `0<=j<=39`, has both endpoint heights at most
   `1+ceil(j(A-L)/L)`.
   In particular every defect selected to discharge such a corridor has endpoint maximum `H<=24`.

2. **RL185.2 — height-dependent corridor multiplicity** (analytic + exact integer certificate). If a selected nonzero ordinary defect has endpoint maximum `H`, then it can serve at most `m_H` clean corridor starts, where for `H=1,...,24`
   `m_H = 40,39,38,36,34,33,31,29,28,26,24,22,21,19,17,16,14,12,10,9,7,5,4,2`.
   These exact caps satisfy
   `m_H <= 2^(25-H)`.

3. **RL185.3 — phase-weighted absolute-flow capacity** (analytic + exact integer certificate). Put
   `f_i=q_i(2^G_i-1)`.
   On an ordinary p-edge with unequal endpoint heights `(a,b)` and `H=max(a,b)`,
   `|f_i|=rho_i |2^-b-2^-a| > 2^-(H+1)`,
   using the inherited `rho_i>1/2`.
   Choosing one forced defect for each of the `10,075,174,499` clean corridors and charging corridor starts to their selected physical defects gives
   `sum_(ordinary i) |f_i| > 10,075,174,499 / 2^26 > 150`.
   Therefore the total absolute `K`-variation over ordinary phases satisfies
   `sum_(ordinary i) |K_(i+1)-K_i| > 50`.

4. **RL185.4 — two-sided signed corrected-flow mass** (analytic + rational interval certificate). The carry term is positive and exceeds `1/2`. The inherited exact total is
   `sum_i f_i = F2 = 3(lambda-1)2^37`,
   and the verifier certifies
   `0<F2<1/2`.
   Since the ordinary absolute-flow variation exceeds 150, the full absolute-flow variation exceeds `150+1/2`. Writing
   `P=sum_i max(f_i,0)` and `N=sum_i max(-f_i,0)`,
   one has `P+N>150.5` and `P-N=F2 in (0,0.5)`. Hence
   `P>75` and `N>75`.
   Equivalently the total positive and negative `K`-variation each exceed 25.
   Because the carry is positive, all negative mass is ordinary; moreover the ordinary signed sum is strictly negative because `f_carry>1/2>F2`.

5. **RL185.5 — signed phase-count floor** (analytic combinatorics + exact integer certificate). RL184's `251,879,363` distinct forced nonzero defects can all be taken with endpoint heights at most 24. Every such ordinary defect crosses at least one of the 24 height thresholds `0,...,23`. Threshold crossings balance in the closed p-rank height cycle. It follows that there are at least
   `10,075,175`
   negative ordinary defect phases and at least
   `10,075,175`
   positive defect phases when the carry is allowed; consequently there are at least
   `10,075,174`
   positive ordinary defect phases.

This is a real signed/weighted advance: the RL184 incidence can no longer be hidden at zero total variation or in a single sign. It is **not yet a K-corridor contradiction**. The inherited K corridor is roughly `1.87e10` wide, so a lower bound of 25 on each directional K-variation is far below the excursion needed for closure. The next useful attack must amplify the weighted lower bound by proving that long zero prefixes / high-height first defects cannot account for most clean corridors, rather than merely proving more unweighted defect incidence.

## 1. Frozen inherited state

Use

`A=217976794617`, `L=137528045312`,
`p=65470613321`, `u=103768467013`,
`Ap-uL=1`, `B=A-L=80448749305`,
`t=L-p=72057431991`.

Retain RL181:

- `1/2<rho_i<=1` over one period;
- `128,081,997,553 < K_i < 146,795,909,391`;
- `K_(i+1)-K_i=(1/3)q_i(2^G_i-1)`;
- the strict normalized p-rank chain.

Retain RL183/RL184:

- clean common-mechanical successor law;
- `h_(i+1)<=h_i+c_i-1`;
- exact chronological mechanical rotation with `c_i in {1,2}`;
- clean 40-edge corridor floor `10,075,174,499`;
- every clean 40-edge corridor contains a nonzero defect;
- distinct nonzero-defect floor `251,879,363`;
- on an ordinary p-edge `G_i=a-b`;
- physical corrected flow
  `f_i=q_i(2^G_i-1)=rho_i(2^-b-2^-a)`;
- exact global flow
  `sum_i f_i=F2=3(lambda-1)2^37`.

All statements remain internal to `(37,0,23,-1)`.

## 2. Mechanical height envelope inside a clean corridor

Write `A=L+B`. For any chronological interval of length `j`,

`sum_(r=0)^(j-1) (c_(s+r)-1)
 = floor(B(s+j)/L)-floor(Bs/L)`,

with the periodic integer extension understood if the interval crosses `L`.

Therefore the number of `c=2` bits in a length-j factor is either

`floor(jB/L)` or `ceil(jB/L)`.

Along a clean p-pair transition the source and target have the same mechanical bit. Since every accelerated exponent is at least one,

`h_(n+1)=h_n+c_n-k_n <= h_n+c_n-1`.

If both endpoint heights at the corridor start are at most one, then at offset j both endpoint heights are at most

`1+ceil(jB/L)`.

The exact values through j=39 give at most 23 late bits, hence endpoint maximum at most 24. This strengthens the implicit height information in RL184's incidence proof.

## 3. Coverage multiplicity versus endpoint height

Fix a physical nonzero defect edge e used by one or more clean corridor starts. Let

`H=max(a,b)`,

where `(a,b)` are its p-endpoint heights.

If e appears at offset j from an admissible shallow start, then necessarily

`H <= 1+ceil(jB/L)`.

For each fixed offset j there is at most one corridor start ending at e, namely the phase shifted backward by j. Hence e can serve no more than the number of offsets `0<=j<=39` satisfying the height inequality.

The exact multiplicity caps are:

| H | cap | H | cap | H | cap |
|---:|---:|---:|---:|---:|---:|
|1|40|9|28|17|14|
|2|39|10|26|18|12|
|3|38|11|24|19|10|
|4|36|12|22|20|9|
|5|34|13|21|21|7|
|6|33|14|19|22|5|
|7|31|15|17|23|4|
|8|29|16|16|24|2|

Every row satisfies the uniform exact inequality

`cap(H) <= 2^(25-H)`.

This is the key capacity conversion. High defects have smaller physical flow, but they also have far fewer possible shallow corridor starts from which they could have arisen.

## 4. Weighted absolute-flow theorem

Every selected defect is ordinary, so `G=a-b !=0`. With `H=max(a,b)`,

`|2^-b-2^-a| >= 2^-H`.

The inherited residue envelope gives `rho_i>1/2`, hence

`|f_i| > 2^-(H+1)`.

For a selected defect of height H,

`2^26 |f_i| > 2^(25-H) >= cap(H)`.

Choose one nonzero defect in each clean corridor and group corridor starts by the physical defect chosen. If `n_i` starts are assigned to physical edge i, then `n_i<=cap(H_i)`. Therefore

`10,075,174,499
 = sum_i n_i
 < 2^26 sum_i |f_i|`.

The selected edges are a subset of ordinary physical phases, proving

`sum_(ordinary i)|f_i|
 > 10,075,174,499/2^26
 > 150`.

Since the exact K drift is `f_i/3`,

`sum_(ordinary i)|K_(i+1)-K_i| > 50`.

This is a total-variation statement. It does not say that K moves monotonically by 50 or that any one prefix leaves the RL181 corridor.

## 5. Two-sided sign mass

The carry source has

`f_t=rho_t(2-2^-h_t)>1/2`,

because `rho_t>1/2` and `h_t>=0`.

The exact total flow is inherited:

`P-N=F2=3(lambda-1)2^37`.

The bundled rational verifier certifies

`0<F2<1/2`.

The full absolute variation is strictly larger than the ordinary variation plus the carry:

`P+N > 150+1/2`.

Thus

`N=((P+N)-(P-N))/2 > (150.5-0.5)/2 =75`

and

`P=N+F2>75`.

Consequently both signs contribute more than 25 units of total K variation.

There is also a strict global sign bias away from the carry:

`sum_(i != t) f_i = F2-f_t <0`.

So ordinary phases collectively have negative corrected-flow drift even though many individual ordinary defects are positive.

## 6. Signed phase counts from height-threshold balance

Let p-rank order be `i_r=pr (mod L)` and write `H_r=h_(i_r)`. Ignoring the corrected `+1` in the carry defect, the p-shift edges form the closed height cycle

`H_0,H_1,...,H_(L-1),H_0`.

For every integer threshold k, the number of edges crossing from `H<=k` to `H>k` equals the number crossing from `H>k` to `H<=k`.

For an ordinary edge:

- upward height crossing means `G<0`;
- downward height crossing means `G>0`.

The closing carry edge is never an upward height crossing and its corrected defect is positive.

RL184 supplies at least `251,879,363` distinct forced ordinary nonzero defects. By RL185.1 all can be chosen with endpoint heights at most 24, so every one crosses at least one threshold among `0,...,23`.

Set

`M=ceil(251,879,363/25)=10,075,175`.

If at least M forced defects of each sign already occur, there is nothing to prove. Otherwise one forced sign occurs fewer than M times, so the other occurs at least

`251,879,363-(M-1)=241,804,189`

times. Assign each majority-sign defect one threshold that it crosses. By pigeonhole, some threshold is crossed by at least

`ceil(241,804,189/24)=10,075,175=M`

majority-sign edges. Threshold balance forces at least M opposite-direction crossings in the full p-rank cycle.

Hence there are at least M negative ordinary defects and at least M positive defects including the carry. At worst the carry accounts for one positive crossing, leaving at least `M-1=10,075,174` positive ordinary defects.

## 7. Barrier and next consumer

RL185 closes the "nonzero count has no sign/weight" weakness, but it exposes a sharper obstruction.

The weighted lower bound is minimized by defects that occur late in a clean corridor, at heights 23 or 24. The exact capacity calculation already penalizes those late defects by allowing them to serve only four or two corridor starts, respectively, yet the resulting total-flow floor is still only `>150`, far below the scale needed to force an escape from the RL181 K corridor.

The next route should therefore attack **late-defect hiding capacity**:

- classify the first nonzero-defect offset in clean corridors;
- exploit the homogeneous prefix law `2^D C_j=3^j C_0`, hence large 2-adic divisibility at long zero prefixes;
- combine that divisibility with RL182 ternary ownership and RL184's actual mechanical words / affine maps;
- prove that only a limited fraction of the ten-billion corridor starts can delay their first defect to the high-height tail;
- feed the resulting lower-height mass back into the RL185 weighted charging inequality.

Only after the weighted variation is amplified to a scale competitive with the K corridor should sign-reversal packing be expected to close the branch.

## 8. Red-team scope

- **Physical starts only:** every corridor charged here is an inherited RL184 physical clean corridor.
- **Selected versus all defects:** one physical nonzero defect is selected per corridor only for charging; no claim is made that each corridor has exactly one.
- **Multiplicity:** a fixed physical phase can receive at most one start per offset; the height envelope further removes impossible offsets.
- **Mechanical balance:** the late-bit count is derived from the exact floor difference, not from a probabilistic frequency assumption.
- **Flow normalization:** `f_i=q_i(2^G_i-1)` is the corrected physical flow; the K drift is `f_i/3`.
- **Carry:** the carry is excluded from the ordinary corridor charging and reintroduced explicitly in the global sign calculation.
- **Signed counts:** the positive count allowing the carry is distinguished from the positive ordinary count.
- **Total variation versus excursion:** `>50` total ordinary K variation is not promoted as a `>50` net displacement and does not contradict the inherited K corridor.
- **Historical barriers:** no necessary local template is promoted as physically realized, and no generic rank/lattice route is revived.
- **No false closure:** the surviving high type, the preferred branch, Gate A/B, non-trivial-cycle exclusion, and Collatz remain open.
