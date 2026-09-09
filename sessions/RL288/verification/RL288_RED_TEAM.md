# RL288 proof-state / scope red team

Result: **PASS**

## Scope audit

- RL288 does not claim Gate A is closed.
- Exact residual remains `k>=25`, `k` odd, `H_can<k`.
- Gate B remains separate/open/frozen.
- Fifth selector remains unscanned.
- Radius 6+ remains frozen.
- No global non-trivial-cycle exclusion is claimed.

## Incoming integrity

- Base head: `71feeb7b91772637a88ac4a9a34bc365f55f7f25`.
- Incoming target blob: `db50b0d082a6f66b8a6c5bddd5afb97e347a2836`.
- Incoming START_HERE blob: `f76505d8ab5aa3004bf07126ce91a9bc624f8127`.
- RL287 verifier/red-team state was clean at RL288 startup.

## Claim audit

The following frozen claims are analytic and appropriately scoped:

1. first-positive entry `0<M<3^d` and `nu_2(M)<=A`, unique equality `(3,2,1)`;
2. positive `M`-magnitude safety can first fail only on boundary `11`;
3. arbitrary valuation-safe reverse boundary-`00` rays exist and block naive globalization of the conditional ancestor sieve;
4. corrected shifted coordinate `T=K+1-3^d` has the displayed exact recurrences, and `T`-magnitude safety has the same unique boundary escape architecture;
5. pairing `M,T` reproduces the inherited two-template boundary hazard rather than closing a finite shifted-valuation induction;
6. for common seed `-7`, first deviation of `w` from `(101)^infinity` at `s` gives `nu_2(U_w)=s`;
7. canonical paired shadows have synchronized first-deviation position because `3^d U_x-U_y` is divisible by the full `2^n` prefix denominator;
8. the synchronized departure gives exactly boundary states `J=-6,-28,-4` and forced off-boundary roots `(2,-6,0),(2,-39,0),(2,-3,0)`;
9. fixed individual shifts `U_w+c2^n` cannot change the common departure valuation after `n>s`.

## Corrections / demotions

One notation error is corrected:

`T=J+2^d-3^d=K+1-3^d`.

The session at one point informally wrote `K-3^d`. The four transition formulas used thereafter were correct; therefore this is a bookkeeping correction, not a theorem demotion.

The conditional mod-54 reverse sieve is **not promoted**. Its assumptions exclude harmless earlier magnitude escapes, and the exact reverse-00 ray theorem shows why it is not yet a global Gate-A contraction.

Finite `H<=22` observations about the shifted `T` candidate remain evidence only.

## Adversarial consistency

The promoted RL288 claims do not contradict RL287's local cylinder-isometry and low-height predecessor barriers:

- first-positive and common-seed synchronization theorems use complete ancestry from the fixed seed;
- reverse-00 families are explicitly local barriers, not claims of global reachability;
- the common-shadow theorem restricts paired fixed-seed histories rather than arbitrary suffix lifts.

The paired-phase barrier is consistent with RL283's already retained two-template boundary hazard and finite shifted-valuation barrier.

## Verifier

`verify_rl288_fixed_seed.py` passes and checks 39,165 legal transitions / two-shadow identities, 39,166 prefixes including the empty prefix, exact first-deviation synchronization through length 16, the three departure states and roots, the first-positive equality witness, explicit reverse-00 rays, and fixed-shift degeneracy samples.

The inherited RL285 multi-million-state `H<=22` finite certificate is intentionally not duplicated in the RL288 fast verifier.

## Conclusion

PASS. The frozen RL288 classification is accurate, scope is preserved, conditional/finite material is correctly demoted or labelled, and RL289 may inherit the normalized joint common-seed shadow-pair target.
