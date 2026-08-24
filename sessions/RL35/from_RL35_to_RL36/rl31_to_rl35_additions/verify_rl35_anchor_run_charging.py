from fractions import Fraction
from math import isqrt
import itertools
import sympy as sp
import sys
sys.set_int_max_str_digits(100000)

R,t=sp.symbols('R t', positive=True)
SHIFT=10000
H=(4*R-1)/3
f=lambda x:(9*x+5)/8
FH=4*R/(4*R-1)
PHH=16*R/(16*R-7)
T=256*R/(256*R-319)
U=(2187*R+3767)/(2187*R)
S=(531441*R+1568693)/(531441*R)
Q=(2000*R+1)/(2000*R)
PII={1:(12*R+2)/(12*R-3),2:(12*R+2)/(12*R-3),3:(6561*R+12325)/(6561*R+9765)}
cores={
'I1':32*R/(32*R-19),'I2':256*R/(256*R-287),'I3':(2187*R+3511)/(2187*R),
'II1':32*R/(32*R-23),'II2':T,'II3':U,
}
qcores={
'I1':(9*R+5)/(9*R),'I2':(81*R+85)/(81*R),'I3':(729*R+1085)/(729*R),
'II1':8*(4*R-1)/(32*R-23),'II2':64*(4*R-1)/(256*R-319),'II3':(729*R+1085)/(729*R),
}
PIk={1:(81*R+73)/(81*R+45),2:(729*R+989)/(729*R+765),3:(6561*R+11557)/(6561*R+9765)}
rfrac={1:sp.Rational(27,16),2:sp.Rational(243,128),3:sp.Rational(2187,1024)}

def positive_after_shift(expr,shift=SHIFT,allow_zero=False):
    num,den=sp.fraction(sp.cancel(expr)); num=sp.Poly(num,R)
    if num.is_zero: return allow_zero,[0]
    shifted=num.shift(shift)
    coeffs=shifted.all_coeffs()
    return all(c>=0 for c in coeffs) and any(c>0 for c in coeffs),coeffs

def lower_v_from_ratio(h,num,den):
    N=3**h*num; D=den; w=0
    while (2**(w+1))*D<=N:w+=1
    return w+1
vII={h:lower_v_from_ratio(h,1,1) for h in range(1,13)}
vI={kk:{h:lower_v_from_ratio(h,int(sp.numer(rfrac[kk])),int(sp.denom(rfrac[kk]))) for h in range(1,13)} for kk in (1,2,3)}
def VH_floor(typ,kk,h):
    q=(h-1)//12; rr=(h-1)%12+1
    return (vII[rr] if typ=='II' else vI[kk][rr])+19*q

