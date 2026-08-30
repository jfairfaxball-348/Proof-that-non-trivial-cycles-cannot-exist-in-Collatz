#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict

A=217_976_794_617
L=137_528_045_312
B=A-L
R=2*L-A
GAP_LOWER=128_081_997_553
GAP_UPPER=293_591_818_782
CLEAN=10_075_174_499
TARGET_T=3**37
TARGET_H=21

assert A==L+B
assert R==L-B
assert 0<R<L
assert B==80_448_749_305

def ceil_div(a,b):
    return (a+b-1)//b

def v2(x):
    return (x & -x).bit_length()-1

def cbit(r):
    return 1 if r<R else 2

# Reconstruct the RL187 late-tail candidates needed by RL188.
late_max={j:(0 if j==0 else ceil_div(j*B,L)) for j in range(40)}
height_envelope={j:1+late_max[j] for j in range(40)}
rows=defaultdict(list)
for tau in range(28,40):
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
                if rlo<=rhi:
                    rows[(T,H)].append((tau,h0,C0,vv,ell,rlo,rhi))

target_rows=rows[(TARGET_T,TARGET_H)]
by_tau=defaultdict(list)
for row in target_rows:
    by_tau[row[0]].append(row)
assert set(by_tau) >= {35,36,37}

# Find the exact raw terminal-rank set on which all three offsets 35,36,37
# have at least one RL187 candidate with common (T,H).
points={0,L}
for tau in (35,36,37):
    for row in by_tau[tau]:
        lo,hi=row[-2],row[-1]
        points.add(lo)
        if hi+1<L:
            points.add(hi+1)
points=sorted(points)
raw_segments=[]
for x,y in zip(points,points[1:]):
    lo,hi=x,y-1
    if lo>hi:
        continue
    sample=lo
    ok=True
    for tau in (35,36,37):
        if not any(row[-2] <= sample <= row[-1] for row in by_tau[tau]):
            ok=False
            break
    if ok:
        raw_segments.append((lo,hi))
raw_merged=[]
for lo,hi in raw_segments:
    if raw_merged and raw_merged[-1][1]+1==lo:
        raw_merged[-1]=(raw_merged[-1][0],hi)
    else:
        raw_merged.append((lo,hi))
assert raw_merged==[(65_145_319_435,L-1)]

# For a terminal rank r, reconstruct the actual 37 chronological mechanical
# bits immediately before the terminal defect.
def cword_before_terminal(r_terminal,n=37):
    return tuple(
        cbit((r_terminal-(n-j)*B) % L)
        for j in range(n)
    )

terminal_delta=Fraction(TARGET_T,2**TARGET_H)

def backward_gap_sequence(word):
    # ds[j] is the normalized p-gap at the start plus j transitions;
    # ds[-1] is the terminal first-defect gap.
    ds=[None]*(len(word)+1)
    ds[-1]=terminal_delta
    for j in range(len(word)-1,-1,-1):
        # zero defect: 2^c delta' = 3 delta
        ds[j]=ds[j+1]*(2**word[j])/3
    return tuple(ds)

# Word changes only when one of the 37 predecessor residues crosses 0 or R.
bounds={65_145_319_435,L}
for j in range(37):
    shift=(37-j)*B
    for threshold in (0,R):
        q=(threshold+shift)%L
        if 65_145_319_435 <= q < L:
            bounds.add(q)
bounds=sorted(bounds)

good=[]
for x,y in zip(bounds,bounds[1:]):
    lo,hi=x,y-1
    if lo>hi:
        continue
    w=cword_before_terminal(lo)
    assert cword_before_terminal(hi)==w
    ds=backward_gap_sequence(w)
    if all(Fraction(GAP_LOWER)<d<Fraction(GAP_UPPER) for d in ds):
        good.append((lo,hi,ds[0],sum(c==2 for c in w)))

# Merge adjacent good intervals; their internal mechanical words may differ.
merged=[]
for lo,hi,_,_ in good:
    if merged and merged[-1][1]+1==lo:
        merged[-1]=(merged[-1][0],hi)
    else:
        merged.append((lo,hi))
assert merged==[(72_797_034_370,103_818_202_602)]
ELO,EHI=merged[0]
EDIAM=EHI-ELO
EWIDTH=EDIAM+1
assert EWIDTH==31_021_168_233

# Every surviving triple's tau=37 start has normalized gap exactly 2^37 or 2^38.
start_gaps=set()
for lo,hi,ds0,ell in good:
    start_gaps.add(ds0)
assert start_gaps=={Fraction(2**37),Fraction(2**38)}

# RL182 ternary reset: odd(C_start)=1 for tau=37, hence C_start is a
# power of two and 3 does not divide it. Therefore the immediately preceding
# defect is odd and nonzero. The triple block is exactly 38 phases long.
for row in by_tau[37]:
    C0=row[2]
    assert C0 >> v2(C0) == 1

# No two triple terminals can be 38 or 40 chronological phases apart:
# their terminal ranks would differ by s*B mod L, which is outside E-E.
for s,expected in ((38,31_435_476_726),(40,54_804_930_024)):
    d=(s*B)%L
    assert d==expected
    assert EDIAM < d < L-EDIAM

# A 39-phase separation would put the next triple's tau=37 start at t+2.
# On E, the two actual mechanical bits are c_t=2 and c_(t+1)=1.
assert ELO>R
r1lo=(ELO+B)%L
r1hi=(EHI+B)%L
assert r1lo<=r1hi<R

# Across those two common-mechanical ordinary transitions,
#   4 delta_1 = 3 delta_t + e0
#   2 delta_2 = 3 delta_1 + e1
# with |e0|,|e1|<1. Hence delta_2 lies within 7/8 of:
center=Fraction(9,8)*terminal_delta
assert center==Fraction(3**39,2**24)
err=Fraction(7,8)
for g in (Fraction(2**37),Fraction(2**38)):
    assert abs(g-center)>err
# Thus no 39-separated pair of triple terminals is possible.

# A later triple terminal cannot occur within 37 phases because its preceding
# 37 zero-defect edges would contain the earlier nonzero terminal. Combining
# this with the 38/39/40 exclusions gives terminal spacing at least 41.

# Density consequence. Nontriple blocks retain RL187's 2/37 density ceiling.
# Group each triple block (3 starts, span 38) with the following nontriple
# blocks up to the next triple. Their total span S is at least 3.
# If those blocks own no N35 starts, density <=3/41.
# If they own K>0 starts, then S>=36 and K<=2S/37; verify the group bound.
assert Fraction(2,37) < Fraction(3,41)
# For K>0, at least one N35 start forces S>=36.  Using K<=2S/37,
# the desired group inequality is equivalent to 29*S>=333.
assert 29*36 >= 333

N35_CAP=(3*L)//41
FORCED_EARLY=CLEAN-N35_CAP
assert N35_CAP==10_063_027_705
assert FORCED_EARLY==12_146_794
assert N35_CAP<CLEAN

print("PASS: RL188 extremal triple spacing and N35 crossover certificate")
print("triple_terminal_rank_core=[72797034370,103818202602]")
print("triple_terminal_rank_core_width=31021168233")
print("triple_terminal_spacing_ge=41")
print("N35_le=10063027705")
print("N35_density_le=3/41")
print("clean_tau_le_34_ge=12146794")
