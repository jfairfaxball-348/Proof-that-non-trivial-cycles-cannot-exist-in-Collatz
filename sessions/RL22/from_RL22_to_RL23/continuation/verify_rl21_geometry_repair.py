from fractions import Fraction
from math import gcd

WORD = '1101101101011011010110110110101101101011011011010110110101101101101011011010110110101101101101011011010110110110101101101011011011010110110101101101101011011010110110101101101101011010'
w = [int(c) for c in WORD]


def Qword(v):
    L = sum(v)
    p = 0
    q = 0
    for i, b in enumerate(v):
        if b:
            q += (1 << i) * 3 ** (L - 1 - p)
            p += 1
    return q

A = len(w)
L = sum(w)
g = gcd(A, L)
a = A // g
ell = L // g
X = 1 << a
Y = 3 ** ell
z = Fraction(X, Y)
lam = z ** g
D = (1 << A) - 3 ** L
Q = Qword(w)
R = Fraction(Q, D)
assert D > 0 and R > 0

# Exact rational phase orbit.
xs = [R]
x = R
for b in w:
    x = Fraction(3 * x + 1, 2) if b else Fraction(x, 2)
    xs.append(x)
assert xs[-1] == R
assert min(xs[:-1]) == R
assert xs[:-1].count(R) == 1

# Canonical imbalance path.
K = 0
E = [0]
for j in range(g):
    K += sum(w[j*a:(j+1)*a])
    E.append(K - (j+1)*ell)
assert E == [0, 1, 1, 1, 0]

# Physical strict-excursion bands.
for j in range(1, g):
    assert xs[j*a] > Fraction(45, 16) * R

# Correct H increment and explicit failure of the printed RL20 formula.
wrong_failures = 0
increments = []
for j in range(g):
    Bj = w[j*a:(j+1)*a]
    Qj = Qword(Bj)
    Hj = z**j * xs[j*a] / (3 ** E[j])
    Hj1 = z**(j+1) * xs[(j+1)*a] / (3 ** E[j+1])
    corrected = z**j * Fraction(Qj, Y * (3 ** E[j+1]))
    printed_rl20 = z**j * Fraction(Qj, Y)
    assert Hj1 - Hj == corrected
    if Hj1 - Hj != printed_rl20:
        wrong_failures += 1
    increments.append(Hj1 - Hj)

assert wrong_failures == 3
assert sum(increments, Fraction(0)) == (lam - 1) * R

# Narrow strip remains true.
for j in range(1, g):
    Hj = z**j * xs[j*a] / (3 ** E[j])
    assert R < Hj < lam * R

print('RL21 geometry repair verifier: PASS')
print('A,L,g,a,ell =', A, L, g, a, ell)
print('E path =', E)
print('unique least rational phase at root = True')
print('printed R20G.12 failures =', wrong_failures)
print('correct increment sum equals strip width = True')
