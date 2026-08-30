#!/usr/bin/env python3
from fractions import Fraction

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
t=L-p
assert A*p-L*u==1

def B(j): return (A*j)//L
def c(j): return B(j+1)-B(j)
def v2(n):
    n=abs(n); assert n
    return (n & -n).bit_length()-1

# Rigorous rational logarithm bounds via atanh series.
def ln_bounds(x, N=100):
    z=Fraction(x-1,x+1)
    s=sum((z**(2*n+1))/Fraction(2*n+1) for n in range(N))
    lo=2*s
    tail=2*z**(2*N+1)/Fraction(2*N+1)/(1-z*z)
    return lo, lo+tail

l2,u2=ln_bounds(2)
l3,u3=ln_bounds(3)
delta_lo=A*l2-L*u3
delta_hi=A*u2-L*l3
assert 0 < delta_lo < delta_hi
# lambda=e^Delta and e^Delta-1>Delta. Hence in v=37 high branch
# F2=3*2^37*(lambda-1)>3*2^37*delta_lo>1/3.
assert 3*(2**37)*delta_lo > Fraction(1,3)

# Exact RL178 necessary transition law.
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

# Start at exact surviving high d=-1 phase-24 state.
paths=[((0,1,3**24), Fraction(0), [])]
counts={24:1}
for i in range(24,29):
    nxt=[]
    for st,s,hist in paths:
        s2=s+flow_term(i,st)
        for ns,ab in step(i,st):
            nxt.append((ns,s2,hist+[(i,ab)]))
    paths=nxt
    counts[i+1]=len({st for st,_,_ in paths})
assert counts=={24:1,25:1,26:2,27:2,28:5,29:10}
assert len(paths)==10

rows=[]
for st,neg,hist in paths:
    f29=flow_term(29,st)
    total=neg+f29
    rows.append((st,neg,f29,total,hist))

best=max(r[3] for r in rows)
worst=min(r[3] for r in rows)
assert best==Fraction(-6_734_508_720_128,7_625_597_484_987)
assert best < Fraction(-7,8)
assert worst==Fraction(-55_387_898_249_216,22_876_792_454_961)

# Since F2>1/3, every path needs later net flow > 1/3-total.
# RL178 residue ordering gives every positive corrected-flow term < rho_i < 1.
# Therefore if that lower requirement >1, at least two later positive terms
# are mandatory; if >2, at least three are mandatory.
assert all(Fraction(1,3)-r[3] > 1 for r in rows)
three_states={
    (0,3,2_144_699_292_645),
    (0,3,2_144_699_292_643),
    (0,1,536_174_823_161),
    (0,2,1_072_349_646_321),
}
three=[r for r in rows if Fraction(1,3)-r[3] > 2]
assert {r[0] for r in three}==three_states
assert len(three)==4

# Exact phase-29 positive pair-state interfaces, and phase-30 transition law.
pos29=sorted(st for st,_,_,_,_ in rows if st[0]>st[1])
assert pos29==[
    (1,0,536_174_823_161),
    (2,0,1_072_349_646_323),
    (2,1,1_072_349_646_323),
]
expected30={
    (1,0,536_174_823_161): {
        (1,0,402_131_117_371),
        (0,1,402_131_117_371),
    },
    (2,0,1_072_349_646_323): {
        (2,1,804_262_234_743),
        (2,0,804_262_234_743),
    },
    (2,1,1_072_349_646_323): {
        (3,2,1_608_524_469_485),
        (3,1,1_608_524_469_485),
        (3,0,1_608_524_469_485),
    },
}
for st in pos29:
    got={ns for ns,_ in step(29,st)}
    assert got==expected30[st]
    assert not any(h==hp for h,hp,_ in got)
# Only first interface admits immediate sign reversal; the other two remain positive.
assert any(h<hp for h,hp,_ in expected30[pos29[0]])
assert all(h>hp for root in pos29[1:] for h,hp,_ in expected30[root])

# RL177 exact zero-height mismatch indices and valuation formula.
zero_js=[1,3,5,6,8,10,11,13,15,17,18,20,22,23]
ck1=[J for J in zero_js if c(J+1)==1]
assert ck1==[1,3,6,8,11,13,15,18,20,23]

# General c_k=1 second-transition theorem by exact local valuation cases.
# d=+1: h,hp=(1,0), alpha in {1,2}, beta=1.
# d=-1: h,hp=(0,1), alpha=1, beta in {1,2}.
def plus_options(vv):
    out=[]
    for a in (1,2):
        b=1; gp=1+b-a; x=a; y=1+b
        ok=(vv==min(x,y)) if x!=y else (vv>x)
        if ok: out.append((a,b,gp))
    return out

def minus_options(vv):
    out=[]
    a=1
    for b in (1,2):
        gp=-1+b-a; x=b; y=1+a
        ok=(vv==min(x,y)) if x!=y else (vv>x)
        if ok: out.append((a,b,gp))
    return out

assert plus_options(1)==[(1,1,1)]
assert plus_options(2)==[]
assert plus_options(3)==[(2,1,0)]
assert minus_options(1)==[(1,1,-1)]
assert minus_options(2)==[]
assert minus_options(3)==[(1,2,0)]
for vv in range(3,12):
    assert plus_options(vv)==[(2,1,0)]
    assert minus_options(vv)==[(1,2,0)]

# Mod-8 classes producing the forbidden valuation exactly 2.
for J in ck1:
    n=J+2
    plus_bad=1 if n%2 else 3
    minus_bad=7 if n%2 else 5
    for r in (1,3,5,7):
        vp=v2((3**n)*r+1)
        vm=v2((3**n)*r-1)
        assert (vp==2)==(r==plus_bad)
        assert (vm==2)==(r==minus_bad)

# High J=23,w=1 specialization recovers + exclusion and - forced continuation.
assert v2(3**25+1)==2
assert v2(3**25-1)==1

print('PASS: RL179 exact high-budget and odd-part sieve certificate.')
print('F2 > 1/3 certified by rational log bounds')
print('10 phase-29 path histories; all require >=2 later positive terms')
print('4 phase-29 histories require >=3 later positive terms')
print('phase-30 zero return excluded from all 3 positive phase-29 interfaces')
print('c_k=1 mod-8 sieve applies at J =', ck1)
