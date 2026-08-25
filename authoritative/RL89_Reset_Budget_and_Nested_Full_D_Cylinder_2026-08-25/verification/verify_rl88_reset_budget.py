#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

# Frozen RL73/RL87 constants.
DELTA0 = 13_201_833_154_443_526_323
C = 42_150_931_628
LOGM_UP = Fraction(42_150_931_628_751_333, 1_000_000)
OLD_ODD_K = 156_601_917
EXPECTED_RAW_K = 2_921_384_818
EXPECTED_ODD_K = 2_921_384_819
EXPECTED_Q_AT_ODD = 123_139_091_657_887_804_990
EXPECTED_GOOD_D23 = 225_242_372
EXPECTED_PAIR_REPEAT = 7


def ceil_frac(x: Fraction) -> int:
    return -(-x.numerator // x.denominator)

# Exact atanh logarithm intervals, same audited method used by RL73/RL49.
def log_interval_int(x: int, terms: int = 260):
    y = Fraction(x - 1, x + 1)
    y2 = y * y
    s = Fraction(0)
    yp = y
    for n in range(terms):
        s += yp / (2 * n + 1)
        yp *= y2
    lo = 2 * s
    tail = 2 * yp / ((2 * terms + 1) * (1 - y2))
    return lo, lo + tail

l2, u2 = log_interval_int(2)
l3, u3 = log_interval_int(3)
beta_lo, beta_hi = l3 / u2, u3 / l2
assert beta_lo < beta_hi
assert beta_lo > Fraction(3, 2)
GAMMA = 2 * beta_hi - 3
assert GAMMA > 0

# Shortcut map and exact (d,T) reset laws.
def shortcut(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

checks = 0
for d in range(1, 6):
    for A in range(2, 80):
        for B in range(2, 80):
            x, y = A & 1, B & 1
            A1, B1 = shortcut(A), shortcut(B)
            d1 = d + y - x
            if d1 < 0:
                continue
            T = 3**d * A - B
            T1 = 3**d1 * A1 - B1
            rhs = (3**y * T + x * 3**(d + y - x) - y) // 2
            assert T1 == rhs
            checks += 1

# Affine word constants: F_w(z)=(3^r z+Q_w)/2^L.
def word_data(bits):
    q = 0
    r = 0
    for i, b in enumerate(bits):
        if b:
            q = 3 * q + (1 << i)
            r += 1
        # for b=0 q is unchanged
    return r, q

# The recurrence above needs the later odd multipliers on prior Q. Verify directly
# by a second recurrence that is applied in chronological order.
def word_data2(bits):
    q = 0
    r = 0
    for i, b in enumerate(bits):
        q = (3 if b else 1) * q + (1 << i if b else 0)
        r += b
    return r, q

for L in range(1, 8):
    for bits in product((0, 1), repeat=L):
        r, q = word_data2(bits)
        assert 0 <= q < (1 << L) * (3**r)
        for z in range(1, 25):
            num = 3**r * z + q
            # If z realizes the word, the affine formula agrees with iteration.
            a = z
            ok = True
            for b in bits:
                if (a & 1) != b:
                    ok = False
                    break
                a = shortcut(a)
            if ok:
                assert num == (1 << L) * a

# Complete height-one excursion algebra: start with 01, stay above height one,
# return for the first time by 10. Net x/y odd counts must agree.
excursions = 0
for L in range(2, 9):
    for cols in product(((0,0),(0,1),(1,0),(1,1)), repeat=L):
        if cols[0] != (0,1) or cols[-1] != (1,0):
            continue
        d = 1
        valid = True
        for j, (x,y) in enumerate(cols):
            d += y - x
            if j < L-1 and d <= 1:
                valid = False
                break
        if not valid or d != 1:
            continue
        xbits = tuple(c[0] for c in cols)
        ybits = tuple(c[1] for c in cols)
        rx, qx = word_data2(xbits)
        ry, qy = word_data2(ybits)
        assert rx == ry
        r = rx
        K = qy - qx
        assert abs(K) < (1 << L) * (3**r)
        excursions += 1

# Canonical full-phase physical entrance / midpoint-congruence identity spot checks.
midpoint_checks = 0
for N in range(3, 1000, 8):
    A = (9 * N + 5) // 8
    B = (27 * N + 127) // 8
    assert 8 * A == 9 * N + 5
    assert 8 * B == 27 * N + 127
    d = 1
    px = py = 0
    qx = qy = 0
    for i in range(24):
        if d == 1:
            assert px == py
            pwt = px
            lhs = (1 << (i + 2)) * (B - A)
            rhs = 3**pwt * (9 * N + 61) + 4 * (qy - qx)
            assert lhs == rhs
            midpoint_checks += 1
        x, y = A & 1, B & 1
        qx = (3 if x else 1) * qx + ((1 << i) if x else 0)
        qy = (3 if y else 1) * qy + ((1 << i) if y else 0)
        px += x
        py += y
        A, B = shortcut(A), shortcut(B)
        d = 1 + py - px

# Explicit ordinary-s=1 reset family: 01,10 can regenerate arbitrary valuation t.
# A common shift by 2^(t+2) preserves the whole tested parity cylinder.
reset_family_checks = 0
for t in range(1, 201):
    m = 1 if t & 1 else 5
    delta0 = (1 + (1 << (t + 2)) * m) // 3
    assert 3 * delta0 - 1 == (1 << (t + 2)) * m
    assert delta0 & 1 and delta0 % 4 == 3
    for h in (0, 1, 7):
        A = 2 + h * (1 << (t + 2))
        B = A + delta0
        assert (A & 1, B & 1) == (0, 1)
        A, B = shortcut(A), shortcut(B)
        assert (A & 1, B & 1) == (1, 0)
        A, B = shortcut(A), shortcut(B)
        assert B - A == (1 << t) * m
        for _ in range(t):
            assert (A & 1) == (B & 1)
            A, B = shortcut(A), shortcut(B)
        assert (B - A) & 1
        assert (A & 1) != (B & 1)
        reset_family_checks += 1

# Combined reset-budget necessary inequality.
# With beta replaced by the exact certified upper endpoint beta_hi, any survivor must satisfy
#   gamma*C*(k-1) + 3*LOGM_UP + (4*beta+3)*(k-1)
#       >= beta*(DELTA0-2*k+4).
def feasibility_margin(k: int) -> Fraction:
    return (
        GAMMA * C * (k - 1)
        + 3 * LOGM_UP
        + (4 * beta_hi + 3) * (k - 1)
        - beta_hi * (DELTA0 - 2 * k + 4)
    )

m0 = feasibility_margin(0)
slope = feasibility_margin(1) - m0
assert slope > 0
raw_k = ceil_frac(-m0 / slope)
assert raw_k == EXPECTED_RAW_K
assert feasibility_margin(raw_k - 1) < 0
assert feasibility_margin(raw_k) >= 0
odd_k = raw_k if raw_k & 1 else raw_k + 1
assert odd_k == EXPECTED_ODD_K
assert odd_k > OLD_ODD_K

# Certified aggregate block-length floor at the first surviving odd k.
def q_lower(k: int) -> int:
    numerator = (
        beta_hi * (DELTA0 - 2 * k + 4)
        - 3 * LOGM_UP
        - (4 * beta_hi + 3) * (k - 1)
    )
    return ceil_frac(numerator / GAMMA)

q0 = q_lower(odd_k)
assert q0 == EXPECTED_Q_AT_ODD
capacity = C * (odd_k - 1)
assert q0 <= capacity
blocks_min = (q0 + C - 1) // C
assert blocks_min == odd_k - 2
avg_floor = q0 // (odd_k - 1)
assert avg_floor == 42_150_931_605

# Near-capacity/cofactor pigeonhole at the new odd lower endpoint.
# Pad to k-1 slots. If deficit d=C-n <=23 then |m|<2^(d+1).
# There are at most sum_{d=0}^{23} 2^(d+1)=2^25-2 signed (d,m) pairs.
deficit = capacity - q0
bad_d23 = deficit // 24
good_d23 = (odd_k - 1) - bad_d23
assert good_d23 == EXPECTED_GOOD_D23
pair_types = (1 << 25) - 2
repeat = (good_d23 + pair_types - 1) // pair_types
assert repeat == EXPECTED_PAIR_REPEAT

print('RL88 reset-budget verifier: PASS')
print('exact d,T arithmetic checks =', checks)
print('complete excursion words checked =', excursions)
print('midpoint congruence identity checks =', midpoint_checks)
print('explicit arbitrary-reset family checks =', reset_family_checks)
assert beta_hi-beta_lo < Fraction(1, 10**150)
print('beta interval width < 1e-150')
print('raw first-Farey necessary k >=', raw_k)
print('odd first-Farey necessary k >=', odd_k)
print('first surviving odd-k aggregate block length >=', q0)
print('block capacity at that k =', capacity)
print('minimum number of nonempty blocks there =', blocks_min)
print('average over k-1 block slots >=', avg_floor, '(floor)')
print('blocks with deficit <=23 forced >=', good_d23)
print('signed (deficit,odd-cofactor) type count <=', pair_types)
print('some such type repeats at least', repeat, 'times')
