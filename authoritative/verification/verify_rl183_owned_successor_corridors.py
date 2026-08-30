#!/usr/bin/env python3
from fractions import Fraction

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
assert A*p-L*u==1

GAP_UPPER=293_591_818_782
EDGE1=10_075_174_578
SHALLOW={
    1:73_801_609_945,
    2:81_605_820_006,
    3:84_804_722_294,
    4:86_264_134_824,
}

# RL183.1: ordinary and carry-free successor corridor floors.
ordinary_h1=EDGE1-1
corridor25=ordinary_h1-24
corridor4=ordinary_h1-3
assert ordinary_h1==10_075_174_577
assert corridor25==10_075_174_553
assert corridor4==10_075_174_574

# Exact ternary ownership depths for endpoint-height cutoffs 1..25.
depth={}
for k in range(1,26):
    n=1
    while not (2**k*GAP_UPPER < 3**n):
        n+=1
    depth[k]=n
expected=[
    25,26,26,27,28,28,29,30,30,31,31,32,33,
    33,34,35,35,36,37,37,38,38,39,40,40,
]
assert [depth[k] for k in range(1,26)]==expected

# RL183.3: exact mechanical-rank split.
R=2*L-A
LATE=A-L
assert R==57_079_296_007
assert LATE==80_448_749_305
assert R+LATE==L

# Local necessary height/mechanical template enumeration.
# State records endpoint heights plus exact affine map C_current = a*C_0+b.
states=[(a,b,Fraction(1),Fraction(0),()) for a in (0,1) for b in (0,1)]
counts=[]
sequence_counts=[]
map_counts=[]
for step in range(1,4):
    nxt=[]
    for a,b,coef,const,seq in states:
        for c in (1,2):
            M=max(a,b)
            # h' = h+c-k with k>=1, so 0 <= h' <= h+c-1.
            for ap in range(a+c):
                for bp in range(b+c):
                    Mp=max(ap,bp)
                    d=c+M-Mp
                    assert d>=1
                    D=2**(M-b)-2**(M-a)
                    factor=Fraction(1,2**d)
                    newcoef=3*factor*coef
                    newconst=factor*(3*const+D)
                    nxt.append((ap,bp,newcoef,newconst,seq+((d,D),)))
    states=nxt
    counts.append(len(states))
    sequence_counts.append(len({z[4] for z in states}))
    map_counts.append(len({(z[2],z[3]) for z in states}))

assert counts==[34,342,3884]
assert sequence_counts==[9,69,606]
assert map_counts==[9,60,357]

# For three transitions remove at most three future carry crossings and at most
# three ordinary common-c switch hits, in addition to the current carry removal.
clean3=ordinary_h1-3-3
assert clean3==10_075_174_571

def ceil_div(a,b):
    return (a+b-1)//b

repeat_template=ceil_div(clean3,counts[-1])
repeat_map=ceil_div(clean3,map_counts[-1])
assert repeat_template==2_594_021
assert repeat_map==28_221_778

# RL183.4: phase-compartment population arithmetic.
location={}
for k,N in SHALLOW.items():
    forced_early=max(0,N-LATE)
    forced_late=max(0,N-R)
    overlap=ceil_div(2**k,3)
    strict_late=max(0,forced_late-overlap)
    location[k]=(forced_early,forced_late,overlap,strict_late)

assert location=={
    1:(0,16_722_313_938,1,16_722_313_937),
    2:(1_157_070_701,24_526_523_999,2,24_526_523_997),
    3:(4_355_972_989,27_725_426_287,3,27_725_426_284),
    4:(5_815_385_519,29_184_838_817,6,29_184_838_811),
}

print("PASS: RL183 owned successor corridor and phase-location certificate")
print("ordinary_h_le_1_starts_ge=",ordinary_h1)
print("ordinary_25_edge_corridors_ge=",corridor25)
print("ownership_depth_max_through_h_le_25=",max(depth.values()))
print("mechanical_c1_ranks=",R)
print("mechanical_c2_ranks=",LATE)
print("clean_three_transition_corridors_ge=",clean3)
print("necessary_three_transition_templates=",counts[-1])
print("distinct_three_transition_affine_maps=",map_counts[-1])
print("repeated_template_floor=",repeat_template)
print("repeated_affine_map_floor=",repeat_map)
for k in sorted(location):
    a,b,o,s=location[k]
    print(f"h_le_{k}_forced_c1={a}")
    print(f"h_le_{k}_forced_c2={b}")
    print(f"h_le_{k}_overlap_cap={o}")
    print(f"h_le_{k}_forced_c2_at_or_above_4m_over_3={s}")
