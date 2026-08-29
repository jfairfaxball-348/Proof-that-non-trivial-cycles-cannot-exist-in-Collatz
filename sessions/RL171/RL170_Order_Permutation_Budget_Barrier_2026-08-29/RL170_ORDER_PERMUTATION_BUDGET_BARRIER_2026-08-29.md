# RL170 — order-permutation budget barrier

Date: 2026-08-29

## Outcome and classification

RL170 tests a genuinely non-chain use of the permutation from chronological
phase order to lifted-defect/state order. It derives an exact full-orbit sum
budget and proves that the entire possible odd-rank contribution is strictly
smaller than the available least-state slack. This direct permutation-budget
route cannot restrict the defect distribution.

New results:

1. **RL170.1 — non-chain order-permutation budget** (analytic, ordinary
   `+1`, physical coprime `g=1` first-survivor least-root scope).
2. **RL170.2 — universal rank-budget slack barrier** (analytic, conditional
   on inherited external `m>=2^71`).

No cycle is constructed or excluded. This is not an individual rank bound,
a monotone chain argument, a count/product argument, a local cylinder, or a
rank-one closure claim.

## 1. Exact full-orbit chronological sum

Let `z_j=q_jy_j`, retaining RL168's defect-value order and ranks

`r_j=#{k:E_k<E_j}`.

The exact ordinary increment `z_(j+1)-z_j=q_j/3` gives

`sum_(j<L) z_j`
` = Lm+(1/3)sum_(i=0)^(L-1)(L-1-i)q_i`.                    (1.1)

The coefficient at `i=L-1` is zero. Unlike RL169, (1.1) sums all
chronological phases and is sensitive to the complete order permutation.

RL168 orders the physical values by `E`, so all states below `y_j` are
distinct odd integers at least `m`. Hence

`y_j>=m+2r_j`.                                              (1.2)

Multiplying by positive `q_j` and summing gives the non-chain budget

`mQ+2R <= Lm+(1/3)sum_(i<L)(L-1-i)q_i`,                    (1.3)

where `Q=sum q_j=3(lambda-1)m` and `R=sum q_jr_j`.

## 2. RL170.2 — universal slack comparison

The ranks are a permutation of `0,...,L-1`. Every proper prefix obeys
`q_j<lambda`, while `q_0=1<lambda`; inherited `5theta<1` gives
`Delta<1/(5L)<1/2` and

`lambda-1=exp(Delta)-1 <2Delta<2/(5L)<1`.                  (2.1)

Thus `lambda<2`, and therefore

`R < 2 sum_(r=0)^(L-1)r = L(L-1)`,

so

`2R<2L(L-1)`.                                               (2.2)

On the right-hand side of (1.3), discard the nonnegative chronological
sum. Using the exact full-cycle mass,

`Lm-mQ=m[L-3(lambda-1)]`.

Since `3(lambda-1)<6/(5L)<1`, this is strictly larger than

`m(L-1)`.                                                   (2.3)

Under the inherited external floor, `m>=2^71>2L` because `L<2^38`.
Consequently

`Lm-mQ>m(L-1)>2L(L-1)>2R`.                                 (2.4)

### Theorem RL170.2

Even before adding the nonnegative chronological term in (1.3), the
least-state slack exceeds the largest possible complete order-permutation
rank contribution. Therefore the full-sum inequality (1.3) cannot force a
contradiction or a phase-distribution restriction in the external-floor
branch.

This proves only that the stated global rearrangement/rank-budget comparison
is slack. It does not supply a realizable countermodel or rule out a future
non-chain relation with additional arithmetic information.

## 3. Exact audit and red teams

`RL170_CERTIFICATES/verify_order_permutation_budget.py` re-certifies
`5theta<1`, the exact survivor and external-floor capacity comparisons, and
checks the exact full-orbit sum identity on 5,460 bounded ordinary
accelerated words with rational trajectories.

- **Ordinary increment:** PASS. The sum identity comes from the actual `+1`
  recurrence.
- **Non-chain scope:** PASS. The rank term is summed over the entire order
  permutation; no monotone chronological chain is selected.
- **Physical order:** PASS. Odd-state packing is used only after RL168's
  physical total order.
- **External qualification:** PASS. Only the slack comparison uses inherited
  external `m>=2^71`.
- **No false closure:** PASS. No cycle model, dense closure discharge, or
  global exclusion is claimed.

## 4. Next target

Seek an additional arithmetic correlation between chronological positions and
defect ranks that is not bounded merely by the universal rank sum. Preserve
the existing ordinary, physical, `g=1`, external-floor, and method-barrier
scope limits.
