from fractions import Fraction
from math import isqrt
import sympy as sp
import sys
sys.set_int_max_str_digits(100000)

R,t=sp.symbols('R t', positive=True)
H=(4*R-1)/3
f=lambda x:(9*x+5)/8
FH=4*R/(4*R-1)
PHH=16*R/(16*R-7)
T=256*R/(256*R-319)  # II k=2,h=1
U=(2187*R+3767)/(2187*R) # exceptional II k=3,h=1
S=(531441*R+1568693)/(531441*R) # exact E + II k=2,h=1 pair max
PII={
    1:(12*R+2)/(12*R-3),
    2:(12*R+2)/(12*R-3),
    3:(6561*R+12325)/(6561*R+9765),
}
cores={
'I1':32*R/(32*R-19),
'I2':256*R/(256*R-287),
'I3':(2187*R+3511)/(2187*R),
'II1':32*R/(32*R-23),
'II2':T,
'II3':U,
}
qcores={
'I1':(9*R+5)/(9*R),
'I2':(81*R+85)/(81*R),
'I3':(729*R+1085)/(729*R),
'II1':8*(4*R-1)/(32*R-23),
'II2':64*(4*R-1)/(256*R-319),
'II3':(729*R+1085)/(729*R),
}
PIk={
1:(81*R+73)/(81*R+45),
2:(729*R+989)/(729*R+765),
3:(6561*R+11557)/(6561*R+9765),
}
rfrac={1:sp.Rational(27,16),2:sp.Rational(243,128),3:sp.Rational(2187,1024)}

def positive_after_shift(expr,shift=800,allow_zero=False):
    num,den=sp.fraction(sp.cancel(expr)); num=sp.expand(num)
    if num==0: return allow_zero,[0]
    poly=sp.Poly(sp.expand(num.subs(R,t+shift)),t)
    coeffs=poly.all_coeffs()
    return all(c>=0 for c in coeffs) and any(c>0 for c in coeffs),coeffs

# Type-II terminal high z=f(last low)<f(H). If the high run continues, nu>=2 would give next odd <=(3z+1)/4<H.
ok,coeffs=positive_after_shift(H-(3*f(H)+1)/4)
assert ok,coeffs[:10]
# Hence first continued type-II HH transition has nu=1 exactly.
assert sp.factor(PII[1]-(1+sp.Rational(5,1)/(9*H)))==0
assert PII[1]==PII[2]
z3=f(f(f(R)))
assert sp.factor(PII[3]-(1+sp.Rational(5,1)/(9*z3)))==0

# Sharper high-run valuation floors inherited from RL32.
def lower_v_from_ratio(h,num,den):
    N=3**h*num; D=den; w=0
    while (2**(w+1))*D <= N: w+=1
    return w+1
vII={h:lower_v_from_ratio(h,1,1) for h in range(1,13)}
vI={kk:{h:lower_v_from_ratio(h,int(sp.numer(rfrac[kk])),int(sp.denom(rfrac[kk])))
         for h in range(1,13)} for kk in (1,2,3)}
def VH_floor(typ,kk,h):
    q=(h-1)//12; rr=(h-1)%12+1
    return (vII[rr] if typ=='II' else vI[kk][rr])+19*q

