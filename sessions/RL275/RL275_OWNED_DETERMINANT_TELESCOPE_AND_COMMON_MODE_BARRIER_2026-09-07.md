# RL275 — owned determinant telescope and common-mode barrier

Date: 2026-09-07

## Classification

Primary:
`OWNED_DISCREPANCY_COMPRESSION_IDENTIFIED`

Companion:
`GATE_A_EXACT_BARRIER`

Gate A is **not** proved. Gate B is not changed. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## 1. Exact Gate-A scope recovered before new work

RL275 was explicitly activated by the user after RL274.

The frozen uniform target is the exact canonical terminal inequality

`H_can >= k=t+3`

for a retained genuine full-phase object, where the internal canonical recurrence starts at

`(d,J)=(1,-13)`,

ends before the omitted terminal `(1,0)` at

`d=1, J=2^k`,

and canonical area is

`H_can = sum_i (d_i-1)`.

Equivalently, the terminal target is `v2(J)<=H_can`.

This is distinct from the arithmetic selector quantity historically also denoted by `H`; in the RL253--RL262 determinant-2 selector that quantity is

`H_sel = 19z-7a`.

RL275 keeps these names separate.

Inherited exact facts used below include:

- RL65: `H_can=sum_j delta_j` for ordered rank displacements `delta_j>=0`;
- RL66: terminal `k` is odd;
- RL243: for the determinant-2 half-word selector, with `ar-q ell=2`, the auxiliary flows
  `P_i=r-W_i^u(q)` and `Q_i=r-W_i^v(q)` satisfy
  `Q_i-P_i=h_i-h_(i+q)` for the owned full-phase height profile `h`;
- RL274: the general determinant/discrepancy identity.

No finite selector elimination is upgraded to a uniform theorem.

## 2. RL274 determinant identity specialized to the owned half-pair

Let `u,v` be binary half-words of common length `a` and common weight `ell`. Put

`z=a-ell`.

Fix the inherited determinant-2 selected shift `q` and normalization `r`:

`ar-q ell = 2`.

Define

`P_i = r-W_i^u(q)`,
`Q_i = r-W_i^v(q)`,

where `W_i^w(q)` counts ones in the cyclic length-`q` window of `w` starting at `i`.

Choose integers `c,d0` and put

`S = d0 z-c a`,
`B = q-r`,
`n0 = d0 B-c q`.

Assume

`0<S<a/gcd(a,q)`.

RL274, with determinant `kappa=2`, gives separately

`Z_(2d0)^u(s) = 2c + sum_(j=0)^(S-1) P_(s+jq)`,

`Z_(2d0)^v(s) = 2c + sum_(j=0)^(S-1) Q_(s+jq)`.

Here `Z_L^w(s)` is the cyclic zero count in the length-`L` window of `w` starting at `s`.

## 3. New exact paired determinant telescope

Subtract the two RL274 identities and use the inherited owned-height derivative:

`Q_i-P_i=h_i-h_(i+q)`.

Then

`Z_(2d0)^v(s)-Z_(2d0)^u(s)`
` = sum_(j=0)^(S-1) (Q-P)_(s+jq)`
` = sum_(j=0)^(S-1) (h_(s+jq)-h_(s+(j+1)q))`
` = h_s-h_(s+Sq)`.

The determinant relation is

`Sq=n0 a+2d0`,

so cyclically

`boxed: Z_(2d0)^v(s)-Z_(2d0)^u(s)=h_s-h_(s+2d0)`.

Classification: **analytic theorem**.

This is an exact compression: the difference of two potentially long resonant determinant sums collapses to two owned endpoint heights.

## 4. The crucial red team: the compression is a tautological differential identity

The same formula follows without the determinant machinery at all.

The full-phase height derivative is exactly the bit imbalance

`h_(i+1)-h_i = v_i-u_i`

(up to the inherited harmless global height-offset convention). Therefore

`Z_L^v(s)-Z_L^u(s)`
` = sum_(j=0)^(L-1) (u_(s+j)-v_(s+j))`
` = h_s-h_(s+L)`.

Taking `L=2d0` reproduces the boxed theorem identically.

Therefore the new paired determinant telescope is **not an independent Gate-A restriction**. It identifies precisely why the most obvious attempt to combine RL274 with the RL243 ownership derivative fails: subtracting the two half-word discrepancy identities merely recovers the pre-existing height telescope.

This is analogous in spirit to the RL263 ordered-prefix barrier: a promising-looking congruence/discrepancy coupling becomes an identity on genuine physical data.

Classification: **exact method barrier**.

## 5. Differential mode versus common mode

The inherited relation

`Q-P=h-h_shift`

controls only the **difference** of the two selected discrepancy flows.

Write informally

- differential mode: `Q-P`;
- common mode: any shared component carried by both `P` and `Q`.

Canonical area and owned height constrain the differential mode. The paired determinant telescope also sees only that differential mode.

But the one-sided counterflow required by the RL274 successor logic is a statement about `beta(P)` itself, for example the useful contradiction

