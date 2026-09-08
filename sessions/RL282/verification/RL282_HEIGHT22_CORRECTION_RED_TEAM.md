# RL282 H<=22 correction red team

Date: 2026-09-08
Verdict: **PASS**

## Questions checked

### 1. Is the promoted claim finite and explicitly capped?

Yes. The only new promoted certificate is `H<=22`. No claim is made for `H>=23`.

### 2. Is the state search gap-free inside the cap?

Yes.

The pre-positive phase is exhaustive BFS from `(1,-13,0)` over every legal exact normalized transition that remains within `H<=22`.

After first entry to positive `d=1`, all paths are transferred to the positive checkpoint automaton.

From a positive even checkpoint, every exact first return within the remaining height cap is enumerated. Between launch and first return, `d>=2`, hence each interior step adds at least one height unit; there is no hidden infinite zero-height interior and no arbitrary word-length truncation.

Positive odd boundary continuations are exact macro-closures: one branch exits even, the other stays odd. The verifier follows the unique stay-odd branch until exact repetition and records every even exit. It uses no orbit-length cutoff. All `13,583` encountered odd origins terminate by repetition, with maximum trace `263`.

### 3. Is there an arbitrary J cutoff?

No.

### 4. Are negative/nonpositive branches incorrectly discarded after positivity?

No. A branch is stopped in Phase A only at its first positive `d=1` state, which is then seeded into Phase B. The positive automaton enumerates subsequent excursions exactly within the cap. The verifier asserts that all first returns encountered from positive checkpoints remain positive.

### 5. Does the certificate really close odd k=5..23?

Yes.

Exact minima are:

`k5:H9, k7:H15, k9:H15, k11:H18, k13:H18, k15:H22`.

No `2^17,2^19,2^21,2^23` terminal occurs at all for `H<=22`.

For any `k<=23`, a Gate-A violation has integer `H<k`, so `H<=22`; therefore the complete cap covers every possible violator in this exponent range.

### 6. Is the residual allowed to become k>=25?

Yes, using inherited authoritative results:

- terminal `k` is odd;
- `k=3` is already Gate-A safe.

Thus after closing odd `5<=k<=23`, the first remaining possible terminal exponent is odd `k=25`.

### 7. Is H<=26 being silently promoted?

No. The earlier `H=23..26` exploration remains evidence only.

### 8. Does this correction claim a uniform valuation invariant?

No. `nu_2(J)<=H` and `J<=2^H` remain unproved candidate invariants.

### 9. Does this undermine RL282's local-tail barrier?

No. The finite certificate and the analytic barrier are compatible. The certificate constrains globally reachable checkpoints in a finite height range; the barrier says final positive tail arithmetic alone is insufficient for a uniform proof.

## Red-team conclusion

`HEIGHT_22_POSITIVE_CHECKPOINT_AUTOMATON_CERTIFIED` and
`K5_TO_K23_GATE_A_CASES_CLOSED_CERTIFIED`

are correctly classified exact finite certificates.

The corrected authoritative Gate-A residual is

`k>=25`, `k` odd, `H_can<k`.

No correction or demotion of the analytic RL282 theorem set is required.
