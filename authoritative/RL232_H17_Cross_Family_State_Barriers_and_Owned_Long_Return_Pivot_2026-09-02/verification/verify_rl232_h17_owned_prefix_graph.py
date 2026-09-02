#!/usr/bin/env python3
from fractions import Fraction

A=217_976_794_617
L=137_528_045_312
B=A-L
R=L-B

# New RL232 K-compatible necessary H17 cores from the prior checkpoint.
A_CORE=(11_443_822_977,28_746_802_249)
B_CORE=(72_981_981_437,100_039_806_527)

# Exact H17 terminal owned numerators and terminal maximum height.
CA=20_383_222_077_370_251   # 11*3^32
CB=27_795_302_832_777_615   # 5*3^33
H=17

def v2(n):
    n=abs(n)
    assert n
    return (n & -n).bit_length()-1

def cbit(r):
    return 1 if r<R else 2

def shifted_intervals(core,j):
    lo,hi=core
    s=(j*B)%L
    a,b=lo+s,hi+s
    if b<L:
        return [(a,b)]
    if a>=L:
        return [(a-L,b-L)]
    return [(0,b-L),(a,L-1)]

def common_bit(core,j):
    bits=set()
    for lo,hi in shifted_intervals(core,j):
        bits.add(cbit(lo))
        bits.add(cbit(hi))
        # A threshold can only matter if it lies inside this ordinary interval.
        if lo < R <= hi:
            bits.update((1,2))
    assert len(bits)==1
    return next(iter(bits))

# Gap-free common mechanical prefixes on the full new corridor-compatible cores.
A_WORD=tuple(common_bit(A_CORE,j) for j in range(4))
B_WORD=tuple(common_bit(B_CORE,j) for j in range(3))
assert A_WORD==(1,2,1,2)
assert B_WORD==(2,1,2)

def normalized_delta(h,hp,C):
    return Fraction(C,1<<max(h,hp))

def successors(state,c):
    """
    Necessary owned-pair successors from the exact RL194 transition law.
    Returned tuples are (h2,hp2,C2,alpha,beta).
    These are necessary states only; survival is NOT a physical realization.
    """
    h,hp,C=state
    g=h-hp
    out=set()
    for alpha in range(1,h+c+1):
        h2=h+c-alpha
        for beta in range(1,hp+c+1):
            hp2=hp+c-beta

            if g>0:
                N=3*C+(1<<g)-1
                eZ=g+beta
                eX=alpha
            elif g<0:
                N=3*C+1-(1<<(-g))
                eZ=beta
                eX=-g+alpha
            else:
                N=3*C
                eZ=beta
                eX=alpha

            vv=v2(N)
            if eZ!=eX:
                d=min(eZ,eX)
                if vv!=d:
                    continue
            else:
                d=eZ
                if vv<=d:
                    continue

            assert N%(1<<d)==0
            C2=N>>d

            # Independent exact normalized-recurrence check.
            lhs=(1<<c)*normalized_delta(h2,hp2,C2)
            rhs=3*normalized_delta(h,hp,C)+Fraction(1,1<<hp)-Fraction(1,1<<h)
            assert lhs==rhs

            out.add((h2,hp2,C2,alpha,beta))
    return out

def initial_states(C):
    # Complete ordered unequal height-pair domain with max height 17.
    return [(17,j,C) for j in range(17)] + [(j,17,C) for j in range(17)]

assert len(initial_states(CA))==len(initial_states(CB))==34

def step(states,c):
    nxt=set()
    edges=0
    for state in states:
        ss=successors(state,c)
        edges+=len(ss)
        for h,hp,C,a,b in ss:
            nxt.add((h,hp,C))
    return nxt,edges

def depth3_certificate(C,word):
    states=set(initial_states(C))
    state_counts=[]
    edge_counts=[]
    for c in word[:3]:
        states,edges=step(states,c)
        state_counts.append(len(states))
        edge_counts.append(edges)

    # Keep initial identities separate to test that every terminal pair survives.
    survivors=[]
    for init in initial_states(C):
        st={init}
        for c in word[:3]:
            st,_=step(st,c)
        survivors.append(len(st))
    return tuple(state_counts),tuple(edge_counts),tuple(survivors)

