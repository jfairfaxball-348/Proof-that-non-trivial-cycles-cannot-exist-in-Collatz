#!/usr/bin/env python3
from fractions import Fraction

# RL53 exact analytic bootstrap for z=39.
# Terminal maxima are certified independently by the C++ automata/chunk logs.
# Stable inherited inputs:
#   Zx > 143/12, E < 5/3, w_j < 17/30,
#   E=sum_j w_j(1-(2/3)^r_j), and the exact terminal Q grammar.

A=123139092617126647266
ELL=77692117359936589403
Z=39
S=Z-1
K=A-ELL-Z+3
CAP=Fraction(17,30)
R=Fraction(143,12)
ECAP=Fraction(5,3)
TINY=Fraction(1,2**1000)


def weight(j,p):
    return Fraction(2**(p+j-1),3**p)

p=0; ps=[]; ws=[]
for j in range(1,S+1):
    while weight(j,p)>CAP:
        p += 1
    ps.append(p); ws.append(weight(j,p))

M=[Fraction(0)]
for w in ws:
    M.append(M[-1]+w)

assert ps[:26] == [2,4,5,7,9,10,12,14,16,17,19,21,22,24,26,28,29,31,33,34,36,38,40,41,43,45]
assert ps[26:38] == [46,48,50,51,53,55,57,58,60,62,63,65]
assert ps[25]+25 == 70


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
assert SECOND + 12*TINY < R

# The weakest terminal-near bound used below is L=104 from (1,38).
L_COMMON=104
assert (27*(3**L_COMMON)).bit_length() <= K+L_COMMON+1-1000


def future_max(P,j0,j1):
    if j0>j1:
        return Fraction(0)
    p=P; total=Fraction(0)
    for j in range(j0,j1+1):
        while weight(j,p)>CAP:
            p += 1
        total += weight(j,p)
    return total


def correction(n,h,P):
    factor=Fraction(2**(P+h),3**(P+h))
    return sum(Fraction(2**(j-1))*factor for j in range(n-h+1,n+1))


def delayed_lb(n,h,P,end_non_tiny,tiny_count):
    outside_prefix=M[n-h]
    future=future_max(P,n+1,end_non_tiny)+tiny_count*TINY
    return R-outside_prefix-future-correction(n,h,P)

# Monotonicity: for fixed n,h, future_max(P,...) and correction(n,h,P)
# are nonincreasing in P, hence delayed_lb is nondecreasing in P.
# It suffices to check P at the cap-forced minimum ps[n-1].

# (1,38)=104 => x37,x38 tiny.  Fifteen delayed among first 26 are impossible.
lb26=delayed_lb(26,15,ps[25],36,2)
assert lb26 > ECAP
# delayed first26 <=14; suffix after x35 has x<=3, y<=14+12=26.

# (3,26)=78 => x35..x38 tiny.  Thirteen delayed among first33 impossible.
lb33=delayed_lb(33,13,ps[32],34,4)
assert lb33 > ECAP
# delayed first33 <=12; suffix after x33 has x<=5, y<=12+5=17.

# (5,17)=60 => x33..x38 tiny.  Ten delayed among first31 impossible.
lb31=delayed_lb(31,10,ps[30],32,6)
assert lb31 > ECAP
# delayed first31 <=9; suffix after x31 has x<=7, y<=9+7=16.

# (7,16)=60 => x31..x38 tiny.  Eight delayed among first30 impossible.
lb30=delayed_lb(30,8,ps[29],30,8)
assert lb30 > ECAP
# delayed first30 <=7; suffix after x30 has x<=8, y<=7+8=15.

# (8,15)=58 => x30..x38 tiny.  Seven delayed among first29 impossible.
lb29=delayed_lb(29,7,ps[28],29,9)
assert lb29 > ECAP
# delayed first29 <=6; suffix after x29 has x<=9, y<=6+9=15.

# (9,15)=61 => x29..x38 tiny.  Seven delayed among first28 impossible.
lb28=delayed_lb(28,7,ps[27],28,10)
assert lb28 > ECAP
# delayed first28 <=6; suffix after x28 has x<=10, y<=6+10=16.

# (10,16)=65 => x28..x38 tiny.  Six delayed among first27 impossible.
lb27=delayed_lb(27,6,ps[26],27,11)
assert lb27 > ECAP
# delayed first27 <=5; suffix after x27 has x<=11, y<=5+11=16.

# (11,16)=67 => all twelve late x-zeros x27..x38 are tiny.
# Hence first26 must be the unique greedy schedule.
assert SECOND + 12*TINY < R
u26=ps[25]+25
assert u26==70

# Five delayed first26 matching y-zeros past u26 already violate E<5/3.
D5=Fraction(0)
for idx,j in enumerate(range(22,27),start=1):
    vmin=u26+idx
    uj=ps[j-1]+j-1
    r=vmin-uj
    D5 += ws[j-1]*(1-Fraction(2,3)**r)
assert D5 > ECAP
# delayed first26 <=4.  Adding y27..y38 gives y<=16, x<=12.

M_INTERNAL=ELL+Z-4
TAIL_AFTER_U26=M_INTERNAL-(u26+1)
assert TAIL_AFTER_U26==ELL-36
assert TAIL_AFTER_U26>67

print('RL53 z=39 analytic bootstrap: PASS')
print('common terminal-near bound: each forced late x-zero weight < 2^-1000')
print('after last 2 tiny: 15-delayed first26 lower bound =',float(lb26),'> 5/3; suffix (3,26)')
print('after last 4 tiny: 13-delayed at u33 lower bound =',float(lb33),'> 5/3; suffix (5,17)')
print('after last 6 tiny: 10-delayed at u31 lower bound =',float(lb31),'> 5/3; suffix (7,16)')
print('after last 8 tiny: 8-delayed at u30 lower bound =',float(lb30),'> 5/3; suffix (8,15)')
print('after last 9 tiny: 7-delayed at u29 lower bound =',float(lb29),'> 5/3; suffix (9,15)')
print('after last 10 tiny: 7-delayed at u28 lower bound =',float(lb28),'> 5/3; suffix (10,16)')
print('after last 11 tiny: 6-delayed at u27 lower bound =',float(lb27),'> 5/3; suffix (11,16)')
print('best non-greedy first26 mass =',float(SECOND),'< 143/12, so first26 greedy is forced')
print('forced u26 =',u26,'; five-delayed defect cost =',float(D5),'> 5/3')
print('final suffix budgets: x<=12, y<=16; required length ell-36 =',TAIL_AFTER_U26)
print('with exact L_terminal(12,16)=67, z=39 is impossible; parity gives z>=41')
