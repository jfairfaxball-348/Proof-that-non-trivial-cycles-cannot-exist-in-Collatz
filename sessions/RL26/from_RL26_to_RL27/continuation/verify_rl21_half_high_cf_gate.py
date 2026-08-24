from fractions import Fraction
from math import isqrt

R0=1<<71

def ln_interval(x:Fraction,N=240):
    x2=x*x;term=x;s=Fraction(0)
    for k in range(N):
        s += term/(2*k+1);term*=x2
    lo=2*s
    tail=2*term/(2*N+1)/(1-x2)
    return lo,lo+tail
ln2_lo,ln2_hi=ln_interval(Fraction(1,3))
ln3_lo,ln3_hi=ln_interval(Fraction(1,2))
beta_lo=ln3_lo/ln2_hi;beta_hi=ln3_hi/ln2_lo

def cf_interval(lo,hi,terms=35):
    out=[]
    for _ in range(terms):
      a0=lo.numerator//lo.denominator;a1=hi.numerator//hi.denominator
      assert a0==a1
      out.append(a0);lo-=a0;hi-=a0
      assert lo>0
      lo,hi=1/hi,1/lo
    return out
cf=cf_interval(beta_lo,beta_hi)
# Matched low/high odd-state pairs give c(R)=1/(6R)+1/(9R+3).
# This upper-bounds Lambda/L after log(1+t)<=t.
c0=Fraction(1,6*R0)+Fraction(1,9*R0+3)
# Legendre if c0/ln2 < 1/(2q^2). It suffices that 2 q^2 c0 < ln2_lo.
# q^2 < ln2_lo/(2c0). exact floor
num=(ln2_lo/(2*c0)).numerator
den=(ln2_lo/(2*c0)).denominator
qmax=isqrt(num//den)
while Fraction(2*qmax*qmax)*c0 >= ln2_lo:qmax-=1
while Fraction(2*(qmax+1)*(qmax+1))*c0 < ln2_lo:qmax+=1
assert 2*qmax*qmax*c0 < ln2_lo
assert not (2*(qmax+1)*(qmax+1)*c0 < ln2_lo)

pm2,pm1=0,1;qm2,qm1=1,0
above=[];first_beyond=None
for idx,a in enumerate(cf):
    p=a*pm1+pm2;q=a*qm1+qm2
    pm2,pm1=pm1,p;qm2,qm1=qm1,q
    dlo=p*ln2_lo-q*ln3_hi
    dhi=p*ln2_hi-q*ln3_lo
    assert dhi<0 or dlo>0
    if q<=qmax and dlo>0:
        # Actual cycle would force Delta <= q*c(R) <= q*c(R0).
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
print('RL21 half-high CF gate verifier: PASS')
print('R0 =',R0)
print('c(R0) =',c0)
print('rigorous qmax =',qmax)
print('therefore q=L/gcd(A,L) >=',qmax+1)
print('above-beta convergents excluded through qmax =',above)
print('first convergent denominator beyond qmax =',first_beyond)
