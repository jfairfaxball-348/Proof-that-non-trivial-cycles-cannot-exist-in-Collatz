# RL201 — coupled finite reverse strips and terminal-spectrum blindness

Date: 2026-08-31. Frozen RL201 component. Prepared for parent review from the passed RL201
incoming state at `e47dcb720028b4465d125c342fe86fb8daac3aa9`.
All physical implications below remain conditional on the sole high branch
`(37,0,23,-1)`; arithmetic witnesses are not cycle realizations.

## 1. Inherited interface and precise consumer

Use `A=217976794617`, `L=137528045312`, `B=A-L=80448749305`,
`p=65470613321`, `pB=1 mod L`, and `R=57079296007`.
The terminal rank lies in RL200's necessary core
`[25583192106,41775866136]` minus its 12 retained isolated deletions.
At the corresponding tau=34 phase a, the two transported trajectory labels have

`Y_0^-=2^34 eta-1`, `Y_0^+=2^34(eta+21)-1`, `h_0^-=h_0^+=1`.

Here minus/plus name the trajectories leading to the lower/upper ordered tau=34
endpoints; they need not remain ordered as ordinary integers at earlier times.
The H21 state is `011` for eta=0 mod9 and `111` for eta=8 mod9.
The terminal signed defect is `+nu` for even eta and `-nu` for odd eta, with
`1<=nu<=21`. The odd parameter s is eta+21 in the positive case and eta in the
negative case, and `nu=v2(3^34 s-1)`.

A **fixed finite local coupled reverse strip** of depth m>=1 fixes BOTH entire
acceleration-exponent words `a_j^-`, `a_j^+` for j=1,...,m. It fixes their actual
mechanical bits, induced nonnegative heights, and any coupling data that are functions
of those words/heights and the completed normalized pair gaps defined below.
The exponents are not available for independent re-selection after eta changes.
The required common leading exponent is 1 in state 011 and 2 in state 111.

The template may prescribe exact pair numerators, relative exponent differences,
height bounds, and every rank-resolved local K value obtained from the completed
gaps. It does not additionally identify a vertex with a different time/trajectory
vertex or impose an absolute endpoint, a complete periodic word, cycle closure,
an absolute-position reconstruction moment, or signed post-terminal K data.
For the two finite verifier fixtures all source/forward-tail time labels are distinct.
The theorem is about compatibility with this stated local consumer, not physical
existence after omitted global identifications are restored.

## 2. Carry completion is necessary at a mechanical seam

Put `b(i)=floor(Ai/L)`, valid for all integer phases, and

`u0=floor(Ap/L)=103768467013`, `Ap=u0 L+1`,
`epsilon(i)=b(i+p)-b(i)-u0`.

Then epsilon is either 0 or 1, and equals 1 exactly when the mechanical rank
`iB mod L` is `L-1`. In particular epsilon(a)=0 at every H21 tau=34 phase in
the refined core. Set `epsilon_j=epsilon(a-j)` and

`c_j^-=b(a-j+1)-b(a-j)`,
`c_j^+=b(a+p-j+1)-b(a+p-j)`,
`C_j^sigma=sum_(k=1)^j c_k^sigma`.

Telescoping gives the exact carry identity

`C_j^+ - C_j^- = epsilon(a)-epsilon(a-j) = -epsilon_j`.

Writing `Z_j^sigma=Y_j^sigma/2^h_j^sigma`, the completed normalized p-gap is

`W_j=2^epsilon_j Z_j^+ - Z_j^-`.

Away from the seam this is the ordinary normalized difference. At a seam it is
essential to include the carry: the ordinary difference need not be invariant under
the translation below. Fixed mechanical weights multiplying W_j are independent of
eta, so every exact local K value obtained from this completed gap is preserved too.

## 3. Exact coupled translation theorem

Let a fixed template have one compatible positive eta0, with positive odd unit
states at every reverse layer. Put

`E_j^sigma=sum_(k=1)^j a_k^sigma`,
`h_j^sigma=1+E_j^sigma-C_j^sigma`,
`M=3^(m+1)`.

For every integer t>=0 put `eta=eta0+Mt`, keeping both exponent words fixed.
Iteration of

`Y_j^sigma=(2^a_j^sigma Y_(j-1)^sigma-1)/3`

gives the exact affine translation

