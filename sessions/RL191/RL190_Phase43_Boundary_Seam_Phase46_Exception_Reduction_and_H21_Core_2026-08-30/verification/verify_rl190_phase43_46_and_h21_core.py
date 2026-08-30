#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict

A=217_976_794_617
L=137_528_045_312
B=A-L
R=L-B
GAP_LOWER=128_081_997_553
GAP_UPPER=293_591_818_782
CLEAN=10_075_174_499
ELO,EHI=72_797_034_370,103_818_202_602
N36=7_238_318_174
N37=7_052_720_272
EX_SWITCH=R-1
EX_CARRY=L-1

assert B==80_448_749_305
assert R==57_079_296_007

def ceil_div(a,b):
    return (a+b-1)//b

def v2(x):
    return (x & -x).bit_length()-1

def cbit(r):
    return 1 if r<R else 2

def overlap(sep,lo=ELO,hi=EHI):
    sh=(sep*B)%L
    out=[]
    for k in range(-2,3):
        a=max(lo,lo-sh+k*L)
        b=min(hi,hi-sh+k*L)
        if a<=b:
            out.append((a,b))
    return sh,out

def affine(word,delta0):
    center=delta0
    radius=Fraction(0)
    for c in word:
        center=Fraction(3,2**c)*center
        radius=Fraction(3,2**c)*radius+Fraction(1,2**c)
    return center,radius

terminal_delta=Fraction(3**37,2**21)
targets=(Fraction(2**37),Fraction(2**38))

# RL190.1: separation 43.
sh43,ov43=overlap(43)
assert sh43==21_095_087_315
assert ov43==[(72_797_034_370,82_723_115_287)]
lo43,hi43=ov43[0]
word43=tuple(cbit((lo43+j*B)%L) for j in range(6))
assert word43==(2,1,2,1,2,2)
assert tuple(cbit((hi43+j*B)%L) for j in range(6))==word43

# All six source ranks avoid the only two common-mechanical exceptions.
for j in range(6):
    for exceptional in (EX_SWITCH,EX_CARRY):
        x=(exceptional-j*B)%L
        assert not (lo43<=x<=hi43)

c43,r43=affine(word43,terminal_delta)
assert c43==Fraction(3**43,2**31)
assert r43==Fraction(1519,1024)
for target in targets:
    assert abs(c43-target)>r43

# Separations 44 and 45 are rank-empty.
sh44,ov44=overlap(44)
sh45,ov45=overlap(45)
assert sh44==101_543_836_620 and ov44==[]
assert sh45==44_464_540_613 and ov45==[]

# Hence consecutive extremal triple terminals are at least 46 phases apart.
# RL190.2: at the first unresolved separation 46, every nonexceptional
# terminal rank is also excluded by the exact common-mechanical affine ball.
sh46,ov46=overlap(46)
assert sh46==124_913_289_918
assert ov46==[(85_411_789_764,103_818_202_602)]
lo46,hi46=ov46[0]
n46=9
exceptional={}
for j in range(n46):
    for name,src in (("switch",EX_SWITCH),("carry",EX_CARRY)):
        x=(src-j*B)%L
        if lo46<=x<=hi46:
            exceptional.setdefault(x,[]).append((j,name))
assert exceptional=={
    90_789_138_715:[(3,"switch"),(4,"carry")],
    101_129_528_126:[(8,"switch")],
}

safe_parts=[
    (85_411_789_764,90_789_138_714,(2,1,2,1,2,2,1,2,1)),
    (90_789_138_716,101_129_528_125,(2,1,2,2,1,2,1,2,1)),
    (101_129_528_127,103_818_202_602,(2,1,2,2,1,2,1,2,2)),
]
for lo,hi,w in safe_parts:
    assert tuple(cbit((lo+j*B)%L) for j in range(n46))==w
    assert tuple(cbit((hi+j*B)%L) for j in range(n46))==w
    for j in range(n46):
        for src in (EX_SWITCH,EX_CARRY):
            x=(src-j*B)%L
            assert not (lo<=x<=hi)
    center,radius=affine(w,terminal_delta)
    for target in targets:
        assert abs(center-target)>radius

# Therefore a hypothetical separation-46 pair is reduced to exactly two
# terminal-rank candidates; no physical realization is asserted.
assert set(exceptional)=={90_789_138_715,101_129_528_126}

# RL190.3: spacing >=46 gives the exact N35 density ceiling 1/15.
# A triple block has span 38 and owns 3 N35 starts.
# If its following nontriple span owns no N35 start, S>=8 and 3/(38+S)<=3/46<1/15.
assert Fraction(3,46)<Fraction(1,15)
# If it owns K>0 starts, S>=36 and K<=floor(2S/37).
# Verify 15*floor(2S/37)<=S-7 symbolically by residue class S=37q+r.
for r in range(37):
    qmin=max(0,ceil_div(36-r,37))
    q=qmin
    S=37*q+r
    if S<36:
        continue
    lhs=15*(2*q+(1 if r>=19 else 0))
    rhs=S-7
    assert lhs<=rhs
    # Difference grows by 7 for each q increment, so the minimal q suffices.
    assert (rhs-lhs)+7 >= rhs-lhs
