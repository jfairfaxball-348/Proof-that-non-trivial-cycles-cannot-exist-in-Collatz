from decimal import Decimal, getcontext
from math import gcd

# RL-14 verifier: analytic constants for the j=1 P2 strict-interior closure,
# plus exact arithmetic checks for the P3 side-resultant valuation geometry.
# Standard-library only.

getcontext().prec = 100
D = Decimal
ln2 = D(2).ln(); ln3 = D(3).ln(); ln6 = D(6).ln()

def pw(base, x):
    return (D(base).ln()*D(x)).exp()

def F(u,v):
    u=D(u); v=D(v)
    return pw(4,1+u) + pw(4,u)*pw(36,v) + pw(9,1-u)

one=D(1); third=one/D(3); half=one/D(2)

# ---------------------------------------------------------------------------
# A. Cyclic minimax C<16 at the limiting density A/L=2.
# F(c,b)=4^(1+c)+4^c 36^b+9^(1-c).
# Every auxiliary one-variable function is a sum of positive exponentials,
# hence convex, so it suffices to check the stated endpoints.
# ---------------------------------------------------------------------------
Ceq=F(third,third)
assert Ceq < D(16)

# Sorted orientation (x,y,z): candidate F(y,x).
assert F(D(0),D(0)) == D(14)
assert F(third,third) < D(16)
assert F(half,D(0)) == D(13)

# Reverse sorted orientation, z<=1/2: candidate F(z,(1-z)/2).
hhalf=F(half,D(1)/D(4))
assert hhalf < D(16)

# Reverse sorted orientation, z>1/2.  The fixed 0.3/0.7 threshold argument:
# max_{x in [0,1/3]} F(x,0.3) occurs at an endpoint by convexity.
t03=D(3)/D(10)
assert F(D(0),t03) < D(16)
assert F(third,t03) < D(16)
# max_{z in [1/2,0.7]} F(z,0.7-z) also occurs at an endpoint.
t07=D(7)/D(10)
assert F(half,t07-half) < D(16)
assert F(t07,D(0)) < D(16)

# ---------------------------------------------------------------------------
# B. Universal growth of the squared logarithmic resultant margin.
# M'(R) >= (1/3) log(64/21) > 0 by log-sum-exp convexity.
# In j=1, A+L is divisible by 3; if A>2L then A-2L>=3.
# Thus D^2/2^(2A) < 21/64.
# But L>=3 in the strict interior and A>=2L+3 imply
# D/2^A > 1-(3/4)^L/8 >= 485/512, contradiction.
# ---------------------------------------------------------------------------
delta=(D(64)/D(21)).ln()/D(3)
assert delta > D('0.37')
assert (D(485)/D(512))**2 > D(21)/D(64)

# ---------------------------------------------------------------------------
# C. Exact integer valuation-tie geometry for the P3 side resultant.
# F_B=8X^B-27, H=4X^(x+y)+6X^y+9.
# If they share a complex root, the minimum p-adic valuation among the
# three H terms must be attained at least twice at p=2 and at p=3.
# The only simultaneous tie is x=y=z=B/3.
# We certify this integer-scaled condition for a broad range.
# ---------------------------------------------------------------------------
def min_tied(vals):
    m=min(vals)
    return sum(v==m for v in vals)>=2

tie_checks=0
for B in range(3,401):
    for x in range(1,B-1):
        for y in range(1,B-x):
            z=B-x-y
            # B-scaled 2-adic valuations of H terms at a root of 8X^B=27:
            v2=(3*z-B, B-3*y, 0)
            # B-scaled 3-adic valuations:
            v3=(3*(x+y), B+3*y, 2*B)
            both=min_tied(v2) and min_tied(v3)
            assert both == (x==y==z), (B,x,y,z,v2,v3)
            tie_checks += 1

# In the coprime j=1 P3 branch, A+L == 0 mod3 and gcd(A,L)=1,
# hence B=A-L is never divisible by 3.
for A in range(3,250):
    for L in range(1,A):
        if gcd(A,L)==1 and (A+L)%3==0:
            assert (A-L)%3 != 0

# ---------------------------------------------------------------------------
# D. Equal-gap descent kernel.
# K(Y)=4Y^2+6Y+9 and (2Y-3)K(Y)=8Y^3-27.
# The reduced resultant S_k=Res(X^k-1,K) is:
#   (3^k-2^k)^2                       if 3|k,
#   9^k+6^k+4^k                       otherwise.
# In particular S_1=19 and S_k <= 19^k.
# ---------------------------------------------------------------------------
def S(k):
    if k%3==0:
        return (3**k-2**k)**2
    return 9**k+6**k+4**k

