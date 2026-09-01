# RL212 — e=16 compressed quotient residue and first ternary holes

Date: 2026-09-01.

Classification:
- Sections 1, 3 and 4: **proved analytic mathematics**, conditional on the inherited
  RL210/RL199 H21 interface.
- Section 2: **exact finite certificate** for the complete stated e=16 recurrence.
- The CRT conclusion in section 4 is a **method barrier** only for combining these
  ternary holes with the ordinary terminal-valuation condition by itself.

All physical statements remain conditional on a physical H21 realization of the
sole inherited high branch `(37,0,23,-1)`.

## 1. Exact e=16 reduction

Use
`A=217976794617`, `L=137528045312`, `p=65470613321`, `K0=2^37`,
`b_i=floor(Ai/L)`, `c_i=b_(i+1)-b_i`.

RL210 proves for the exact short above-p offset `e=16` that
`h_t=h_(p+t)` for `0<=t<=16` and `K_0=...=K_17=2^37`.
The inherited H21 source at `p+16` has height one and lower odd endpoint
`y_(p+16)=2^34 eta-1`. Hence `h_16=1`.

The exact root heights obey `h_0=h_1=0`, `h_i>=0` and
`a_i=c_i+h_i-h_(i+1)>=1`. The mechanical heights are

`b_0,...,b_16 = 0,1,3,4,6,7,9,11,12,14,15,17,19,20,22,23,25`.

For any admissible root prefix write

`2^S y_16 = 3^16 y_0 + Q`.

Because `S=b_16-h_16=24`, every admissible prefix has the same `S=24`.

At phase 16, `rho_16=2^25/3^16` and `K_16=2^37`. The matched heights equal one,
so the normalized p-gap gives exactly

`y_(p+16)-y_16 = 2 K_16/rho_16 = 3^16*2^13`.

Therefore

`y_16 = 2^34 eta-1-3^16*2^13`.

Reducing `2^24 y_16=3^16 y_0+Q` modulo `3^16` yields the exact quotient-residue
selector

`eta = (2^24+Q) (2^58)^(-1) (mod 3^16)`.        (E16)

This is an absolute endpoint condition, not the retired normalized-gap denominator
test.

## 2. Exact compressed automaton and first informative ternary level

Run the recurrence only on `(h_i,Q_i mod 3^k)`, starting after the anchored first
edge at `(h_1,Q_1)=(0,1)`. The transition is

`Q_(i+1)=3Q_i+2^(b_i-h_i) (mod 3^k)`

for every `0<=h_(i+1)<h_i+c_i`. This quotient-state automaton is exact for the
displayed modulus; it never enumerates physical-cycle populations.

The complete exact recurrence contains 108,950 root prefixes ending in `h_16=1`.
Equation (E16) maps them injectively to 108,950 eta residues modulo `3^16`.
The inherited H21 law permits only `eta=0 or 8 (mod9)`, leaving 45,046 abstract
prefixes: 29,286 in state011 and 15,760 in state111.

For `3^k`, the number of reachable H21-compatible residue classes is

| k | modulus | reachable / H21-compatible |
|---:|---:|---:|
| 2 | 9 | 2 / 2 |
| 3 | 27 | 6 / 6 |
| 4 | 81 | 18 / 18 |
| 5 | 243 | 54 / 54 |
| 6 | 729 | 162 / 162 |
| 7 | 2187 | **469 / 486** |

Thus no new eta information exists through modulus 729. The first informative
ternary level is exactly `3^7=2187`, where the 17 impossible residues are

`[0, 53, 431, 891, 917, 972, 1160, 1295, 1458, 1493, 1565, 1620, 1701, 1862, 2060, 2088, 2106]`.

The state011 holes are `[0, 891, 972, 1458, 1620, 1701, 2088, 2106]` and the state111 holes are
`[53, 431, 917, 1160, 1295, 1493, 1565, 1862, 2060]`. Both states remain nonempty, so this is not a state or mod18
class exclusion.

At `3^7`, the complete compressed state counts at phases 1 through 16 are

`[1,2,3,7,12,30,85,173,401,586,1071,1912,2308,3416,3655,4950]`.

Only 1,243 distinct terminal `Q mod2187` values occur at height one. This finite
automaton and the 17-hole list are the promoted certificate; the 45,046 raw
H21-compatible prefixes are deliberately not promoted as a list.

## 3. Root p-gap unit lift

At the absolute root, `h_0=h_p=0`, so

`y_p-y_0=K_0=2^37`.

Fix an exact e=16 prefix and its eta modulo `3^16`. Lifting
`eta -> eta+t*3^16`, `t=0,1,2`, changes `y_0 mod3` by

`2^(24+34)t = 2^58 t = t (mod3)`.

Also `2^37=2 (mod3)`. Therefore both `y_0` and `y_p` are units modulo3 exactly
when `y_0=2 (mod3)`, which occurs for exactly one `t`. Every H21-compatible
prefix consequently has one and only one unit-preserving lift modulo `3^17`.

Since `3^16` is divisible by 2187, this lift preserves eta modulo 2187. It
therefore removes none of the 469 surviving low residue classes and does not
select state011 versus state111. Adding `3^17` thereafter preserves all ternary
conditions and flips parity, so terminal sign is not selected by this local
consumer.

## 4. CRT boundary with the standard terminal valuation

The inherited H21 terminal rule writes an odd `s` from eta according to parity and
requires `1<=v2(3^34 s-1)<=21`. Equivalently one odd residue of `s modulo 2^22`
is forbidden by `v2>=22`; the first-rank exceptional cuts occur at a different
terminal rank and do not apply to the e=16 rank.

The new ternary condition depends only on eta modulo `3^7=2187`. Because

`gcd(3^7,2^22)=1`,

the Chinese remainder theorem combines every surviving ternary class with either
parity and with any allowed terminal residue of the corresponding parity. Hence
the ordinary terminal-valuation condition, **by itself**, cannot convert the 17
ternary holes into a deletion of the e=16 terminal rank.

This is not a proof that every surviving residue is physically realized. It is a
precise statement that a stronger consumer must couple the ternary quotient state
to complete-word/absolute information rather than merely append the inherited
2-adic terminal test.

## 5. Scope

The e=16 terminal rank remains `34,124,151,203`. No necessary rank is deleted.
The global frontier remains `13,415,865,871`, split
`7,091,831,284` above p and `6,324,034,587` below p.

No physical H21 incidence or charge, terminal sign, sole-branch contradiction,
Gate A/B closure, nontrivial-cycle exclusion or global Collatz conclusion is
proved. RL206 corrections, the below-p `37/60/97` constants, the p-shift carry,
RL210 first-divergence conditions, RL211 e=4 selector and all ownership/global
scope locks remain binding.
