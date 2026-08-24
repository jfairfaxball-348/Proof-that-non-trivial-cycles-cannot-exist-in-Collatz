#!/usr/bin/env python3
from fractions import Fraction

# RL51 exact certificate for the stable z=27 survivor.
# It uses only already-audited stable RL50 inputs:
#   * 26 internal x-zeros when z=27;
#   * each x-zero weight w < 17/30 (safe post-zero prefix cap);
#   * on the sole stable CF survivor E < 5/3;
#   * 2 Zx + E = 12 + (27/2) zeta (1+2^-k) > 51/2;
#   * terminal J=2^k, k=t+3.

A   = 123139092617126647266
ELL =  77692117359936589403
QGAP = A-ELL
Z = 27
S = Z-1                 # internal x-zeros = internal y-zeros
K = QGAP-Z+3            # t=q-z, k=t+3
M_INTERNAL = ELL+Z-4    # (ell-3) ones + (z-1) zeros
CAP = Fraction(17,30)
ZX_LOWER = Fraction(143,12)  # follows strictly from E<5/3


def weight(j,p):
    """Weight of the j-th x-zero (j>=1) with p x-ones before it."""
    return Fraction(2**(p+j-1),3**p)


def greedy_from(j0, p0, n=S):
    """Coordinatewise-maximal zero schedule under w<=CAP and nondecreasing p."""
    p=p0
    ps=[]
    ws=[]
    for j in range(j0,n+1):
        while weight(j,p)>CAP:
            p += 1
        ps.append(p)
        ws.append(weight(j,p))
    return ps,ws

# The total zero mass is monotone decreasing in every p_j, while p_j is
# nondecreasing. Hence the global maximum is the greedy minimal p-sequence.
pstar,wstar=greedy_from(1,0)
ZMAX=sum(wstar,Fraction(0))
assert all(w<CAP for w in wstar)  # strict cap is respected by the maximizer
assert ZMAX>ZX_LOWER

# Any non-greedy schedule has a first index j where p_j >= p*_j+1.
# For each possible first deviation, maximize the rest greedily from that
# elevated p. The maximum of these 26 exact candidates is therefore the exact
# best non-greedy total in the relaxed cap class.
second_candidates=[]
for idx in range(S):
    j=idx+1
    prefix=sum(wstar[:idx],Fraction(0))
    pdev=pstar[idx]+1
    wdev=weight(j,pdev)
    assert wdev<CAP
    if j<S:
        _,wtail=greedy_from(j+1,pdev)
        total=prefix+wdev+sum(wtail,Fraction(0))
    else:
        total=prefix+wdev
    second_candidates.append((total,j,pdev))

SECOND,jdev,pdev=max(second_candidates,key=lambda x:x[0])
assert SECOND < ZX_LOWER

# Therefore the genuine z=27 survivor, which has Zx>143/12, must use exactly
# pstar. In particular its last x-zero position is u_26=p_26+25=70.
assert pstar == [2,4,5,7,9,10,12,14,16,17,19,21,22,24,26,28,29,31,33,34,36,38,40,41,43,45]
LAST_X_ZERO = pstar[-1] + S-1
assert LAST_X_ZERO == 70
TAIL_LEN = M_INTERNAL-(LAST_X_ZERO+1)  # x=1 columns after position 70
assert TAIL_LEN == ELL-48
assert TAIL_LEN > 56

# Exact backward grammar for an x=1-only suffix.
# At height d set Qd=J+(2^d-1).
# Forward 11: Q -> 3Q/2, so backward 11 exists iff 3|Q and sends Q->2Q/3.
# Forward 10: Q_d -> (Q_d-1)/2 at height d-1, so backward 10 sends Q->2Q+1
# and raises d by one. Each backward 10 consumes one y-zero. There are at most
# S=26 such descents in the entire internal word.
#
# We only need to disprove a chain of length 57. Residues modulo 3^58 are
# sufficient: each backward 11 division loses one 3-adic digit, so during any
# 57-step chain at least one digit remains. Thus the BFS below is exact for
# existence/nonexistence of a 57-edge predecessor chain; it does not construct
# the astronomically large 2^K.
TARGET=57
PREC0=TARGET+1
MOD0=3**PREC0
q0=(pow(2,K,MOD0)+1) % MOD0  # terminal Q_1 = 2^K+1 modulo 3^58

# states are (number_of_backward_10_steps, residue_Q, precision)
states={(0,q0,PREC0)}
layer_counts=[1]
for depth in range(1,TARGET+1):
    nxt=set()
    for a,q,prec in states:
        mod=3**prec
        assert 0 <= q < mod
        # backward 11: exact divisibility test at current precision
        if q % 3 == 0:
            assert prec>=2  # TARGET+1 precision guarantees this through depth 57
            qB=(2*(q//3)) % (3**(prec-1))
            nxt.add((a,qB,prec-1))
        # backward 10: at most 26 y-zero descents in the whole word
        if a<S:
            qA=(2*q+1) % mod
            nxt.add((a+1,qA,prec))
    states=nxt
    layer_counts.append(len(states))
    if not states:
        break

MAX_TAIL=next(i-1 for i,c in enumerate(layer_counts) if i>0 and c==0)
assert MAX_TAIL==56, (MAX_TAIL,layer_counts[-5:])
assert len(layer_counts)>=58 and layer_counts[57]==0

# Independent exact symbolic cross-check. Represent a backward-tail value as
#     Q = (A*2^K + B)/3^b.
# Backward 11 is legal iff the numerator is divisible by 3^(b+1), then
#     (A,B,b) -> (2A,2B,b+1).
# Backward 10 sends
#     (A,B,b) -> (2A, 2B+3^b, b).
# This uses no truncated 3-adic residue state.
from functools import lru_cache
@lru_cache(None)
def symbolic_max(a,b,Acoef,Bcoef):
    best=0
    mod=3**(b+1)
    if (Acoef*pow(2,K,mod)+Bcoef) % mod == 0:
        best=max(best,1+symbolic_max(a,b+1,2*Acoef,2*Bcoef))
    if a<S:
        best=max(best,1+symbolic_max(a+1,b,2*Acoef,2*Bcoef+3**b))
    return best

SYMBOLIC_MAX=symbolic_max(0,0,1,1)
assert SYMBOLIC_MAX==MAX_TAIL==56

print('RL51 z=27 terminal-tail certificate: PASS')
print('stable lower bound: Zx > 143/12 =', float(ZX_LOWER))
print('26-zero greedy maximum Zx =', ZMAX, '=', float(ZMAX))
print('best non-greedy 26-zero Zx =', SECOND, '=', float(SECOND))
print('best non-greedy first deviation: zero', jdev, 'uses p=', pdev)
print('unique forced x-one counts before zeros =', pstar)
print('forced last x-zero position =', LAST_X_ZERO)
print('required x=1-only suffix length = ell-48 =', TAIL_LEN)
print('exact backward terminal-power maximum x=1-only suffix length =', MAX_TAIL)
print('z=27 is impossible for the sole stable continued-fraction survivor')
print('since q is odd and t is even, the survivor now satisfies z>=29')
