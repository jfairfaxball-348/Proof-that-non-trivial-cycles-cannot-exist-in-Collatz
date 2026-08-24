from fractions import Fraction
from math import isqrt

R0 = 1 << 71

# Rigorous rational intervals from ln z = 2 atanh((z-1)/(z+1)).
def ln_interval(x: Fraction, N=220):
    # returns interval for 2*atanh(x), 0<x<1
    x2 = x*x
    term = x
    s = Fraction(0)
    for k in range(N):
        s += term / (2*k + 1)
        term *= x2
    lo = 2*s
    # term=x^(2N+1); bound all remaining denominators by (2N+1)
    tail = 2 * term / (2*N + 1) / (1 - x2)
    return lo, lo + tail

ln2_lo, ln2_hi = ln_interval(Fraction(1,3))  # ln 2
ln3_lo, ln3_hi = ln_interval(Fraction(1,2))  # ln 3
assert ln2_lo > 0 and ln3_lo > 0

beta_lo = ln3_lo / ln2_hi
beta_hi = ln3_hi / ln2_lo

# Exact CF prefix from a rational interval enclosing beta=ln3/ln2.
def cf_interval(lo, hi, terms=30):
    out=[]
    for _ in range(terms):
        a0 = lo.numerator // lo.denominator
        a1 = hi.numerator // hi.denominator
        assert a0 == a1
        a=a0; out.append(a)
        lo -= a; hi -= a
        assert lo > 0
        lo, hi = 1/hi, 1/lo
    return out

cf = cf_interval(beta_lo, beta_hi, 30)
expected = [1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,9,2,5,7,1,1,4,8]
assert cf == expected

# Largest q for which 2q^2 < 3 R0 ln 2 is rigorously guaranteed
# using the lower rational bound for ln2.
n,d = ln2_lo.numerator, ln2_lo.denominator
qmax = isqrt((3*R0*n - 1)//(2*d))
assert 2*qmax*qmax * d < 3*R0*n
assert not (2*(qmax+1)*(qmax+1) * ln2_hi.denominator < 3*R0*ln2_hi.numerator)

# Convergents and exact exclusion of every convergent above beta through qmax.
pm2,pm1 = 0,1
qm2,qm1 = 1,0
above=[]
first_beyond=None
for idx,a in enumerate(cf):
    p = a*pm1 + pm2
    q = a*qm1 + qm2
    pm2,pm1 = pm1,p
    qm2,qm1 = qm1,q

    # Rigorous sign interval for Delta=p ln2-q ln3.
    delta_lo = p*ln2_lo - q*ln3_hi
    delta_hi = p*ln2_hi - q*ln3_lo
    assert delta_hi < 0 or delta_lo > 0

    if q <= qmax and delta_lo > 0:
        # Product bound for an actual cycle would force
        # Delta <= q/(3R) <= q/(3R0).  Exclude it exactly.
        assert delta_lo > Fraction(q, 3*R0)
        above.append((p,q))
    if q > qmax and first_beyond is None:
        first_beyond=(p,q,delta_lo>0)
        break

expected_above=[
    (2,1),(8,5),(65,41),(485,306),(24727,15601),
    (125743,79335),(301994,190537),(17087915,10781274),
    (272500658,171928773),(630138897,397573379),
    (10439860591,6586818670),
]
assert above == expected_above
assert first_beyond is not None

print('RL20 global continued-fraction gate verifier: PASS')
print('R0 =', R0)
print('rigorous qmax =', qmax)
print('therefore reduced odd-count denominator q=L/gcd(A,L) >=', qmax+1)
print('above-beta convergents excluded through qmax =', above)
print('first convergent denominator beyond qmax =', first_beyond)
