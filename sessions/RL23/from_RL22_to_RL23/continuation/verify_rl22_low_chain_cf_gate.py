from fractions import Fraction
from math import isqrt

# ---------- exact chain-product comparisons ----------
# P1^5-P2^3 has positive denominator and numerator
# 64*(1102248 R^4 + 11006199 R^3 + 17126345 R^2 + 7207325 R - 164125).
# After R=t+5 the coefficients are all positive.
poly_p2_shift = [
    70543872,
    2115274176,
    22243617920,
    99523820800,
    161837504000,
]
assert all(c > 0 for c in poly_p2_shift)

# P1^7-P3^3 likewise has positive denominator; after R=t+5
# the numerator coefficients below are all positive.
poly_p3_shift = [
    2690502967296,
    105635569526784,
    1681067890287616,
    13966741383070144,
    64163666187277440,
    155003228690156800,
    154171798063552000,
]
assert all(c > 0 for c in poly_p3_shift)

# P1-F(H)^3 numerator is 4*(8R^2-31R+5); after R=t+5:
assert all(c > 0 for c in [32,196,200])

# Direct exact spot checks of the stated closed forms and comparisons.
def F(s):
    return 1 + Fraction(1,3*s)

def chain_values(R):
    H = Fraction(4*R-1,3)
    f = lambda x: Fraction(9*x+5,8)
    x = [Fraction(R)]
    for _ in range(3):
        x.append(f(x[-1]))
    P = []
    for k in (1,2,3):
        prod = F(H)
        for i in range(k):
            y = Fraction(3*x[i]+1,2)
            prod *= F(x[i])*F(y)
        P.append(prod)
    return H,P

for R in [5,7,11,101,1009]:
    H,P = chain_values(R)
    P1,P2,P3=P
    assert P1 == Fraction(4*(9*R+5),9*(4*R-1))
    assert P2 == Fraction(4*(81*R+85),81*(4*R-1))
    assert P3 == Fraction(4*(729*R+1085),729*(4*R-1))
    assert P1 == 1 + Fraction(29,36*R-9)
    assert P2**3 <= P1**5
    assert P3**3 <= P1**7
    assert F(H)**3 <= P1

# ---------- exact continued-fraction certificate ----------
R0=1<<71

def ln_interval(x:Fraction,N=240):
    x2=x*x
    term=x
    s=Fraction(0)
    for k in range(N):
        s += term/(2*k+1)
        term *= x2
    lo=2*s
    tail=2*term/(2*N+1)/(1-x2)
    return lo,lo+tail

ln2_lo,ln2_hi=ln_interval(Fraction(1,3))
ln3_lo,ln3_hi=ln_interval(Fraction(1,2))
beta_lo=ln3_lo/ln2_hi
beta_hi=ln3_hi/ln2_lo

def cf_interval(lo,hi,terms=35):
    out=[]
    for _ in range(terms):
        a0=lo.numerator//lo.denominator
        a1=hi.numerator//hi.denominator
        assert a0==a1
        out.append(a0)
        lo-=a0
        hi-=a0
        assert lo>0
        lo,hi=1/hi,1/lo
    return out

cf=cf_interval(beta_lo,beta_hi)
c0=Fraction(29,108*R0-27)

# Legendre if 2 q^2 c0 < log 2.
T=ln2_lo/(2*c0)
qmax=isqrt(T.numerator//T.denominator)
while Fraction(2*qmax*qmax)*c0 >= ln2_lo:
    qmax-=1
while Fraction(2*(qmax+1)*(qmax+1))*c0 < ln2_lo:
    qmax+=1
assert 2*qmax*qmax*c0 < ln2_lo
assert not (2*(qmax+1)*(qmax+1)*c0 < ln2_lo)

pm2,pm1=0,1
qm2,qm1=1,0
above=[]
first_beyond=None
for a in cf:
    p=a*pm1+pm2
    q=a*qm1+qm2
    pm2,pm1=pm1,p
    qm2,qm1=qm1,q
    dlo=p*ln2_lo-q*ln3_hi
    dhi=p*ln2_hi-q*ln3_lo
    assert dhi<0 or dlo>0
    if q<=qmax and dlo>0:
        assert dlo > q*c0
        above.append((p,q))
    if q>qmax and first_beyond is None:
        first_beyond=(p,q,dlo>0)
        break

expected=[
    (2,1),(8,5),(65,41),(485,306),(24727,15601),
    (125743,79335),(301994,190537),(17087915,10781274),
    (272500658,171928773),(630138897,397573379),
    (10439860591,6586818670),
]
assert above==expected
assert first_beyond==(103768467013,65470613321,False)
assert qmax==55204624167

print('RL22 low-chain CF gate verifier: PASS')
print('R0 =',R0)
print('c(R0) =',c0)
print('rigorous qmax =',qmax)
print('therefore q=L/gcd(A,L) >=',qmax+1)
print('first convergent denominator beyond qmax =',first_beyond)
