#!/usr/bin/env python3
from math import ceil
from collections import Counter

A=1100
Q=317
K=31
TERMINAL_J=2**K

def step_x(d,J,x):
    """Exact RL45/RL64 u-driven internal transition. Returns (d',J',y) or None."""
    if J & 1:
        y=x
        if x==0:
            return d,(J+3**d-2**d)//2,y
        return d,(3*J+2**d-1)//2,y
    y=1-x
    if x==0:
        return d+1,(3*J+3**(d+1)-2**d-1)//2,y
    if d<=1:
        return None
    return d-1,J//2,y

def inv_step_x(d2,J2,x):
    """All exact predecessors for one fixed x-bit."""
    cands=[]

    # same-bit predecessor
    d=d2
    if x==0:
        J=2*J2-3**d+2**d
        if J&1:
            out=step_x(d,J,x)
            if out and out[:2]==(d2,J2):
                cands.append((d,J,out[2]))
    else:
        num=2*J2-2**d+1
        if num%3==0:
            J=num//3
            if J&1:
                out=step_x(d,J,x)
                if out and out[:2]==(d2,J2):
                    cands.append((d,J,out[2]))

    # skew predecessor
    if x==0:
        d=d2-1
        if d>=1:
            num=2*J2-3**(d+1)+2**d+1
            if num%3==0:
                J=num//3
                if J%2==0:
                    out=step_x(d,J,x)
                    if out and out[:2]==(d2,J2):
                        cands.append((d,J,out[2]))
    else:
        d=d2+1
        J=2*J2
        out=step_x(d,J,x)
        if out and out[:2]==(d2,J2):
            cands.append((d,J,out[2]))
    return cands

def inverse_suffix(bits):
    # entries (d,J,H_suffix,ybits) at the boundary before bits
    curr=[(1,TERMINAL_J,0,"")]
    for ch in reversed(bits):
        x=int(ch)
        nxt=[]
        for d2,J2,Hacc,ybits in curr:
            for d,J,y in inv_step_x(d2,J2,x):
                nxt.append((d,J,Hacc+d-1,str(y)+ybits))
        curr=nxt
    return curr

# RL257 exact right prefix family, now carrying canonical area.
right_weights=list(range(9,0,-1))
prefixes=[(1,-13,"",0,0)] # d,J,rbits,E_right,H_prefix
for w in right_weights:
    nxt=[]
    for d,J,bits,cost,H in prefixes:
        for x in (0,1):
            out=step_x(d,J,x)
            if out is None:
                continue
            d2,J2,_=out
            nxt.append((d2,J2,bits+str(x),cost+(0 if x else w),H+d-1))
    prefixes=nxt
assert len(prefixes)==199
assert min(p[3] for p in prefixes)==11
assert sorted(p[2] for p in prefixes if p[3]==11)==["110110111","110111010"]

# All ten-bit suffixes and exact inverse terminal chains.
left_weights=list(range(1,11))
suffixes=[]
admissible_suffix_chains=0
admissible_suffix_words=0
for mask in range(1<<10):
    bits="".join("1" if ((mask>>(9-i))&1) else "0" for i in range(10))
    cost=sum(w for i,w in enumerate(left_weights) if bits[i]=="0")
    chains=inverse_suffix(bits)
    suffixes.append((bits,cost,chains))
    if cost<=16:
        admissible_suffix_words+=1
        admissible_suffix_chains+=len(chains)
assert admissible_suffix_words==141
assert admissible_suffix_chains==2706

# RL256/RL257 exact complement-capacity test.
blocks=[(129,161),(278,310),(446,478),(595,627),
        (763,795),(912,944),(1061,1093)]
gaps=[]
for idx,(lo,hi) in enumerate(blocks):
    next_lo=blocks[(idx+1)%len(blocks)][0]
    start=(hi+1)%A
    end=(next_lo-1)%A
    if idx<len(blocks)-1:
        pts=list(range(start,end+1))
    else:
        pts=list(range(start,A))+list(range(0,end+1))
    gaps.append(pts)
assert [len(g) for g in gaps]==[116,135,116,135,116,116,135]

def excluded_roots(zero_positions):
    ex=set()
    for p in zero_positions:
        p%=A
        ex.add(p)
        ex.add((p-Q+1)%A)
    return ex

def capacity(excluded):
    total=0
    for pts in gaps:
        coords=([p if p>=pts[0] else p+A for p in pts]
                if pts[0]>pts[-1] else pts)
        last=-10**18
        for c,p in zip(coords,pts):
            if p in excluded:
                continue
            if c-last>=3:
                total+=1
                last=c
    return total

