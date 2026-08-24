from fractions import Fraction
from itertools import product
from math import gcd


def Qword(w: str) -> int:
    L = w.count('1')
    r = 0
    Q = 0
    for i, b in enumerate(w):
        if b == '1':
            r += 1
            Q += (1 << i) * (3 ** (L - r))
    return Q


def rot(w: str, m: int) -> str:
    return w[m:] + w[:m]


def pow3(e: int) -> Fraction:
    return Fraction(3**e, 1) if e >= 0 else Fraction(1, 3**(-e))


def cyclic_adjacent_distance(a: str, b: str) -> int:
    assert len(a) == len(b) and a.count('1') == b.count('1')
    s = 0
    vals = []
    for x, y in zip(a, b):
        s += int(x) - int(y)
        vals.append(s)
    assert s == 0
    vals.sort()
    med = vals[len(vals)//2]
    return sum(abs(v-med) for v in vals)

# ------------------------------------------------------------------
# A. Rotation numerator transport / ownership-defect ideal invariance.
# Exact identity:
#   2^m Q(rot_m w) - 3^{P_m}Q(w) = D Q(prefix_m)
# where D=2^A-3^L.
# ------------------------------------------------------------------
rotation_checks = 0
gcd_checks = 0
for A in range(2, 10):
    for bits in product('01', repeat=A):
        w = ''.join(bits)
        L = w.count('1')
        D = (1 << A) - 3**L
        if D == 0:
            continue
        Q0 = Qword(w)
        for m in range(A+1):
            p = w[:m].count('1')
            Qm = Qword(rot(w, m % A)) if m < A else Q0
            lhs = (1 << m) * Qm - (3**p) * Q0
            rhs = D * Qword(w[:m])
            assert lhs == rhs
            rotation_checks += 1
            if m < A:
                assert gcd(abs(D), Qm) == gcd(abs(D), Q0)
                gcd_checks += 1

# ------------------------------------------------------------------
# B. Corrected canonical-block lift.
# For equal block length a and target block weight ell, with
# E_j=K_j-j ell, y_j=3^{-E_j}x_j, z=2^a/3^ell,
# H_j=z^j y_j, the correct increment is
#   H_{j+1}-H_j = z^j 3^{-E_{j+1}} Q(B_j)/3^ell.
# The printed RL20 formula omitted 3^{-E_{j+1}}.
# ------------------------------------------------------------------
block_checks = 0
scale_trade_checks = 0
for G in range(2, 5):
    for a in range(2, 5):
        A = G*a
        for bits in product('01', repeat=A):
            w = ''.join(bits)
            L = w.count('1')
            if L % G:
                continue
            ell = L // G
            if ell == 0:
                continue
            X = 1 << a
            Y = 3**ell
            z = Fraction(X, Y)
            # arbitrary positive rational entry state, to avoid using closure
            x = Fraction(7, 1)
            K = 0
            H_prev = x
            for j in range(G):
                Bj = w[j*a:(j+1)*a]
                rj = Bj.count('1')
                Qj = Qword(Bj)
                # advance exact affine block map
                x_next = Fraction((3**rj)*x + Qj, X)
                K += rj
                E_next = K - (j+1)*ell
                H_next = (z**(j+1)) * x_next * pow3(-E_next)
                correct = (z**j) * Fraction(Qj, Y) * pow3(-E_next)
                assert H_next - H_prev == correct
                block_checks += 1
                if Qj != 0 and x_next != 0 and H_next != 0:
                    assert Fraction(H_next-H_prev, H_next) == Fraction(Qj, X) / x_next
                    scale_trade_checks += 1
                x = x_next
                H_prev = H_next

# ------------------------------------------------------------------
# C. Mandatory RL20 radius-4 fake negative control.
# ------------------------------------------------------------------
fake = (
'1101101101011011010110110110101101101011011011010110110101101101101011011010110110101101101101011011010110110110101101101011011011010110110101101101101011011010110110101101101101011010'
)
A = len(fake); L = fake.count('1')
assert (A, L) == (184, 116)
D = (1 << A) - 3**L
Q = Qword(fake)
expected_rem = 322171738410077807581692882247758374512983113782519312
assert Q % D == expected_rem
assert gcd(D, Q) == 1
R = Fraction(Q, D)
assert R.denominator == D

# Exact rational fixed orbit: positive and least at the root rotation.
xs = [R]
x = R
for b in fake:
    x = (3*x+1)/2 if b == '1' else x/2
    xs.append(x)
assert xs[-1] == R
phase = xs[:-1]
assert all(v > 0 for v in phase)
assert min(phase) == phase[0]

# inherited all-rotation radius minimum = 4
mind = min(cyclic_adjacent_distance(fake, rot(fake, m)) for m in range(1, A))
assert mind == 4

# canonical gcd-block strict excursion E=(0,1,1,1,0)
G = gcd(A, L); a = A//G; ell = L//G
assert (G, a, ell) == (4, 46, 29)
P = [0]
for b in fake:
    P.append(P[-1] + (b == '1'))
E = [P[j*a]-j*ell for j in range(G+1)]
assert E == [0,1,1,1,0]
z = Fraction(1 << a, 3**ell)
for j in range(G):
    Bj = fake[j*a:(j+1)*a]
    Qj = Qword(Bj)
    Ej = E[j]
    En = E[j+1]
    Hj = (z**j) * phase[j*a] * pow3(-Ej)
    Hn = (z**(j+1)) * (R if j+1 == G else phase[(j+1)*a]) * pow3(-En)
    correct = (z**j) * Fraction(Qj, 3**ell) * pow3(-En)
    printed = (z**j) * Fraction(Qj, 3**ell)
    assert Hn-Hj == correct
    if En != 0 and Qj != 0:
        assert Hn-Hj != printed

# ------------------------------------------------------------------
# D. Exact plateau scale-prepayment stress family.
# This is a method stress test, not a genuine cycle/full-D construction.
# Blocks are 1^r 0^(a-r), so Q=3^r-2^r exactly.
# ------------------------------------------------------------------
def minQ_block(a, r):
    assert 0 <= r <= a
    return '1'*r + '0'*(a-r)

stress_checks = 0
# A good above-resonance reduced pair with generous spare dimensions.
a0, ell0 = 485, 306
z0 = Fraction(1 << a0, 3**ell0)
assert z0 > 1
for n in range(1, 25):
    for h in range(1, min(12, ell0, a0-ell0)+1):
        rs = [ell0+h] + [ell0]*n + [ell0-h]
        Es = [0, h] + [h]*n + [0]
        total = Fraction(0,1)
        for j, rj in enumerate(rs):
            Bj = minQ_block(a0, rj)
            Qj = Qword(Bj)
            En = Es[j+1]
            inc = (z0**j) * Fraction(Qj, 3**ell0) * pow3(-En)
            total += inc
            if j == 0:
                assert inc == 1 - Fraction(2,3)**(ell0+h)
            elif j <= n:
                assert inc == (z0**j) * (Fraction(1,3)**h) * (1-Fraction(2,3)**ell0)
            else:
                assert inc == (z0**j) * (Fraction(1,3)**h) * (1-Fraction(2,3)**(ell0-h))
            stress_checks += 1
        # no assertion of full-phase closure: this is purely an exact local-cost identity
        assert total > 0

print('RL78 D|Q rotation/block-scale verifier: PASS')
print('rotation transport checks =', rotation_checks)
print('rotation gcd-invariance checks =', gcd_checks)
print('corrected block-lift checks =', block_checks)
print('scale-trade checks =', scale_trade_checks)
print('stress-family block checks =', stress_checks)
print('RL20 fake D gcd Q =', gcd(D,Q))
print('RL20 fake reduced denominator = D =', D)
print('RL20 fake rational least state ~', float(R))
print('RL20 fake canonical E path =', E)
print('RL20 fake minimum rotation radius =', mind)