`Y_j^sigma(eta)-Y_j^sigma(eta0)
 =2^(34+E_j^sigma) 3^(m+1-j) t`.

For 0<=j<=m this is an even multiple of 3. Thus integrality, oddness, unit status
modulo 3, and positivity are preserved. The reverse identity with odd target fixes
the exact forward acceleration exponent, so the prescribed exponent words also
remain exact. Heights, all fixed height bounds, and every relative exponent or
height defect are unchanged.

Normalizing the difference gives

`Z_j^sigma(eta)-Z_j^sigma(eta0)
 =2^(33+C_j^sigma) 3^(m+1-j) t`.

Since `epsilon_j+C_j^+=C_j^-`, multiplication by the carry factor makes the
plus and minus translations equal. Therefore **W_j is unchanged exactly at every
layer**, including seam layers. Every numerator obtained by multiplying W_j by a
fixed dyadic denominator determined by the template is also unchanged. Hence all
the fixed, genuinely coupled consumer data in Section 1 survive the translation.

This is stronger than independent reverse extendability: here neither endpoint may
change even one of its already prescribed exponents, and the full coupled gap/defect
data are retained. It does not extend through an omitted global vertex identification:
different time layers generally acquire different absolute translations.

## 4. Every terminal sign and valuation survives a fixed compatible state template

Fix any sign sigma in {+1,-1} and any nu in {1,...,21}. Put `Q=2^(nu+1)` and

`s_nu = (3^34)^(-1) + 2^nu mod Q`.

This residue is odd, and

`3^34 s_nu-1 = 2^nu mod 2^(nu+1)`.

For positive sign require `eta=s_nu-21 mod Q`; this is an even residue. For
negative sign require `eta=s_nu mod Q`; this is odd. Since M is odd, CRT solves
either requirement simultaneously with `eta=eta0 mod M`. Arbitrarily large positive
representatives exist and can be written `eta0+Mt` with t>=0.

The H21 state remains unchanged because m>=1 implies 9 divides M. Every reverse
constraint in Section 3 remains unchanged. RL199's affine forward tail then has
the requested terminal sign and exact valuation nu. Both terminal heights are
nonnegative, namely 21 and 21-nu, and the terminal numerator remains `7*3^35`.

Thus **each compatible fixed state template supports all 42 pairs
`(terminal sign,nu)` with sign in {+,-} and 1<=nu<=21** under the named local
consumer. It cannot exclude either parity class within that state or any terminal
valuation. It may still exclude a state because its leading word is state-specific.
An independently supplied signed successor-K interval may exclude some members of
this spectrum; that is additional data, not a contradiction of this theorem.

## 5. A forced earlier defect and a possible height anchor

At tau=35, RL199 gives the endpoint residues

`(Y_1^-,Y_1^+)=(2,1) mod3` in state 011,
`(Y_1^-,Y_1^+)=(1,2) mod3` in state 111.

The source mechanical bit at tau=36 is 1 on both trajectories. Let the common
tau=35 height be e, so e=0 for 011 and e=1 for 111. Reverse integrality forces
the earlier exponents to have opposite parity. More precisely,

- state 011: `a_2^-` odd, `a_2^+` even;
- state 111: `a_2^-` even, `a_2^+` odd.

Since `h_2^sigma=e+a_2^sigma-1`, both cases give

`h_2^- even`, `h_2^+ odd`.

The tau=36 p-defect is therefore odd and nonzero. Its magnitude/sign are not fixed.
For state 111 positivity of exponents additionally gives `h_2^->=2`, `h_2^+>=1`;
state 011 permits `h_2^-=0`. Thus an independent proof of the absolute height
`h_2^-=0` would select state 011. Nothing here proves that height is zero.
This does not reopen the excluded H21 zero-edge route: tau=36 is before the
co-owned tau=35 zero-defect prefix, and the two heights are unequal.

## 6. Optional state-partner lemma (different exponent templates)

Suppose a compatible state-011 template of depth m>=2 has both tau=36 heights
at least one. Form another template by replacing

`a_1^sigma=1` with 2,
`a_2^sigma` with `a_2^sigma-1`,

and leaving all earlier exponents unchanged. These remain positive; the tau=35
heights become 1 and all heights from tau=36 backward are unchanged.

For its eta1 choose

