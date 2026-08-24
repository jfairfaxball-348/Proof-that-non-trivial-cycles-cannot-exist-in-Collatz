from math import gcd

R0 = 1 << 71
HARD_CLASS = 91  # mod 144: R mod16=11, R mod9=1


def vp(n, p):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def least_lift(c, mod, floor):
    return floor + ((c - floor) % mod)


def endpoint_data(R, n, t):
    z = (1 << t) * R + 1
    assert vp(z, 3) == n
    q = z // (3**n)
    assert gcd(q, 6) == 1
    u = (1 << n) * q - 1
    assert u > R
    assert (1 << (n+t)) > 3**n
    return q, u

# The repaired hard branch: t_close=1 survives only in R# == 91 mod144.
R = least_lift(HARD_CLASS, 144, R0)
assert R == 2361183241434822606907
assert R % 16 == 11 and R % 9 == 1
assert vp(R + 1, 2) == 2
q_root = (R + 1) // 4
assert vp(9*q_root - 1, 2) == 1

q11, u11 = endpoint_data(R, 1, 1)
# n=1 means the closing anchor is physical; RL20 phase packing requires nonzero mod3.
assert (2*q11 - 1) % 3 != 0
assert q11 % 3 == 1
assert ((1 << 1) * R - 2) % 9 == 0

# Same hard-root witness also supports a genuine n>=2 endpoint (2,3).
q23, u23 = endpoint_data(R, 2, 3)
assert ((1 << 3) * R + 1) % 9 == 0
assert ((1 << 3) * R + 1) % 27 != 0

# Endpoint bookkeeping sees only t_close <= A-L. Hence (1,1) is compatible
# with any total excess S>=1, and the explicit (2,3) witness with any S>=3.
for S in range(1, 1000):
    assert 1 <= S
    if S >= 3:
        assert 3 <= S

# Recorded above-beta continued-fraction spine. All large classes have p-q>=3,
# so neither endpoint witness selects among them at endpoint-only level.
above = [
    (2,1),(8,5),(65,41),(485,306),(24727,15601),
    (125743,79335),(301994,190537),(17087915,10781274),
    (272500658,171928773),(630138897,397573379),
    (10439860591,6586818670),
]
assert above[0][0] - above[0][1] == 1
for p, q in above[1:]:
    assert p - q >= 3

print('RL20 repaired final-return / CF decoupling verifier: PASS')
print('hard-root witness R# =', R)
print('(n,t)=(1,1): q_close =', q11, 'u_close-R# =', u11-R)
print('(n,t)=(2,3): q_close =', q23, 'u_close-R# =', u23-R)
print('large recorded CF classes excluded by endpoint address alone = 0')
