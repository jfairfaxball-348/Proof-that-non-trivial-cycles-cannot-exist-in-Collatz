# RL48 Research Progress

Date: 2026-08-22

## Executive result

RL48 does **not** close RL, but it makes a substantial structural advance on both remaining gates.

1. **Gate A limitation theorem:** the RL47 separable rank-envelope relaxation is now proved incapable of excluding any candidate with terminal zero count `z=q-t>=42`.  Therefore the requested uniform theorem cannot be obtained by merely sharpening constants in that relaxation; a new coupling invariant for synchronized height-one motion is mathematically necessary.
2. **Gate B same-root selector:** the `f,L` common root modulo `M=2^a-3^ell` is explicit and unique because `gcd(q,ell)=1`.  This removes the different-root ambiguity without a global resultant.
3. **Phase collapse:** at that canonical root, the RL45 phase polynomial satisfies the exact identity
   `P(rho)=4+Q(v)/3^ell (mod M)`.
   Thus the full phase condition is equivalent to the scalar divisibility
   `M | Q(v)+4*3^ell`.
4. **Rank-defect bridge candidate:** conditional on the standard general word reconstruction `v=111 y 0^(t+1)` (which must be checked against the missing RL43/RL44 source), the phase condition becomes
   `12D + 2^(a-t-2) = 237*3^(ell-3) (mod M)`,
   where
   `D=sum_{delta_j>0} 3^(r-j)2^b_j(2^delta_j-1)`
   and `sum delta_j=H`.  Under a hypothetical strict violation, `D` has at most `t+2` active ranks.

This replaces the previously vague “three-polynomial same-root subresultant” target by one explicit displacement congruence.

## Verification baseline

- outer bundle checksum: PASS;
- all internal `SHA256SUMS.txt`: PASS;
- `verification/run_rl47_core_verifiers.sh`: PASS;
- full q134 stress suite `t=2,4,...,16`: PASS, including independent rerun of `t=16` with `hit 0`;
- all three new RL48 progress verifiers: PASS.

The known Boost/GCC aggressive-loop warning appears during q134 compilation exactly as documented in RL47; logical output is unchanged.

## New analytic theorem A — barrier for the RL47 rank relaxation

Write `C=(3/8)zeta^2`.  For the first 72 ranks, if `z=q-t>=42`, the coordinate cap rather than terminal room controls the RL47 envelope.  Each such synchronized baseline weight is `>C/2`; the baseline therefore contributes `>72C`.  The strict-violation displacement budget has at least four units (`t+2>=4`), whose first marginals add `>C` in the enlarged concave maximization.  Hence

`relaxed_max > 73C = (219/8)zeta^2`.

But for `k=t+3>=5`,

`terminal_target <= 14+(837/64)zeta`,

and the difference is already `19/64>0` at `zeta=1` and grows thereafter.  Therefore the enlarged RL47 relaxation lies above the target whenever `z>=42` and cannot certify exclusion.

**Interpretation:** Gate A now has a proved method barrier.  The missing theorem must control the mass of synchronized height-one ranks, not just their independent prefix caps and total displacement.

## New analytic theorem B — canonical same root

Let

`f(T)=3T^q-2`, `L(T)=2T^ell-1`, `M=2^a-3^ell`, `a=q+ell`, `gcd(q,ell)=1`.

Choose Bezout integers `u,v` with `uq+vell=1` and define in `R=Z/MZ`

`rho=(2/3)^u (1/2)^v`.

Because `2^a=3^ell (mod M)`, one has `(2/3)^ell=(1/2)^q`, from which

`rho^q=2/3`, `rho^ell=1/2`.

Thus `f(rho)=L(rho)=0`.  Uniqueness follows because the ratio of any two common roots has both q-th and ell-th power 1, and Bezout forces that ratio to be 1.

This is valid modulo the full composite `M`, so the selected root is automatically compatible with every prime-power factor of `M`.

## New analytic theorem C — phase scalar

For each run `(t,m,k)` in the RL45 phase word,

`3(rho^b-rho^(b+kq)) = 2^t(3^k-2^k)/3^(m+k-1)`.

Summing over runs gives exactly the standard normalized word polynomial:

`P(rho)=4+Q(v)/3^ell (mod M)`.

Therefore the full phase condition is equivalent to

`M | Q(v)+4*3^ell`.

On the audited `(65,41)` proper-factor countermodel, the verifier finds

`P(rho) mod M = 401307695918737978`,

with gcd 1 against `M`, so the countermodel is rejected by the same-root scalar exactly as expected.

## Candidate Gate-B compression into rank displacement

Assuming the general word reconstruction `v=111 y 0^(t+1)`, let

`Qx=sum 2^a_j3^(r-j)`, `Qy=sum 2^b_j3^(r-j)`, `D=Qx-Qy`.

RL47's exact terminal identity gives

`2Qy+3D = 14*3^r + 2^(a-1)-2^(a-k-1)`.

The reconstructed full word gives

`Q(v)=19*3^r+8Qy`.

Combining yields

`Q(v)=75*3^r+2^(a+1)-2^(a-k+1)-12D`.

The same-root phase scalar then becomes

`12D+2^(a-t-2) = 237*3^(ell-3) (mod 2^a-3^ell)`.

Under a strict violation,

`D=sum_{delta_j>0}3^(r-j)2^b_j(2^delta_j-1)`,

with at most `t+2` active ranks and total displacement `sum delta_j<=t+2`.

This is the most concrete radius-3 bridge target currently available.

## Exact proof-state update

### Analytic, unconditional from material in the RL47->RL48 bundle

- all inherited RL47 analytic facts;
- RL48 barrier theorem for the existing separable rank relaxation;
- canonical unique `f,L` common root in `Z/MZ`;
- exact phase collapse `P(rho)=4+Q(v)/3^ell` for the RL45 phase-word/run definition.

### Analytic but historical-definition audit pending

- the general `v=111 y 0^(t+1)` reconstruction for arbitrary terminal suffix `t`;
- the resulting defect congruence
  `12D+2^(a-t-2) = 237*3^(ell-3) (mod M)`.

The algebra after that reconstruction is exact and is verified on both the inherited t=0 countermodel and the audited RL47 t=2 witness.

### Exact finite certificates

- all inherited RL47 certificates;
- q134 low-t stress suite through `t=16` rerun successfully in RL48.

### Still open

- uniform Gate A theorem `H>=t+3`;
- the new coupling invariant needed for `z>=42` (and generally the low/moderate-t region);
- exact audit of the general phase-word reconstruction from RL43/RL44;
- matching the explicit defect congruence to the exact audited radius-3 theorem;
- global RL closure.

## Recommended next attack

The next highest-value step is **not** more q134 computation.  It is to obtain the RL43/RL44 radius-3/phase provenance and audit two exact statements:

1. confirm the general full phase word is `v=111 y 0^(t+1)` (or correct the constants if not);
2. translate the audited radius-3 theorem into the defect congruence variables above.

In parallel, Gate A needs a synchronized-height-one mass identity/potential.  The barrier theorem shows that no proof using only independent cap/room bounds plus total displacement can succeed for `z>=42`.
