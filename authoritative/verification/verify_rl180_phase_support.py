#!/usr/bin/env python3
from fractions import Fraction
A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u0=103_768_467_013
assert A*p-L*u0==1

def B(j): return (A*j)//L
def c(j): return B(j+1)-B(j)
def v2(n):
    n=abs(n); assert n
    return (n & -n).bit_length()-1

def step(i,state):
    h,hp,C=state
    g=h-hp
    digit=c(i)
    out=[]
    for a in range(1,h+digit+1):
        for b in range(1,hp+digit+1):
            gp2=g+b-a
            if g>0:
                N=3*C+(1<<g)-1
                wv=v2(N); vg_b=g+b
                if a<vg_b:
                    if gp2<=0 or wv!=a: continue
                    C2=N>>a
                elif a>vg_b:
                    if gp2>=0 or wv!=vg_b: continue
                    C2=N>>vg_b
                else:
                    if gp2!=0 or wv<=a: continue
                    C2=N>>a
            elif g<0:
                e=-g
                N=3*C+1-(1<<e)
                wv=v2(N); ve_a=e+a
                if b<ve_a:
                    if gp2>=0 or wv!=b: continue
                    C2=N>>b
                elif b>ve_a:
                    if gp2<=0 or wv!=ve_a: continue
                    C2=N>>ve_a
                else:
                    if gp2!=0 or wv<=b: continue
                    C2=N>>b
            else:
                N=3*C
                wv=v2(N)
                if b<a:
                    if gp2>=0 or wv!=b: continue
                    C2=N>>b
                elif b>a:
                    if gp2<=0 or wv!=a: continue
                    C2=N>>a
                else:
                    if gp2!=0 or wv<=a: continue
                    C2=N>>a
            h2=h+digit-a; hp2=hp+digit-b
            assert h2>=0 and hp2>=0 and h2-hp2==gp2
            if gp2: assert C2&1
            else: assert C2%2==0
            out.append(((h2,hp2,C2),(a,b)))
    return out

def flow_term(i,state):
    h,hp,_=state
    return Fraction(2**(B(i)-hp)-2**(B(i)-h),3**i)

# Reconstruct the ten RL179 phase-29 histories from the exact high start.
paths=[((0,1,3**24), Fraction(0), [])]
for i in range(24,29):
    nxt=[]
    for st,total,hist in paths:
        total2=total+flow_term(i,st)
        for ns,ab in step(i,st):
            nxt.append((ns,total2,hist+[(i,ab)]))
    paths=nxt
assert len(paths)==10 and len({st for st,_,_ in paths})==10
roots={st for st,_,_ in paths}

# Propagate necessary states through phase 31 and include flow terms 29,30,31.
cur=[(st,st,total,hist) for st,total,hist in paths]
for i in range(29,32):
    nxt=[]
    for st,root,total,hist in cur:
        total2=total+flow_term(i,st)
        if i==31:
            nxt.append((st,root,total2,hist))
        else:
            for ns,ab in step(i,st):
                nxt.append((ns,root,total2,hist+[(i,ab)]))
    cur=nxt
best=max(total for _,_,total,_ in cur)
assert best==Fraction(64_458_869_178_368,205_891_132_094_649)
assert best<Fraction(1,3)

best_root={}
for _,root,total,_ in cur:
    best_root[root]=max(best_root.get(root,total),total)
need3={r for r,b in best_root.items() if Fraction(1,3)-b>2}
assert len(need3)==6
assert (0,3,2_144_699_292_643) in need3
assert Fraction(1,3)-best_root[(0,3,2_144_699_292_643)]>3

# Worst-root delayed-support ladder.  Each future positive corrected-flow term
# is <1 by the inherited RL178 residue-weight theorem.  Therefore a remaining
# deficit >k forces at least k+1 positive phases after the cutoff.
worst=(0,3,2_144_699_292_643)
w=[x for x in paths if x[0]==worst]
assert len(w)==1
cur=[w[0]]
checks={33:3,35:2,37:1,39:0}
for i in range(29,40):
    nxt=[]
    for st,total,hist in cur:
        total2=total+flow_term(i,st)
        for ns,ab in step(i,st):
            nxt.append((ns,total2,hist+[(i,ab)]))
    cur=nxt
    if i in checks:
        b=max(total for _,total,_ in cur)
        assert Fraction(1,3)-b>checks[i]

print('PASS: RL180 exact phase-support certificate')
print('phase31_global_max=',best)
print('all_high_histories_need_positive_phase_at_or_after_32=PASS')
print('phase29_roots_needing_at_least_3_positive_phases_at_or_after_32=',len(need3))
print('worst_root_needs_at_least_4_at_or_after_34=PASS')
print('worst_root_needs_at_least_3_at_or_after_36=PASS')
print('worst_root_needs_at_least_2_at_or_after_38=PASS')
print('worst_root_needs_at_least_1_at_or_after_40=PASS')
