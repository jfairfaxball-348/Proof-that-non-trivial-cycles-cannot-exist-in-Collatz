#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
DELTA0=13201833154443526323
C=42150931628
LOGM_UP=Fraction(42150931628751333,1000000)
SSTAR_EXPECTED=26594276905
K0=2921750257
LAST=2921758703
NEXT=2921758705
EXPECTED_COUNT=4224
MU=Fraction(1,7000001)
LAM=Fraction(5000000,52500238500033)
SHORT=15000053
corners=[('A',0,7000001),('B',5000031,3675001),('C',7500033,2000001),('D',10000033,335001),('E',15000039,0)]

def ceil_frac(x): return -(-x.numerator//x.denominator)
def log_interval_int(x,terms=260):
    y=Fraction(x-1,x+1); y2=y*y; s=Fraction(0); yp=y
    for n in range(terms): s+=yp/(2*n+1); yp*=y2
    lo=2*s; tail=2*yp/((2*terms+1)*(1-y2)); return lo,lo+tail
l2,u2=log_interval_int(2); l3,u3=log_interval_int(3)
beta_lo=l3/u2; beta_hi=u3/l2; gamma=2*beta_hi-3
SSTAR=(LOGM_UP.numerator*beta_lo.denominator)//(LOGM_UP.denominator*beta_lo.numerator)
assert SSTAR==SSTAR_EXPECTED

def q_lower(k):
    num=beta_hi*(DELTA0-2*k+4)-3*LOGM_UP-(4*beta_hi+3)*(k-1)
    return ceil_frac(num/gamma)
def rsum_upper(k,b,q):
    U=Fraction(k-1,1)+b*SSTAR+(LOGM_UP+b-q)/beta_hi
    return ceil_frac(U)-1
def top(k):
    b=k-1; q=q_lower(k); D=C*b-q; R=rsum_upper(k,b,q)
    w=LAM*D+MU*R; bad=w.numerator//w.denominator
    good=b-bad; cap=D//(C-SHORT)
    return q,D,R,bad,good,cap,good-cap
# enumerate all feasible pair supports for optimality audit
feasible=[]
for (n1,d1,r1),(n2,d2,r2) in combinations(corners,2):
    det=d1*r2-d2*r1
    if not det: continue
    l=Fraction(r2-r1,det); m=Fraction(d1-d2,det)
    if l<0 or m<0: continue
    if min(l*d+m*r for _,d,r in corners)>=1: feasible.append((n1+n2,l,m))
assert [n for n,_,_ in feasible]==['AC','CD','DE']
assert (LAM*C).numerator//(LAM*C).denominator==4014
cnt=0; worst=None; worst_k=None
for k in range(K0,LAST+1,2):
    st=top(k); assert st[-1]>0,(k,st)
    D,R=st[1],st[2]
    ac=LAM*D+MU*R
    assert all(ac <= l*D+m*R for _,l,m in feasible)
    cnt+=1
    if worst is None or st[-1]<worst: worst=st[-1]; worst_k=k
assert cnt==EXPECTED_COUNT
assert worst_k==LAST and worst==11277
assert top(LAST)==(123139091657860279878,15759623655746978,9943247233940797,2921373407,385295,374018,11277)
assert top(NEXT)==(123139091657860279731,15759707957610381,9943300422494703,2921389034,369670,374020,-4350)
# optimal-support comparison also holds at first failure
D,R=top(NEXT)[1:3]; ac=LAM*D+MU*R
assert all(ac <= l*D+m*R for _,l,m in feasible)
print('RL94 coupled interval verifier: PASS')
print('odd values eliminated =',cnt)
print('eliminated odd interval =',K0,'through',LAST)
print('last margin =',top(LAST)[-1])
print('next odd =',NEXT,'margin =',top(NEXT)[-1])
print('common successor ceiling =',SHORT)
print('new surviving odd lower endpoint >=',NEXT)
print('terminal-direction optimal support = AC among',*[n for n,_,_ in feasible])
