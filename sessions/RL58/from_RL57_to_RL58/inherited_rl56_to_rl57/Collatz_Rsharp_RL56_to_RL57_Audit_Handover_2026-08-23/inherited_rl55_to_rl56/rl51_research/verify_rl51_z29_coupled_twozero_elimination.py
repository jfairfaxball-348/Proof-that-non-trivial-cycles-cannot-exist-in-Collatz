#!/usr/bin/env python3
from fractions import Fraction

# RL51 exact coupled elimination of z=29 for the sole stable continued-fraction survivor.
# Stable inherited inputs used:
#   * E < 5/3 and Zx > 143/12;
#   * each x-zero weight is < 17/30;
#   * zero displacement: E=sum_j w_j[1-(2/3)^r_j], r_j=v_j-u_j>=0;
#   * terminal J=2^k with Q_d=J+2^d-1 and the exact four backward maps.

A   = 123139092617126647266
ELL =  77692117359936589403
QGAP = A-ELL
Z = 29
S = Z-1                       # 28 internal x-zeros and 28 internal y-zeros
K = QGAP-Z+3                  # q-26
M_INTERNAL = ELL+Z-4          # (ell-3) x-ones plus (z-1) x-zeros
CAP = Fraction(17,30)
ZX_REQ = Fraction(143,12)
E_CAP = Fraction(5,3)


def weight(j,p):
    # j-th x-zero, with p x-ones before it
    return Fraction(2**(p+j-1),3**p)


def greedy_from(j0,p0,n):
    p=p0
    ps=[]
    ws=[]
    for j in range(j0,n+1):
        while weight(j,p)>CAP:
            p += 1
        ps.append(p)
        ws.append(weight(j,p))
    return ps,ws

# ---------------------------------------------------------------------------
# 1. Terminal suffixes with at most one x-zero have length at most 72.
# ---------------------------------------------------------------------------
# Backward maps in Q_d=J+2^d-1:
#   11: Q -> 2Q/3, requires 3|Q, d fixed
#   10: Q -> 2Q+1, d -> d+1, consumes one y-zero
#   00: Q -> 2Q-(3^d-1), d fixed, consumes one x-zero and one y-zero
#   01: Q -> 2Q/3-3^(d-1), requires d>1 and 3|Q,
#       d -> d-1, consumes one x-zero.
# We disprove a 73-edge suffix. 74 ternary digits suffice because each
# dividing edge loses one digit and there are at most 73 edges.
TARGET1=73
PREC1=TARGET1+1
mods1=[1]
for _ in range(PREC1):
    mods1.append(mods1[-1]*3)
pow3=[1]
for _ in range(40):
    pow3.append(pow3[-1]*3)