def seed(typ,kk,h):
    pre=3*kk-1 if typ=='I' else 3*kk
    vh=VH_floor(typ,kk,h)
    if typ=='I' and h==1:vh=max(vh,3)
    V=pre+vh; n=2*kk+h
    if h==1:P=cores[f'{typ}{kk}']
    else:
        rem=h-2
        first=PIk[kk] if typ=='I' else PII[kk]
        P=qcores[f'{typ}{kk}']*first*PHH**(rem//2)
        if rem%2:P*=FH
    return n,V,sp.factor(P)

def SUPPORT(n,V):
    return T**(12*V-19*n)*S**(8*n-5*V)

# Type-II continuation: if its terminal high is followed by another high, outgoing valuation is exactly 1.
ok,coeffs=positive_after_shift(H-(3*f(H)+1)/4)
assert ok,coeffs[:10]
assert sp.factor(PII[1]-(1+sp.Rational(5,1)/(9*H)))==0
z3=f(f(f(R)))
assert sp.factor(PII[3]-(1+sp.Rational(5,1)/(9*z3)))==0

# Direct exceptional E=II3,h=1 has forced k=2 successor.
a2=(256*R-319)/243; a1=(32*R-23)/27
g3=lambda xx:(2187*xx+3767)/2048
ok,_=positive_after_shift(g3(R)-a2);assert ok
ok,_=positive_after_shift(a1-g3(a2));assert ok

# Itemization:
# T item = II2,h=1 not consumed by E.
# S item = E followed by T, with exact product S.
# E followed by any other k=2 block is one nonanchor composite item.
# All other blocks are nonanchor individual items.

# Nonanchor individuals pay for themselves plus up to 24 odd states of a trailing 1-2 anchor-item remainder.
for typ in ('I','II'):
    for kk in (1,2,3):
        for h in range(1,13):
            if (typ,kk,h) in (('II',3,1),('II',2,1)):
                continue
            n,V,P=seed(typ,kk,h)
            ok,coeffs=positive_after_shift(SUPPORT(n,V)-P*Q**(n+24),allow_zero=True)
            assert ok,(typ,kk,h,n,V,coeffs[:10])
# h==13 bases are needed for the two h==1 anchor/paired residues before the +12 extension can be used.
for typ,kk in (('II',2),('II',3)):
    n,V,P=seed(typ,kk,13)
    ok,coeffs=positive_after_shift(SUPPORT(n,V)-P*Q**(n+24),allow_zero=True)
    assert ok,(typ,kk,13,n,V,coeffs[:10])

# Nonanchor E+k2 composites; E+T is the S anchor and is excluded here.
nE,VE,PE=seed('II',3,1)
for typ in ('I','II'):
    for h in range(1,13):
        if typ=='II' and h==1:continue
        n,V,P=seed(typ,2,h)
        nt,vt=nE+n,VE+V
        ok,coeffs=positive_after_shift(SUPPORT(nt,vt)-PE*P*Q**(nt+24),allow_zero=True)
        assert ok,('Epair',typ,h,nt,vt,coeffs[:10])
# Special h==13 base for E + (II2,h=13), since h==1 is the S anchor.
n,V,P=seed('II',2,13);nt,vt=nE+n,VE+V
ok,coeffs=positive_after_shift(SUPPORT(nt,vt)-PE*P*Q**(nt+24),allow_zero=True)
assert ok,('Epair','II',13,nt,vt,coeffs[:10])

# Extension h->h+12: product gains <=PHH^6, support gains S, required Q power gains Q^12.
ok,coeffs=positive_after_shift(S-PHH**6*Q**12)
assert ok,coeffs[:10]
# Support increases with actual V.
K=sp.factor(T**12/S**5)
ok,coeffs=positive_after_shift(K-1)
assert ok,coeffs[:10]

# --- Exact anchor-item dynamics and 3/4/5-word charging. ---
# T: map g2, product pT. S: E+T map, exact collapsed product pS.
maps={
'T':(Fraction(243,256),Fraction(319,256)),
'S':(Fraction(531441,524288),Fraction(1568693,524288)),
}
domain_low={'S':(Fraction(1),Fraction(0)),'T':(Fraction(256,243),Fraction(-319,243))}
domain_high={'S':(Fraction(256,243),Fraction(-319,243)),'T':(Fraction(32,27),Fraction(-23,27))}

def lin_expr(z):
    return sp.Rational(z[0].numerator,z[0].denominator)*R+sp.Rational(z[1].numerator,z[1].denominator)
def lin_eval(z,rval):return z[0]*rval+z[1]
def preimage(bound,A,B):return (bound[0]/A,(bound[1]-B)/A)
def word_interval(word):
    A=Fraction(1);B=Fraction(0); lows=[]; highs=[]
    for ch in word:
        lows.append(preimage(domain_low[ch],A,B))
        highs.append(preimage(domain_high[ch],A,B))
        a,b=maps[ch];A,B=a*A,a*B+b
    lo=max(lows,key=lambda z:lin_eval(z,SHIFT))
    hi=min(highs,key=lambda z:lin_eval(z,SHIFT))
    return lo,hi,lows,highs,A,B

allowed_words={}
for m in (3,4,5):
    good=[]
    for word in map(''.join,itertools.product('ST',repeat=m)):
        lo,hi,lows,highs,A,B=word_interval(word)
        loe,hie=lin_expr(lo),lin_expr(hi)
        if lin_eval(lo,SHIFT)>=lin_eval(hi,SHIFT):
            # certify permanently empty for every R>=SHIFT
            ok,_=positive_after_shift(loe-hie,allow_zero=True)
            assert ok,('empty-domain',word)
            continue
        # certify chosen lower endpoint is the max of all lower constraints and lies below every upper constraint.
        for z in lows:
            ok,_=positive_after_shift(loe-lin_expr(z),allow_zero=True);assert ok,('low-domain',word,z)
        for z in highs:
            ok,_=positive_after_shift(lin_expr(z)-loe);assert ok,('high-domain',word,z)
        # Entire word correction product is 1+B/(A*x), decreasing in its initial low x.
        assert B>0
        Pmax=1+sp.Rational(B.numerator,B.denominator)/(sp.Rational(A.numerator,A.denominator)*loe)
        n=12*word.count('S')+5*word.count('T')
        sup=T**word.count('T')*S**word.count('S')
        ok,coeffs=positive_after_shift(sup-Pmax*Q**n)
        assert ok,('anchor-word',word,n,coeffs[:10])
        good.append(word)
    allowed_words[m]=good

# A pure-anchor cycle of only one or two items is impossible at R>=SHIFT: any positive affine fixed point is <SHIFT.
for word in ('T','S','TT','TS','ST','SS'):
    A=Fraction(1);B=Fraction(0)
    for ch in word:
        a,b=maps[ch];A,B=a*A,a*B+b
    if A<1:
        fixed=B/(1-A)
        assert fixed<SHIFT,(word,fixed)
    else:
        # x=A*x+B has no positive solution if A>=1 and B>0.
        assert B>0

# Combinatorial globalization:
# - if a nonanchor item exists, each maximal anchor run is split into 3-item chunks plus <=2-item remainder;
#   the nonanchor Q^(n+24) reserve pays the remainder (each anchor item has n<=12).
# - if all items are anchors and there are >=3 items, every item count >=3 is a sum of 3,4,5, so the cycle is
#   partitioned into certified anchor words. 1-2 item pure-anchor cycles were excluded above.
# Therefore lambda*Q^L <= T^(12A-19L) S^(8L-5A).

# --- Rigorous exact coefficient at inherited R0 and continued-fraction gate. ---
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
T0,S0,Q0=eval_frac(T),eval_frac(S),eval_frac(Q)
tlo,thi=ln_ratio_interval(T0,90);slo,shi=ln_ratio_interval(S0,90);qlo,qhi=ln_ratio_interval(Q0,90)
l2lo,l2hi=ln_ratio_interval(Fraction(2),280);l3lo,l3hi=ln_ratio_interval(Fraction(3),280)
blo=l3lo/l2hi;bhi=l3hi/l2lo
assert 12*blo-19>0 and 8-5*bhi>0 and 12*tlo-5*shi>0
Nlo=(12*blo-19)*tlo+(8-5*blo)*slo
Nhi=(12*bhi-19)*thi+(8-5*bhi)*shi
Mlo=Nlo-qhi;Mhi=Nhi-qlo
klo=12*tlo-5*shi;khi=12*thi-5*slo
Dlo=1-khi/l2lo;Dhi=1-klo/l2hi
assert Mlo>0 and Dlo>0
C0_lo=Mlo/Dhi;C0_hi=Mhi/Dlo
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

print('RL35 anchor-run charging verifier: PASS')
print('analytic support/charging threshold R >=',SHIFT)
print('Q =',Q)
print('allowed 3/4/5 anchor words =',allowed_words)
import mpmath as mp
mp.mp.dps=60
beta=mp.log(3)/mp.log(2);ct=mp.mpf(319)/256;cs=mp.mpf(1568693)/531441
casym=(12*beta-19)*ct+(8-5*beta)*cs-mp.mpf(1)/2000
print('global asymptotic coefficient =',casym)
print('R0*C_exact(R0) interval =',mp.mpf(R0*C0_lo.numerator)/C0_lo.denominator,mp.mpf(R0*C0_hi.numerator)/C0_hi.denominator)
print('rigorous qmax =',qmax)
print('therefore q=L/gcd(A,L) >=',qmax+1)
print('first convergent denominator beyond qmax =',first_beyond)
