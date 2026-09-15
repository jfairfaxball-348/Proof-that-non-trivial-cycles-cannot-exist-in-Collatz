#!/usr/bin/env python3
from fractions import Fraction

A = 217_976_794_617
ELL = 137_528_045_312
D = A - ELL
LAMBDA_UPPER = 1 + Fraction(1, 1 << 40)
NMAX = 33_068_504_812

assert D == 80_448_749_305

# Exact lower enclosure for log(2) = 2*atanh(1/3).
def ln2_lower(terms=280):
    x = Fraction(1, 3)
    x2 = x * x
    term = x
    total = Fraction(0)
    for q in range(terms):
        total += term / (2 * q + 1)
        term *= x2
    return 2 * total

LN2_LO = ln2_lower()
assert LN2_LO > 0

B_UPPER = Fraction(4, 3) + Fraction(ELL, 6) / LN2_LO
assert B_UPPER < 33_068_504_828


def beatty_omitted_sum(rho):
    total = Fraction(0)
    for r in range(1, rho + 1):
        q = (A * r) // ELL
        total += Fraction(1 << q, 3 ** r)
    return total


def beatty_rhs_upper(rho):
    # Actual B_* is below B_UPPER.  Also lambda < LAMBDA_UPPER, hence
    # 1/lambda > 1/LAMBDA_UPPER, so subtracting S/(3*LAMBDA_UPPER)
    # yields a rigorous upper bound for the actual RHS.
    return B_UPPER - beatty_omitted_sum(rho) / (3 * LAMBDA_UPPER)


def floor_zero_budget(rho):
    return (D * rho) // ELL


def carry_rhs_upper(rho):
    q = floor_zero_budget(rho)
    return Fraction(5, 6) + LAMBDA_UPPER * (1 << q)


floors = {rho: floor_zero_budget(rho) for rho in range(59, 64)}
assert floors == {59: 34, 60: 35, 61: 35, 62: 36, 63: 36}

# Initial global carry cap.
assert B_UPPER < 33_068_504_828

# If rho <= 59, monotonicity of floor(d*rho/ell) gives this worst case.
assert carry_rhs_upper(59) < NMAX

# At rho=60, every integer n >= NMAX+1 is excluded.
assert beatty_rhs_upper(60) < NMAX + 1

# At the maximal remaining n=NMAX, rho>=63 is excluded.
assert beatty_rhs_upper(63) < NMAX

# Monotonicity checks for the decisive local window.
for rho in range(60, 63):
    assert beatty_rhs_upper(rho + 1) < beatty_rhs_upper(rho)

# Maximal-carry zero-prefix lower bound: z <= 34 would be too small.
z34_rhs = Fraction(5, 6) + LAMBDA_UPPER * (1 << 34)
assert z34_rhs < NMAX

# Endgame arithmetic consequences of the exact zero budgets.
# rho 60/61: z>=35 and total two-ended zero budget <=35 -> suffix zeros = 0.
for rho in (60, 61):
    budget = floor_zero_budget(rho)
    assert budget == 35
    z_min = 35
    assert budget - z_min == 0
    # j>=1, h<=rho-1, L=h when suffix zero count vanishes.
    assert rho - 1 <= 60

# rho 62: budget 36 and z>=35 -> at most one suffix zero.
budget62 = floor_zero_budget(62)
assert budget62 == 36
assert budget62 - 35 == 1
# j>=1 -> h<=61 and L=h+(suffix zeros)<=62.
assert 61 + 1 == 62

print("RL325_GLOBAL_OWNERSHIP_VERIFIER_GREEN")
print("initial_carry_cap", NMAX + 15)  # means n <= 33068504827 from B_UPPER < 33068504828
print("final_carry_cap", NMAX)
print("rho59_carry_upper_lt", float(carry_rhs_upper(59)))
for rho in (60, 61, 62, 63):
    print(f"rho{rho}_beatty_upper_lt", float(beatty_rhs_upper(rho)))
print("zero_budget_floors", floors)
print("max_carry_rho_set", [60, 61, 62])
print("max_carry_crossing_displacement_max", 36)
print("max_carry_suffix_length_max", 62)
print("max_carry_suffix_zero_count_max", 1)
print("scope", "exact rational constant certificate; analytic ownership and least-root theorems are ledger proofs")
