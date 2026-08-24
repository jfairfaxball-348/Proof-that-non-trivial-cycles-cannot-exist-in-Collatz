from fractions import Fraction
from math import gcd

a = 485
ell = 306
g = 2
A = g*a
L = g*ell
X = 1 << a
Y = 3 ** ell
D = (1 << A) - 3 ** L
assert D > 0 and gcd(D, 6) == 1
assert 15 * (1 << A) < 16 * 3 ** L

# Exact upper-mechanical first block: all proper prefixes satisfy 3^P > 2^m,
# while the full reduced block has weight ell and 2^a > 3^ell.
P = [0]
p = 0
for m in range(1, a):
    while 3 ** p <= 2 ** m:
        p += 1
    P.append(p)
P.append(ell)
B = [P[i+1] - P[i] for i in range(a)]
assert all(b in (0, 1) for b in B)
assert sum(B) == ell
assert B[:4] == [1, 1, 0, 1]
assert B[-2:] == [1, 0]
for m in range(1, a):
    assert 3 ** P[m] > 2 ** m
assert 2 ** a > 3 ** ell

SWAPS = [
325,75,157,390,422,70,81,200,471,116,233,333,241,384,251,392,67,289,59,433,
306,281,108,463,460,327,295,51,371,173,411,254,387,189,35,403,159,373,48,319,
360,86,352,227,230,346,94,5,154,279,37,8,273,181,130,186,43,56,363,222,430,
417,205,292,92,357,466,132,111,162,382,419,322,214,32,265,195,474,349,167,398,
97,479,308,414,40,170,119,100,211,121,216,428,303,203,10,105,314,165,468
]
assert len(SWAPS) == 100 and len(set(SWAPS)) == 100
C = B[:]
used = []
for i in SWAPS:
    assert 0 <= i < a-1
    assert all(abs(i-j) > 1 for j in used)
    assert C[i:i+2] == [0, 1]
    C[i], C[i+1] = 1, 0
    used.append(i)
assert sum(C) == ell
assert C[:4] == [1, 1, 0, 1]
assert C[-2:] == [1, 0]

d = B + C
assert len(d) == A and sum(d) == L
assert d[:4] == [1, 1, 0, 1]
assert d[a:a+4] == [1, 1, 0, 1]
assert d[-2:] == [1, 0]

# Primitive.
for p0 in range(1, A):
    if A % p0 == 0:
        assert d != d[:p0] * (A // p0)

# Exact canonical balance.
assert sum(d[:a]) == ell and sum(d[a:]) == ell
E = [0, sum(d[:a])-ell, sum(d)-2*ell]
assert E == [0, 0, 0]

# Proper suffix slope condition.
pref = [0]
s = 0
for b in d:
    s += b
    pref.append(s)
for k in range(1, A):
    suffix_weight = L - pref[A-k]
    assert 2 ** k > 3 ** suffix_weight


def Qword(v):
    LL = sum(v)
    pp = 0
    q = 0
    for i, b in enumerate(v):
        if b:
            q += (1 << i) * 3 ** (LL - 1 - pp)
            pp += 1
    return q

Q = Qword(d)
assert Q % D != 0

# Exact rational phase numerators. Every phase has common denominator D.
N = Q
nums = [N]
for b in d[:-1]:
    num = 3*N + D if b else N
    assert num % 2 == 0
    N = num // 2
    nums.append(N)
assert len(nums) == A
mn = min(nums)
assert nums[0] == mn and nums.count(mn) == 1
R = Fraction(nums[0], D)
x = Fraction(nums[a], D)
assert R > 0
assert R < x
assert 15*x < 16*R

# Rotation divisibility identity in exact block form.
U = Qword(B)
V = Qword(C)
assert Q == Y*U + X*V
assert X*x == Y*R + U
assert X*R == Y*x + V
assert (X+Y)*(x-R) == U-V
assert (X-Y)*(x+R) == U+V

# The proper-factor quotient is deliberately nonintegral here.
assert (U-V) % (X+Y) != 0

# Equal-weight first-difference 2-adic lemma on this witness.
def v2(n):
    n = abs(n)
    c = 0
    while n and n % 2 == 0:
        n //= 2
        c += 1
    return c

first_diff = next(i for i,(bb,cc) in enumerate(zip(B,C)) if bb != cc)
assert first_diff == 5
assert v2(U-V) == first_diff

# Cyclic adjacent-transposition distance depends only on relative shift.
def cyclic_shift_distance(k):
    zc = 0
    cumulative = []
    for i, xx in enumerate(d):
        yy = d[(i+k) % A]
        zc += xx - yy
        cumulative.append(zc)
    assert cumulative[-1] == 0
    vals = sorted(-v for v in cumulative)
    med = vals[len(vals)//2]
    return sum(abs(med + v) for v in cumulative)

balanced_distance = cyclic_shift_distance(a)
assert balanced_distance == 200
best = min((cyclic_shift_distance(k), k) for k in range(1, A))
assert best == (110, 65)

print('RL21 balanced-return countermodel verifier: PASS')
print('A,L,g,a,ell =', A, L, g, a, ell)
print('lambda < 16/15 = True')
print('canonical E path =', E)
print('unique least positive rational phase at root = True')
print('balanced phase ratio ~= %.12f' % float(x/R))
print('balanced shift distance =', balanced_distance)
print('all-rotation minimum =', best)
print('D divides Q =', Q % D == 0)
print('(X+Y) divides Q(B)-Q(C) =', (U-V) % (X+Y) == 0)
print('first block disagreement = v2(Q(B)-Q(C)) =', first_diff)
