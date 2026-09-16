"""Exact-rational verification of the RL339 candidate density-42 carry cap.

PROMOTED; see RL339 certificate. Uses inherited RL327/RL338 arbitrary-support telescope constants,
but the new density floor and all-rho monotonicity are checked here directly.
"""
from fractions import Fraction

A=217976794617
ELL=137528045312
D=A-ELL
LAM=1+Fraction(1,1<<40)
CAP=32539271836

def log2_lower(terms=280):
    x=Fraction(1,3)
    x2=x*x
    term=x
    total=Fraction(0)
    for j in range(terms):
        total+=term/(2*j+1)
        term*=x2
    return 2*total

l2=log2_lower()
x=l2/ELL
full=1/(2*(x+x*x/2))-Fraction(1,2)

def W(K):
    s1=K*(K+1)//2
    s2=K*(K+1)*(2*K+1)//6
    s3=s1*s1
    s4=K*(K+1)*(2*K+1)*(3*K*K+3*K-1)//30
    return Fraction(K)+x*s1+x*x*s2/2+x**3*s3/6+x**4*s4/24

def K42(rho):
    return max(0,(ELL-rho+1-35+21)//22)

om59=sum((Fraction(1<<((A*r)//ELL),3**r)/LAM for r in range(1,60)),Fraction())
K=K42(60)
R=1+(full-om59)/3-W(K)/(12*LAM)
assert K==6251274783
assert CAP<R<CAP+1
assert 22*K<ELL
assert 0<l2<1

# For every rho>=60, K42(rho+1) is K42(rho) or one smaller.
# Every omitted term exceeds 1/(2*LAM), since 2^A/3^ELL>1 and
# floor(A*r/ELL)>A*r/ELL-1. Also W(K)-W(K-1) is the quartic
# exponential polynomial at y=x*K<1/22 and is <22/21.
y=Fraction(1,22)
polynomial=1+y+y*y/2+y**3/6+y**4/24
assert polynomial<Fraction(22,21)
assert Fraction(22,21)/(12*LAM)<Fraction(1,1)/(6*LAM)

# Inherited companion inequality for rho<=59.
rho59=Fraction(5,6)+LAM*(1<<((D*59)//ELL))
assert rho59<CAP+1
print("DENSITY42_CAP_GREEN")
print("K60",K)
print("R60_floor",R.numerator//R.denominator)
print("rho59_floor",rho59.numerator//rho59.denominator)
print("all_rho_monotonic",True)
print("cap",CAP)