def seed(typ,kk,h):
    pre=3*kk-1 if typ=='I' else 3*kk
    vh=VH_floor(typ,kk,h)
    if typ=='I' and h==1: vh=max(vh,3)
    V=pre+vh; n=2*kk+h
    if h==1:
        P=cores[f'{typ}{kk}']
    else:
        rem=h-2
        first=PIk[kk] if typ=='I' else PII[kk]
        P=qcores[f'{typ}{kk}']*first*PHH**(rem//2)
        if rem%2: P*=FH
    return n,V,sp.factor(P)

def RHS(n,V):
    # Supporting line through T=(n,V)=(5,8) and S=(12,19), where S is the induced E+T superblock.
    return T**(12*V-19*n)*S**(8*n-5*V)

# Exceptional E=II k=3,h=1 must be followed by a k=2 block.
a2=(256*R-319)/243
a1=(32*R-23)/27
g3=lambda x:(2187*x+3767)/2048
ok,coeffs=positive_after_shift(g3(R)-a2)
assert ok,coeffs[:10]
ok,coeffs=positive_after_shift(a1-g3(a2))
assert ok,coeffs[:10]

# Exact collapse for E followed by II k=2,h=1.
x=sp.symbols('x',positive=True)
P3x=(2187*x+3767)/(2187*x)
y=g3(x)
P2y=(243*y+319)/(243*y)
assert sp.factor(P3x*P2y-(531441*x+1568693)/(531441*x))==0
assert sp.factor(sp.diff((531441*x+1568693)/(531441*x),x)) == -sp.Rational(1568693,531441)/x**2

# Every non-E seed satisfies the new support line for R>=800.
E=('II',3,1)
for typ in ('I','II'):
    for kk in (1,2,3):
        for h in range(1,13):
            if (typ,kk,h)==E: continue
            n,V,P=seed(typ,kk,h)
            ok,coeffs=positive_after_shift(RHS(n,V)-P,allow_zero=True)
            assert ok,(typ,kk,h,n,V,coeffs[:10])

# Pair E with its forced k=2 successor. Use exact S if successor is direct II2; otherwise U times the successor bound.
nE,VE,PE=seed(*E)
for typ in ('I','II'):
    for h in range(1,13):
        n,V,P=seed(typ,2,h)
        PP=S if (typ=='II' and h==1) else PE*P
        ok,coeffs=positive_after_shift(RHS(nE+n,VE+V)-PP,allow_zero=True)
        assert ok,(typ,h,nE+n,VE+V,coeffs[:10])

# The exceptional residue h=1 is paired, so the h==13 representative must be checked separately before the +12 extension is used on h=13,25,... .
n13,V13,P13=seed('II',3,13)
ok,coeffs=positive_after_shift(RHS(n13,V13)-P13,allow_zero=True)
assert ok,('II',3,13,n13,V13,coeffs[:10])

# h->h+12 adds n=12, V>=19, product <=PHH^6. RHS gains exactly S.
ok,coeffs=positive_after_shift(S-PHH**6)
assert ok,coeffs[:10]

# RHS increases with actual V by T^12/S^5.
K=sp.factor(T**12/S**5)
ok,coeffs=positive_after_shift(K-1)
assert ok,coeffs[:10]
for expr in (T,S,K):
    ok,coeffs=positive_after_shift(-sp.diff(expr,R))
    assert ok,coeffs[:10]
assert sp.Rational(sp.numer(K.subs(R,800)),sp.denom(K.subs(R,800))) < 2

cT=sp.limit(R*(T-1),R,sp.oo)
cS=sp.limit(R*(S-1),R,sp.oo)
assert cT==sp.Rational(319,256)
assert cS==sp.Rational(1568693,531441)

# Rigorous R0 coefficient + continued-fraction exclusion.
def ln_ratio_interval(u:Fraction,N=120):
    assert u>0
    if u==1:return Fraction(0),Fraction(0)
    if u<1:
        lo,hi=ln_ratio_interval(1/u,N);return -hi,-lo
    xx=(u-1)/(u+1);x2=xx*xx;term=xx;acc=Fraction(0)
    for j in range(N):
        acc+=term/Fraction(2*j+1);term*=x2
    lo=2*acc;tail=2*term/Fraction(2*N+1)/(1-x2)
    return lo,lo+tail

R0=1<<71
def eval_frac(expr):
    e=sp.cancel(expr.subs(R,R0));return Fraction(int(sp.numer(e)),int(sp.denom(e)))
T0=eval_frac(T);S0=eval_frac(S)
tlo,thi=ln_ratio_interval(T0,90);slo,shi=ln_ratio_interval(S0,90)
l2lo,l2hi=ln_ratio_interval(Fraction(2),280);l3lo,l3hi=ln_ratio_interval(Fraction(3),280)
blo=l3lo/l2hi;bhi=l3hi/l2lo
# N=(12 beta-19)t +(8-5 beta)s, positive partials in beta,t,s.
assert 12*blo-19>0 and 8-5*bhi>0 and 12*tlo-5*shi>0
Nlo=(12*blo-19)*tlo+(8-5*blo)*slo
Nhi=(12*bhi-19)*thi+(8-5*bhi)*shi
# D=1-(12t-5s)/ln2
klo=12*tlo-5*shi;khi=12*thi-5*slo
Dlo=1-khi/l2lo;Dhi=1-klo/l2hi
assert Nlo>0 and Dlo>0
C0_lo=Nlo/Dhi;C0_hi=Nhi/Dlo
assert 0<C0_lo<C0_hi

def cf_interval(lo,hi,terms=45):
    out=[]
    for _ in range(terms):
        a0=lo.numerator//lo.denominator;a1=hi.numerator//hi.denominator
        assert a0==a1;out.append(a0);lo-=a0;hi-=a0;assert lo>0;lo,hi=1/hi,1/lo
    return out
cf=cf_interval(blo,bhi)
Tleg=l2lo/(2*C0_hi)
qmax=isqrt(Tleg.numerator//Tleg.denominator)
while 2*qmax*qmax*C0_hi>=l2lo:qmax-=1
while 2*(qmax+1)*(qmax+1)*C0_hi<l2lo:qmax+=1
pm2,pm1=0,1;qm2,qm1=1,0;above=[];first_beyond=None
for aa in cf:
    p=aa*pm1+pm2;q=aa*qm1+qm2;pm2,pm1=pm1,p;qm2,qm1=qm1,q
    dlo=p*l2lo-q*l3hi;dhi=p*l2hi-q*l3lo;assert dhi<0 or dlo>0
    if q<=qmax and dlo>0:
        assert dlo>q*C0_hi;above.append((p,q))
    if q>qmax and first_beyond is None:
        first_beyond=(p,q,dlo>0);break
expected=[(2,1),(8,5),(65,41),(485,306),(24727,15601),(125743,79335),(301994,190537),(17087915,10781274),(272500658,171928773),(630138897,397573379),(10439860591,6586818670)]
assert above==expected
assert first_beyond==(103768467013,65470613321,False)

print('RL34 type-II continuation / induced-superblock verifier: PASS')
print('support valid for R>=800; CF application uses inherited external R>=2^71')
print('S =',S)
import mpmath as mp
mp.mp.dps=60
beta=mp.log(3)/mp.log(2);ct=mp.mpf(319)/256;cs=mp.mpf(1568693)/531441
casym=(12*beta-19)*ct+(8-5*beta)*cs
print('global asymptotic coefficient =',casym)
print('R0*C_exact(R0) interval =',mp.mpf(R0*C0_lo.numerator)/C0_lo.denominator,mp.mpf(R0*C0_hi.numerator)/C0_hi.denominator)
print('rigorous qmax =',qmax)
print('therefore q=L/gcd(A,L) >=',qmax+1)
print('first convergent denominator beyond qmax =',first_beyond)
