#!/usr/bin/env python3
from fractions import Fraction

# RL54: uniform analytic defect recurrence for the sole safe CF survivor.
# This does NOT prove terminal-negligibility. It proves that IF a common
# terminal certificate makes each late x-zero <= 2^-1000, then the late-zero
# induction has a z-independent form for every odd z>=41.

Q = 45446975257190057863   # inherited CF denominator, z=q-t so z<=q
CAP = Fraction(17,30)
RREQ = Fraction(143,12)
ECAP = Fraction(5,3)
TINY = Fraction(1,2**1000)

def weight(j,p): return Fraction(2**(p+j-1),3**p)

# Greedy cap schedule through the only fixed indices needed analytically.
p=0; ps=[]; ws=[]
for j in range(1,30):
    while weight(j,p)>CAP: p += 1
    ps.append(p); ws.append(weight(j,p))
M=[Fraction(0)]
for w in ws: M.append(M[-1]+w)
M21,M22=M[21],M[22]
assert ps[25]==45 and ps[26]==46 and ps[27]==48 and ps[28]==50

# For n>=30 use h=n-22. The delayed-block correction equals
#   C_n = w_n * r_m, m=n-22,
#   r_m=(2^(m+1)-2)/3^m.
# Since w_n<=17/30 and r_m decreases for m>=2, n>=30 is controlled by m=8.
def ratio(m): return Fraction(2**(m+1)-2,3**m)
for m in range(2,30): assert ratio(m+1) < ratio(m)
LB_NGE30 = RREQ - M22 - CAP*ratio(8) - Q*TINY
assert LB_NGE30 > ECAP

# n=29 is the sole exceptional endpoint where the crude cap is slightly too
# weak, so use its exact greedy weight p_29=50.
w29=ws[28]
LB29 = RREQ - M22 - w29*ratio(7) - Q*TINY
assert LB29 > ECAP

# Fixed cleanup stages n=28,h=7 and n=27,h=6.  The correction is the exact
# delayed block used in the inherited defect inequality.
def correction(n,h,P):
    f=Fraction(2**(P+h),3**(P+h))
    return sum(Fraction(2**(j-1))*f for j in range(n-h+1,n+1))
LB28 = RREQ - M21 - correction(28,7,ps[27]) - Q*TINY
LB27 = RREQ - M21 - correction(27,6,ps[26]) - Q*TINY
assert LB28 > ECAP and LB27 > ECAP

# Consequence for z>=41. Let R=z-27 be the number of x-zero indices after
# the first 26. At a stage with current index n>=29, t=(z-1)-n later weights
# already tiny. h=n-22 delayed matching y-zeroes are impossible, so at most
# n-23 are delayed. Adding the t later y-indices gives
#   (n-23)+t = z-24 = R+3.
# At n=28,27 the two cleanup stages give y<=z-23=R+4.
for z in range(41,201,2):
    R=z-27
    for n in range(29,z):
        t=(z-1)-n
        assert (n-23)+t == R+3
    t=(z-1)-28
    assert 6+t == R+4
    t=(z-1)-27
    assert 5+t == R+4

# Once all R late weights are tiny, the inherited exact non-greedy ceiling
# for the first 26 is separated from 143/12 by far more than Q*2^-1000.
SECOND=Fraction(0)
# recompute exact best schedule with one forced deviation from greedy
# through 26, as in RL53/RL54.
def greedy_from(j0,p0,j1):
    p=p0; total=Fraction(0)
    for j in range(j0,j1+1):
        while weight(j,p)>CAP: p+=1
        total += weight(j,p)
    return total
seconds=[]
for idx in range(26):
    j=idx+1
    prefix=sum(ws[:idx],Fraction(0))
    pdev=ps[idx]+1
    total=prefix+weight(j,pdev)
    if j<26: total += greedy_from(j+1,pdev,26)
    seconds.append(total)
SECOND=max(seconds)
assert SECOND + Q*TINY < RREQ

# Five delayed first-26 matching y-zeroes after u26=70 already violate E<5/3.
u26=70
D5=Fraction(0)
for idx,j in enumerate(range(22,27),start=1):
    vmin=u26+idx
    uj=ps[j-1]+j-1
    r=vmin-uj
    D5 += ws[j-1]*(1-Fraction(2,3)**r)
assert D5>ECAP

print('RL54 uniform late-zero defect recurrence: PASS')
print('n>=30 uniform lower bound =',float(LB_NGE30),'>5/3')
print('n=29 exact lower bound    =',float(LB29),'>5/3')
print('n=28 cleanup lower bound  =',float(LB28),'>5/3')
print('n=27 cleanup lower bound  =',float(LB27),'>5/3')
print('For every odd z>=41 (within the inherited survivor, z<=q): R=z-27 late x-zeros')
print('  stages n>=29 need only terminal y-cap R+3')
print('  final two cleanup stages need terminal y-cap R+4')
print('Therefore ONE terminal-negligibility certificate for cap (R,R+4) dominates the entire cascade.')
print('After all R late weights are tiny, first26 is greedy, u26=70, and the final suffix cap is exactly (R,R+4).')
