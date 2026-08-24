from math import gcd
from decimal import Decimal, getcontext

# RL-13 verifier: closes the one-orbit P3, j=0, strict [1,1,1] interior.
# Standard-library only. The infinite tail uses the same published LMN
# two-logarithm estimate already inherited and explicitly recorded in RL-11.


def bezout(a,b):
    old_r,r=a,b; old_s,s=1,0; old_t,t=0,1
    while r:
        q=old_r//r
        old_r,r=r,old_r-q*r
        old_s,s=s,old_s-q*s
        old_t,t=t,old_t-q*t
    return old_r,old_s,old_t


def modpow_signed(a,e,n):
    if e>=0: return pow(a,e,n)
    return pow(pow(a,-1,n),-e,n)


def theta_sigma(A,L,D):
    gg,u,v=bezout(L,A)
    assert gg==1 and u*L+v*A==1
    th=(modpow_signed(2,u,D)*modpow_signed(3,v,D))%D
    assert pow(th,L,D)==2%D and pow(th,A,D)==3%D
    sig=pow(th,-3,D)
    return th,sig


def p3_zero(A,L,x,y,z):
    D=(1<<A)-3**L
    _,sig=theta_sigma(A,L,D)
    return (4+6*pow(sig,x,D)+9*pow(sig,x+y,D))%D==0

# ---------------------------------------------------------------------------
# A. Analytic numerical constants used in the proof.
# ---------------------------------------------------------------------------
getcontext().prec=100
ln2=Decimal(2).ln(); ln3=Decimal(3).ln()

# Near-density resultant: D^6 < 569^L.  Since 569 < (72/25)^6,
# delta=D/2^A < D/3^L < (24/25)^L.
assert Decimal(569) < (Decimal(72)/Decimal(25))**6
q=Decimal(24)/Decimal(25)
assert q < Decimal('0.961')
assert q**180 < ln2/(Decimal(4)*Decimal(180))
assert q*(Decimal(181)/Decimal(180)) < 1

# LMN tail at L >= 183000.  Safe logarithmic decay constant:
# log(25/24) > 0.0408.
c0=Decimal('0.0408')
assert (Decimal(25)/Decimal(24)).ln() > c0
lmn_const=Decimal(22)*(Decimal(21)**2)*ln2*ln3
assert lmn_const < Decimal(7400)
assert c0*Decimal(183000)-Decimal('0.694') > Decimal(7400)
assert (Decimal(4)*Decimal(183000)).ln()+Decimal('0.06') < Decimal(21)

# Far-density pointwise resultant margin.
def mfun(t):
    # (1+t)log2 - (1/3)log(10*2^(2t)+9)
    t=Decimal(t)
    u=(Decimal(2)**(Decimal(2)*t))
    return (Decimal(1)+t)*ln2 - (Decimal(10)*u+Decimal(9)).ln()/Decimal(3)

assert mfun(Decimal(3)/Decimal(4)) > Decimal('0.0068')
assert mfun(Decimal(3)) > Decimal('0.61')
assert Decimal('0.0068')*Decimal(102) > Decimal('0.6932')
assert ln2 < Decimal('0.694')

# ---------------------------------------------------------------------------
# B. Continued-fraction certificate for the near-density finite tail.
# If L>=180, Legendre forces A/L to be a convergent of beta=log3/log2.
# ---------------------------------------------------------------------------
beta=ln3/ln2
x=beta
cf=[]; conv=[]
p_m2,p_m1=0,1; q_m2,q_m1=1,0
for _ in range(30):
    aa=int(x)
    cf.append(aa)
    p=aa*p_m1+p_m2; qq=aa*q_m1+q_m2
    conv.append((p,qq,Decimal(p)/Decimal(qq)-beta))
    p_m2,p_m1=p_m1,p; q_m2,q_m1=q_m1,qq
    if qq>183000:
        break
    x=1/(x-Decimal(aa))

expected_cf=[1,1,1,2,2,3,1,5,2,23,2,2,1,1]
assert cf[:len(expected_cf)]==expected_cf, cf
upper_div3=[]
for p,qq,diff in conv:
    if 180<=qq<183000 and qq%3==0 and diff>0:
        upper_div3.append((p,qq))