tail_ex=excluded_roots([p%A for p in range(-28,0)])
assert capacity(tail_ex)==287

pairs=[]
budget_pairs=0
for pref in prefixes:
    d,J,rbits,rcost,Hpref=pref
    rex=excluded_roots([3+i for i,ch in enumerate(rbits) if ch=="0"])
    for lbits,lcost,chains in suffixes:
        E=rcost+lcost
        if E>27:
            continue
        budget_pairs+=1
        lex=excluded_roots([(-39+i)%A for i,ch in enumerate(lbits) if ch=="0"])
        if 260+E<=capacity(tail_ex|rex|lex):
            pairs.append((pref,lbits,lcost,chains))
assert budget_pairs==3064
assert len(pairs)==2719

# Expand exact terminal inverse ownership.
owned_chain_realizations=sum(len(chains) for _,_,_,chains in pairs)
assert owned_chain_realizations==53335

# Gate-A-dangerous k=31 means total H_can <=30.
# Middle length = 1068 - 9 - 10 = 1049.
# For a positive height path from s to e, exact unavoidable area is
# s(s-1)/2 + (e-1)(e-2)/2.
low=[]
distinct_flank_pairs=set()
for pref,lbits,lcost,chains in pairs:
    sd,sJ,rbits,rcost,Hpref=pref
    for ed,eJ,Hsuf,ybits in chains:
        bridge=sd*(sd-1)//2+(ed-1)*(ed-2)//2
        lower=Hpref+Hsuf+bridge
        if lower<=30:
            middle_budget=30-Hpref-Hsuf
            low.append((pref,lbits,lcost,ed,eJ,Hsuf,ybits,middle_budget,bridge,lower))
            distinct_flank_pairs.add((rbits,lbits))

assert len(low)==667
assert len(distinct_flank_pairs)==348
assert min(x[9] for x in low)==21
assert max(x[9] for x in low)==30

# Distinct exact low-area middle automata.
cases=sorted(set((x[7],x[0][0],x[0][1]) for x in low))
assert len(cases)==71
assert min(b for b,_,_ in cases)==1
assert max(b for b,_,_ in cases)==10

def run_low_area_automaton(budget,d0,J0):
    # states carry exact middle area spent so far.
    states={(d0,J0,0)}
    seen={}
    depth=0
    maxJ=J0
    while True:
        key=tuple(sorted(states))
        if key in seen:
            return ("repeat",seen[key],depth,depth-seen[key],maxJ,len(states))
        if not states:
            return ("empty",None,depth,None,maxJ,0)
        seen[key]=depth
        nxt=set()
        for d,J,h in states:
            maxJ=max(maxJ,J)
            for x in (0,1):
                out=step_x(d,J,x)
                if out is None:
                    continue
                d2,J2,_=out
                h2=h+d-1
                if h2<=budget:
                    nxt.add((d2,J2,h2))
                    maxJ=max(maxJ,J2)
        states=nxt
        depth+=1

results=[run_low_area_automaton(*case) for case in cases]
status=Counter(r[0] for r in results)
assert status==Counter({"repeat":55,"empty":16})
assert max(r[2] for r in results)==154
assert sorted(set(r[3] for r in results if r[0]=="repeat"))==[1,2,3,11,33]
assert max(r[4] for r in results)==212

min_required_J=min(x[4] for x in low)
max_required_J=max(x[4] for x in low)
assert min_required_J==9049478310
assert max_required_J==81445305262
assert max(r[4] for r in results)<min_required_J

# Therefore no low-area automaton can ever hit any required terminal-side
# predecessor: it dies or cycles after its finite preperiod, and throughout
# the complete preperiod+cycle all J are <=212.
print("RL258 low-area canonical middle verifier: PASS")
print("k31_capacity_flank_pairs=",len(pairs))
print("terminal_inverse_chains_for_141_suffixes=",admissible_suffix_chains)
print("owned_chain_realizations=",owned_chain_realizations)
print("gateA_low_area_realizations=",len(low))
print("gateA_low_area_distinct_flank_pairs=",len(distinct_flank_pairs))
print("distinct_low_area_middle_automata=",len(cases))
print("empty_automata=",status["empty"])
print("repeating_automata=",status["repeat"])
print("latest_empty_or_repeat_depth=",max(r[2] for r in results))
print("repeat_periods=",sorted(set(r[3] for r in results if r[0]=="repeat")))
print("max_reachable_J=",max(r[4] for r in results))
print("min_required_terminal_predecessor_J=",min_required_J)
print("middle_length=1049")
print("conclusion=k31_first_halving_frontier_is_GateA_safe")
print("classification=TARGETED_GATE_A_CERTIFICATE")
