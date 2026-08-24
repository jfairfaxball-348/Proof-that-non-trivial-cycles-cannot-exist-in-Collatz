from fractions import Fraction
from math import isqrt
import sympy as sp

R,t=sp.symbols('R t', positive=True)
FH=4*R/(4*R-1)
PHH=16*R/(16*R-7)
T=256*R/(256*R-319)
cores={
'I1':((27*R+19)/(27*R),3),
'I2':((243*R+287)/(243*R),5),
'I3':((2187*R+3511)/(2187*R),7),
'II1':(32*R/(32*R-23),3),
'II2':(T,5),
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
S5=sp.factor(qcores['I1'][0]*PHH*FH)
K=sp.factor(T/S5)
CTILT=sp.factor(((S5-1)/5+sp.Rational(37,200)*(K-1))/(1-sp.Rational(3,2)*(K-1)))

def positive_after_shift(expr,shift=160,allow_zero=False):
    num,den=sp.fraction(sp.together(expr))
    num=sp.expand(num)
    if num==0:
        return allow_zero,[0]
    poly=sp.Poly(sp.expand(num.subs(R,t+shift)),t)
    coeffs=poly.all_coeffs()
    return all(c>=0 for c in coeffs) and any(c>0 for c in coeffs),coeffs

# Basic factor identities and positivity.
assert sp.factor(S5-64*R*(9*R+5)/(9*(4*R-1)*(16*R-7)))==0
assert sp.factor(K-36*(4*R-1)*(16*R-7)/((9*R+5)*(256*R-319)))==0
ok,coeffs=positive_after_shift(K-1)
assert ok,coeffs

# V_H >= ceil((4h+2)/3) is checked arithmetically by the three residue classes.
# The exponent comparisons are 2^(4q)<3^(3q), 2^(4q+1)<3^(3q+1),
# and 2^(4q+3)<3^(3q+2), reduced to 16<27, 2<3, 8<9.
assert 16<27 and 2<3 and 8<9

def ceil_div(a,b): return (a+b-1)//b

# Seed inequalities h=1,...,6 for all six chain types.
for typ in ('I','II'):
    for kk in (1,2,3):
        name=f'{typ}{kk}'
        pre=3*kk-1 if typ=='I' else 3*kk
        for h in range(1,7):
            n=2*kk+h
            Vstar=pre+ceil_div(4*h+2,3)
            E=5*Vstar-7*n
            if h==1:
                P=cores[name][0]
            else:
                Q=qcores[name][0]
                if h%2==0:
                    P=Q*PHH**(h//2)
                else:
                    P=Q*PHH**((h-1)//2)*FH
            expr=S5**n*K**E-P**5
            ok,coeffs=positive_after_shift(expr,allow_zero=True)
            assert ok,(name,h,n,Vstar,E,coeffs)

# h -> h+6 extension: product acquires PHH^3, n +=6, Vstar +=8,
# so E=5V-7n drops by 2.
ok,coeffs=positive_after_shift(S5**6-PHH**15*K**2)
assert ok,coeffs

# Rational majorant simplification and monotonicity.
expected=(66135744*R**3-12111620*R**2-68717407*R+8324757)/(900*(4*R-1)*(16*R-7)*(4608*R**2-3203*R-8731))
assert sp.factor(CTILT-expected)==0
num,den=sp.fraction(sp.together(-sp.diff(CTILT,R)))
poly=sp.Poly(sp.expand(num.subs(R,t+160)),t)
assert all(c>=0 for c in poly.all_coeffs()) and any(c>0 for c in poly.all_coeffs())
dpoly=sp.Poly(sp.expand(den.subs(R,t+160)),t)
assert all(c>0 for c in dpoly.all_coeffs())
assert sp.limit(R*CTILT,R,sp.oo)==sp.Rational(38273,153600)
assert sp.Rational(38273,153600)<sp.Rational(51033,204800)<sp.Rational(319,1280)
assert 3**200 < 2**317

# Exact continued-fraction gate under inherited R>=2^71.
R0=1<<71

def frac_subs(expr,RR):
    return Fraction(int(sp.numer(expr.subs(R,RR))),int(sp.denom(expr.subs(R,RR))))

c0=frac_subs(CTILT,R0)

def ln_interval(x:Fraction,N=260):
    x2=x*x; term=x; s=Fraction(0)
    for j in range(N):
        s += term/(2*j+1)
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

expected_above=[
    (2,1),(8,5),(65,41),(485,306),(24727,15601),
    (125743,79335),(301994,190537),(17087915,10781274),
    (272500658,171928773),(630138897,397573379),
    (10439860591,6586818670),
]
assert above==expected_above
assert first_beyond==(103768467013,65470613321,False)
assert qmax==57307562129

print('RL24 tilted valuation packing verifier: PASS')
print('S5 =',S5)
print('K =',K)
print('C_tilt(R) =',CTILT)
print('asymptotic coefficient =',sp.Rational(38273,153600),'=',float(sp.Rational(38273,153600)))
print('R0 =',R0)
print('C_tilt(R0) =',c0)
print('rigorous qmax =',qmax)
print('therefore q=L/gcd(A,L) >=',qmax+1)
print('first convergent denominator beyond qmax =',first_beyond)