q0=(pow(2,K,mods1[PREC1])+1) % mods1[PREC1]
states={(0,0,1,q0,PREC1)} # (xz,yz,d,Q,precision)
layer1=[1]
for depth in range(1,TARGET1+1):
    nxt=set()
    for xz,yz,d,Q,prec in states:
        mod=mods1[prec]
        if Q%3==0:
            assert prec>=2
            nxt.add((xz,yz,d,(2*(Q//3))%mods1[prec-1],prec-1))
        if yz<S:
            nxt.add((xz,yz+1,d+1,(2*Q+1)%mod,prec))
        if xz<1 and yz<S:
            nxt.add((xz+1,yz+1,d,(2*Q-(pow3[d]-1))%mod,prec))
        if xz<1 and d>1 and Q%3==0:
            assert prec>=2
            nxt.add((xz+1,yz,d-1,(2*(Q//3)-pow3[d-1])%mods1[prec-1],prec-1))
    states=nxt
    layer1.append(len(states))
    if not states:
        break
MAX_ONE_X=next(i-1 for i,c in enumerate(layer1) if i>0 and c==0)
assert MAX_ONE_X==72
assert layer1[73]==0

# Therefore both the final and second-final x-zero are within a 73-column
# terminal window. A deliberately crude common bound on either pre-zero weight:
#   g_end < 27/2^K  (using zeta<2),
#   w < (g_end/2)*(3/2)^72 < 27*3^72 / 2^(K+73) < 2^-1000.
# (The second-final zero actually has an additional /2 from the final x-zero.)
assert (27*(3**72)).bit_length() <= K+73-1000
TINY = Fraction(1,2**1000)

# ---------------------------------------------------------------------------
# 2. With the last two weights tiny, the first 26 x-zero schedule is rigid.
# ---------------------------------------------------------------------------
N=26
pstar,wstar=greedy_from(1,0,N)
Z26_MAX=sum(wstar,Fraction(0))
second=[]
for idx in range(N):
    j=idx+1
    prefix=sum(wstar[:idx],Fraction(0))
    pdev=pstar[idx]+1
    wdev=weight(j,pdev)
    if j<N:
        _,tail=greedy_from(j+1,pdev,N)
        total=prefix+wdev+sum(tail,Fraction(0))
    else:
        total=prefix+wdev
    second.append((total,j,pdev))
SECOND,jdev,pdev=max(second,key=lambda x:x[0])
assert SECOND + 2*TINY < ZX_REQ
assert pstar == [2,4,5,7,9,10,12,14,16,17,19,21,22,24,26,28,29,31,33,34,36,38,40,41,43,45]
# Hence any genuine z=29 survivor must have these first 26 p_j exactly.
u=[pstar[j-1]+j-1 for j in range(1,N+1)]
w=wstar
assert u[-1]==70

# ---------------------------------------------------------------------------
# 3. E<5/3 allows at most four of the first 26 matching y-zeros after col 70.
# ---------------------------------------------------------------------------
# If at least five are after u_26=70, order forces y-zero indices 22..26 to
# occupy positions at least 71,72,73,74,75. Their minimum displacement-energy
# alone already exceeds 5/3.
D5=Fraction(0)
for idx,j in enumerate(range(22,27),start=1):
    vmin=70+idx
    r=vmin-u[j-1]
    assert r>=1
    D5 += w[j-1]*(1-Fraction(2,3)**r)
assert D5 > E_CAP
# So at most 4 of y-zero indices 1..26 occur after column 70. Since
# v_27>=u_27>70 and v_28>=u_28>70, the suffix after col 70 contains at most
# 4+2=6 y-zero edges.
MAX_SUFFIX_YZERO=6

# ---------------------------------------------------------------------------
# 4. Exact terminal automaton with <=2 x-zeros and <=6 y-zeros dies at 20.
# ---------------------------------------------------------------------------
TARGET2=20
PREC2=TARGET2+1
mods2=[1]
for _ in range(PREC2):
    mods2.append(mods2[-1]*3)
q0b=(pow(2,K,mods2[PREC2])+1) % mods2[PREC2]
states={(0,0,1,q0b,PREC2)}
layer2=[1]
for depth in range(1,TARGET2+1):
    nxt=set()
    for xz,yz,d,Q,prec in states:
        mod=mods2[prec]
        if Q%3==0:
            assert prec>=2
            nxt.add((xz,yz,d,(2*(Q//3))%mods2[prec-1],prec-1))
        if yz<MAX_SUFFIX_YZERO:
            nxt.add((xz,yz+1,d+1,(2*Q+1)%mod,prec))
        if xz<2 and yz<MAX_SUFFIX_YZERO:
            nxt.add((xz+1,yz+1,d,(2*Q-(pow3[d]-1))%mod,prec))
        if xz<2 and d>1 and Q%3==0:
            assert prec>=2
            nxt.add((xz+1,yz,d-1,(2*(Q//3)-pow3[d-1])%mods2[prec-1],prec-1))
    states=nxt
    layer2.append(len(states))
    if not states:
        break
MAX_COUPLED_TAIL=next(i-1 for i,c in enumerate(layer2) if i>0 and c==0)
assert MAX_COUPLED_TAIL==19
assert layer2[20]==0

# But after the forced 26th x-zero at zero-based column 70, a z=29 word has
# exactly two x-zeros left and an internal suffix of astronomical length.
TAIL_AFTER_U26=M_INTERNAL-(70+1)
assert TAIL_AFTER_U26==ELL-46
assert TAIL_AFTER_U26>MAX_COUPLED_TAIL

print('RL51 z=29 coupled two-zero elimination: PASS')
print('maximum terminal suffix with <=1 x-zero and <=28 y-zeros =',MAX_ONE_X)
print('therefore final two x-zero weights are each < 2^-1000')
print('best non-greedy first-26 zero mass =',float(SECOND))
print('required mass Zx > 143/12 =',float(ZX_REQ))
print('forced first-26 x-zero schedule =',pstar)
print('forced u_26 =',u[-1])
print('minimum E cost if five of y_1..y_26 lie after column 70 =',float(D5))
print('hence suffix after column 70 has at most',MAX_SUFFIX_YZERO,'y-zero edges')
print('maximum terminal suffix with <=2 x-zeros and <=6 y-zeros =',MAX_COUPLED_TAIL)
print('required suffix length after u_26 = ell-46 =',TAIL_AFTER_U26)
print('z=29 is impossible for the sole stable continued-fraction survivor')
print('parity therefore upgrades the sole stable survivor to z>=31')