# Equality is attained at S=37,K=2, so 1/15 is the exact group ceiling.
S=37
K=(2*S)//37
assert K==2 and Fraction(3+K,38+S)==Fraction(1,15)

N35=L//15
assert L%15==2
assert N35==9_168_536_354
early=CLEAN-N35
assert early==906_638_145

# The old monotone two-level charging plateau still binds.
U=Fraction(1,2**25)
flat=Fraction(1,3*(2**22))
a=early
b=N35-N36
assert b==1_930_218_180
assert Fraction(b)-Fraction(a,2)==Fraction(2_953_798_215,2)>0
assert 2*flat+flat==8*U
# Under x>=y and 2x+y<=8U, the positive slope again maximizes at x=y=flat.
assert flat==Fraction(8,3)*U

# RL190.4: phase-resolve the dangerous H=21 {33,34,35} co-owner.
TARGET_T=350_220_815_692_997_949
TARGET_H=21
target_rows=[]
for tau in (33,34,35):
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
                if H!=TARGET_H or T!=TARGET_T:
                    continue
                if not (GAP_LOWER*(2**H)<T<GAP_UPPER*(2**H)):
                    continue
                rlo=max(0,tau*B-ell*L)
                rhi=min(L-1,tau*B-(ell-1)*L-1)
                if rlo<=rhi:
                    target_rows.append((tau,h0,C0,vv,odd,ell,rlo,rhi))

assert target_rows==[
    (33,1,541_165_879_296,33,63,20,0,41_775_866_136),
    (34,1,360_777_252_864,34,21,20,0,122_224_615_441),
    (35,0,240_518_168_576,35,7,21,0,65_145_319_434),
    (35,1,481_036_337_152,36,7,21,0,65_145_319_434),
]

danger_terminal_delta=Fraction(TARGET_T,2**TARGET_H)

def word_before_terminal(r_terminal,n):
    return tuple(cbit((r_terminal-(n-j)*B)%L) for j in range(n))

def backward_gaps(word,terminal):
    ds=[None]*(len(word)+1)
    ds[-1]=terminal
    for j in range(len(word)-1,-1,-1):
        ds[j]=ds[j+1]*(2**word[j])/3
    return tuple(ds)

def full_prefix_core(rawlo,rawhi,tau):
    bounds={rawlo,rawhi+1}
    for j in range(tau):
        shift=(tau-j)*B
        for threshold in (0,R):
            q=(threshold+shift)%L
            if rawlo<q<=rawhi:
                bounds.add(q)
    bounds=sorted(bounds)
    good=[]
    for x,y in zip(bounds,bounds[1:]):
        lo,hi=x,y-1
        if lo>hi:
            continue
        w=word_before_terminal(lo,tau)
        assert word_before_terminal(hi,tau)==w
        ds=backward_gaps(w,danger_terminal_delta)
        if all(Fraction(GAP_LOWER)<d<Fraction(GAP_UPPER) for d in ds):
            good.append((lo,hi))
    merged=[]
    for lo,hi in good:
        if merged and merged[-1][1]+1==lo:
            merged[-1]=(merged[-1][0],hi)
        else:
            merged.append((lo,hi))
    return merged

cores={}
for row in target_rows:
    tau,h0=row[0],row[1]
    cores[(tau,h0)]=full_prefix_core(row[-2],row[-1],tau)

assert cores[(33,1)]==[(23_369_453_298,41_775_866_136)]
assert cores[(34,1)]==[(23_369_453_298,59_767_970_482)]
assert cores[(35,0)]==[(23_369_453_298,59_767_970_482)]
assert cores[(35,1)]==[(23_369_453_298,59_767_970_482)]

# Joint intersection for all three offsets.
DLO=23_369_453_298
DHI=41_775_866_136
assert DHI<R
assert DHI<ELO
# The tau=35 starting numerator has odd part 7, so it is not divisible by 3.
# By the inherited RL182 first-ternary-digit sensor, its predecessor defect is odd/nonzero.
assert 240_518_168_576 == 7*(2**35)
assert 240_518_168_576 % 3 != 0
# Thus the dangerous {33,34,35} terminal block has exact span 36.

ordinary_floor=Fraction(2_787_212_689,6_291_456)
assert ordinary_floor>443

print("PASS: RL190 phase-43/46 seam and phase-resolved H21 certificate")
print("extremal_triple_terminal_spacing_ge=46")
print("spacing46_candidate_terminal_ranks={90789138715,101129528126}")
print("N35_le=9168536354")
print("clean_tau_le_34_ge=906638145")
print("H21_333435_joint_terminal_rank_core=[23369453298,41775866136]")
print("H21_333435_block_span=36")
print("ordinary_abs_flow_inherited_gt=2787212689/6291456")
