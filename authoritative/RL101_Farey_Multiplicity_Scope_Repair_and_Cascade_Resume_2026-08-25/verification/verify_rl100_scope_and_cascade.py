#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

# Frozen global/cascade constants
DELTA0=13201833154443526323
C=42150931628
LOGM_UP=Fraction(42150931628751333,1000000)
SSTAR_EXPECTED=26594276905
K0=2921801523
LAST=2921813803
NEXT=2921813805
EXPECTED_COUNT=6141
SHORT=15000053

# Farey / raw-multiplicity constants
P=114208327604
Q=72057431991
LOW_N,LOW_D=103768467013,65470613321
UP_N,UP_D=10439860591,6586818670
GMAX=125777718029
NEXT_DISTINCT_Q=78644250661

# Repaired final geometry
corners=[
    ('A',0,7000001),
    ('B',5000031,4500001),
    ('C',7500032,3250001),
    ('D',10000033,2005001),
    ('E',15000036,0),
]
LAM=Fraction(234375,3281264468752)
MU=Fraction(1,7000001)


def ceil_frac(x):
    return -(-x.numerator//x.denominator)


def log_interval_int(x,terms=260):
    y=Fraction(x-1,x+1)
    y2=y*y
    s=Fraction(0)
    yp=y
    for n in range(terms):
        s += yp/(2*n+1)
        yp *= y2
    lo=2*s
    tail=2*yp/((2*terms+1)*(1-y2))
    return lo,lo+tail

# Exact rational interval for beta=log_2(3)
l2,u2=log_interval_int(2)
l3,u3=log_interval_int(3)
beta_lo=l3/u2
beta_hi=u3/l2
assert Fraction(P,Q)>beta_hi

delta_lo=Fraction(P,1)-beta_hi*Q
delta_hi=Fraction(P,1)-beta_lo*Q
assert delta_lo>0
assert GMAX*delta_hi < 1
assert (GMAX+1)*delta_lo > 1

# Farey-neighbor structure and next distinct denominator lower bound
assert UP_N*LOW_D-LOW_N*UP_D == 1
assert P==LOW_N+UP_N and Q==LOW_D+UP_D
assert P*LOW_D-LOW_N*Q == 1
assert UP_N*Q-P*UP_D == 1
assert min(Q+UP_D,Q+LOW_D)==NEXT_DISTINCT_Q

# Exact log_2(3) interval also reproduces frozen S* used by the cascade
betaL=beta_lo
betaH=beta_hi
gamma=2*betaH-3
SSTAR=(LOGM_UP.numerator*betaL.denominator)//(LOGM_UP.denominator*betaL.numerator)
assert SSTAR==SSTAR_EXPECTED


def q_lower(k):
    num=betaH*(DELTA0-2*k+4)-3*LOGM_UP-(4*betaH+3)*(k-1)
    return ceil_frac(num/gamma)


def rsum_upper(k,b,q):
    U=Fraction(k-1,1)+b*SSTAR+(LOGM_UP+b-q)/betaH
    return ceil_frac(U)-1


def top(k,l=LAM,m=MU):
    b=k-1
    q=q_lower(k)
    D=C*b-q
    R=rsum_upper(k,b,q)
    w=l*D+m*R
    bad=w.numerator//w.denominator
    good=b-bad
    cap=D//(C-SHORT)
    return q,D,R,bad,good,cap,good-cap

# Re-enumerate exact feasible two-corner supports
feasible=[]
for (n1,d1,r1),(n2,d2,r2) in combinations(corners,2):
    det=d1*r2-d2*r1
    if not det:
        continue
    l=Fraction(r2-r1,det)
    m=Fraction(d1-d2,det)
    if l<0 or m<0:
        continue
    if min(l*d+m*r for _,d,r in corners)>=1:
        feasible.append((n1+n2,l,m))

assert [n for n,_,_ in feasible]==['AC','CD','DE']
assert feasible[0][1:]==(LAM,MU)
assert (LAM*C).numerator//(LAM*C).denominator==3010

# Corner support checks
assert [LAM*d+MU*r for _,d,r in corners] == [
    Fraction(1,1),
    Fraction(3281266734377,3281264468752),
    Fraction(1,1),
    Fraction(3283605963127,3281264468752),
    Fraction(878908359375,820316117188),
]

# A-C is terminal-direction optimal over the whole promoted interval
cnt=0
worst=None
worst_k=None
for k in range(K0,LAST+1,2):
    st=top(k)
    assert st[-1]>0,(k,st)
    D,R=st[1],st[2]
    ac=LAM*D+MU*R
    assert all(ac<=l*D+m*R for _,l,m in feasible),(k,ac,feasible)
    cnt+=1
    if worst is None or st[-1]<worst:
        worst=st[-1]
        worst_k=k

assert cnt==EXPECTED_COUNT
assert worst_k==LAST and worst==10323
assert top(K0)[-1]==83636507
assert top(LAST)==(
    123139091657856223450,
    18082139992506206,
    11408591894055483,
    2921374341,
    439461,
    429138,
    10323,
)
assert top(NEXT)==(
    123139091657856223302,
    18082224294369610,
    11408645082609389,
    2921387961,
    425843,
    429140,
    -3297,
)

print('RL100 scope + repaired cascade verifier: PASS')
print('Beatty first-pair raw multiplicity g <=',GMAX)
print('next distinct admissible reduced denominator >=',NEXT_DISTINCT_Q)
print('repaired middle depth = 7500031')
print('feasible supports =',*[n for n,_,_ in feasible])
print('terminal support = AC')
print('floor(lambda*C) =', (LAM*C).numerator//(LAM*C).denominator)
print('odd values newly eliminated =',cnt)
print('eliminated interval =',K0,'through',LAST)
print('last margin =',top(LAST)[-1])
print('next odd =',NEXT,'margin =',top(NEXT)[-1])
