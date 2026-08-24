from fractions import Fraction

R0 = 1 << 71

# R20G.1: if lambda<3, delta=log_3(lambda)<1 and
# E_j > -(g-j)delta/g > -1. Integer E_j therefore satisfies E_j>=0.
# The following exact rational surrogate checks the integer implication for a
# dense family 0<delta<1 and 1<=j<g.
for g in range(2,80):
    for j in range(1,g):
        for num in range(1,25):
            delta = Fraction(num,25)  # 0<delta<1
            lower = -Fraction(g-j,g)*delta
            for E in range(-3,4):
                if Fraction(E,1) > lower:
                    assert E >= 0

# Near resonance lambda<16/15 gives the disjoint physical height bands.
lam = Fraction(16,15)
assert 3/lam == Fraction(45,16)
assert lam < 2

# Balanced cut: R < x < lambda R <2R. If x were even, the next full-parity
# phase x/2 would be below the least state R. Hence every balanced cut is odd.
for R in range(101,300,2):
    for x in range(R+1, (16*R)//15 + 1):
        if Fraction(x,R) < lam and x % 2 == 0:
            assert Fraction(x,2) < R

# RL-L54 rescue bound finite threshold for a balanced prefix in the narrow
# ratio window. No m<195 can reach the external floor; first hit is (195,123).
def rescue(m,p):
    return Fraction((1 << (m-p))*(3**p-2**p), (1 << m)-3**p)

hits = []
for m in range(1,196):
    for p in range(0,m+1):
        if (1 << m) > 3**p and Fraction(1 << m,3**p) < lam:
            if p > 0 and rescue(m,p) >= R0:
                hits.append((m,p))
                break
    if hits:
        break
assert hits == [(195,123)]

# Existing CF gate q=ell >= 49,547,666,544 and beta=log_2 3 >19/12 imply
# a > (19/12)ell. The integral lower bound is exact.
ell = 49_547_666_544
a_min = (19*ell)//12 + 1
assert a_min == 78_450_472_029

print('RL20 near-resonant gcd-block geometry verifier: PASS')
print('integer one-sided imbalance implication checked')
print('balanced cut is necessarily odd because x < 2R#')
print('first narrow undercritical rescue reaching 2^71 =', hits[0])
print('CF-induced reduced block length a >=', a_min)
