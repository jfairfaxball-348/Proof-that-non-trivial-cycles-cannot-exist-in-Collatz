from fractions import Fraction
from math import isqrt
import sympy as sp

R,t=sp.symbols('R t', positive=True)
FH=4*R/(4*R-1)
PHH=16*R/(16*R-7)
T=256*R/(256*R-319)   # G^5

cores={
'I1':((27*R+19)/(27*R),3),
'I2':((243*R+287)/(243*R),5),
'I3':((2187*R+3511)/(2187*R),7),
'II1':(32*R/(32*R-23),3),
'II2':(256*R/(256*R-319),5),
'II3':((2187*R+3767)/(2187*R),7),
}
qcores={
'I1':((9*R+5)/(9*R),2),
'I2':((81*R+85)/(81*R),4),
'I3':((729*R+1085)/(729*R),6),
'II1':(8*(4*R-1)/(32*R-23),2),
'II2':(64*(4*R-1)/(256*R-319),4),
'II3':((729*R+1085)/(729*R),6),
}

def positive_after_shift(expr, shift=160):
    expr=sp.together(expr)
    num,den=sp.fraction(expr)
    if sp.expand(num)==0:
        return True, [0]
    poly=sp.Poly(sp.expand(num.subs(R,t+shift)),t)
    coeffs=list(reversed(poly.all_coeffs()))
    return all(c>=0 for c in coeffs) and any(c>0 for c in coeffs), coeffs

# Core blocks.  II2 is the equality case defining T=G^5.
for name,(C,n) in cores.items():
    ok,coeffs=positive_after_shift(T**n-C**5)
    assert ok, (name,coeffs)

# A high->high odd transition pair has product <= PHH.  Check target pair mean.
ok,coeffs=positive_after_shift(T**2-PHH**5)
assert ok, coeffs

# Once a core is followed by at least one extra high state, pair its terminal
# high with the first extra high.  An odd number of remaining highs is paired;
# an even number leaves one final high bounded by FH.  These two seed checks
# plus the pair check cover arbitrarily long high runs.
for name,(Q,nq) in qcores.items():
    # m=1: Q * PHH, length nq+2
    ok,coeffs=positive_after_shift(T**(nq+2)-(Q*PHH)**5)
    assert ok, ('m1',name,coeffs)
    # m=2: Q * PHH * FH, length nq+3
    ok,coeffs=positive_after_shift(T**(nq+3)-(Q*PHH*FH)**5)
    assert ok, ('m2',name,coeffs)

# Strict improvement over the RL22 threshold factor FH.
ok,coeffs=positive_after_shift(FH**5-T)
assert ok, coeffs

# Numerical sanity checks for the high-high transition formula.
def Fq(x): return 1+Fraction(1,3*x)
for RR in [160,161,1009,10**6]:
    HH=Fraction(4*RR-1,3)
    bound=Fraction(16*RR,16*RR-7)
    for nu in range(1,12):
        # smallest rational a compatible with a>=H and next odd b>=H
        amin=max(HH, Fraction((1<<nu)*HH-1,3))
        b=Fraction(3*amin+1,1<<nu)
        assert b>=HH
        prod=Fq(amin)*Fq(b)
        assert prod<=bound

# Exact continued-fraction gate under the inherited external floor R>=2^71.
R0=1<<71

def ln_interval(x:Fraction,N=260):
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

def cf_interval(lo,hi,terms=40):
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
# log(lambda)/L <= (1/5)log(1+319/(256R-319)) <= c(R)
c0=Fraction(319,5*(256*R0-319))
Tleg=ln2_lo/(2*c0)
qmax=isqrt(Tleg.numerator//Tleg.denominator)
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

print('RL23 high-run packing / CF gate verifier: PASS')
print('analytic factor: G(R)^5 = 256R/(256R-319)')
print('asymptotic coefficient = 319/1280 =', float(Fraction(319,1280)))
print('R0 =',R0)
print('linearized c(R0) =',c0)
print('rigorous qmax =',qmax)
print('therefore q=L/gcd(A,L) >=',qmax+1)
print('first convergent denominator beyond qmax =',first_beyond)
