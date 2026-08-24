#!/usr/bin/env python3
from fractions import Fraction

# Analytic/scalar half of the RL52 z=35 bootstrap.  Terminal maxima are checked
# independently by verify_rl52_terminal_event_automaton.cpp.
A=123139092617126647266
ELL=77692117359936589403
Q=A-ELL
Z=35
S=Z-1
K=Q-Z+3
CAP=Fraction(17,30)
R=Fraction(143,12)
ECAP=Fraction(5,3)
TINY=Fraction(1,2**1000)


def weight(j,p):
    return Fraction(2**(p+j-1),3**p)

# first-26 greedy schedule and exact best non-greedy competitor
p=0; ps=[]; ws=[]
for j in range(1,27):
    while weight(j,p)>CAP:
        p+=1
    ps.append(p); ws.append(weight(j,p))
assert ps == [2,4,5,7,9,10,12,14,16,17,19,21,22,24,26,28,29,31,33,34,36,38,40,41,43,45]
M=[Fraction(0)]
for w in ws: M.append(M[-1]+w)


def greedy_from(j0,p0,j1):
    p=p0; total=Fraction(0)
    for j in range(j0,j1+1):
        while weight(j,p)>CAP:
            p+=1
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
assert SECOND + 8*TINY < R

# Any late zero within 85 terminal columns has weight < 2^-1000.
# g_end < 27/2^K (zeta<2), and going backward multiplies g by at most 3/2
# per column; a zero weight is half its post-zero g.
assert (27*(3**85)).bit_length() <= K+86-1000


def future(P,endj):
    return greedy_from(27,P,endj) if endj>=27 else Fraction(0)


def correction(P,h):
    # If h of y_1..y_26 are after u_26, order forces indices 27-h..26
    # to have r_j >= P+h-p_j.  Their attenuated terms telescope.
    factor=Fraction(2**(P+h),3**(P+h))
    return sum(Fraction(2**(j-1))*factor for j in range(27-h,27))


def stage(endj, tiny_count, pfail, h_excluded):
    # effective non-negligible future zeros are 27..endj; tiny_count later
    relax=M[25]+weight(26,pfail)+future(pfail,endj)+tiny_count*TINY
    assert relax <= R
    pmax=pfail-1
    lbs=[]
    for P in range(45,pmax+1):
        lb=R-M[26-h_excluded]-future(P,endj)-tiny_count*TINY-correction(P,h_excluded)
        lbs.append((lb,P))
        assert lb>ECAP
    return pmax,min(lbs)

# After terminal arithmetic makes the last 2,4,6 x-zeros tiny, the scalar/
# defect problem reduces successively to effective S=32,30,28.
pmax32,min32=stage(32,2,57,11)   # delayed first26 <=10
pmax30,min30=stage(30,4,54,9)    # delayed first26 <=8
pmax28,min28=stage(28,6,50,7)    # delayed first26 <=6
assert (pmax32,pmax30,pmax28)==(56,53,49)

# Once all eight future x-zero weights are tiny, first26 must be the unique
# greedy schedule.  Then u_26=70 and five delayed matching y-zeros already
# exceed E<5/3 exactly as in the z=29 argument.
u=[ps[j-1]+j-1 for j in range(1,27)]
assert u[-1]==70
D5=Fraction(0)
for idx,j in enumerate(range(22,27),start=1):
    vmin=70+idx
    r=vmin-u[j-1]
    D5 += ws[j-1]*(1-Fraction(2,3)**r)
assert D5>ECAP

M_INTERNAL=ELL+Z-4
TAIL_AFTER_U26=M_INTERNAL-71
assert TAIL_AFTER_U26==ELL-40
assert TAIL_AFTER_U26>48

print('RL52 z=35 analytic bootstrap: PASS')
print('late-zero common bound: each forced terminal-near weight < 2^-1000')
print('after last 2 tiny: p26<=',pmax32,'and delayed first26 <=10; min defect lb=',float(min32[0]))
print('after last 4 tiny: p26<=',pmax30,'and delayed first26 <=8; min defect lb=',float(min30[0]))
print('after last 6 tiny: p26<=',pmax28,'and delayed first26 <=6; min defect lb=',float(min28[0]))
print('after all 8 tiny: first26 greedy schedule is forced; u26=',u[-1])
print('five delayed first26 defect cost=',float(D5),'> 5/3, hence delayed <=4')
print('final suffix budgets: x-zero <=8, y-zero <=12')
print('required suffix length after u26 = ell-40 =',TAIL_AFTER_U26)
