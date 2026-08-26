# RL102 — prefix/suffix content transport and strict-excursion barrier

Date: 2026-08-26

## 0. Outcome and scope

RL102 completed the requested full-ownership/content attack on the current
raw-multiplicity first-surplus cylinder.  It does **not** prove a lower bound
on the least cylinder representative, exclude any raw multiplicity, close
either global Gate, exclude nontrivial cycles, or prove Collatz.

The direct numerator-decomposition subroute has an exact barrier: after the
ordinary `+1` constants are kept, its full-denominator consequence is the
already-known rotation transport/cycle-closure identity.  In the equal-slope
branch, reduction modulo the local factor supplies no residue condition on
the prefix numerator.  The two-sided physical excursion also cannot, by
itself, give a scale-homogeneous packing contradiction: an exact primitive
positive generalized-increment cycle realizes the same qualitative geometry.

These are route barriers, not demotions of RL101's cylinder or physical-state
theorems.  The next target therefore isolates a genuinely non-homogeneous
`s=1` lattice/content consumer.

## 1. Exact ordinary-`+1` prefix/suffix decomposition

Let the maximum-rooted full word split as `W=ab`.  Write

`n=|a|`, `r=wt(a)`, `u=2^n`, `v=3^r`,

`U=2^(A-n)`, `V=3^(L-r)`, and `D=uU-vV=2^A-3^L`.

Let `C=Q(a)` and `E=Q(b)` be the ordinary-`+1` word numerators.  The exact
concatenation rule is

`Q(W)=V C+uE`.                                             (RL102.1)

If `M` is the physical state at the cut before `a`, and `X` the physical
state at the cut after `a`, the two affine equations are

`uX=vM+C`,                                                 (RL102.2)

`UM=VX+E`.                                                 (RL102.3)

Eliminating `X` gives

`DM=VC+uE=Q(W)`.                                           (RL102.4)

Thus the requested full-cycle `D|Q(W)` input is present exactly as integer
closure, but the prefix/suffix expression is its canonical numerator.

For the rotated full word `W'=ba`, direct subtraction gives the independent
looking but exact identity

`u Q(W')-v Q(W)=D C`.                                      (RL102.5)

This is precisely the RL78 rotation transport specialized to the first
surplus cut.  If `D|Q(W)`, it implies only `D|Q(W')`; it imposes no new
congruence on `C`, because the prefix term already carries the full factor
`D`.

Classification: **analytic identity**.

## 2. Equal reduced-slope factor audit

In the proper equal-slope branch, let the local first-surplus counts be
`(n,r)=(gp,gq)` and global counts `(A,L)=(Gp,Gq)`, with `g<G`.
Then

`D_g=2^(gp)-3^(gq)=u-v` divides `D=2^(Gp)-3^(Gq)`.

Reducing (RL102.5) modulo `D_g` gives

`u[Q(W')-Q(W)] == 0 (mod D_g)`,

because `u==v (mod D_g)` and `D_g|D`.  Since `u` is a unit modulo `D_g`,

`Q(W') == Q(W) (mod D_g)`.                                (RL102.6)

Full ownership already gives `D_g|Q(W)`, hence also
`D_g|Q(W')`.  Again, the local factor has only transported full-word
divisibility around the rotation; it does not constrain `Q(a)` or force a
nonzero multiple of `D` into a bounded interval.

Classification: **analytic route barrier for the direct decomposition**.

## 3. Strict-excursion generalized-increment red team

The following exact witness tests whether first-surplus arithmetic and the
physical inequalities alone can contradict a positive primitive cycle.

Use `(p,q)=(65,41)`, global multiplicity `G=3`, and raw local multiplicity
`g=2`.  The deterministic word constructed by
`verification/find_generalized_excursion_witness.py` is primitive and is the
parity word of a positive integer cycle for

`T_s(n)=n/2` for even `n`, and `(3n+s)/2` for odd `n`,

where the exact increment is

`s=1697535785403803429530459988901995256069001612190296230341>1`.

At its actual maximum `M`, its backward raw segment has counts `(130,82)`,
has no earlier surplus, and satisfies exactly

`2 x_p<M`, and `16 x_(gp)>15M`.

The witness is deliberately **not** an ordinary Collatz cycle and does not
satisfy full ordinary `D|Q`.  It proves only the necessary red-team point:
the first-surplus/deep-return geometry and its scale-free state inequalities
persist in the generalized-increment setting.  Therefore an RL20-style
strict-excursion or population inequality that uses only those homogeneous
data cannot be the missing ordinary-`+1` ownership consumer.

Classification: **exact finite generalized-map countermodel to a
scale-homogeneous geometry-only contradiction**.

## 4. Required red-team ledger

1. **Ordinary `+1` / RL79.** Equations (RL102.1)--(RL102.5) retain ordinary
   constants, but their form persists with all numerators multiplied by a
   generalized increment.  They do not isolate `s=1`; no lower-content
   theorem is promoted.
2. **RL20 fake / full `D|Q`.** The transport identity itself holds for every
   word.  The implication from full divisibility to the rotated word is real,
   but adds no independent prefix condition.  This direct subroute therefore
   fails the required ownership-discriminator standard.
3. **RL81 physical-state check.** `M`, `X`, `x_p`, and `x_(gp)` above are
   actual cycle states.  No normalized quotient coordinate is placed in a
   physical interval.
4. **Primitivity.** The finite generalized witness is checked primitive by
   its verifier.  It is a red team only, never an ordinary owned cycle.
5. **Raw multiplicity and scope.** The identities quantify over all splits
   and all raw multiplicities.  The finite witness has `g=2` at a nearby
   reduced slope and is not evidence about the first-Farey branch.
6. **External floor.** No use of the inherited `R#>=2^71` external
   computational input occurs in this RL102 result.
7. **Distinct slopes.** The inherited RL83 result remains only
   `qQ>3R# log 2` in the distinct-slope branch.  No new physical upper
   resource was obtained, so no finite eliminability is claimed.

## 5. Frozen route decision

Freeze only the following narrow architectures:

- direct prefix/suffix use of `D|Q(W)` followed by reduction modulo the local
  equal-slope factor;
- ordinary rotation transport used as if it supplied new prefix content;
- strict-excursion packing using only scale-homogeneous physical ratios or
  the corrected RL20 narrow-lift cost.

Do **not** freeze RL101's raw-cylinder compression, physical representative
theorem, or its ordinary-`+1` physical excursion.  They remain inherited
inputs awaiting an `s=1`-specific consumer.

The deferred raw-`g=1` cascade remains paused at the RL101-repaired state.

## 6. Verification

The portable local verifier ran successfully:

- `python3 verification/verify_rl102_prefix_suffix_and_excursion.py`

It performs 81,792 exact word/split algebra checks through length 12,
72 exact owned prefix/suffix closure checks, and reconstructs the deterministic
primitive generalized-increment witness with all asserted inequalities.

No historical expensive certificate was rerun under the verification-economy
rule.
