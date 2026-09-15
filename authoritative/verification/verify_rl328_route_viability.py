#!/usr/bin/env python3
from fractions import Fraction
from math import gcd
A=217_976_794_617; ELL=137_528_045_312; RHO=60; T=ELL-RHO
LAMBDA_UPPER=1+Fraction(1,1<<40); HIGH=20_390_252_058
assert gcd(A,ELL)==1

def log_interval_atanh(x,terms=280):
    x2=x*x; term=x; total=Fraction(0)
    for i in range(terms): total+=term/(2*i+1); term*=x2
    lower=2*total; return lower, lower+2*term/(2*terms+1)/(1-x2)
ln2,_=log_interval_atanh(Fraction(1,3))
x=ln2/ELL
full=1/(2*(x+x*x/2))-Fraction(1,2)
def omitted(last):
    return sum((Fraction(1<<((A*r)//ELL),3**r) for r in range(1,last+1)),Fraction(0))/LAMBDA_UPPER
ideal=(full-omitted(RHO-1))/3
def w(k):
    s1=k*(k+1)//2; s2=k*(k+1)*(2*k+1)//6; s3=s1*s1; s4=k*(k+1)*(2*k+1)*(3*k*k+3*k-1)//30
    return Fraction(k)+ln2*s1/ELL+ln2**2*s2/(2*ELL**2)+ln2**3*s3/(6*ELL**3)+ln2**4*s4/(24*ELL**4)
def rhs(k,f=1): return 1+ideal-f*w(k)/(12*LAMBDA_UPPER)
Kgraph=(3*(T+1)+51)//52
assert Kgraph==7_934_310_304
assert 32_393_913_987 < rhs(Kgraph) < 32_393_913_988

def first(f):
    lo,hi=0,ELL
    while lo<hi:
        m=(lo+hi)//2
        if rhs(m,f)<HIGH: hi=m
        else: lo=m+1
    return lo
k1=first(1); k2=first(2)
assert k1==112_933_933_538 and k2==64_392_480_586
r1=Fraction((T+1)-k1,k1); r2=Fraction((T+1)-k2,k2)
assert r1<Fraction(218,1000) and r2<Fraction(1136,1000) and Fraction(49,3)>r2
print('RL328_ROUTE_VIABILITY_VERIFIER_GREEN')
print('optimistic_graph_carry_rhs_lt',float(rhs(Kgraph)))
print('K_required_current_consumer',k1)
print('Z_over_K_required_lt',float(r1))
print('K_required_factor2_ceiling',k2)
print('Z_over_K_factor2_required_lt',float(r2))
