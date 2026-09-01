# RL211 exact absolute e=4 selector certificate

Constants:
`A=217976794617`, `L=137528045312`, `p=65470613321`, `K0=2^37`.
For `b_i=floor(Ai/L)`, the first five values are `0,1,3,4,6`, hence the four
mechanical digits are `1,2,1,2`.

Under the RL210 e=4 lock and the inherited H21 source height one:
`h0=h1=0`, `h4=1`. Positive acceleration leaves exactly:
- `00001 -> a=1211 -> Q=85`;
- `00101 -> a=1121 -> Q=73`;
- `00111 -> a=1112 -> Q=65`.

The source equation and flat K gap give
`y4=2^34 eta-1-81*2^32`.
Reducing `2^5 y4=81*y0+Q` modulo 81 gives
`eta=45,3,56 mod81`.
Their residues modulo 9 are `0,3,2`; only 0 belongs to the inherited physical
H21 state set `{0,8}`. Thus only `00001/1211` remains.

For this surviving word the three lifts `45,126,207 mod243` give
`(y0,yp) mod3 = (1,0),(0,2),(2,1)` using the exact root relation
`yp-y0=2^37`. Since every odd physical cycle state is a unit modulo 3,
only `eta=207 mod243` survives.

Certificate classification: exact finite arithmetic supporting analytic theorem.
It does not certify physical incidence, rank deletion, terminal sign, Gate closure,
or global cycle exclusion.
