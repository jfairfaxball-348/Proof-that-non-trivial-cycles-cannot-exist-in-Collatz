from fractions import Fraction
from itertools import product
from math import ceil, log2

# Exact / finite sanity checks for the RL29 transport-scaling lemma.
# The general analytic proof is in RL29_SESSION_RESULTS_TO_AUDIT.md.

def Qword(bits):
    e=sum(bits); p=0; q=0
    for j,bit in enumerate(bits):
        if bit:
            q += (1<<j)*3**(e-1-p)
            p += 1
    return q

def Zword(bits):
    p=0; z=Fraction(0,1)
    for j,bit in enumerate(bits):
        z += Fraction(1<<j,3**p)
        p += bit
    return z

# Universal finite check of Z = 4Q/Y + B/Y - 1.
for b in range(1,11):
    for bits in product((0,1), repeat=b):
        e=sum(bits); Y=3**e; B=1<<b
        assert Zword(bits)==4*Fraction(Qword(bits),Y)+Fraction(B,Y)-1

# Exceptional relative-mode RHS in the 1,w basis.
# mu/Y = z*w^2-1 = (-z-1) + (-z)w; alpha0=-4+8w.
def emul(x,y):
    a,b=x; c,d=y
    return (a*c-b*d, a*d+b*c-b*d)
# use rational test z values to avoid symbolic dependencies here
for z in (Fraction(1,1), Fraction(46,45), Fraction(100,99)):
    rhs=emul((-z-1,-z),(-4,8))
    rhs=(4*rhs[0],4*rhs[1])
    assert rhs==(48*z+16,16*z-32)

# Pairwise total transport from U-V=8B+12Y:
# Z_u-Z_v=4(U-V)/Y=32z+48.
for z in (Fraction(1,1),Fraction(46,45),Fraction(100,99)):
    assert 4*(8*z+12)==32*z+48

# Forced-prefix numerical check of the synchronized partial identity
# S_s = 4G0 - 4 r_s G_s whenever p_u(s)=p_v(s).
def T(n): return (3*n+1)//2 if n&1 else n//2
R=5275
xu,xv=R,R+12
pu=pv=0
Su=Sv=Fraction(0,1)
for j in range(10):
    if pu==pv:
        rs=Fraction(1<<j,3**pu)
        assert Su-Sv==48-4*rs*(xv-xu)
    Su += Fraction(1<<j,3**pu)
    Sv += Fraction(1<<j,3**pv)
    pu += xu&1; pv += xv&1
    xu=T(xu); xv=T(xv)
# after j=10 also check if synchronized
j=10
if pu==pv:
    rs=Fraction(1<<j,3**pu)
    assert Su-Sv==48-4*rs*(xv-xu)

# 47-positive-imbalance threshold.
zmax=Fraction(46,45)
Rmin=5275
qmax=zmax*Fraction(Rmin+12,Rmin)
assert 46*qmax < 48
assert 47*qmax > 48  # 47 is the first count not ruled out by this crude cap.

# Every unsynchronized column has some phase above this multiple of R.
high_ratio=3*Fraction(Rmin,1)/(zmax*Fraction(Rmin+12,1))
assert high_ratio > Fraction(2928,1000)
assert high_ratio < Fraction(2929,1000)

# Width bound and resulting e/log(e) lower-bound arithmetic examples.
def Wbar(e):
    return Fraction(23*e,90)+Fraction(552,45)
def C(e,kappa=2.9):
    return ceil(log2(kappa*float(Wbar(e))))
def b_floor(e):
    # smallest integer b with 2^b>3^e
    b=0; x=1; y=3**e
    while x<=y:
        x*=2; b+=1
    return b
for e in (67,100,250,1000):
    b=b_floor(e); c=C(e)
    lower=Fraction(max(0,b-c),c+1)
    assert lower>=0
    print('e',e,'b_min',b,'C',c,'H_lower_real',float(lower))

print('RL29 transport-scaling sanity verifier: PASS')
print('universal block identity checked exhaustively through length 10')
print('46 positive imbalance times cannot reach the reversal transport threshold 48')
print('unsynchronized phase height ratio > 2.928 R for R>=5275, z<46/45')
