#!/usr/bin/env python3
from fractions import Fraction

# Exact coupled elimination of z=31 for the sole stable continued-fraction survivor.
# Inputs: Zx>143/12, E<5/3, sequential x-prefix cap w<17/30,
# E=sum w_j[1-(2/3)^r_j], terminal J=2^k, and the exact Q backward maps.

A=123139092617126647266
ELL=77692117359936589403
Q=A-ELL
Z=31
S=Z-1                         # 30 internal zeros in each word
K=Q-Z+3                       # q-28
M_INTERNAL=ELL+Z-4            # ell+27
CAP=Fraction(17,30)
R=Fraction(143,12)
ECAP=Fraction(5,3)


def weight(j,p):
    return Fraction(2**(p+j-1),3**p)


def greedy_prefix(n,p0=0,j0=1):
    p=p0
    ps=[]; ws=[]
    for j in range(j0,n+1):
        while weight(j,p)>CAP:
            p+=1
        ps.append(p); ws.append(weight(j,p))
    return ps,ws


def future_max(P, endj=S):
    # exact coordinatewise maximal future zero mass for j=27..endj
    p=P; total=Fraction(0); ps=[]
    for j in range(27,endj+1):
        while weight(j,p)>CAP:
            p+=1
        ps.append(p); total+=weight(j,p)
    return total,ps

# Greedy reference and maximal prefixes.
pstar,wstar=greedy_prefix(26)
assert pstar[-1]==45
M17=sum(wstar[:17],Fraction(0))
M25=sum(wstar[:25],Fraction(0))

# ---------------------------------------------------------------------------
# 1. Any scalar-feasible z=31 schedule has p_26<=53, hence u_26<=78.
# ---------------------------------------------------------------------------
# For fixed p_26=P, the first 25 zeros are maximized by the greedy prefix,
# and zeros 27..30 are maximized greedily starting from P. At P=54 even this
# relaxed maximum is already below the required Zx mass. Larger P only lowers
# w_26 and the future greedy maximum.
PFAIL=54
F54,_=future_max(PFAIL)
RELAX54=M25+weight(26,PFAIL)+F54
assert RELAX54 <= R
PMIN=pstar[-1]
PMAX=53
assert PMIN==45

# ---------------------------------------------------------------------------
# 2. Nine of y_1..y_26 cannot be delayed past u_26.
# ---------------------------------------------------------------------------
# Put P=p_26 and c=u_26=P+25. If at least nine of the first 26 matching y-zeros
# occur after c, order forces indices 18..26 to positions at least c+1..c+9.
# For j=18..26 the minimum displacement is
#     r_j >= P+9-p_j.
# Since w_j=2^(j-1)(2/3)^p_j,
#     w_j(2/3)^(P+9-p_j)=2^(j-1)(2/3)^(P+9),
# independent of p_j. Thus their defect contribution is at least
#     T - C(P),
# where T is their x-zero mass and C(P) is explicit.
# Meanwhile total Zx>R, prefix j<=17 is <=M17, and future j>=27 is <=F(P), so
#     T > R-M17-F(P).
# Hence E > R-M17-F(P)-C(P). We check this exact rational lower bound for every
# possible P=45..53.

def correction(P):
    factor=Fraction(2**(P+9),3**(P+9))
    return sum(Fraction(2**(j-1),1)*factor for j in range(18,27))

lbs=[]
for P in range(PMIN,PMAX+1):
    F,_=future_max(P)
    lb=R-M17-F-correction(P)
    lbs.append((lb,P))
    assert lb > ECAP
MIN_LB,MIN_P=min(lbs,key=lambda t:t[0])

# Therefore at most eight of y_1..y_26 lie after u_26. The remaining x-zero
# indices 27..30 force their matching y-zeros after u_26 as well, so the suffix
# after u_26 contains at most 8+4=12 y-zero edges and exactly 4 x-zero edges.
MAX_DELAYED_FIRST26=8
MAX_SUFFIX_Y=12
MAX_SUFFIX_X=4

# ---------------------------------------------------------------------------
# 3. Exact terminal automaton with <=4 x-zero and <=12 y-zero edges.
# ---------------------------------------------------------------------------
# It dies at depth 39, so the maximum such terminal suffix has length 38.
TARGET=39
PREC=TARGET+1
mods=[1]
for _ in range(PREC):
    mods.append(mods[-1]*3)
pow3=[1]
for _ in range(60):
    pow3.append(pow3[-1]*3)
q0=(pow(2,K,mods[PREC])+1)%mods[PREC]
states={(0,0,1,q0,PREC)}
layers=[1]
for depth in range(1,TARGET+1):
    nxt=set()
    for xz,yz,d,Qv,prec in states:
        mod=mods[prec]
        # backward 11
        if Qv%3==0:
            assert prec>=2
            nxt.add((xz,yz,d,(2*(Qv//3))%mods[prec-1],prec-1))
        # backward 10
        if yz<MAX_SUFFIX_Y:
            nxt.add((xz,yz+1,d+1,(2*Qv+1)%mod,prec))
        # backward 00
        if xz<MAX_SUFFIX_X and yz<MAX_SUFFIX_Y:
            nxt.add((xz+1,yz+1,d,(2*Qv-(pow3[d]-1))%mod,prec))
        # backward 01
        if xz<MAX_SUFFIX_X and d>1 and Qv%3==0:
            assert prec>=2
            nxt.add((xz+1,yz,d-1,(2*(Qv//3)-pow3[d-1])%mods[prec-1],prec-1))
    states=nxt
    layers.append(len(states))
    if not states:
        break
MAX_TAIL=next(i-1 for i,c in enumerate(layers) if i>0 and c==0)
assert MAX_TAIL==38
assert layers[39]==0

# Since p_26<=53, u_26=p_26+25<=78. Therefore the actual suffix after u_26
# has length at least M_INTERNAL-79 = ell-52, absurdly larger than 38.
U26_MAX=PMAX+25
TAIL_MIN=M_INTERNAL-(U26_MAX+1)
assert U26_MAX==78
assert TAIL_MIN==ELL-52
assert TAIL_MIN>MAX_TAIL

print('RL51 z=31 coupled elimination: PASS')
print('relaxed maximum at p_26=54 =',float(RELAX54),'<=',float(R))
print('therefore 45 <= p_26 <= 53 and u_26 <=',U26_MAX)
print('minimum nine-delayed defect lower bound =',float(MIN_LB),'at p_26 =',MIN_P)
print('E bound = 5/3 =',float(ECAP))
print('therefore at most',MAX_DELAYED_FIRST26,'of y_1..y_26 lie after u_26')
print('terminal suffix budgets: x-zero <=',MAX_SUFFIX_X,'y-zero <=',MAX_SUFFIX_Y)
print('exact maximum such terminal suffix length =',MAX_TAIL)
print('required suffix length is at least ell-52 =',TAIL_MIN)
print('z=31 is impossible for the sole stable continued-fraction survivor')
print('parity therefore upgrades the sole stable survivor to z>=33')
