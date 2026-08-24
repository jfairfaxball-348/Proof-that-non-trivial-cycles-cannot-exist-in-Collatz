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
T=256*R/(256*R-319)                 # type-II k=2,h=1
U=(2187*R+3767)/(2187*R)            # type-II k=3,h=1
K=sp.factor(T**7/U**5)

# Repaired type-I h=1 cores: h=1 forces outgoing valuation 3.
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
# Type-I first HH pair, now using the exact terminal-height floor for each k.
PIk={
1:(81*R+73)/(81*R+45),
2:(729*R+989)/(729*R+765),
3:(6561*R+11557)/(6561*R+9765),
}
rfrac={1:sp.Rational(27,16),2:sp.Rational(243,128),3:sp.Rational(2187,1024)}

def positive_after_shift(expr,shift=161,allow_zero=False):
    num,den=sp.fraction(sp.together(expr))
    num=sp.expand(num)
    if num==0:
        return allow_zero,[0]
    poly=sp.Poly(sp.expand(num.subs(R,t+shift)),t)
    coeffs=poly.all_coeffs()
    return all(c>=0 for c in coeffs) and any(c>0 for c in coeffs),coeffs

# --- Analytic repair checks for type-I h=1 and h>=2. ---
zmax=2*f(H)
# If terminal type-I high is followed directly by a low (h=1), nu=1,2 remain high;
# nu>=4 falls below R. Thus nu=3 exactly.
for kk in (1,2,3):
    zmin=2*(f(R) if kk==1 else f(f(R)) if kk==2 else f(f(f(R))))
    ok,_=positive_after_shift((3*zmin+1)/4-H)  # nu=2 still high
    assert ok
ok,_=positive_after_shift(R-(3*zmax+1)/16)    # nu>=4 below minimum
assert ok
# For h>=2, nu>=3 would already leave the high interval, hence first HH nu is 1 or 2.
ok,_=positive_after_shift(H-(3*zmax+1)/8)
assert ok

# h=1 next-low >=R yields exact start thresholds for k=1,2; k=3 already clears it at x=R.
xmins={1:(32*R-19)/27, 2:(256*R-287)/243, 3:R}
for kk in (1,2):
    x=xmins[kk]; fk=x
    for _ in range(kk): fk=f(fk)
    assert sp.factor(2*fk-(8*R-1)/3)==0
fk=f(f(f(R)))
ok,_=positive_after_shift(2*fk-(8*R-1)/3)
assert ok
# Generic type-I core products decrease with start x.
generic_I_core={1:lambda x:(27*x+19)/(27*x),
                2:lambda x:(243*x+287)/(243*x),
                3:lambda x:(2187*x+3511)/(2187*x)}
for kk in (1,2,3):
    assert sp.factor(generic_I_core[kk](xmins[kk])-cores[f'I{kk}'])==0

# Exact k-specific first-pair formulas from F(a)F(b)=1+(2^nu+3)/(9a), nu<=2.
A={1:2*f(R),2:2*f(f(R)),3:2*f(f(f(R)))}
for kk in (1,2,3):
    assert sp.factor(PIk[kk]-(1+sp.Rational(7,1)/(9*A[kk])))==0

# --- Sharper high-run valuation floor. ---
# Exact segment identity gives 2^V_H > 3^h h0/ell.
# Type II: h0/ell>1.
# Type I: h0/ell>A_k/H > r_k.
for kk in (1,2,3):
    ok,_=positive_after_shift(A[kk]/H-rfrac[kk])
    assert ok
assert 2**19 < 3**12

def lower_v_from_ratio(h,num,den):
    # If 2^w <= 3^h*num/den, then strict 2^V > RHS forces V>=w+1.
    N=3**h*num; D=den; w=0
    while (2**(w+1))*D <= N:
        w+=1
    return w+1

vII={h:lower_v_from_ratio(h,1,1) for h in range(1,13)}
vI={kk:{h:lower_v_from_ratio(h,int(sp.numer(rfrac[kk])),int(sp.denom(rfrac[kk])))
         for h in range(1,13)} for kk in (1,2,3)}

def VH_floor(typ,kk,h):
    q=(h-1)//12; r=(h-1)%12+1
    base=vII[r] if typ=='II' else vI[kk][r]
    return base+19*q

