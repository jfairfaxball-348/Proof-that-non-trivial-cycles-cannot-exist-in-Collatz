# RL206 frozen interface before quotient-residual derivation

Date: 2026-08-31. Status: verified incoming-interface recovery; apply both RL206 correction ledgers where relevant.
BASE_HEAD: `8df2f8529a839ed777674118d0943eb4af3a1b51`.
Authority tree: `539f45504530cc1973655e4078edf79462023ff1`.

The exact interface below was frozen after the incoming gate and after the narrowly
identified RL20 increment repair. It does not assume that an exhaustive canonical
Gate-B witness or a universal small-residual modulus theorem has already been proved.

## Full-word ownership and quotient states

Let `d=d_0...d_(A-1)` be a binary full-parity word with length `A`, weight
`0<L<A`, prefix weights `P_m=sum_(i<m)d_i`, and

`Q(d)=sum_(d_i=1) 2^i 3^(L-1-P_i)`, `D=2^A-3^L>0`.

For a left rotation let `Q_m=Q(rot_m(d))`. A genuine owned ordinary cycle has
`D|Q_0`; its integer states are `R_m=Q_m/D` and satisfy

`2R_(m+1)-3^(d_m)R_m=d_m` (cyclic indices),

`2^m R_m-3^(P_m)R_0=Q(d_0...d_(m-1))`.

Without ownership the same equalities hold on the rational fixed orbit. They alone
must not be called a new ownership theorem. The full-word modulus here is `D`.
Sources: incoming RL205 report section 2; RL79 report sections 2–3.

## Balanced cuts and strict excursions: branch scope

For a primitive hypothetical owned cycle rooted at its least state `R#`, put
`A=g a`, `L=g ell`, `g=gcd(A,L)>1`, `X=2^a`, `Y=3^ell`,
`z=X/Y`, `lambda=z^g`, `K_j=P_(ja)`, `E_j=K_j-j ell`,
`x_j=R_(ja)`, `y_j=3^(-E_j)x_j`, and `H_j=z^j y_j`.

Under `lambda<16/15`, inherited least-state suffix domination gives `E_j>=0`
at proper cuts. A balanced cut `E_j=0` yields a distinct odd state
`R#<x_j<lambda R#`. If all proper `E_j>=1`, the strict-excursion branch has
`x_j>(45/16)R#` and a nondecreasing normalized lift from `R#` to `lambda R#`.
The `g=1` case and other resonance branches are not covered by this dichotomy.

For block `B_j` with weight `r_j=ell+E_(j+1)-E_j`, raw numerator `Q(B_j)`:

`X x_(j+1)-3^(r_j)x_j=Q(B_j)`,

`c_j=3^(-E_(j+1))Q(B_j)=Xy_(j+1)-Yy_j`,

`H_(j+1)-H_j=(z^j/Y)c_j`.

The last formula explicitly repairs R20G.12; the printed raw coefficient omitted
`3^(-E_(j+1))`. Strictness holds iff the block contains a `1`. The height bounds,
nonnegative monotonicity and total strip width `(lambda-1)R#` remain valid.
See `../corrections/RL20_INCREMENT_NORMALIZATION_REPAIR.md` for the first invalid expression and proof.

## Gate-B and radius-3 contracts

RL72 G7 and G8 label balanced-return and strict-excursion contradictions as open
programmes. They do not give an exhaustive canonical close pair or prove `M|W`.
RL72 R3.0's closed local obstruction requires primitive full-`D` self-rotations,
exact cyclic adjacent-transposition distance 3 and its branch-specific support,
orientation and gcd hypotheses, retaining the inherited external dependency ledger.
No radius-3 leaf is invoked in this recovery.

For equal-weight binary words, cyclic adjacent-transposition distance is
`min_(c in Z) sum_i |c+S_i|`, with `S_i` the cumulative bit difference.
The RL20 fake has minimum distance 4, not a qualifying radius-3 pair.

The RL48/RL64 retained half-word architecture uses the separate factor
`M=2^a-3^ell`. Its full-phase ownership includes the exact condition
`M|Q(v)+4*3^ell`. This is a branch-specific ownership definition, not a global
Gate-B modulus. The raw half-rotation weighted-difference splice is a known
proper-factor identity (RL72 S2); the raw phase defect has quotient magnitude at
least one (RL72 S3). No universal `M|W` is inferred from either.

## Required countermodels and scope locks

The frozen 184-bit RL20 local-grammar fake has `A=184`, `L=116`,
`D=2334616309231614197768369354039452620227287343359226095`,
`Q=623664726303251068611736310410781607975198703790695886677`,
`gcd(D,Q)=1`, and nonzero `Q mod D`.
It has no integer quotient state `Q_m/D`; that premise must be used essentially.
Its endpoint residue witness is not its rational fixed state.

RL79's canonical generalized increment is `s=D/gcd(D,Q)`, with integer
states `n_m=Q_m/gcd(D,Q)` and normalized states `n_m/s=Q_m/D`.
Homogeneous identities cannot supply the missing integer-lattice ownership fact.
This does not forbid predicates such as integrality of `n_m/s`, which do distinguish
ordinary ownership. The precise proposed family must be stated before a no-go claim.

No free-context uniform size bound, global Gate closure, rank deletion, H21 incidence
or charge, or inherited external-floor upgrade is assumed or established here.
All seven RL206 red teams remain mandatory.