`beta(P)>z-k+4`

against the inherited zero-budget ceiling.

No inequality for `beta(P)` follows from the paired telescope alone, because shared negative mass can sit in `P` and `Q` while cancelling completely from `Q-P`.

Thus RL275 identifies the exact missing type of theorem:

> a **one-sided absolute ownership consumer**, not another identity obtained by subtracting the two half-word equations.

It must use information not invariant under common-mode changes, such as the absolute canonical `(T,J)` state, the full-phase quotient `N`, chronological owned recurrence, or another genuinely absolute physical datum.

## 6. Infinite arithmetic/window stress family for the common-mode kernel

The following family is **not** claimed to satisfy the canonical full-phase recurrence. It is a method-barrier family showing that the determinant/resonance/window algebra itself allows unbounded shared counterflow.

For every integer `n>=5`, set

`a=16n+4`,
`ell=10n+3`,
`z=6n+1`,
`q=8n-2`,
`r=5n-1`.

Then exactly

`ar-q ell=2`,

`12a-19ell=2n-9>0`,

`8ell-5a=4>0`,

so

`19/12<a/ell<8/5`.

Also

`H_sel=19z-7a=2n-9>0`,

and `gcd(a,q)|8`, hence the RL274 distinct-sample condition for the `(c,d0)=(7,19)` selector is satisfied.

Take the common clustered word

`u=v=1^ell 0^z`.

Then the height difference is constant and `P=Q`; nevertheless the selected counterflow is unbounded. A direct cyclic-window count gives

`beta(P)=beta(Q)=(5n+4)(3n-1)=15n^2+7n-4`.

Indeed a length-`q` window wholly inside the one-block occurs `ell-q+1=2n+6` times and contributes deficit `q-r=3n-1`; every intermediate excess `1,...,3n-2` occurs twice. Summing gives the displayed formula.

Classification: **analytic stress family for the algebraic method only**.

It is not a Collatz/full-phase counterexample and must never be used as one. Its purpose is narrower: determinant-2 arithmetic, the retained resonance interval, cyclic-window realizability, and zero differential height do not by themselves control the common counterflow.

## 7. Fixed full-word-form finite stress test

The portable RL275 verifier also tests a stronger finite red team that respects the exact fixed half-word shape

`u=110 x 1 0^t`,
`v=111 x 0^(t+1)`

with `k=5`, `t=2`, and `x=y`, hence zero internal rank displacement and word-level `H_can=0`.

Across `5<=n<=300` using a balanced mechanical internal word, the exact selected flows remain in `{-1,0,1}` and satisfy

`beta(P)=3n`,
`beta(Q)=3n+3`.

For this stress family `z-k+4=6n`, so the coarse one-sided zero-budget ceiling is not violated by `P`.

This is **finite verifier evidence only**, not an infinite theorem and not a full-phase/canonical witness. In particular it deliberately omits the absolute canonical `J` recurrence and full-`D` phase quotient, which are precisely the data RL275 concludes must be consumed next.

## 8. Why this does not revive rejected routes

RL275 does not claim:

- that low canonical area bounds synchronized pumping depth;
- that the paired height telescope is a new congruence;
- that the stress families are canonical/full-phase objects;
- that a finite verifier proves Gate A;
- that the fifth selector is eliminated;
- that Radius 6 or another bounded radius is useful.

The RL66 zero-displacement pumping barrier, RL263 physical-telescope barrier, RL264 affine-ray barrier, and all correction/demotion ledgers remain binding.

## 9. Exact state after RL275

Gate A remains the odd-`k` uniform theorem

`H_can>=k`.

RL275 rules out one tempting route:

`RL274 determinant discrepancy`
` + paired u/v subtraction`
` + owned-height derivative`

because it collapses to the ordinary height telescope.

The surviving target is one-sided and absolute. A useful theorem must constrain at least one of

- `beta(P)` itself rather than `Q-P`;
- the full-phase quotient `N` in an Archimedean/order-sensitive way;
- an absolute canonical `(d,T,J,H_can)` state along a chronological owned recurrence;
- a repeated owned structure whose contribution does not cancel between the two halves.

## 10. Recommended successor

RL276 should attack a **one-sided absolute ownership consumer** in this order:

1. combine the RL65/RL66 ordered phase-digit ladder with RL241's finite carry decomposition of the full-phase quotient, seeking a true size/order restriction on `N`, not CRT compatibility alone;
2. test whether the frozen RL231--RL237 chronological owned-defect/recurrence machinery supplies such a one-sided consumer, preserving every stop-and-repair demotion and its known saturation boundary;
3. use the fifth arithmetic selector only as a controlled falsification/test bed if a proposed absolute theorem needs examples;
4. do not start Radius 6+;
5. do not promote any statement invariant under common-mode addition as a Gate-A closure mechanism.

A strong RL276 result would prove `H_can>=k`, or force `beta(P)>z-k+4`, or derive an impossible full-phase quotient range. A meaningful partial result would isolate an exact one-sided recurrence/quotient inequality that is not another physical telescope.
