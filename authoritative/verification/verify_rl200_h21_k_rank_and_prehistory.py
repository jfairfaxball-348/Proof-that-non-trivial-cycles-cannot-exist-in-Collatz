#!/usr/bin/env python3
from fractions import Fraction

A=217_976_794_617
L=137_528_045_312
B=A-L
R=2*L-A
p=65_470_613_321
DLO,DHI=23_369_453_298,41_775_866_136
KLO,KHI=128_081_997_553,146_795_909_391
RSTAR=25_583_192_106
T=7*(3**35)

def ln_bounds(x, terms=110):
    x=Fraction(x)
    z=(x-1)/(x+1)
    z2=z*z
    term=z
    partial=Fraction(0)
    for j in range(terms):
        partial += term/(2*j+1)
        term *= z2
    lower=2*partial
    tail=2*abs(term)/Fraction(2*terms+1)/(1-z2)
    return lower, lower+tail

def mul(c, bounds):
    lo,hi=bounds
    return (c*lo,c*hi) if c>=0 else (c*hi,c*lo)

ln2=ln_bounds(2)
ln3=ln_bounds(3)
delta_lo=A*ln2[0]-L*ln3[1]
delta_hi=A*ln2[1]-L*ln3[0]
assert 0 < delta_lo < delta_hi < Fraction(1,2**40)
assert ln2[0] > L*delta_hi

ln87=ln_bounds(Fraction(8,7))

def log_k_over_u(r,u):
    i=(p*r)%L
    n=(A*i-r)//L
    assert A*i == n*L+r
    # K/U = (7*3^35/2^21)*(2^n/3^i)/U.
    # Write 7=2^3/(8/7) and U=2^37*(U/2^37).
    ur=ln_bounds(Fraction(u,2**37))
    pieces=[
        mul(n-55,ln2),
        mul(35-i,ln3),
        (-ln87[1],-ln87[0]),
        (-ur[1],-ur[0]),
    ]
    return sum(x[0] for x in pieces),sum(x[1] for x in pieces)

lo,hi=log_k_over_u(RSTAR-1,KHI)
assert lo>0
lo,hi=log_k_over_u(RSTAR,KHI)
assert hi<0
lo,hi=log_k_over_u(DHI,KLO)
assert lo>0

# Strict monotonicity plus the boundary checks give the exact corridor intersection.
assert DLO < RSTAR <= DHI

deletions={
    26_058_127_773,28_746_802_249,36_398_517_184,39_087_191_660,41_775_866_136,
    23_783_761_791,28_746_802_250,31_435_476_726,34_124_151_202,36_812_825_678,
    23_369_453_298,26_058_127_774,36_398_517_185,39_087_191_661,
}
assert len(deletions)==14
retained=sorted(x for x in deletions if RSTAR<=x<=DHI)
assert len(retained)==12
assert sorted(x for x in deletions if x<RSTAR)==[23_369_453_298,23_783_761_791]
interval_count=DHI-RSTAR+1
remaining=interval_count-len(retained)
old_remaining=DHI-DLO+1-14
newly_removed=old_remaining-remaining
assert interval_count==16_192_674_031
assert remaining==16_192_674_019
assert old_remaining==18_406_412_825
assert newly_removed==2_213_738_806

def shifted(lo,hi,k):
    a=(lo-k*B)%L
    b=(hi-k*B)%L
    assert a<=b
    return a,b

assert shifted(RSTAR,DHI,34)==(40_886_621_976,57_079_296_006)
assert shifted(RSTAR,DHI,36)==(17_517_168_678,33_709_842_708)
assert shifted(RSTAR,DHI,37)==(74_596_464_685,90_789_138_715)
assert shifted(RSTAR,DHI,36)[1] < R
assert shifted(RSTAR,DHI,37)[0] >= R

# Reverse-prehistory theorem: for every unit residue y mod 9, exactly two exponent
# classes mod 6 give both integer and unit predecessors.
safe={}
for y in (1,2,4,5,7,8):
    vals=[]
    for a in range(1,7):
        z=(pow(2,a,9)*y)%9
        if z%3==1 and z!=1:
            vals.append(a%6)
    assert len(vals)==2
    safe[y]=tuple(vals)

def v2(n):
    return (n & -n).bit_length()-1

reps={0:18,8:8,9:9,17:17}
expected_nu={0:1,8:2,9:4,17:3}

def tau35_pair(eta):
    ylo=(2**34)*eta-1
    yhi=(2**34)*(eta+21)-1
    if eta%9==0:
        zlo=(2*ylo-1)//3
        zhi=(2*yhi-1)//3
        h=0
    else:
        assert eta%9==8
        zlo=(4*ylo-1)//3
        zhi=(4*yhi-1)//3
        h=1
    assert zlo>0 and zhi>0 and zlo%2==zhi%2==1
    assert zlo%3 and zhi%3
    return [zlo,zhi],[h,h]

def reverse_one(y,h,c):
    # Choose the first safe exponent >= c-h, then lift by period six if necessary.
    choices=safe[y%9]
    a=min(x if x else 6 for x in choices)
    while a < max(1,c-h):
        a += 6
    x=(2**a*y-1)//3
    assert 3*x==2**a*y-1
    assert x>0 and x%2==1 and x%3
    hp=h+a-c
    assert hp>=0
    return x,hp

word=[1,2,1,2,2,1,1,2,1,2,1,2]
for cls,eta in reps.items():
    assert eta%18==cls
    if eta%2==0:
        nu=v2((3**34)*(eta+21)-1)
    else:
        nu=v2((3**34)*eta-1)
    assert nu==expected_nu[cls] and 1<=nu<=21
    ys,hs=tau35_pair(eta)
    for j in range(2):
        y,h=ys[j],hs[j]
        for c in word:
            y,h=reverse_one(y,h,c)

print("PASS RL200 exact H21 K-rank/prehistory certificate")
print("h21_K_rank_core=[25583192106,41775866136]")
print("h21_K_core_interval_ranks=16192674031")
print("h21_retained_inherited_deletions=12")
print("h21_remaining_certificate_ranks=16192674019")
print("newly_removed_previously_surviving_ranks=2213738806")
print("tau34_rank_interval=[40886621976,57079296006]")
print("pre_tau35_first_two_mechanical_bits=1,2")
print("terminal_K_eta_blind=yes")
print("finite_uncoupled_unit_prehistory_class_blind=yes")
print("representative_eta=0:18,8:8,9:9,17:17")
print("terminal_state_classes_remain=0,8,9,17")
print("class_selector=not_achieved")
