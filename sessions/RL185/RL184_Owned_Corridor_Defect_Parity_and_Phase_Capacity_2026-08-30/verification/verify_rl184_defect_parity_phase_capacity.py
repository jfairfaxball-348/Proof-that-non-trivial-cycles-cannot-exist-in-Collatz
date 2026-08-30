#!/usr/bin/env python3
from fractions import Fraction

A=217_976_794_617
L=137_528_045_312
B=A-L
R=2*L-A
assert B==80_448_749_305
assert R==57_079_296_007
assert R==L-B

GAP_LOWER=128_081_997_553
GAP_UPPER=293_591_818_782
ORDINARY_H1=10_075_174_577
CLEAN3=10_075_174_571
SHALLOW={
    1:73_801_609_945,
    2:81_605_820_006,
    3:84_804_722_294,
    4:86_264_134_824,
}

def ceil_div(a,b):
    return (a+b-1)//b

assert GAP_LOWER*3 > 1
late_refined={}
for k,N in SHALLOW.items():
    forced_late=max(0,N-R)
    late_refined[k]=max(0,forced_late-1)
assert late_refined=={
    1:16_722_313_937,
    2:24_526_523_998,
    3:27_725_426_286,
    4:29_184_838_816,
}

def c_of(r):
    return 1 if r<R else 2

breaks={0,L}
for j in range(3):
    breaks.add((R-j*B)%L)
bs=sorted(breaks)
samples=set()
for x in bs:
    if x<L:
        samples.add(x)
for lo,hi in zip(bs,bs[1:]):
    if lo+1 < hi:
        samples.add(lo+1)
words=set()
for r in samples:
    rr=r
    w=[]
    for _ in range(3):
        w.append(c_of(rr))
        rr=(rr+B)%L
    words.add(tuple(w))
expected_words={(1,2,1),(1,2,2),(2,1,2),(2,2,1)}
assert words==expected_words

initial=[(a,b,Fraction(1),Fraction(0),()) for a in (0,1) for b in (0,1)]
templates=[]
maps=set()
zero_templates=0
zero_maps=set()
bad_zero=[]
for word in sorted(words):
    states=initial
    for c in word:
        nxt=[]
        for a,b,coef,const,seq in states:
            M=max(a,b)
            D=2**(M-b)-2**(M-a)
            for ap in range(a+c):
                for bp in range(b+c):
                    Mp=max(ap,bp)
                    d=c+M-Mp
                    assert d>=1
                    f=Fraction(1,2**d)
                    nxt.append((ap,bp,3*f*coef,f*(3*const+D),seq+((d,D),)))
        states=nxt
    for state in states:
        templates.append((word,state))
        maps.add((state[2],state[3]))
        if state[3]==0:
            zero_templates+=1
            zero_maps.add((state[2],state[3]))
            if any(D!=0 for d,D in state[4]):
                bad_zero.append((word,state))

assert len(templates)==1_818
assert len(maps)==270
assert zero_templates==210
assert len(zero_maps)==4
assert not bad_zero

repeat_template=ceil_div(CLEAN3,len(templates))
repeat_map=ceil_div(CLEAN3,len(maps))
assert repeat_template==5_541_901
assert repeat_map==37_315_462

C_MAX=2*GAP_UPPER
assert C_MAX==587_183_637_564
assert 2**39 < C_MAX < 2**40

lo=(39*B)//L
hi=ceil_div(39*B,L)
assert (lo,hi)==(22,23)

terminal=3**39
assert terminal > GAP_UPPER*(2**23)
assert terminal < GAP_UPPER*(2**24)
assert terminal > GAP_LOWER*(2**24)
assert terminal % 2 == 1

clean40=ORDINARY_H1-39-39
assert clean40==10_075_174_499
distinct_nonzero=ceil_div(clean40,40)
assert distinct_nonzero==251_879_363

print("PASS: RL184 defect parity and phase-capacity certificate")
print("mechanical_words=", ",".join("".join(map(str,w)) for w in sorted(words)))
print("restricted_three_transition_templates=",len(templates))
print("restricted_affine_maps=",len(maps))
print("repeated_template_floor=",repeat_template)
print("repeated_affine_map_floor=",repeat_map)
print("zero_intercept_templates=",zero_templates)
print("zero_intercept_maps=",len(zero_maps))
for k in sorted(late_refined):
    print(f"h_le_{k}_late_at_or_above_4m_over_3_ge={late_refined[k]}")
print("clean_40_edge_corridors_ge=",clean40)
print("distinct_nonzero_defect_phases_ge=",distinct_nonzero)