# --- New local supporting line. ---
# P <= T^(7V-11n) U^(8n-5V).
# Exact equality anchors: II2,h=1 => (n,V,P)=(5,8,T),
#                         II3,h=1 => (7,11,U).
for typ in ('I','II'):
    for kk in (1,2,3):
        name=f'{typ}{kk}'
        pre=3*kk-1 if typ=='I' else 3*kk
        for h in range(1,13):
            n=2*kk+h
            vh=VH_floor(typ,kk,h)
            if typ=='I' and h==1:
                vh=max(vh,3)
            Vstar=pre+vh
            if h==1:
                P=cores[name]
            else:
                rem=h-2
                P=qcores[name]*(PIk[kk] if typ=='I' else PHH)
                P*=PHH**(rem//2)
                if rem%2:
                    P*=FH
            rhs=T**(7*Vstar-11*n)*U**(8*n-5*Vstar)
            ok,coeffs=positive_after_shift(rhs-P,allow_zero=True)
            assert ok,(name,h,n,Vstar,coeffs[:10])

# h->h+12: n+12, certified V+19, and six additional generic HH pairs.
# The support RHS gains exactly T*U.
ok,coeffs=positive_after_shift(T*U-PHH**6)
assert ok,coeffs[:10]

# Support RHS increases with actual V because T^7/U^5>1.
ok,coeffs=positive_after_shift(K-1)
assert ok,coeffs[:10]
# T,U,K decrease; K<2 at R=161 and hence denominator below is positive.
for expr in (T,U,K):
    ok,coeffs=positive_after_shift(-sp.diff(expr,R))
    assert ok,coeffs[:10]
assert sp.Rational(sp.numer(K.subs(R,161)),sp.denom(K.subs(R,161))) < 2

cT=sp.limit(R*(T-1),R,sp.oo)
cU=sp.limit(R*(U-1),R,sp.oo)
assert cT==sp.Rational(319,256)
assert cU==sp.Rational(3767,2187)

# --- Rigorous exact coefficient at R0 and CF gate. ---
def ln_ratio_interval(u:Fraction,N=120):
    assert u>0
    if u==1: return Fraction(0),Fraction(0)
    if u<1:
        lo,hi=ln_ratio_interval(1/u,N)
        return -hi,-lo
    x=(u-1)/(u+1)
    x2=x*x; term=x; acc=Fraction(0)
    for j in range(N):
        acc += term/Fraction(2*j+1)
        term *= x2
    lo=2*acc
    tail=2*term/Fraction(2*N+1)/(1-x2)
    return lo,lo+tail

R0=1<<71
T0=Fraction(int(sp.numer(sp.cancel(T.subs(R,R0)))),int(sp.denom(sp.cancel(T.subs(R,R0)))))
U0=Fraction(int(sp.numer(sp.cancel(U.subs(R,R0)))),int(sp.denom(sp.cancel(U.subs(R,R0)))))
tlo,thi=ln_ratio_interval(T0,80)
ulo,uhi=ln_ratio_interval(U0,80)
l2lo,l2hi=ln_ratio_interval(Fraction(2),260)
l3lo,l3hi=ln_ratio_interval(Fraction(3),260)
blo=l3lo/l2hi; bhi=l3hi/l2lo
# N=(7 beta-11)t +(8-5 beta)u = -11t+8u+beta(7t-5u).
# Since k=7t-5u>0, N increases in beta,t,u (partials are positive in our beta interval).
Nhi=(7*bhi-Fraction(11))*thi+(Fraction(8)-5*bhi)*uhi
Nlo=(7*blo-Fraction(11))*tlo+(Fraction(8)-5*blo)*ulo
# D=1-(7t-5u)/ln2. Lower D uses upper k and lower ln2.
khi=7*thi-5*ulo
klo=7*tlo-5*uhi
Dlo=Fraction(1)-khi/l2lo
Dhi=Fraction(1)-klo/l2hi
assert Nlo>0 and Dlo>0
C0_lo=Nlo/Dhi; C0_hi=Nhi/Dlo
assert 0<C0_lo<C0_hi

# Continued fraction reconstruction and exclusion.
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

cf=cf_interval(blo,bhi)
Tleg=l2lo/(2*C0_hi)
qmax=isqrt(Tleg.numerator//Tleg.denominator)
while 2*qmax*qmax*C0_hi >= l2lo: qmax-=1
while 2*(qmax+1)*(qmax+1)*C0_hi < l2lo: qmax+=1

pm2,pm1=0,1; qm2,qm1=1,0
above=[]; first_beyond=None
for aa in cf:
    p=aa*pm1+pm2; q=aa*qm1+qm2
    pm2,pm1=pm1,p; qm2,qm1=qm1,q
    dlo=p*l2lo-q*l3hi
    dhi=p*l2hi-q*l3lo
    assert dhi<0 or dlo>0
    if q<=qmax and dlo>0:
        assert dlo > q*C0_hi
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

print('RL32 refined high-run supporting-line verifier: PASS')
print('vII residues h=1..12 =',vII)
print('vI residues h=1..12 =',vI)
print('T =',T)
print('U =',U)
print('K=T^7/U^5 >1 and decreasing')
import mpmath as mp
mp.mp.dps=50
beta=mp.log(3)/mp.log(2)
casym=(7*beta-11)*mp.mpf(319)/256+(8-5*beta)*mp.mpf(3767)/2187
print('global asymptotic coefficient =',casym)
print('R0*C_exact(R0) interval =',float(R0*C0_lo),float(R0*C0_hi))
print('rigorous qmax =',qmax)
print('therefore q=L/gcd(A,L) >=',qmax+1)
print('first convergent denominator beyond qmax =',first_beyond)