`2^36(eta1-eta0)+1 = 0 mod 3^(m+1)`, with `eta1>=eta0`.

Since `2^36=1 mod9`, eta1=8 mod9 as required for state 111. Put
`D=2^36(eta1-eta0)+1`. At tau=36, for an endpoint whose fixed source height is h,

`Y_2^(011)=(2^(h+36)eta0 -3*2^(h+1)-3)/9`,
`Y_2^(111)=(2^(h+36)eta1 -5*2^h-3)/9`,

so their difference is `2^h D/9`. At later reverse layers j>=2, fixed exponent
recurrence gives

`Y_j^(111),sigma-Y_j^(011),sigma
 =2^(h_j^sigma+C_j^sigma-3) D/3^j`.

These are even multiples of 3: at j=2 use h>=1, and at j>=3 use C_j>=4 and
h_j>=0. Hence unit odd integrality is preserved. At j=1 the exact relation is
`Y_1^(111)=2Y_1^(011)+D/3`; it preserves oddness and exchanges unit residues.
Every completed gap is equal across the two templates, because its normalized
translation is `2^(C_j^sigma-3)D/3^j` for j>=2, and the carry identity cancels it.
The equality of completed gaps also holds directly at j=0 and j=1.

This constructs a state-111 partner with identical completed gaps and identical
heights from tau=36 backward; the tau=35 physical numerator doubles because its
common height rises by one. Applying Section 4 separately to the two templates
produces all four mod-18 classes and all 21 valuations.

This is NOT state blindness of one fixed exponent word: the first two exponent
pairs and tau=35 height change. A zero tau=36 height can obstruct the switch, and
an independently prescribed leading exponent or height can select a state.

## 7. Exact verification, dependencies, and missing global datum

Command:

`python3 verification/verify_rl201_coupled_reverse.py`

Result: PASS. The verifier independently propagates affine Fraction expressions
and literal integer reverse recurrences, checking equality of completed gaps and
dyadic numerators, fixed exponents/heights, positivity, unit status, all 33 exact
exponent-one tail steps, terminal valuation/sign/height, and the terminal numerator.
It verifies exactly 168 witnesses: two actual canonical-rank fixtures, two distinct
state templates, both signs, and every nu from 1 through 21.

Fixtures:

- Terminal rank 30000000000, tau=34 phase 74483362526, depth 16, no seam;
  maximal local height 35. State seeds eta=18 and eta=43207982. Witness digest
  `98c2c15ac7385a5292338dd445fad061586e8646ec91e2127498a512e068e6d7`.
- Terminal rank 31435476725, tau=34 phase 72057431995, depth 6; the strip crosses
  the actual seam and epsilon=1 exactly at layer 4. Maximal local height 9.
  State seeds eta=18 and eta=1610. Witness digest
  `dab85bc6ce3d00a42c4ddbcd74701aac7df1671dfdb8576a50017f5b13de1c44`.
  The verifier explicitly confirms that the ordinary uncompleted normalized gap
  changes at the seam while the completed gap remains exactly invariant.
  At that layer the plus trajectory is at canonical phase zero, but its assigned
  height is 4. Therefore this fixture does **not** impose the inherited canonical
  anchor h_0=0. It is solely a local arithmetic carry regression, not a full
  canonical-height or all-anchor-compatible witness. No compatibility with that
  omitted global anchor is claimed for this fixture.

The finite checks do not enumerate all ranks or all eta. The infinite claim comes
from the exact algebraic translation/CRT proof. Both ranks are necessary-rank
witness labels only, not certified physical terminals. The exact fixtures support the analytic proof within its stated scope; independent
review and final fresh-unpack verification are recorded in this handover.

Load-bearing inherited facts: RL199's oriented endpoints, state dictionary, terminal
valuation/height/numerator formula; RL200's refined core and first extra mechanical
bits; the carry completion used in the inherited p-gap/K definitions. The carry
identity itself is re-derived explicitly from A,L,p above.

The missing datum must constrain an **absolute endpoint value** or its global
identification: an orbit closure/overlap identity, a reconstruction moment fixing
absolute position, a globally anchored height, or an independently certified signed
successor-K value. Even exact rank-resolved K values throughout a finite coupled
reverse strip preserve the translation freedom and cannot by themselves determine
the terminal spectrum.
