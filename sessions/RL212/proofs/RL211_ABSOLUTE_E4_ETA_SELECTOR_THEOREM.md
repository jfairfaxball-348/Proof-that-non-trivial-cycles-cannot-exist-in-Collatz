# RL211 — absolute e=4 eta selector and flat-K denominator boundary

Date: 2026-08-31. Classification: **proved analytic mathematics** for Theorems 1–2;
**method barrier** for Theorem 3. All physical statements are conditional on the
sole inherited high branch `(37,0,23,-1)` and a physical H21 realization.

## 1. Inputs

Use
`A=217976794617`, `L=137528045312`, `p=65470613321`,
`b_i=floor(Ai/L)`, `rho_i=2^b_i/3^i`, and `K_0=2^37`.

Inherited RL199 gives at a tau34 H21 source phase `a`
`h_a=1` and lower odd endpoint
`y_a=2^34 eta-1`, with physical eta classes
`0,8,9,17 mod18`; equivalently state `011 <=> eta=0 mod9` and
state `111 <=> eta=8 mod9`.

Inherited RL210 proves for the exact short above-p offset `e=4`, `a=p+4`,
that `h_t=h_(p+t)` for `0<=t<=4` and
`K_0=K_1=...=K_5=2^37`.

Every odd state on a physical cycle is a unit modulo 3.

## 2. Theorem 1: exact root prefix and eta modulo 81

The source height and RL210 equality give `h_4=1`. Direct floor arithmetic gives
`b_0,...,b_4=0,1,3,4,6`, hence
`c_0,...,c_3=1,2,1,2`.

With `h_0=h_1=0`, `h_i>=0`, and
`a_i=c_i+h_i-h_(i+1)>=1`, exhaustive symbolic propagation leaves exactly
three height/exponent words:
`00001/1211`, `00101/1121`, `00111/1112`.

For any acceleration word write
`2^S y_4=3^4 y_0+Q`. All three have `S=b_4-h_4=5`, and direct recurrence gives
`Q=85,73,65` respectively.

At phase 4 there is no p-shift carry. Since the heights at 4 and p+4 are both one,
the normalized gap identity
`K_4=rho_4(x_(p+4)-x_4)` gives
`y_(p+4)-y_4=2K_4/rho_4=3^4*2^32`.
Therefore
`y_4=2^34 eta-1-3^4*2^32`.

Reducing the three equations `2^5 y_4=3^4 y_0+Q` modulo `3^4=81`
gives respectively
`eta=45,3,56 mod81`.
Modulo 9 these are `0,3,2`. Physical H21 allows only 0 or 8 modulo 9.
Therefore only
`h_0...h_4=00001`, `a_0...a_3=1211`,
and `eta=45 mod81` survive. QED.

## 3. Theorem 2: exact lift to eta modulo 243

At the absolute root, `h_0=h_p=0` and `rho_0=1`, so
`y_p-y_0=K_0=2^37`.

For the surviving prefix, lift `eta=45 mod81` to the three residues modulo243:
`45,126,207`.
Substitution into the exact formula for `y_0` gives
`y_0 mod3 = 1,0,2`, respectively. Adding `2^37=2 mod3` gives
`y_p mod3 = 0,2,1`.
A physical cycle has both states units modulo3, so only the third lift is possible:

`eta = 207 (mod 243)`.

Hence state `111` and eta classes `8,17 mod18` are excluded for e=4.
The parity/sign bit is not selected, because adding 243 changes parity. QED.

## 4. Theorem 3: flat-K denominator barrier

RL195's complete-word denominator theorem says that the odd part of the reduced
denominator of `Delta_i=K_i/rho_i` is the global reconstructed-orbit denominator.
Exact `K_0=2^37` already makes that odd denominator one for a complete admissible word.

On any RL210 matched phase with `K_t=2^37`,
`Delta_t=2^37*3^t/2^b_t=3^t*2^(37-b_t)`,
which is dyadic whether or not it is integral. At a first mismatch m the cumulative
drift before m still gives `K_m=K_0`, so the same conclusion holds there.

Thus checking the RL195 denominator criterion again on the flat-K segment adds no
independent obstruction. Any successful continuation must use quotient-state residue,
absolute endpoint value, complete-word moment, inequality, or another datum not reduced
to dyadicity of the normalized gap. QED.

## 5. Scope

No rank is deleted. No physical H21 incidence or charge is proved.
The result is an exact state/lift selector on the one e=4 necessary offset and a
rigorous retirement of one tempting but invalid denominator shortcut.
