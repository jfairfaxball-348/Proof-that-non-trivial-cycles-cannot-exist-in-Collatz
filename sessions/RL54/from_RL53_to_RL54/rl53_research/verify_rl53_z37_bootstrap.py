#!/usr/bin/env python3
from fractions import Fraction

# RL53 analytic half of the exact z=37 terminal/defect bootstrap.
# Terminal maxima are certified independently by the C++ verifiers.
# Stable inherited inputs:
#   Zx > 143/12, E < 5/3, w_j < 17/30,
#   E=sum_j w_j(1-(2/3)^r_j), and terminal Q grammar.

A=123139092617126647266
ELL=77692117359936589403
Z=37
S=Z-1
K=A-ELL-Z+3
CAP=Fraction(17,30)
R=Fraction(143,12)
ECAP=Fraction(5,3)
TINY=Fraction(1,2**1000)


def weight(j,p):
    return Fraction(2**(p+j-1),3**p)

# Coordinatewise minimal/maximum-mass schedule under the sequential cap.
p=0; ps=[]; ws=[]
for j in range(1,S+1):
    while weight(j,p)>CAP:
        p += 1
    ps.append(p); ws.append(weight(j,p))

M=[Fraction(0)]
for w in ws:
    M.append(M[-1]+w)

assert ps[:26] == [2,4,5,7,9,10,12,14,16,17,19,21,22,24,26,28,29,31,33,34,36,38,40,41,43,45]
assert ps[26:31] == [46,48,50,51,53]
assert ps[25]+25 == 70

# Exact best non-greedy first-26 mass.
def greedy_from(j0,p0,j1):
    p=p0; total=Fraction(0)
    for j in range(j0,j1+1):
        while weight(j,p)>CAP:
            p += 1
        total += weight(j,p)
    return total

second=[]
for idx in range(26):
    j=idx+1
    prefix=sum(ws[:idx],Fraction(0))
    pdev=ps[idx]+1
    total=prefix+weight(j,pdev)
    if j<26:
        total += greedy_from(j+1,pdev,26)
    second.append(total)
SECOND=max(second)
assert SECOND + 10*TINY < R

# A terminal maximum of 97 already makes every subsequently forced late zero
# vastly smaller than 2^-1000.  If a zero is within L terminal columns,
# w < 27*3^L / 2^(K+L+1), using g_end<27/2^K.
L_COMMON=97
assert (27*(3**L_COMMON)).bit_length() <= K+L_COMMON+1-1000


def future_max(P,j0,j1):
    """Exact coordinatewise maximum mass on j0..j1 with p_{j0-1}<=P."""
    if j0>j1:
        return Fraction(0)
    p=P; total=Fraction(0)
    for j in range(j0,j1+1):
        while weight(j,p)>CAP:
            p += 1
        total += weight(j,p)
    return total


def correction(n,h,P):
    # If h of y_1..y_n occur after u_n=P+n-1, order forces indices
    # n-h+1..n to have r_j >= P+h-p_j.  The attenuated terms cancel p_j.
    factor=Fraction(2**(P+h),3**(P+h))
    return sum(Fraction(2**(j-1))*factor for j in range(n-h+1,n+1))


def delayed_lb(n,h,P,end_non_tiny,tiny_count):
    # Lower bound for E if h of the first n matching y-zeros are delayed
    # beyond u_n, after the stated later x-zeros are already tiny.
    outside_prefix=M[n-h]
    future=future_max(P,n+1,end_non_tiny)+tiny_count*TINY
    return R-outside_prefix-future-correction(n,h,P)

# Monotonicity lemma used below: for fixed n,h, future_max(P,...) is
# nonincreasing in P, and correction(n,h,P) strictly decreases in P.
# Hence delayed_lb is nondecreasing in P.  It suffices to check the cap-forced
# minimum P=ps[n-1].

# Stage A: (1,36)=97 => x_35,x_36 tiny.  Thirteen delayed among first 26
# already violate E<5/3, so delayed first26 <=12 and any suffix after x_33
# has y-zero <=12+10=22, x-zero <=3.
lb26=delayed_lb(26,13,ps[25],34,2)
assert lb26 > ECAP

# (3,22)=69 => x_33..x_36 tiny.  At u_31, ten delayed first31 are impossible.
lb31=delayed_lb(31,10,ps[30],32,4)
assert lb31 > ECAP
# Thus delayed first31 <=9; suffix after x_31 has y<=9+5=14, x<=5.

# (5,14)=52 => x_31..x_36 tiny.  At u_29, nine delayed are impossible.
lb29=delayed_lb(29,9,ps[28],30,6)
assert lb29 > ECAP
# delayed first29 <=8; suffix after x_29 has y<=8+7=15, x<=7.

# (7,15)=57 => x_29..x_36 tiny.  At u_28, seven delayed are impossible.
lb28=delayed_lb(28,7,ps[27],28,8)
assert lb28 > ECAP
# delayed first28 <=6; suffix after x_28 has y<=6+8=14, x<=8.

# (8,14)=59 => x_28..x_36 tiny.  At u_27, six delayed are impossible.
lb27=delayed_lb(27,6,ps[26],27,9)
assert lb27 > ECAP
# delayed first27 <=5; suffix after x_27 has y<=5+9=14, x<=9.

# (9,14)=60 => all ten late x-zeros x_27..x_36 are tiny.  Therefore the
# first 26 must be the unique greedy schedule, since every non-greedy first26
# schedule misses the required mass even after all ten tiny contributions.
assert SECOND + 10*TINY < R
u26=ps[25]+25
assert u26==70

# With the greedy first26 schedule forced, five delayed matching y-zeros past
# u26 already cost >5/3, hence delayed first26<=4.  Adding y_27..y_36 gives
# the final suffix budget y<=14, while x<=10.
D5=Fraction(0)
for idx,j in enumerate(range(22,27),start=1):
    vmin=u26+idx
    uj=ps[j-1]+j-1
    r=vmin-uj
    D5 += ws[j-1]*(1-Fraction(2,3)**r)
assert D5 > ECAP

# (10,14)=60 then contradicts the genuine suffix after zero-based column 70.
M_INTERNAL=ELL+Z-4
TAIL_AFTER_U26=M_INTERNAL-(u26+1)
assert TAIL_AFTER_U26==ELL-38
assert TAIL_AFTER_U26>60

print('RL53 z=37 analytic bootstrap: PASS')
print('common terminal-near bound: each forced late x-zero weight < 2^-1000')
print('after last 2 tiny: 13-delayed E lower bound =',float(lb26),'> 5/3; suffix for x33 is (3,22)')
print('after last 4 tiny: 10-delayed at u31 lower bound =',float(lb31),'> 5/3; suffix is (5,14)')
print('after last 6 tiny: 9-delayed at u29 lower bound =',float(lb29),'> 5/3; suffix is (7,15)')
print('after last 8 tiny: 7-delayed at u28 lower bound =',float(lb28),'> 5/3; suffix is (8,14)')
print('after last 9 tiny: 6-delayed at u27 lower bound =',float(lb27),'> 5/3; suffix is (9,14)')
print('best non-greedy first26 mass =',float(SECOND),'< 143/12, so first26 greedy is forced')
print('forced u26 =',u26,'; five-delayed defect cost =',float(D5),'> 5/3')
print('final suffix budgets: x<=10, y<=14; required length ell-38 =',TAIL_AFTER_U26)
print('with exact L_terminal(10,14)=60, z=37 is impossible; parity gives z>=39')