a_states,a_edges,a_surv=depth3_certificate(CA,A_WORD)
b_states,b_edges,b_surv=depth3_certificate(CB,B_WORD)

assert a_states==(329,2301,10451)
assert a_edges==(329,2555,12436)
assert b_states==(370,2349,12471)
assert b_edges==(370,2595,14904)
assert all(n>0 for n in a_surv)
assert all(n>0 for n in b_surv)

def first_zero_interfaces(C,c):
    rows=[]
    for init in initial_states(C):
        for h,hp,C2,alpha,beta in successors(init,c):
            if h==hp:
                rows.append((init,alpha,beta,h,C2,v2(C2)))
    return rows

a_zero=first_zero_interfaces(CA,A_WORD[0])
b_zero=first_zero_interfaces(CB,B_WORD[0])

# H17-A: immediate zero is possible only from g=-1, initial (16,17).
assert len(a_zero)==3
assert {row[0][:2] for row in a_zero}=={(16,17)}
assert {(row[1],row[2]) for row in a_zero}=={(1,2),(2,3),(3,4)}
assert sorted((row[1],row[2],row[3],row[4],row[5]) for row in a_zero)==[
    (1,2,16,15_287_416_558_027_688,3),
    (2,3,15,7_643_708_279_013_844,2),
    (3,4,14,3_821_854_139_506_922,1),
]

# H17-B: immediate zero is possible only from g=+2, initial (17,15).
assert b_zero==[
    ((17,15,CB),3,1,16,10_423_238_562_291_606,1)
]

def all_zero_path_counts(C,word):
    # Count necessary paths for which EVERY successor defect seen so far is zero.
    current=[(s,[]) for s in initial_states(C)]
    counts=[]
    histories=[]
    for c in word:
        nxt=[]
        for state,hist in current:
            for h,hp,C2,alpha,beta in successors(state,c):
                if h==hp:
                    nxt.append(((h,hp,C2),hist+[(alpha,beta,h,C2,v2(C2))]))
        current=nxt
        counts.append(len(current))
        histories=current
    return tuple(counts),histories

a_zero_counts,a_hist=all_zero_path_counts(CA,A_WORD)
b_zero_counts,b_hist=all_zero_path_counts(CB,B_WORD[:2])

assert a_zero_counts==(3,3,1,0)
assert b_zero_counts==(1,0)

# The unique H17-A three-zero necessary path, before the fourth zero becomes impossible.
a3_counts,a3_hist=all_zero_path_counts(CA,A_WORD[:3])
assert a3_counts==(3,3,1)
assert len(a3_hist)==1
state,hist=a3_hist[0]
assert hist==[
    (1,2,16,15_287_416_558_027_688,3),
    (1,1,17,22_931_124_837_041_532,2),
    (1,1,17,34_396_687_255_562_298,1),
]

print("PASS: RL232 H17 owned-prefix graph checkpoint")
print(f"H17_A_common_mechanical_prefix={''.join(map(str,A_WORD))}")
print(f"H17_B_common_mechanical_prefix={''.join(map(str,B_WORD))}")
print(f"H17_A_depth3_state_counts={a_states}")
print(f"H17_A_depth3_edge_counts={a_edges}")
print(f"H17_B_depth3_state_counts={b_states}")
print(f"H17_B_depth3_edge_counts={b_edges}")
print("H17_A_all_34_terminal_height_pairs_survive_depth3=yes")
print("H17_B_all_34_terminal_height_pairs_survive_depth3=yes")
print("H17_A_immediate_zero_requires_terminal_g=-1")
print("H17_A_four_consecutive_postterminal_zeros_impossible=yes")
print("H17_B_immediate_zero_requires_terminal_g=+2")
print("H17_B_two_consecutive_postterminal_zeros_impossible=yes")
print("combined_H17_incidence_cap_1615_proved=no")
print("classification=EXACT_LOCAL_THEOREM_PLUS_METHOD_BARRIER")
