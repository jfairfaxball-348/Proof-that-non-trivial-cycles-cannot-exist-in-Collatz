from decimal import Decimal, getcontext
from math import gcd

# RL-16 verifier.
#  A. complete coefficient-5 P3 [2,1] boundary closure, j=0 and j=1;
#  B. complete coprime j=2, P2, [1,1,1] strict-interior closure.
# Standard-library only. Infinite tails use the same published
# Laurent-Mignotte-Nesterenko (LMN) estimate inherited from RL-11.

getcontext().prec = 110
D0 = Decimal
ln2 = D0(2).ln()
ln3 = D0(3).ln()
beta = ln3 / ln2



# Extended Euclid helper used to construct the common base theta.
def xgcd(a,b):
    orr,rr=a,b; os,ss=1,0; ot,tt=0,1
    while rr:
        q=orr//rr
        orr,rr=rr,orr-q*rr
        os,ss=ss,os-q*ss
        ot,tt=tt,ot-q*tt
    return orr,os,ot


def modpow_signed(a,e,n):
    return pow(a,e,n) if e>=0 else pow(pow(a,-1,n),-e,n)


def theta_base(A,L,DD):
    g,u,v=xgcd(L,A)
    assert g==1 and u*L+v*A==1
    th=(modpow_signed(2,u,DD)*modpow_signed(3,v,DD))%DD
    assert pow(th,L,DD)==2%DD
    assert pow(th,A,DD)==3%DD
    return th

# ---------------------------------------------------------------------------
# Shared LMN numerical constants.
# log Lambda >= -22 M^2 log2 log3,
# M=max(log(A/log3+L/log2)+0.06,21).
# Once delta<1/2 we have A<2L, hence the logarithmic argument is <4L.
# ---------------------------------------------------------------------------
assert ln2 < D0('0.694') and ln3 < D0('1.099')
LMN21 = D0(22)*(D0(21)**2)*D0('0.694')*D0('1.099')
assert LMN21 < D0(7400)


def lmn_logbranch(L):
    L=D0(L)
    return D0(22)*D0('0.694')*D0('1.099')*((D0(4)*L).ln()+D0('0.06'))**2

# ---------------------------------------------------------------------------
# A. j=0 P3 [2,1] boundary.
# L=3n and tau^n=2.  Boundary forms are
#   10 tau^t + 9 = 0,   4 tau^z + 15 = 0,   t+z=B=A-L.
# For p=2^(B/n)>27/8, the minimax of the two root-product bases is
# M(p)=12+sqrt(9+40p) < (64/9)p.
# Therefore any boundary survivor forces delta=D/2^A < (8/9)^n.
# ---------------------------------------------------------------------------
assert (D0(8)/D0(9))**6 < D0(1)/D0(2)
# Minimax threshold identity and positive derivative beyond p=27/8.
p0=D0(27)/D0(8)
M0=D0(12)+(D0(9)+D0(40)*p0).sqrt()
assert M0==D0(24)
assert D0(64)*p0/D0(9)==D0(24)
assert D0(64)/D0(9)-D0(20)/(D0(9)+D0(40)*p0).sqrt() > 0

# LMN tail: c0=(1/3)log(9/8)>0.0392; cutoff L<189000.
c0=(D0(9)/D0(8)).ln()/D0(3)
assert c0 > D0('0.0392')
L0_j0=D0(189000)
assert D0('0.0392')*L0_j0-D0('0.694') > D0(7400)
assert lmn_logbranch(189000) < D0(3200)
# (log(4L)+.06)^2/L decreases once log(4L)+.06>2.
assert (D0(4)*L0_j0).ln()+D0('0.06') > D0(2)

# Legendre threshold for 180<=L<189000.  If the barrier holds, then
# 0<A/L-beta<2(8/9)^(L/3)/(L log2)<1/(2L^2).
assert (D0(8)/D0(9))**D0(60) < ln2/(D0(4)*D0(180))
assert (D0(8)/D0(9))*(D0(183)/D0(180)) < 1

# Continued fraction certificate for beta=log3/log2.
x=beta
cf=[]; conv=[]
p_m2,p_m1=0,1; q_m2,q_m1=1,0
for _ in range(40):
    aa=int(x); cf.append(aa)
    p=aa*p_m1+p_m2; q=aa*q_m1+q_m2
    conv.append((p,q,D0(p)/D0(q)-beta))
    p_m2,p_m1=p_m1,p; q_m2,q_m1=q_m1,q
    if q>189000: break
    x=1/(x-D0(aa))
