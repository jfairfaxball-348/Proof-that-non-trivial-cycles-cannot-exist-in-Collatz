#!/usr/bin/env python3
from fractions import Fraction

A=217_976_794_617
L=137_528_045_312
B=A-L
R=L-B
ELO,EHI=72_797_034_370,103_818_202_602
CLEAN=10_075_174_499
N36=7_238_318_174
N37=7_052_720_272
GAP_LOWER=128_081_997_553
GAP_UPPER=293_591_818_782

assert B==80_448_749_305
assert R==57_079_296_007

def ceil_div(a,b):
    return (a+b-1)//b

def cbit(r):
    return 1 if r<R else 2

def overlap_intervals(sep,lo=ELO,hi=EHI):
    sh=(sep*B)%L
    out=[]
    for k in range(-2,3):
        a=max(lo,lo-sh+k*L)
        b=min(hi,hi-sh+k*L)
        if a<=b:
            out.append((a,b))
    return sh,out

def atom_intervals(lo,hi,n):
    # For fixed j, r -> (r+jB) mod L changes c only at preimages
    # of the wrap rank 0 and mechanical threshold R.
    bounds={lo,hi+1}
    for j in range(n):
        shift=(j*B)%L
        for q in (0,R):
            x=(q-shift)%L
            if lo<x<=hi:
                bounds.add(x)
    bounds=sorted(bounds)
    atoms=[(x,y-1) for x,y in zip(bounds,bounds[1:]) if x<=y-1]
    assert atoms and atoms[0][0]==lo and atoms[-1][1]==hi
    assert sum(b-a+1 for a,b in atoms)==hi-lo+1
    return atoms

def universal_ball(word):
    # Carry-completed normalized gap Delta_i=K_i/rho_i obeys
    # 2^c Delta_{i+1}=3 Delta_i+epsilon_i.
    # Every ordinary source has |epsilon_i|<1; at the unique carry
    # epsilon_i=2-2^-h_i, hence universally |epsilon_i|<2.
    #
    # Start terminal Delta=3^37/2^21.  Use the conservative strict
    # bound |epsilon_i|<2 at every step.
    radnum=0
    S=0
    for c in word:
        radnum=3*radnum + 2*(1<<S)
        S+=c
    # center = 3^(37+n)/2^(21+S), radius=radnum/2^S
    return 37+len(word),21+S,radnum,S

# RL191.1: the two RL190 exceptional separation-46 ranks are now ordinary
# inputs to the universal carry-completed gap law; no common-mechanical
# assumption is needed.
_,ov46=overlap_intervals(46)
assert ov46==[(85_411_789_764,103_818_202_602)]
exceptional=(90_789_138_715,101_129_528_126)
for r in exceptional:
    word=tuple(cbit((r+j*B)%L) for j in range(9))
    p3,denexp,radnum,S=universal_ball(word)
    assert p3==46
    for target in (2**37,2**38):
        distnum=abs(3**46-target*(1<<denexp))
        assert distnum>radnum*(1<<21)

# RL191.2: exact finite resonance scan, separations 46..1000.
# Every necessary terminal-rank overlap is partitioned into exact
# constant-mechanical-word atoms.  The conservative universal affine ball
# misses both permitted later tau=37 start gaps on every atom.
targets=(2**37,2**38)
atoms_checked=0
nonempty_separations=0
min_margin=None
worst=None
for sep in range(46,1001):
    _,overlaps=overlap_intervals(sep)
    if overlaps:
        nonempty_separations+=1
    n=sep-37
    for lo,hi in overlaps:
        for a,b in atom_intervals(lo,hi,n):
            word=tuple(cbit((a+j*B)%L) for j in range(n))
            assert tuple(cbit((b+j*B)%L) for j in range(n))==word
            p3,denexp,radnum,S=universal_ball(word)
            assert p3==sep
            for target in targets:
                distnum=abs(3**sep-target*(1<<denexp))
                rhs=radnum*(1<<21)
                assert distnum>rhs
                margin=Fraction(distnum-rhs,1<<denexp)
                if min_margin is None or margin<min_margin:
                    min_margin=margin
                    worst=(sep,a,b,target,S)
            atoms_checked+=1

assert atoms_checked==24_173
assert nonempty_separations==432
assert min_margin>5_999_580
assert worst==(665,103_606_717_628,103_809_541_145,2**37,996)
# Therefore consecutive extremal triple terminals have spacing at least 1001.

