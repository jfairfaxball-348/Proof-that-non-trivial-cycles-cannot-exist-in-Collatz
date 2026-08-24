#!/usr/bin/env python3
from fractions import Fraction

# RL54 exact rational analysis for z=41 in the sole inherited safe CF survivor.
# This file proves the defect recurrence and records exactly which terminal
# classes are needed. It does NOT claim z=41 is closed unless all listed
# terminal classes are independently certified.

A=123139092617126647266
ELL=77692117359936589403
Z=41
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
for w in ws: M.append(M[-1]+w)
assert ps[25]==45 and ps[25]+25==70
assert ps[26:40] == [46,48,50,51,53,55,57,58,60,62,63,65,67,69]

def future_max(P,j0,j1):
    if j0>j1: return Fraction(0)
    p=P; total=Fraction(0)
    for j in range(j0,j1+1):
        while weight(j,p)>CAP:
            p += 1
        total += weight(j,p)
    return total

def correction(n,h,P):
    f=Fraction(2**(P+h),3**(P+h))
    return sum(Fraction(2**(j-1))*f for j in range(n-h+1,n+1))

def delayed_lb(n,h,P,end_non_tiny,tiny_count):
    return R-M[n-h]-future_max(P,n+1,end_non_tiny)-tiny_count*TINY-correction(n,h,P)

# Clean self-seeding invariant. If the last t late x-zero weights are tiny,
# t=0..11, then at n=40-t the hypothesis that 18-t matching y-zeroes are
# delayed beyond u_n forces E>5/3. Hence at most 17-t are delayed and the
# suffix immediately after x_n has budgets (x<=t,y<=17). A terminal bound
# L(t,17) then forces x_n tiny and advances t -> t+1.
chain=[]
for t in range(0,12):
    n=40-t; h=18-t; P=ps[n-1]
    lb=delayed_lb(n,h,P,40-t,t)
    assert lb>ECAP
    assert (h-1)+t==17
    chain.append((t,n,h,lb))

# The Y=17 invariant genuinely breaks at t=12.
fail12=delayed_lb(28,6,ps[27],28,12)
assert fail12<ECAP

# Two Y=18 cleanup stages.
lb12=delayed_lb(28,7,ps[27],28,12)
lb13=delayed_lb(27,6,ps[26],27,13)
assert lb12>ECAP and lb13>ECAP
# They require L(12,18), then L(13,18), to force all 14 late weights tiny.

# Once all 14 late weights are tiny, first26 greedy is forced.
def greedy_from(j0,p0,j1):
    p=p0; total=Fraction(0)
    for j in range(j0,j1+1):
        while weight(j,p)>CAP: p+=1
        total += weight(j,p)
    return total
second=[]
for idx in range(26):
    j=idx+1
    total=sum(ws[:idx],Fraction(0))
    pdev=ps[idx]+1
    total += weight(j,pdev)
    if j<26: total += greedy_from(j+1,pdev,26)
    second.append(total)
SECOND=max(second)
assert SECOND+14*TINY<R
u26=70
D5=Fraction(0)
for idx,j in enumerate(range(22,27),start=1):
    vmin=u26+idx
    uj=ps[j-1]+j-1
    r=vmin-uj
    D5 += ws[j-1]*(1-Fraction(2,3)**r)
assert D5>ECAP
# delayed first26 <=4; 14 later y-zeroes => final suffix (14,18).
TAIL_AFTER_U26=(ELL+Z-4)-(u26+1)
assert TAIL_AFTER_U26==ELL-34

# Independently certified in this RL54 session:
CERTIFIED_L17={0:41,1:46,2:47,3:51,4:54,5:59,6:64,7:65,8:70}
for t,L in CERTIFIED_L17.items():
    assert (27*(3**L)).bit_length() <= K+L+1-1000

print('RL54 z=41 self-seeding defect recurrence: PASS')
for t,n,h,lb in chain:
    print(f't={t:2d}: at n={n}, {h} delayed gives E>={float(lb):.15f}>5/3; terminal target L({t},17)')
print('Y=17 invariant breaks exactly at t=12: six-delayed lb =',float(fail12),'<5/3')
print('cleanup t=12: seven-delayed lb =',float(lb12),'>5/3; target L(12,18)')
print('cleanup t=13: six-delayed lb =',float(lb13),'>5/3; target L(13,18)')
print('certified terminal classes so far:',CERTIFIED_L17)
print('therefore the recurrence has rigorously forced the last 9 late x-zero weights tiny')
print('next exact obstruction: certify L_terminal(9,17)')
print('if L(9..11,17), L(12..14,18) are certified, z=41 closes')
print('final genuine suffix after u26 would have length ell-34 =',TAIL_AFTER_U26)