expected_cf=[1,1,1,2,2,3,1,5,2,23,2,2,1,1]
assert cf[:len(expected_cf)]==expected_cf
upper_div3=[(p,q) for p,q,diff in conv if 180<=q<189000 and q%3==0 and diff>0]
assert upper_div3==[(485,306),(125743,79335)], upper_div3
j0_cf_barrier=[]
for A,L in upper_div3:
    DD=(1<<A)-3**L; n=L//3
    ok=DD*(9**n) < (1<<A)*(8**n)
    j0_cf_barrier.append((A,L,ok))
assert all(not ok for _,_,ok in j0_cf_barrier)

# Small L<180: barrier implies 2^A<9*3^L, hence A is among Amin..Amin+3.
j0_small_tested=0; j0_small_barrier=[]
for L in range(3,180,3):
    p3=3**L; Amin=(p3-1).bit_length(); n=L//3
    for A in range(Amin,Amin+4):
        if gcd(A,L)!=1: continue
        DD=(1<<A)-p3
        if DD<=0: continue
        j0_small_tested+=1
        if DD*(9**n) < (1<<A)*(8**n):
            j0_small_barrier.append((A,L))
assert j0_small_barrier==[(5,3),(7,3),(11,6),(16,9),(29,18),(34,21),(43,27),(62,39)]

