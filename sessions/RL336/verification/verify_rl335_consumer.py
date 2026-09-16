#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
A=217_976_794_617;ELL=137_528_045_312
BOOT=32_546_289_531; CAP=BOOT-1
C=Fraction(25_120_009_946_627,10**14)
def log_interval_atanh(x,terms=280):
 x2=x*x;term=x;total=Fraction(0)
 for j in range(terms): total+=term/(2*j+1);term*=x2
 lo=2*total;return lo,lo+2*term/(2*terms+1)/(1-x2)
l2,_=log_interval_atanh(Fraction(1,3));LAM=1+Fraction(1,1<<40);b2=129
x=l2/ELL; full=1/(2*(x+x*x/2))-Fraction(1,2)
rho59=Fraction(5,6)+LAM*(1<<(((A-ELL)*59)//ELL))
@lru_cache(None)
def W(K):
 s1=K*(K+1)//2;s2=K*(K+1)*(2*K+1)//6;s3=s1*s1;s4=K*(K+1)*(2*K+1)*(3*K*K+3*K-1)//30
 return Fraction(K)+l2*s1/ELL+l2**2*s2/(2*ELL**2)+l2**3*s3/(6*ELL**3)+l2**4*s4/(24*ELL**4)
def ks(rho):
 K=(2*(ELL-rho+1)-b2+44)//45; s=b2-(2*(ELL-rho+1)-45*K); assert 0<=s<=44; return K,s
def St(K0,h,s):
 K=K0+h;S=45*h+s;return Fraction(K)+C*(Fraction(K,2)-Fraction(57,56)*S-Fraction(3,2))
def gain(K0,s):
 w=W(K0);m=St(K0,1,s)-St(K0,0,s);assert m<1
 x=(St(K0,0,s)-w)/(1-m);q=max(0,x.numerator//x.denominator)
 vals=[(h,max(Fraction(h),St(K0,h,s)-w)) for h in {0,q,q+1}];return min(vals,key=lambda r:r[1])
def omitterm(r):return Fraction(1<<((A*r)//ELL),3**r)/LAM
om=Fraction(0);maxrhs=None
for r in range(1,2894):
 om+=omitterm(r);rho=r+1
 if rho<60:continue
 K,s=ks(rho);h,g=gain(K,s);R=1+(full-om)/3-W(K)/(12*LAM)-g/(12*LAM);assert R<BOOT
 if maxrhs is None or R>maxrhs[0]:maxrhs=(R,rho,h,g)
om59=sum((omitterm(r) for r in range(1,60)),Fraction())
K60,s60=ks(60);h60,g60=gain(K60,s60);R60=1+(full-om59)/3-W(K60)/(12*LAM)-g60/(12*LAM)
assert (K60,s60)==(6_112_357_564,3) and h60==59_101_261 and g60==59_101_261
assert R60<BOOT and R60.numerator//R60.denominator==32_546_289_526
Kmin,_=ks(21_999_999);hu,gu=gain(Kmin,44)
assert St(K60+1,0,0)-St(K60,0,0)>W(K60+1)-W(K60)
om2894=sum((omitterm(r) for r in range(1,2895)),Fraction());K2895,_=ks(2895)
R2895=1+(full-om2894)/3-W(K2895)/(12*LAM)-gu/(12*LAM)
assert R2895<BOOT and R2895.numerator//R2895.denominator==CAP
Q=1<<256
sumq=1837579385638164133130126995943207589379866951507814208093753543882794175686281825504
omit22_lower=Fraction(sumq,Q)/LAM;K22,_=ks(22_000_000)
R22=1+(full-omit22_lower)/3-W(K22)/(12*LAM)
assert R22<BOOT and rho59<BOOT
print('RL335_Q28_CONSUMER_GREEN')
print('rho60',K60,s60,'h',h60,'rhs',float(R60),'floor',R60.numerator//R60.denominator)
print('finite_max',maxrhs[1],float(maxrhs[0]))
print('uniform_gain',hu,float(gu),'bridge2895',float(R2895),'floor',R2895.numerator//R2895.denominator)
print('ordinary22000000',float(R22),'cap',CAP)
