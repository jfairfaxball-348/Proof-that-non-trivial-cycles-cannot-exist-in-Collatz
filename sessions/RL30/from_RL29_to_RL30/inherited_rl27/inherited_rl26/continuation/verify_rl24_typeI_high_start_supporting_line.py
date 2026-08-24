from fractions import Fraction
from math import isqrt
import sympy as sp

R,t=sp.symbols('R t', positive=True)
FH=4*R/(4*R-1)
PHH=16*R/(16*R-7)
PI=(81*R+73)/(81*R+45)
C=(27*R+19)/(27*R)
T=256*R/(256*R-319)
J=sp.factor(T**3/C**5)
cores={
'I1':(C,3),
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
CH=sp.factor((4*(C-1)+sp.Rational(151,200)*(J-1))/(12-sp.Rational(9,2)*(J-1)))

def positive_after_shift(expr,shift=161,allow_zero=False):
    num,den=sp.fraction(sp.together(expr))
    num=sp.expand(num)
    if num==0:
        return allow_zero,[0]
    poly=sp.Poly(sp.expand(num.subs(R,t+shift)),t)
    coeffs=poly.all_coeffs()
    return all(c>=0 for c in coeffs) and any(c>0 for c in coeffs),coeffs

# Improved type-I first high/high pair.
A0=(9*R+5)/4
p1=1+5/(9*A0)
p2=1+7/(9*A0)
p3=1+11/(32*R-11)
ok,coeffs=positive_after_shift(PI-p1); assert ok,coeffs
assert sp.factor(PI-p2)==0
ok,coeffs=positive_after_shift(PI-p3); assert ok,coeffs
# For nu>=3 the threshold expression decreases with s=2^nu; derivative numerator is negative.
s=sp.symbols('s', positive=True)
f=(s+3)/(s*(4*R-1)-3)
assert sp.simplify(sp.diff(f,s) + 12*R/(s*(4*R-1)-3)**2)==0

# Supporting factor is increasing with valuation exponent.
ok,coeffs=positive_after_shift(J-1); assert ok,coeffs
assert 16<27 and 2<3 and 8<9

def ceildiv(a,b): return (a+b-1)//b

# 36 seed inequalities h=1,...,6.
for typ in ('I','II'):
    for kk in (1,2,3):
        name=f'{typ}{kk}'
        pre=3*kk-1 if typ=='I' else 3*kk
        for h in range(1,7):
            n=2*kk+h
            Vstar=pre+ceildiv(4*h+2,3)
            E=3*Vstar-4*n
            assert E>=0
            if h==1:
                P=cores[name][0]
            else:
                Q=qcores[name][0]
                first=PI if typ=='I' else PHH
                rem=h-2
                P=Q*first*PHH**(rem//2)
                if rem%2:
                    P*=FH
            expr=C**(4*n)*J**E-P**12
            ok,coeffs=positive_after_shift(expr,allow_zero=True)
            assert ok,(name,h,n,Vstar,E,coeffs)

# Six-high extension preserves E and adds three generic HH pairs.
ok,coeffs=positive_after_shift(C**24-PHH**36)
assert ok,coeffs

# Rational majorant monotonicity and asymptotic coefficient.
num,den=sp.fraction(sp.together(-sp.diff(CH,R)))
poly=sp.Poly(sp.expand(num.subs(R,t+161)),t)
assert all(c>=0 for c in poly.all_coeffs()) and any(c>0 for c in poly.all_coeffs())
dpoly=sp.Poly(sp.expand(den.subs(R,t+161)),t)
assert all(c>0 for c in dpoly.all_coeffs())
assert sp.limit(R*CH,R,sp.oo)==sp.Rational(457841,1843200)
assert sp.Rational(457841,1843200)<sp.Rational(38273,153600)<sp.Rational(319,1280)
assert 3**200<2**317

# Continued-fraction gate under inherited external R>=2^71.
R0=1<<71
val=sp.cancel(CH.subs(R,R0))
c0=Fraction(int(sp.numer(val)),int(sp.denom(val)))

def ln_interval(x:Fraction,N=260):
    x2=x*x; term=x; acc=Fraction(0)
    for j in range(N):
        acc += term/(2*j+1)
        term *= x2
    lo=2*acc
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
assert qmax==57397300722

print('RL24 type-I high-start supporting-line verifier: PASS')
print('PI =',PI)
print('C =',C)
print('T =',T)
print('J =',J)
print('C_H asymptotic coefficient =',sp.Rational(457841,1843200),'=',float(sp.Rational(457841,1843200)))
print('R0 =',R0)
print('C_H(R0) =',c0)
print('rigorous qmax =',qmax)
print('therefore q=L/gcd(A,L) >=',qmax+1)
print('first convergent denominator beyond qmax =',first_beyond)