# Direct exact boundary evaluation kills the eight small barrier pairs.
j0_boundary_tests=0; j0_boundary_zeros=[]
for A,L in j0_small_barrier:
    DD=(1<<A)-3**L
    th=theta_base(A,L,DD); tau=pow(th,3,DD); B=A-L
    assert L%3==0 and pow(tau,L//3,DD)==2%DD
    for t in range(1,B):
        z=B-t
        f=(10*pow(tau,t,DD)+9)%DD
        g=(4*pow(tau,z,DD)+15)%DD
        assert (f==0)==(g==0)
        j0_boundary_tests+=1
        if f==0: j0_boundary_zeros.append((A,L,t,z))
assert j0_boundary_zeros==[]

# ---------------------------------------------------------------------------
# B. j=1 P3 [2,1] boundary.
# h=(2L-A)/3, h<B/4, tau^h=4/3.  Choosing the shorter of t,z and
# bounding both coefficient forms by the larger 10X^s+9 resultant gives
# |R| < 2^A exp(-0.53B).
# ---------------------------------------------------------------------------
q43=(D0(4)/D0(3)).ln()
kappa_quarter=(D0(11)/D0(4))*ln2-D0(1)/D0(2)*ln3 \
    -D0(1)/D0(4)*(D0(241)/D0(9)).ln()
assert kappa_quarter > D0('0.534')
assert kappa_quarter > D0('0.53')
# Monotonicity: g(x)>log 10>log 8, hence kappa'(eta)<0.
assert D0(10).ln() > D0(8).ln()
# Boundary B>=2 gives delta<1/2; h<B/4 gives B>4L/7.
assert (-D0('0.53')*D0(2)).exp() < D0(1)/D0(2)
assert D0('0.53')*D0(4)/D0(7) > D0('0.302')
L0_j1=D0(25000)
assert D0('0.302')*L0_j1-D0('0.694') > D0(7400)
assert lmn_logbranch(25000) < D0(2600)
assert (D0(4)*L0_j1).ln()+D0('0.06') > D0(2)

# Exact parameter-only finite certificate.  S=floor(B/2), Q=ceil(S/h),
# N=10*4^Q+9*3^Q; any boundary solution would require
# D*3^(Qh) <= 3^S*N^h.
j1_pairs=0; j1_barrier=[]
p3=1
for L in range(1,25000):
    p3*=3
    A=(p3-1).bit_length()  # delta<1/2 forces the least A
    if A>=2*L or gcd(A,L)!=1 or (A+L)%3: continue
    B=A-L
    if B<2: continue
    C=2*L-A
    if C<=0 or C%3: continue
    h=C//3
    assert 4*h<B
    DD=(1<<A)-p3
    S=B//2
    Q=(S+h-1)//h
    N=10*(4**Q)+9*(3**Q)
    j1_pairs+=1
    if DD*(3**(Q*h)) <= (3**S)*(N**h):
        j1_barrier.append((A,L,B,h,S,Q))
assert j1_barrier==[], j1_barrier

# ---------------------------------------------------------------------------
# C. coprime j=2 P2 [1,1,1] strict interior.
# B=A-L=3h and tau^h=3/2.  Rotate the simplex to omit a largest gap,
# so H=X^s+2X^b+4 with s<=2L/3.  For J=2X^h-3,
# |Res(J,H)| <= 2^s(3(3/2)^(s/h)+4)^h.
# The normalized gap is increasing in eta=h/L and at the positivity
# threshold eta0=log(3/2)/(3log2) equals (1/3)log(4/3)>0.095.
# ---------------------------------------------------------------------------
eta0=(D0(3)/D0(2)).ln()/(D0(3)*ln2)
kappa0=(D0(4)/D0(3)).ln()/D0(3)
assert kappa0 > D0('0.0958')
assert kappa0 > D0('0.095')
# derivative positivity follows from g(x)<=log7<log8.
assert D0(7).ln() < D0(8).ln()
# L>=8 gives delta<1/2.
assert (-D0('0.095')*D0(8)).exp() < D0(1)/D0(2)
L0_j2=D0(78000)
assert D0('0.095')*L0_j2-D0('0.694') > D0(7400)
assert lmn_logbranch(78000) < D0(2800)
assert (D0(4)*L0_j2).ln()+D0('0.06') > D0(2)

# Exact finite certificate.  For L>=8 only Amin can survive.  For L<8,
# the exponential barrier bounds A to a tiny neighborhood; Amin..Amin+3
# is an explicit safe superset.
j2_pairs=0; j2_barrier=[]
p3=1
for L in range(1,78000):
    p3*=3
    if L<3: continue
    Amin=(p3-1).bit_length()
    As=[Amin] if L>=8 else list(range(Amin,Amin+4))
    for A in As:
        if A<=L or gcd(A,L)!=1: continue
        B=A-L
        if B<=0 or B%3: continue
        h=B//3
        DD=(1<<A)-p3
        if DD<=0: continue
        S=(2*L)//3
        Q=(S+h-1)//h
        N=3*(3**Q)+4*(2**Q)
        j2_pairs+=1
        if DD*(2**(Q*h)) <= (2**S)*(N**h):
            j2_barrier.append((A,L,B,h,S,Q))
assert [(x[0],x[1]) for x in j2_barrier]==[(8,5),(65,41)], j2_barrier

# Direct exact strict-simplex check on the only two coarse survivors.
j2_simplex_tests=0; j2_zeros=[]
for A,L,*_ in j2_barrier:
    DD=(1<<A)-3**L
    th=theta_base(A,L,DD); tau=pow(th,3,DD)
    h=(A-L)//3
    assert pow(tau,h,DD)==3*pow(2,-1,DD)%DD
    pw=[1]*(L+1)
    for e in range(1,L+1): pw[e]=(pw[e-1]*tau)%DD
    for x in range(1,L-1):
        for y in range(1,L-x):
            z=L-x-y
            if z<1: continue
            H=(pw[x+y]+2*pw[y]+4)%DD
            j2_simplex_tests+=1
            if H==0: j2_zeros.append((A,L,x,y,z))
assert j2_zeros==[]

print('RL-16 P3-boundary / j=2 P2 verifier: PASS')
print('j=0 LMN cutoff L<',189000)
print('j=0 CF upper convergents:',upper_div3)
print('j=0 CF barrier outcomes:',j0_cf_barrier)
print('j=0 small exact parameter tests:',j0_small_tested)
print('j=0 small barrier pairs:',j0_small_barrier)
print('j=0 direct boundary tests:',j0_boundary_tests,'zeros:',j0_boundary_zeros)
print('j=1 boundary kappa(1/4):',kappa_quarter)
print('j=1 LMN cutoff L<',25000)
print('j=1 exact parameter pairs:',j1_pairs,'barrier survivors:',j1_barrier)
print('j=2 P2 universal margin:',kappa0)
print('j=2 P2 LMN cutoff L<',78000)
print('j=2 P2 exact parameter pairs:',j2_pairs)
print('j=2 P2 coarse barrier survivors:',j2_barrier)
print('j=2 P2 direct strict-simplex tests:',j2_simplex_tests,'zeros:',j2_zeros)
