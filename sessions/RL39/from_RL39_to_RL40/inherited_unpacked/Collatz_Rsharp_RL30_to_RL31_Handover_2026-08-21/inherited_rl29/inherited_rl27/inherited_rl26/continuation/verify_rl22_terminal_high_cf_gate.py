from fractions import Fraction
from math import isqrt

# Six block-mean comparisons.  After clearing positive denominators in
# F_H^(2k+1)-P, substituting R=t+160 gives the coefficient lists below.
shift_coeffs = {
    'I1': [80,38988,6331959,342700659],
    'II1': [64,30336,4792352,252318720],
    'I2': [17152,13933440,4526344800,735015081060,59663352653703,1936756967056767],
    'II2': [1024,655360,157327360,16796871680,674232729856,167641128960],
    'I3': [5181440,5856850944,2836978857216,763363588236480,123229540205401392,
           11934579238964218620,642074413810988876679,14802876129425730032151],
    'II3': [987136,1166570496,589161952512,164882337359040,27622160377730352,
            2770611882481949436,154093152078308042631,3666446620597763855127],
}
assert all(all(c>0 for c in cs) for cs in shift_coeffs.values())

# Direct exact checks of closed forms and comparisons at representative R>=160.
def F(x): return 1+Fraction(1,3*x)
def f(x): return Fraction(9*x+5,8)
for R in [160,161,1009,10**6]:
    H=Fraction(4*R-1,3)
    FH=F(H)
    PI=[]; PII=[]
    for k in (1,2,3):
        # Type I starts at R and terminal z=2 f^k(R).
        x=Fraction(R); prod=Fraction(1)
        for _ in range(k):
            y=Fraction(3*x+1,2)
            prod*=F(x)*F(y)
            x=f(x)
        PI.append(prod*F(2*x))

        # Type II uses the smallest x0>=R with f^k(x0)>=H.
        x0=H
        for _ in range(k):
            x0=Fraction(8*x0-5,9)
        if x0<R: x0=Fraction(R)
        x=x0; prod=Fraction(1)
        for _ in range(k):
            y=Fraction(3*x+1,2)
            prod*=F(x)*F(y)
            x=f(x)
        PII.append(prod*F(x))

    assert PI[0] == Fraction(27*R+19,27*R)
    assert PI[1] == Fraction(243*R+287,243*R)
    assert PI[2] == Fraction(2187*R+3511,2187*R)
    assert PII[0] == Fraction(32*R,32*R-23)
    assert PII[1] == Fraction(256*R,256*R-319)
    assert PII[2] == Fraction(2187*R+3767,2187*R)
    for k,P in enumerate(PI,1): assert P <= FH**(2*k+1)
    for k,P in enumerate(PII,1): assert P <= FH**(2*k+1)

# Exact CF gate.
R0=1<<71

def ln_interval(x:Fraction,N=240):
    x2=x*x; term=x; s=Fraction(0)
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
        lo-=a0; hi-=a0
        assert lo>0
        lo,hi=1/hi,1/lo
    return out

cf=cf_interval(beta_lo,beta_hi)
c0=Fraction(1,4*R0-1)
T=ln2_lo/(2*c0)
qmax=isqrt(T.numerator//T.denominator)
while 2*qmax*qmax*c0 >= ln2_lo: qmax-=1
while 2*(qmax+1)*(qmax+1)*c0 < ln2_lo: qmax+=1
assert 2*qmax*qmax*c0 < ln2_lo
assert not (2*(qmax+1)*(qmax+1)*c0 < ln2_lo)

pm2,pm1=0,1; qm2,qm1=1,0
above=[]; first_beyond=None
for a in cf:
    p=a*pm1+pm2; q=a*qm1+qm2
    pm2,pm1=pm1,p; qm2,qm1=qm1,q
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
assert qmax==57212717232

print('RL22 terminal-high CF gate verifier: PASS')
print('R0 =',R0)
print('c(R0) =',c0)
print('rigorous qmax =',qmax)
print('therefore q=L/gcd(A,L) >=',qmax+1)
print('first convergent denominator beyond qmax =',first_beyond)
