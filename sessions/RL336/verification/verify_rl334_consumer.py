#!/usr/bin/env python3
import contextlib,io,runpy
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
with contextlib.redirect_stdout(io.StringIO()): B=runpy.run_path(str(Path(__file__).with_name('verify_rl334_self_consistent_ownership.py')))
A=B['A'];ELL=B['ELL'];l2=B['l2lo'];LAM=B['LAM'];full=B['full'];b2=B['b2'];rho59=B['rho59'];BOOT=B['H'];CAP=B['CAP']
C=Fraction(25_120_009_946_627,10**14)
@lru_cache(None)
def W(K):
 s1=K*(K+1)//2;s2=K*(K+1)*(2*K+1)//6;s3=s1*s1;s4=K*(K+1)*(2*K+1)*(3*K*K+3*K-1)//30
 return Fraction(K)+l2*s1/ELL+l2**2*s2/(2*ELL**2)+l2**3*s3/(6*ELL**3)+l2**4*s4/(24*ELL**4)
def ks(rho):
 K=(2*(ELL-rho+1)-b2+44)//45
 s=b2-(2*(ELL-rho+1)-45*K)
 assert 0<=s<=44
 return K,s
def St(K0,h,s):
 K=K0+h;S=45*h+s
 return Fraction(K)+C*(Fraction(K,2)-Fraction(45,44)*S-2)
def gain(K0,s):
 w=W(K0);m=St(K0,1,s)-St(K0,0,s);assert m<1
 x=(St(K0,0,s)-w)/(1-m);q=max(0,x.numerator//x.denominator)
 vals=[(h,max(Fraction(h),St(K0,h,s)-w)) for h in {0,q,q+1}]
 return min(vals,key=lambda r:r[1])
def omitterm(r):return Fraction(1<<((A*r)//ELL),3**r)/LAM
# exact finite rho 60..2894 incrementally
om=Fraction(0); maxrhs=None; mingain=None
for r in range(1,2894):
 om+=omitterm(r);rho=r+1
 if rho<60:continue
 K,s=ks(rho);h,g=gain(K,s);R=1+(full-om)/3-W(K)/(12*LAM)-g/(12*LAM)
 assert R<BOOT
 if maxrhs is None or R>maxrhs[0]:maxrhs=(R,rho,h,g)
 mingain=g if mingain is None else min(mingain,g)
R60=None
# recompute rho60 exactly
om59=sum((omitterm(r) for r in range(1,60)),Fraction())
K60,s60=ks(60);h60,g60=gain(K60,s60);R60=1+(full-om59)/3-W(K60)/(12*LAM)-g60/(12*LAM)
assert h60==58_816_735 and g60==58_816_735
assert R60.numerator//R60.denominator==CAP and R60<BOOT
# Uniform bridge: worst K at upper end and worst endpoint slack.
UNIFORM_END=21_999_999
Kmin,_=ks(UNIFORM_END);hu,gu=gain(Kmin,44)
# structural-minus-weight improves as K decreases; check at largest K.
assert St(K60+1,0,0)-St(K60,0,0) > W(K60+1)-W(K60)
# exact omitted sum to rho=2895
om2894=sum((omitterm(r) for r in range(1,2895)),Fraction())
K2895,s2895=ks(2895)
R2895=1+(full-om2894)/3-W(K2895)/(12*LAM)-gu/(12*LAM)
assert R2895<BOOT
# rigorous ordinary consumer at rho=22,000,000 using floor fixed-point omitted sum Q=2^256.
Q=1<<256
sumq=int(Path(__file__).with_name('RL334_OMIT_RHO22000000_Q256.txt').read_text().strip())
omit22_lower=Fraction(sumq,Q)/LAM
rho=22_000_000;K22,_=ks(rho)
R22=1+(full-omit22_lower)/3-W(K22)/(12*LAM)
assert R22<BOOT
assert rho59<BOOT
print('RL334_Q22_CONSUMER_GREEN')
print('rho60_h_gain',h60,int(g60),'rhs',float(R60),'floor',R60.numerator//R60.denominator)
print('finite_60_2894_max',maxrhs[1],float(maxrhs[0]),'min_gain',float(mingain))
print('uniform_gain',hu,float(gu),'bridge2895',float(R2895))
print('ordinary_rho22000000_upper',float(R22),'bootstrap',BOOT,'cap',CAP)
