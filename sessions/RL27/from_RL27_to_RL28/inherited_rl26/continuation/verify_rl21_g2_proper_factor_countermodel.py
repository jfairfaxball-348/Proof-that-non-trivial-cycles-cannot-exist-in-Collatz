from fractions import Fraction
from math import gcd

UWORD = '11011011010110110110101101110011011100110110110101110101011011100'
VWORD = '11111111110111000111110011011011110101010111110011101000011100000'
u = [int(c) for c in UWORD]
v = [int(c) for c in VWORD]
a = 65
ell = 41
assert len(u) == len(v) == a
assert sum(u) == sum(v) == ell

X = 1 << a
Y = 3 ** ell
A = 2*a
L = 2*ell
D = X*X - Y*Y
assert D > 0 and gcd(D, 6) == 1
assert 15 * X*X < 16 * Y*Y
assert gcd(X-Y, X+Y) == 1


def Qword(w):
    LL = sum(w)
    p = 0
    q = 0
    for i,b in enumerate(w):
        if b:
            q += (1 << i) * 3 ** (LL-1-p)
            p += 1
    return q

U = Qword(u)
V = Qword(v)
assert U - V == 4 * (X+Y)
assert (U+V) % (X-Y) != 0

d = u+v
Q = Qword(d)
assert Q == Y*U + X*V
assert Q % D != 0

# Both block prefix envelopes.
for w in (u,v):
    p = 0
    for m,b in enumerate(w, 1):
        p += b
        if m < a:
            assert 3 ** p > 2 ** m

# Primitive.
for p0 in range(1, A):
    if A % p0 == 0:
        assert d != d[:p0] * (A//p0)

# Full suffix contraction package.
pref = [0]
s = 0
for b in d:
    s += b
    pref.append(s)
for k in range(1, A):
    sw = L - pref[A-k]
    assert 2 ** k > 3 ** sw

# Exact rational orbit using common numerator denominator D.
N = Q
nums = [N]
for b in d[:-1]:
    num = 3*N + D if b else N
    assert num % 2 == 0
    N = num // 2
    nums.append(N)
assert nums[0] == min(nums)
assert nums.count(nums[0]) == 1
R = Fraction(nums[0], D)
x = Fraction(nums[a], D)
assert R > 0
assert x - R == 4
assert 15*x < 16*R

# Exact factor/state identities.
assert (X+Y)*(x-R) == U-V
assert (X-Y)*(x+R) == U+V
assert (U-V) % (X+Y) == 0
assert (U+V) % (X-Y) != 0

# Balanced E path.
assert [0, sum(u)-ell, sum(d)-2*ell] == [0,0,0]

# Cyclic adjacent-transposition shift distance.
def dist_shift(k):
    z = 0
    cumulative = []
    for i,b in enumerate(d):
        z += b - d[(i+k)%A]
        cumulative.append(z)
    assert cumulative[-1] == 0
    vals = sorted(-q for q in cumulative)
    med = vals[len(vals)//2]
    return sum(abs(med+q) for q in cumulative)

half_dist = dist_shift(a)
best = min((dist_shift(k), k) for k in range(1,A))
assert half_dist == 340
assert best == (48, 1)

print('RL21 g=2 proper-factor countermodel verifier: PASS')
print('A,L,a,ell =', A,L,a,ell)
print('x-R =', x-R)
print('(X+Y) quotient =', (U-V)//(X+Y))
print('(X-Y) divides U+V =', (U+V)%(X-Y)==0)
print('D divides Q =', Q%D==0)
print('balanced shift distance =', half_dist)
print('all-rotation minimum =', best)
