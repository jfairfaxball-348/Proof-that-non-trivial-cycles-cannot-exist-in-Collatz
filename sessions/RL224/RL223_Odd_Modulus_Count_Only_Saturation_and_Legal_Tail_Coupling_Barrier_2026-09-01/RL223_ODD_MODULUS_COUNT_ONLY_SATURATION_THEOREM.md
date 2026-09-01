# RL223 odd-modulus count-only saturation theorem

Date: 2026-09-01.

## Classification and exact scope

**Classification: proved analytic theorem, supported by a gap-free exact finite
certificate.**

The theorem below describes ordinary binary parity words having one fixed total
length and one fixed total odd count.  It does **not** describe candidate-specific
continuations from one fixed exact `y16`; it does not encode the inherited
phase-51 cylinders, H21 nonnegative-height/incidence/charge conditions,
least-state ownership, cyclic closure, or the physical shortcut floor.

It therefore certifies a structural blindness result for the count-only
relaxation, not a legal-H21 survivor or deletion.

## Definitions

For the ordinary shortcut Collatz map

`C(x)=x/2` for even `x`, and `C(x)=(3x+1)/2` for odd `x`,

let `w=(w_0,...,w_(N-1))` be a binary parity word with `M` ones.  If its one
positions are `0<=r_1<...<r_M<N`, define

`Q(w)=sum_(i=1)^M 2^(r_i) 3^(M-i)`.

Every realization of `w` satisfies

`2^N x_N = 3^M x_0 + Q(w)`.

For `q>=2` with `gcd(q,6)=1`, put

`S_(N,M)(q)={Q(w) mod q : w in {0,1}^N, sum w_j=M}`.

This is an exact finite set.  Its two useful recurrences, with all operations
modulo `q`, are

`S_(n,m)=2*S_(n-1,m) union (3^(m-1)+2*S_(n-1,m-1))`

and

`S_(n,m)=S_(n-1,m) union (3*S_(n-1,m-1)+2^(n-1))`,

with `S_(0,0)={0}` and the set empty outside `0<=m<=n`.

Every binary word is the ordinary parity word of infinitely many positive
starts: its starting residue class is

`x_0 = -3^(-M) Q(w) (mod 2^N)`.

This ordinary parity legality varies the starting integer with the word and must
not be confused with continuation legality from one fixed current `y16`.

## Euler-block saturation theorem

Let `H=phi(q)`.  If

`min(M,N-M) >= q*H`,

then

`S_(N,M)(q)=Z/qZ`.

### Proof

Euler's theorem gives `2^H=3^H=1 (mod q)`.  Place `q` consecutive blocks of
length `2H` and weight `H`, independently chosen as

`B0=1^H 0^H`,

`B1=1^(H-1) 0 1 0^(H-1)`.

Both variants begin with `1`.  Changing block `j`, indexed from zero, from
`B0` to `B1` moves the block's last one by one position.  If the blocks begin at
global position `R` and the fixed filler after them contains `F` ones, the exact
change in the numerator is

`delta_j=2^(R+2Hj+H-1) 3^(F+(q-1-j)H)`.

Every `delta_j` is a unit modulo `q`, and

`delta_(j+1)/delta_j=2^(2H)3^(-H)=1 (mod q)`.

Thus all `q` switches add the same unit `delta`.  Switching exactly
`t=0,...,q-1` blocks produces `q` distinct residues and hence all of `Z/qZ`.
The capacity hypothesis leaves a filler with exactly `M-qH` ones and
`N-M-qH` zeros, so every constructed word has the prescribed totals.  This
proves the theorem.

Since `phi(q)<=q-1`, the factorization-free sufficient condition is

`min(M,N-M) >= q(q-1)`.

For RL223,

`A=217976794617`, `L=137528045312`,

`N=A-24=217976794593`,

`M=L-16=137528045296`,

`N-M=80448749297`.

The exact endpoint of the uniform bound is

`283635*283634=80448529590 <= 80448749297`,

while

`283636*283635=80449096860 > 80448749297`.

Therefore `S_(N,M)(q)=Z/qZ` for every `q` with `2<=q<=283635` and
`gcd(q,6)=1`.  There are exactly **94,544** such moduli; the largest eligible
one is `283633`.

## Fixed-prefix corollary and exact q=5 type guard

For a fixed prefix `p` of length `ell` and weight `r`, concatenation gives

`Q(pv)=3^(M-r)Q(p)+2^ell Q(v)`.

Hence the same saturation conclusion holds for the formal count-only
completions of `p` whenever the residual one and zero capacities each exceed
`q*phi(q)`.  This still varies the realization after `p` and does not establish
continuation from the exact endpoint of `p`.

For the inherited common arithmetic witness, direct shortcut iteration from

`y16=63944214675001842327551`

follows the exact 52-bit, 35-one prefix

`P=1111111111111001101111010011001010101111110110011000`

and ends at

`y51=710371286312677333954849`.

Put `B0=11110000` and `B1=11101000`.  The formal word

`P · (four independently selected B blocks) · 1^137528045245 · 0^80448749264`

has the exact totals `(N,M)`.  Modulo 5, selected masks give

`0011 -> 0`, `0001 -> 1`, `0000 -> 2`, `1111 -> 3`, `0111 -> 4`.

For the same tuple,

`y0=24921895945404894117887`

and the return target is `T=3 (mod 5)`, so mask `1111` is a formal count-only
match.  Only `P` is verified as the actual continuation from `y16`; none of the
selectable blocks is asserted to be the actual continuation from `y51`.

## Endpoint-return interpretation

For a legal tail from `y16` to `y_end`, the affine identity gives

`Qtail=2^N y_end-3^M y16`.

The candidate return target is

`T(c)=2^N y0-3^M y16`.

Since `2` is a unit modulo every allowed `q`,

`Qtail=T(c) (mod q)` if and only if `y_end=y0 (mod q)`.

On an inherited affine `k`-lift,

`T(k+1)-T(k)=3*2^34*(2^A-3^L)=3*2^34*D`.

Thus the target image modulo `q` has `q/gcd(D,q)` residues, but the count-only
word side is already all of `Z/qZ` in the proved range.  Candidate selectivity
requires independently certified legal-continuation data.

## Exact limitations

- The direct finite DP covers every eligible `5<=q<=1023`; direct DP outside
  that interval was not run and is not claimed.
- The analytic uniform theorem covers every `q<=283635` coprime to 6; no uniform
  assertion is made above that bound.
- For `q=5,N=2,M=1`, `S_(2,1)(5)={1,2}`, so short fixed-count saturation is not
  unconditional.
- No actual legal H21 continuation residue set was computed.
- RL223 deletes **0 candidates, 0 prefixes, and 0 ranks** and proves no Gate,
  branch contradiction, or global Collatz result.
