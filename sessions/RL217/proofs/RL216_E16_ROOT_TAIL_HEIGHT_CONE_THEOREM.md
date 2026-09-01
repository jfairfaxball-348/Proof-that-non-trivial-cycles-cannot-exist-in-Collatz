# RL216 — exact e=16 root-tail height cone and canonical-prefix exclusion

Date: 2026-09-01. Classification: **proved exact recurrence lemma plus exact finite modular certificate** at the scopes separated below.

All physical implications remain conditional on a physical H21 realization of the inherited sole high branch `(37,0,23,-1)`. Arithmetic root candidates and abstract prefixes are not promoted to physical words, populations or cycles.

## 1. Incoming e=16 family

Retain the RL215 constants and e=16 family

`A=217976794617`, `L=137528045312`, `p=65470613321`,
`u=103768467013`, `K0=2^37`,

and the 45,046 exact H21-compatible root prefixes. For every such prefix RL212 gives

`2^24 y_16 = 3^16 y_0 + Q`,

while the matched p-shift source gives

`y_(p+16)=2^34 eta-1`,
`y_(p+16)-y_16=3^16*2^13`.

Hence at every lifted candidate

`y_16 = 2^34 eta - 1 - 3^16*2^13`.                         (H1)

RL215 parametrizes the remaining lifts by

`y_0=y_0^*+3*2^58 k`.

The corresponding eta lift is exact:

`eta=eta_*+3^17 k`.                                        (H2)

This is the same lift relation already used in the RL215 mod18 and Hensel accounting.

## 2. Exact forward height obstruction

For a genuine odd Collatz state `y_i`, define its chronological acceleration exponent

`a_i = v_2(3 y_i+1)`,
`y_(i+1)=(3 y_i+1)/2^a_i`.

The inherited mechanical-height relation is

`a_i=c_i+h_i-h_(i+1)`,
`c_i=b_(i+1)-b_i`, `b_i=floor(Ai/L)`.

Therefore

`h_(i+1)=c_i+h_i-a_i`.                                    (H3)

Every physical height is a nonnegative integer. Consequently, once a candidate root state and starting height are fixed, its deterministic forward odd trajectory is impossible as a physical word if (H3) produces a negative height at any phase.

At e=16 the root prefix has `h_16=1`. Equations (H1)-(H3) therefore define an exact second-phase consumer with no logarithmic approximation, no endpoint-moment rewrite and no use of RL209's signed-successor anchor.

## 3. Residue-class projection without candidate enumeration

Fix one e=16 prefix and a k interval. On a residue branch

`k = r + 2^m t`,

write the current state exactly as

`y_i=A_i t+B_i`.

At phase i,

`3y_i+1 = 3A_i t + (3B_i+1)`.

If

`v_2(3B_i+1) < v_2(A_i)`,

then `a_i=v_2(3B_i+1)` for every integer t on that branch. If the inequality fails, split t by parity. The two children are exact residue classes modulo `2^(m+1)`, and the affine state remains integral after substitution.

If every term in the affine expression is divisible by `2^(h_i+c_i+1)`, then every candidate in that branch has

`a_i>h_i+c_i`,

so (H3) gives `h_(i+1)<0` and the entire residue branch is excluded. Otherwise a fixed admissible acceleration exponent advances the branch exactly to phase i+1.

The number of integers in a finite k interval belonging to `k=r mod2^m` is counted by the first congruent integer and an exact floor division. Thus this is a modular/range-counting projection onto the RL215 progressions, not a scan of the full candidate family.

## 4. Canonical minimum-Q prefix

Among the 45,046 H21-compatible e=16 prefixes, the unique minimum-Q prefix is

`Q=43,013,953`.

Its base data are

`eta_0 mod3^16 = 33,322,841`,
`lift t=2`,
`eta_*=119,416,283 mod3^17`,
`y_0^*=799,582,255,090,532,351`.

It is state111 (`eta=8 mod9`) and has `eta=1709 mod2187`.

The exact RL215 two-sided window gives

`28,812 <= k <= 36,180`,

so this prefix contributes exactly **7,369** RL215 candidates. The inherited terminal Hensel congruence removes none of these 7,369 candidates.

## 5. Exact modular height-cone certificate

Apply the residue-class procedure of section 3 from phase 16 through phase 174. The verifier reconstructs the entire RL212/RL215 prefix domain, identifies the canonical minimum-Q prefix, derives its k interval, and then performs only exact 2-adic residue splitting and range counts.

The resulting certificate contains **6,219** disjoint failure residue branches whose exact interval populations sum to **7,369**. No residue branch survives through phase 174. The latest first negative-height failure occurs at phase **174**.

The canonical sorted failure-class digest is

`b7f03ca354275de4e4d9aaa0698ab6e39d088232331a3f2f9b111a01df96d972`.

Therefore the canonical minimum-Q e=16 prefix has no physical realization inside the complete RL215 two-sided/Hensel-surviving family and is deleted exactly.

This is RL216-CERT1.

## 6. Exact population consequence

Deleting only this certified prefix removes **7,369** arithmetic candidates from RL215 and leaves

**331,927,916**

candidates in the deliberately conservative targeted family, across **45,045** e=16 prefixes.

The deleted prefix contains 3,684 candidates in mod18 class 8 and 3,685 in class 17. Thus the post-RL216 targeted candidate totals are

- class 0: 107,901,476;
- class 8: 58,062,518;
- class 9: 107,901,377;
- class 17: 58,062,545.

Both H21 states remain. The deleted prefix's eta residue 1709 modulo2187 occurs in eleven other exact prefixes, so all **469** RL212 reachable eta classes modulo2187 remain represented.

## 7. Scope

RL216 meets its success criterion by deleting one exact e=16 prefix. It does **not** claim that the same horizon kills every prefix, and it does not infer a physical population count from arithmetic candidates.

No necessary terminal rank is deleted: e=16 terminal rank `34,124,151,203` remains possible through other prefixes. The global necessary-rank frontier therefore remains **13,415,865,871**: 7,091,831,284 above p and 6,324,034,587 below p.

No quotient residue `(Q/D) modD` is determined. No physical H21 incidence or charge, branch contradiction, Gate closure or global nontrivial-cycle exclusion is proved.