assert upper_div3==[(485,306),(125743,79335)], upper_div3

barrier_outcomes=[]
for A,L in upper_div3:
    D=(1<<A)-3**L
    ok=D**6 < 569**L
    barrier_outcomes.append((A,L,ok))
assert all(not ok for _,_,ok in barrier_outcomes)

# ---------------------------------------------------------------------------
# C. Exact finite canonical scan: near-density L<180, B/L<3/4.
# ---------------------------------------------------------------------------
near_pairs=0; near_compositions=0; near_zeros=[]
for L in range(3,180,3):
    p3=3**L
    # 4(A-L)<3L -> A<7L/4, and D>0 supplies lower endpoint.
    for A in range(L+1,(7*L+3)//4):
        if gcd(A,L)!=1 or A%3==0:
            continue
        D=(1<<A)-p3
        if D<=1:
            continue
        B=A-L
        if B<3 or not (4*B<3*L):
            continue
        near_pairs += 1
        _,sig=theta_sigma(A,L,D)
        pw=[1]*(B+1)
        for ee in range(1,B+1): pw[ee]=(pw[ee-1]*sig)%D
        for x0 in range(1,B-1):
            for y0 in range(1,B-x0):
                z0=B-x0-y0
                if z0<1: continue
                near_compositions += 1
                if (4+6*pw[x0]+9*pw[x0+y0])%D==0:
                    near_zeros.append((A,L,x0,y0,z0))
assert near_zeros==[], near_zeros

# ---------------------------------------------------------------------------
# D. Exact finite canonical scan: far-density B/L>=3/4.
# Analytically: L>=102 is impossible; for L<102, t>=3 is impossible.
# Thus it suffices to scan L<102 and A<4L exactly.
# ---------------------------------------------------------------------------
far_pairs=0; far_compositions=0; far_zeros=[]
for L in range(3,102,3):
    for A in range(L+1,4*L):
        if gcd(A,L)!=1 or A%3==0:
            continue
        D=(1<<A)-3**L
        if D<=1:
            continue
        B=A-L
        if B<3 or not (4*B>=3*L):
            continue
        far_pairs += 1
        _,sig=theta_sigma(A,L,D)
        pw=[1]*(B+1)
        for ee in range(1,B+1): pw[ee]=(pw[ee-1]*sig)%D
        for x0 in range(1,B-1):
            for y0 in range(1,B-x0):
                z0=B-x0-y0
                if z0<1: continue
                far_compositions += 1
                if (4+6*pw[x0]+9*pw[x0+y0])%D==0:
                    far_zeros.append((A,L,x0,y0,z0))
assert far_zeros==[], far_zeros

print('RL-13 P3 j=0 strict-interior verifier: PASS')
print('near-density CF upper convergents with 3|L:', upper_div3)
print('near-density exact barrier outcomes:', barrier_outcomes)
print('near-density finite parameter pairs L<180:', near_pairs)
print('near-density finite compositions checked:', near_compositions)
print('near-density zeros:', near_zeros)
print('far-density finite parameter pairs:', far_pairs)
print('far-density finite compositions checked:', far_compositions)
print('far-density zeros:', far_zeros)
print('LMN cutoff L<:',183000)

# ---------------------------------------------------------------------------
# E. RL-L84/RL-L85 numerical constants for the j=1, P2 p-adic normalized
# resultant slice A>=5L.  The v_2(Resultant)=s statement is analytic.
# ---------------------------------------------------------------------------
def p2_low_density_margin(R):
    R=Decimal(R)
    term=Decimal(16)+Decimal(5)*(Decimal(6)**(Decimal(6)/(R+Decimal(1))))
    return R*ln2 + Decimal(2)*ln2/Decimal(3) - (R+Decimal(1))*term.ln()/Decimal(6)

assert p2_low_density_margin(Decimal(5)) > Decimal('0.0991')
assert Decimal('0.0991')*Decimal(7) > ln2
assert p2_low_density_margin(Decimal('5.75'))*Decimal(4) > ln2
assert p2_low_density_margin(Decimal('5.6'))*Decimal(5) > ln2
print('j=1 P2 A>=5L margin at R=5:', p2_low_density_margin(Decimal(5)))
print('j=1 P2 A>=5L slice: analytic exclusion constants PASS')