# RL191.3: exact grouped N35 density using spacing >=1001.
# Triple block span=38 and owns 3 N35 starts.  Following nontriple span S
# is at least 963.  Inherited capacity K<=floor(2S/37).
# Prove (3+K)/(38+S) <= 57/1037 by S=37q+r.
MIN_S=1001-38
assert MIN_S==963
for r in range(37):
    q=max(0,ceil_div(MIN_S-r,37))
    S=37*q+r
    K=2*q+(1 if r>=19 else 0)
    # Equivalent cross-multiplied slack:
    # 57(38+S)-1037(3+K) = 57S-945-1037K.
    slack=57*S-945-1037*K
    assert slack>=0
    # Increasing q by one raises slack by 35, so the minimal q suffices.
    assert slack+35>=slack
# Exact arithmetic equality occurs at S=999,K=54.
assert Fraction(3+54,38+999)==Fraction(57,1037)

N35=(57*L)//1037
assert (57*L)%1037==886
assert N35==7_559_400_754
early=CLEAN-N35
tau35=N35-N36
tau36=N36-N37
assert early==2_515_773_745
assert tau35==321_082_580
assert tau36==185_597_902

# RL191.4: safe offset-sensitive charging after the N35 crossover.
# Reuse RL187's exact terminal-height vocabulary and high co-ownership sets.
late_max={j:(0 if j==0 else ceil_div(j*B,L)) for j in range(40)}
height_envelope={j:1+late_max[j] for j in range(40)}
tail_H={
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
allowed_by_tau={}
for tau in range(40):
    if tau<28:
        allowed_by_tau[tau]=tuple(range(1,height_envelope[tau]+1))
    else:
        allowed_by_tau[tau]=tail_H[tau]

U=Fraction(1,2**25)
x=Fraction(10,3)*U  # tau<=34
y=Fraction(4,3)*U   # tau=35
w36=Fraction(4,3)*U # tau=36
wlong=U             # tau>=37

def charge(tau):
    if tau<=34:
        return x
    if tau==35:
        return y
    if tau==36:
        return w36
    return wlong

# Conservative low-height check from RL187.
for H in range(1,18):
    lhs=sum(charge(t) for t in range(40) if H in allowed_by_tau[t])
    assert lhs<=Fraction(1,2**(H+1))

joint_high={
    18:{(28,29,30,31,32,33,34,35)},
    19:{(30,31,32,33,34),(31,32,33,34,35,36)},
    20:{(31,32,33,34,35,36)},
    21:{(33,34,35),(34,35,36,37)},
    22:{(35,36)},
    23:{(37,38)},
    24:{(39,)},
}
for H,families in joint_high.items():
    for fam in families:
        lhs=sum(charge(t) for t in fam)
        assert lhs<=Fraction(1,2**(H+1))

# Binding equalities explicitly.
assert sum(charge(t) for t in (31,32,33,34,35,36))==Fraction(1,2**21)
assert sum(charge(t) for t in (33,34,35))==Fraction(1,2**22)

ordinary_floor=(
    early*x
    + tau35*y
    + tau36*w36
    + N37*wlong
)
assert ordinary_floor==Fraction(24_171_310_097,50_331_648)
assert ordinary_floor>480

# Inherited RL187 signed-total/carry argument converts ordinary absolute
# variation V into >V/2 for each sign and >V/6 for each directional K variation.
signed_floor=ordinary_floor/2
K_direction_floor=ordinary_floor/6
assert signed_floor==Fraction(24_171_310_097,100_663_296)
assert K_direction_floor==Fraction(24_171_310_097,301_989_888)
assert signed_floor>240
assert K_direction_floor>80

print("PASS: RL191 universal carry-completed gap transport, spacing-1001, and flow-480 certificate")
print("spacing46_exceptional_ranks_excluded=yes")
print("separations_46_through_1000_excluded=yes")
print("constant_word_atoms_checked=24173")
print("nonempty_separations_checked=432")
print("minimum_affine_safety_margin_gt=5999580")
print("extremal_triple_terminal_spacing_ge=1001")
print("N35_le=7559400754")
print("clean_tau_le_34_ge=2515773745")
print("tau35_population_cap_boundary=321082580")
print("ordinary_abs_flow_gt=24171310097/50331648")
print("ordinary_abs_flow_gt_480=yes")
print("each_signed_flow_gt=24171310097/100663296")
print("each_directional_K_variation_gt=24171310097/301989888")
print("each_directional_K_variation_gt_80=yes")