assert S(1)==19
for k in range(1,200):
    assert S(k) <= 19**k

# Tiny direct check that D=19 has no positive A,L solution in the relevant
# range; analytically A>=3 would already fail mod 8.
sol19=[]
for A in range(1,100):
    for L in range(1,A):
        if (1<<A)-3**L==19:
            sol19.append((A,L))
assert sol19==[]

print('RL-14 j=1 P2 closure / P3 descent verifier: PASS')
print('equilateral limiting C =', Ceq)
print('reverse z=1/2 endpoint =', hhalf)
print('F(0,0.3) =',F(D(0),t03))
print('F(1/3,0.3) =',F(third,t03))
print('F(1/2,0.2) =',F(half,t07-half))
print('F(0.7,0) =',F(t07,D(0)))
print('universal derivative lower bound delta =',delta)
print('P3 valuation-tie triples checked:',tie_checks)
print('S_1 =',S(1))
print('D=19 solutions:',sol19)

# ---------------------------------------------------------------------------
# E. RL-L92: j=1 P3 parameter inequality D > 4^B.
# Assuming D<4^B gives delta<2^{-C}, C=2L-A>=3, hence for L>=14
# C>0.4L and log Lambda < log(8/7)-0.4 L log2.
# The inherited LMN estimate closes L>=27000; the exact scan below finds no
# parameter survivor below 27000.
# ---------------------------------------------------------------------------
ln4over3=(D(4)/D(3)).ln()
assert (ln4over3-D('0.4')*ln2)*D(14) > D(1)/D(7)
assert D('0.4')*ln2 > D('0.277')
assert (D(8)/D(7)).ln() < D('0.134')
L0=D(27000)
lmn_const=D(22)*(D(21)**2)*D('0.694')*D('1.099')
upper_mag=D('0.277')*L0-D('0.134')
assert lmn_const < D(7400)
assert upper_mag > D(7478)
logbranch=D(22)*D('0.694')*D('1.099')*((D(4)*L0).ln()+D('0.06'))**2
assert logbranch < D(2300)
assert upper_mag > logbranch
assert (D(4)*L0).ln()+D('0.06') > D(2)

barrier_pairs=[]
first_congruence_pairs=0
for L in range(1,27000):
    p3=3**L
    Amin=(p3-1).bit_length()  # exact least A with 2^A > 3^L
    A=Amin + ((-L-Amin)%3)   # least such A with A+L == 0 mod 3
    if A>=2*L:
        continue
    first_congruence_pairs += 1
    # Any later congruent A'=A+3h has 3^L/2^A' < 1/8 and C'=2L-A'>=3,
    # so D'/4^(A'-L) > 8*(7/8)=7.  Thus only this first congruent A can
    # possibly satisfy D<4^B.
    if gcd(A,L)!=1:
        continue
    B=A-L
    DD=(1<<A)-p3
    if DD < (1<<(2*B)):
        barrier_pairs.append((A,L,B,DD))
assert barrier_pairs==[], barrier_pairs

print('j=1 P3 D>4^B exact first-congruence pairs:',first_congruence_pairs)
print('j=1 P3 D<4^B finite survivors:',barrier_pairs)
print('LMN cutoff for D>4^B theorem: L<27000')

# ---------------------------------------------------------------------------
# F. RL-L94: plus equal-pair branch closes whenever k<=4h, i.e. d<=4q.
# We certify the small k endpoint inequalities used after the general
# 3*9^k comparison takes over.
# ---------------------------------------------------------------------------
assert S(1) < 4**4
assert S(2) < 4**5
assert S(3) < 4**6
assert S(4) < 4**7
# For k>=5, (3*9^k)^4 < 4^(7k) follows from the k=5 endpoint and growth.
assert (3*9**5)**4 < 4**(7*5)
assert 9**4 < 4**7
print('plus equal-pair d<=4q comparison constants: PASS')

# ---------------------------------------------------------------------------
# G. RL-L95 size endpoint: if 1<=k<B, both possible 2-cyclotomic
# divisors forced by the equal-gap cube-root relation are <4^B.
# ---------------------------------------------------------------------------
for B in range(2,1000):
    for k in range(1,B):
        assert 2**k-1 < 4**B
        assert 2**(2*k)+2**k+1 < 4**B
print('equal-gap cube-root cyclotomic size checks: PASS')
