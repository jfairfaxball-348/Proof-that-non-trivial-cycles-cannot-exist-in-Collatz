#!/usr/bin/env python3
from math import ceil

P = 114_208_327_604
Q = 72_057_431_991
DELTA0 = 13_201_833_154_443_526_323
Z = 40_249_491_324_522_944
DJ = 930_959
B_RETURN = 43_234_459_194

# Exact inherited log certificate from RL86.
assert pow(3, 1_000_000) < pow(2, 1_584_963)
assert 400_000_000_000 < pow(2, 39)

# If M < 400e9*(3/2)^Q, then log2 M is strictly below this rational.
U_NUM = 39_000_000 + 584_963 * Q
U_DEN = 1_000_000
C_BLOCK = U_NUM // U_DEN  # U is nonintegral, so n < U implies n <= floor(U).
assert U_NUM % U_DEN != 0
assert C_BLOCK == 42_150_931_628

# RL73 giant low-k block is far too long under the first-Farey physical cap.
assert Z > C_BLOCK
assert Z // C_BLOCK == 954_889

# Generalized RL73 count splice for arbitrary Gate-A violation H<k.
def ceil_div(a: int, b: int) -> int:
    return -(-a // b)

def block_zero_lower(k: int) -> int:
    # Lower bound on 00s in one maximal height-one synchronized block
    # from the RL73 global skew/count identities and e,H <= k-1.
    return ceil_div(DELTA0 - 5*k + 7, 2*(k-1))

assert block_zero_lower(165) == Z

# Necessary k threshold after every physical synchronized block is capped by C_BLOCK.
K_MIN_RAW = ceil_div(DELTA0 + 2*C_BLOCK + 7, 2*C_BLOCK + 5)
assert K_MIN_RAW == 156_601_916
K_MIN_ODD = K_MIN_RAW if K_MIN_RAW % 2 else K_MIN_RAW + 1
assert K_MIN_ODD == 156_601_917
assert block_zero_lower(K_MIN_ODD - 2) > C_BLOCK
assert block_zero_lower(K_MIN_ODD) <= C_BLOCK

# RL81 terminal physical state B_j = 2^(k-2) N, with inherited N >= 2^71.
# Thus 2^(k+69) <= M < 2^U.
K_MAX = C_BLOCK - 69
assert K_MAX == 42_150_931_559
assert K_MAX % 2 == 1
assert K_MIN_ODD <= K_MAX

# Elementary quotient-fiber / range packing audit.
# Distinct J values in the physical box can only force a linear span.
SPAN_FROM_DJ = ceil_div(DJ - 1, 4)
assert SPAN_FROM_DJ == 232_740

# Check the fixed-J feasible interval formula and multiplicity bound exhaustively on small boxes.
def feasible_As(R: int, M: int, J: int):
    return [A for A in range(R, M+1)
            if R <= 3*A + 1 - J <= M]

def formula_interval(R: int, M: int, J: int):
    lo = max(R, ceil_div(J + R - 1, 3))
    hi = min(M, (J + M - 1)//3)
    return [] if lo > hi else list(range(lo, hi+1))

checks = 0
for R in range(1, 12):
    for M in range(R, 18):
        for J in range(3*R-M-4, 3*M-R+6):
            a = feasible_As(R, M, J)
            b = formula_interval(R, M, J)
            assert a == b
            assert len(a) <= (M-R)//3 + 1
            checks += 1

# Difference-law arithmetic checks.  For any synchronized word of length n
# with s odd/11 columns, delta_n = 3^s delta_0 / 2^n.
# Choosing delta_0 = 2^n*m makes integrality explicit; m odd gives odd exit delta.
diff_checks = 0
for n in range(1, 18):
    for s in range(n+1):
        for m in (-9, -5, -1, 1, 3, 7):
            d0 = (1 << n) * m
            dn_num = pow(3, s) * d0
            assert dn_num % (1 << n) == 0
            dn = dn_num // (1 << n)
            assert dn == pow(3, s) * m
            assert dn % 2 != 0
            diff_checks += 1

print('RL87 physical-difference packing verifier: PASS')
print(f'first Farey pair = ({P}, {Q})')
print(f'log exponent upper numerator/denominator = {U_NUM}/{U_DEN}')
print(f'physical synchronized-block length <= {C_BLOCK}')
print(f'RL73 low-k giant 00 count = {Z}')
print(f'giant/block-cap integer ratio = {Z // C_BLOCK}')
print(f'first-Farey Gate-A necessary raw k >= {K_MIN_RAW}')
print(f'first-Farey Gate-A necessary odd k >= {K_MIN_ODD}')
print(f'first-Farey terminal physical k <= {K_MAX}')
print(f'quotient-only D_J span floor = {SPAN_FROM_DJ}')
print(f'finite-fiber interval checks = {checks}')
print(f'difference-law arithmetic checks = {diff_checks}')
