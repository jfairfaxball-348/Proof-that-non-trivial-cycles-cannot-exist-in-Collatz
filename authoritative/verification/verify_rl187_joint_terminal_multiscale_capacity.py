#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
B=A-L
GAP_LOWER=128_081_997_553
GAP_UPPER=293_591_818_782
CLEAN=10_075_174_499
assert A*p-L*u==1

def ceil_div(a,b):
    return (a+b-1)//b

def v2(x):
    return (x & -x).bit_length()-1

# RL185/RL186 inherited mechanical height envelope and late-tail vocabulary.
late_max={j:(0 if j==0 else ceil_div(j*B,L)) for j in range(40)}
height_envelope={j:1+late_max[j] for j in range(40)}
assert height_envelope[39]==24

# RL187.1 exact joint first-defect ownership.
# For a shallow zero-prefix start at offset tau>0:
#   T=C_tau=3^tau*odd(C0)
# and telescoping d_j=c_j+M_j-M_(j+1) gives
#   H=h0+tau+ell-v2(C0),
# where ell is the number of c=2 mechanical bits in the tau transitions.
# If r is the terminal mechanical residue, fixed ell is possible exactly on
#   tau*B-ell*L <= r < tau*B-(ell-1)*L
# after clipping to 0<=r<L.
rows=defaultdict(list)
tail_H={}
for tau in range(28,40):
    possible_H=set()
    ell0=(tau*B)//L
    ell1=ceil_div(tau*B,L)
    for h0 in (0,1):
        lo=GAP_LOWER*(2**h0)
        hi=GAP_UPPER*(2**h0)
        step=2**tau
        for k in range(lo//step+1,(hi-1)//step+1):
            C0=k*step
            vv=v2(C0)
            odd=C0>>vv
            T=(3**tau)*odd
            for ell in sorted(set((ell0,ell1))):
                H=h0+tau+ell-vv
                if H<1 or H>height_envelope[tau]:
                    continue
                if not (GAP_LOWER*(2**H) < T < GAP_UPPER*(2**H)):
                    continue
                rlo=max(0,tau*B-ell*L)
                rhi=min(L-1,tau*B-(ell-1)*L-1)
                if rlo>rhi:
                    continue
                rows[(T,H)].append((tau,h0,C0,vv,ell,rlo,rhi))
                possible_H.add(H)
    tail_H[tau]=tuple(sorted(possible_H))

expected_tail={
    28:(7,8,9,10,11,12,13,14,15,16,17,18),
    29:(8,9,10,11,12,13,14,15,16,17,18),
    30:(10,12,13,14,15,16,17,18,19),
    31:(12,13,14,15,16,17,18,19,20),
    32:(13,15,16,17,18,19,20),
    33:(15,16,17,18,19,20,21),
    34:(16,18,19,20,21),
    35:(18,19,20,21,22),
    36:(19,20,21,22),
    37:(21,23),
    38:(23,),
    39:(24,),
}
assert tail_H==expected_tail

# Maximal simultaneously compatible offset sets for a fixed terminal defect.
def maximal_sets_for_height(H):
    seen=set()
    for (T,H0),rs in rows.items():
        if H0!=H:
            continue
        points={0}
        for row in rs:
            lo,hi=row[-2],row[-1]
            points.add(lo)
            if hi+1<L:
                points.add(hi+1)
        for r in points:
            ts=frozenset(row[0] for row in rs if row[-2] <= r <= row[-1])
            if ts:
                seen.add(ts)
    return {s for s in seen if not any(s<t for t in seen)}

joint_high={H:{tuple(sorted(s)) for s in maximal_sets_for_height(H)} for H in range(18,25)}
expected_joint_high={
    18:{(28,29,30,31,32,33,34,35)},
    19:{(30,31,32,33,34),(31,32,33,34,35,36)},
    20:{(31,32,33,34,35,36)},
    21:{(33,34,35),(34,35,36,37)},
    22:{(35,36)},
    23:{(37,38)},
    24:{(39,)},
}
assert joint_high==expected_joint_high

# RL187.2 multiscale survival-density staircase.
# Partition the cyclic defect sequence into blocks ending at one nonzero defect.
# A start with first-defect offset tau forces a block span of at least tau+1
# physical phase positions.  Joint ownership bounds how many such starts a
# single block can contain.
all_joint_sets=set()
for (T,H),rs in rows.items():
    points={0}
    for row in rs:
        lo,hi=row[-2],row[-1]
        points.add(lo)
        if hi+1<L:
            points.add(hi+1)
    for r in points:
        ts=frozenset(row[0] for row in rs if row[-2] <= r <= row[-1])
        if ts:
            all_joint_sets.add(ts)

density={}
density_witness={}
for n in range(28,40):
    best=Fraction(0)
    witness=None
    for S in all_joint_sets:
        T=sorted(t for t in S if t>=n)
        if not T:
            continue
        d=Fraction(len(T),max(T)+1)
        if d>best:
            best=d
            witness=tuple(T)
    density[n]=best
    density_witness[n]=witness

expected_density={
    28:Fraction(2,9),
    29:Fraction(7,36),
    30:Fraction(1,6),
    31:Fraction(6,37),
    32:Fraction(5,37),
    33:Fraction(4,37),
    34:Fraction(2,19),
    35:Fraction(3,38),
    36:Fraction(1,19),
    37:Fraction(2,39),
    38:Fraction(1,39),
    39:Fraction(1,40),
}
assert density==expected_density

Ncap={n:(density[n].numerator*L)//density[n].denominator for n in range(28,40)}
assert Ncap[36]==7_238_318_174
assert Ncap[37]==7_052_720_272
assert Ncap[38]==3_526_360_136
assert Ncap[39]==3_438_201_132

# RL187.3 joint weighted charging.
# For H<=17 use the conservative RL186 offset vocabulary.  For H>=18 use
# exact joint terminal-defect families above.
allowed_by_tau={}
for tau in range(40):
    if tau<28:
        allowed_by_tau[tau]=tuple(range(1,height_envelope[tau]+1))
    else:
        allowed_by_tau[tau]=tail_H[tau]

w_short=Fraction(1,3*(2**22))   # tau<=35
w_36=Fraction(1,3*(2**23))      # tau=36
w_long=Fraction(1,2**25)        # tau>=37
def charge(t):
    if t<=35:
        return w_short
    if t==36:
        return w_36
    return w_long

# Low heights: even charging every individually allowed offset is safe.
for H in range(1,18):
    lhs=sum(charge(t) for t in range(40) if H in allowed_by_tau[t])
    assert lhs <= Fraction(1,2**(H+1))

# High heights: exact co-ownership families are required.
for H in range(18,25):
    for S in joint_high[H]:
        lhs=sum(charge(t) for t in S)
        assert lhs <= Fraction(1,2**(H+1))

# Therefore total ordinary |f| exceeds the sum of charges over all CLEAN starts.
# Minimize that charge using the N_36 and N_37 survival caps.
N36=Ncap[36]
N37=Ncap[37]
ordinary_floor=(
    Fraction(CLEAN,3*(2**22))
    - Fraction(N36,3*(2**23))
    - Fraction(N37,3*(2**25))
)
assert ordinary_floor==Fraction(2_787_212_689,6_291_456)
assert ordinary_floor>443

# Re-certify inherited exact signed total 0<F2<1/2.
def ln_bounds_int(x,N=80):
    x=Fraction(x)
    z=(x-1)/(x+1)
    z2=z*z
    term=z
    s=Fraction(0)
    for n in range(N):
        s += term/Fraction(2*n+1)
        term *= z2
    lo=2*s
    tail=2*term/Fraction(2*N+1)/(1-z2)
    return lo,lo+tail

@lru_cache(maxsize=None)
def exp_bounds_pos(x,N=36):
    assert 0<=x<1
    term=Fraction(1)
    s=term
    for k in range(1,N+1):
        term=term*x/k
        s += term
    nxt=term*x/Fraction(N+1)
    tail=nxt/(1-x/Fraction(N+2))
    return s,s+tail

l2_lo,l2_hi=ln_bounds_int(2)
l3_lo,l3_hi=ln_bounds_int(3)
d_lo=A*l2_lo-L*l3_hi
d_hi=A*l2_hi-L*l3_lo
assert 0<d_lo<d_hi<Fraction(1,1000)
ed_lo,_=exp_bounds_pos(d_lo)
_,ed_hi=exp_bounds_pos(d_hi)
F2_lo=3*(2**37)*(ed_lo-1)
F2_hi=3*(2**37)*(ed_hi-1)
assert F2_lo>0
assert F2_hi<Fraction(1,2)

# Carry is inherited positive >1/2.  Full absolute flow is therefore
# > ordinary_floor+1/2 while net F2<1/2, so both signs exceed ordinary_floor/2.
signed_floor=ordinary_floor/2
K_direction_floor=signed_floor/3
assert signed_floor>217
assert K_direction_floor>Fraction(738,10) # >73.8

print("PASS: RL187 joint terminal ownership and multiscale capacity certificate")
print("N36_le=7238318174")
print("N37_le=7052720272")
print("N38_le=3526360136")
print("N39_le=3438201132")
print("ordinary_abs_flow_gt=2787212689/6291456")
print("ordinary_abs_flow_gt_443=yes")
print("each_signed_flow_gt=2787212689/12582912")
print("each_directional_K_variation_gt=2787212689/37748736")
print("each_directional_K_variation_gt_73_8=yes")
