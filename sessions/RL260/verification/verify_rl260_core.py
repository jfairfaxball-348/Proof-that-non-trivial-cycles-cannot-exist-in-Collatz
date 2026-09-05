#!/usr/bin/env python3
from itertools import product
from math import gcd
from pathlib import Path

A=1119; ELL=706; Z=413; Q=802; R=506; HSEL=14; N=10; K=31
BLOCKS=[(129,161),(297,329),(446,478),(614,646),(763,795),(931,963),(1080,1112)]

def step_x(d,J,x):
    if J & 1:
        y=x
        if x==0: return d,(J+3**d-2**d)//2,y
        return d,(3*J+2**d-1)//2,y
    y=1-x
    if x==0: return d+1,(3*J+3**(d+1)-2**d-1)//2,y
    if d<=1: return None
    return d-1,J//2,y

def inv_step_x(d2,J2,x):
    c=[]; d=d2
    if x==0:
        J=2*J2-3**d+2**d
        if J&1:
            o=step_x(d,J,x)
            if o and o[:2]==(d2,J2): c.append((d,J,o[2]))
    else:
        num=2*J2-2**d+1
        if num%3==0:
            J=num//3
            if J&1:
                o=step_x(d,J,x)
                if o and o[:2]==(d2,J2): c.append((d,J,o[2]))
    if x==0:
        d=d2-1
        if d>=1:
            num=2*J2-3**(d+1)+2**d+1
            if num%3==0:
                J=num//3
                if J%2==0:
                    o=step_x(d,J,x)
                    if o and o[:2]==(d2,J2): c.append((d,J,o[2]))
    else:
        d=d2+1; J=2*J2
        o=step_x(d,J,x)
        if o and o[:2]==(d2,J2): c.append((d,J,o[2]))
    return c

def inverse_suffix(bits,k):
    cur=[(1,2**k,0,'')]
    for ch in reversed(bits):
        nxt=[]
        for d2,J2,Hacc,ys in cur:
            for d,J,y in inv_step_x(d2,J2,int(ch)):
                nxt.append((d,J,Hacc+d-1,str(y)+ys))
        cur=nxt
    return cur

def forward_bits(bits):
    d,J,H=1,-13,0; ys=''
    for ch in bits:
        o=step_x(d,J,int(ch)); assert o is not None
        d2,J2,y=o; H+=d-1; d,J=d2,J2; ys+=str(y)
    return d,J,H,ys

def cyclic_runs(S,a):
    starts=[x for x in S if (x-1)%a not in S]; out=[]
    for st in sorted(starts):
        pts=[]; cur=st
        while cur in S:
            pts.append(cur); cur=(cur+1)%a
            if cur==st: break
        out.append(pts)
    return out

U=set()
for lo,hi in BLOCKS: U.update(range(lo,hi+1))
C=set(range(A))-U
GAPS=cyclic_runs(C,A)

def excluded_roots(zs):
    ex=set()
    for p in zs:
        p%=A; ex.add(p); ex.add((p-Q+1)%A)
    return ex

def capacity(ex):
    total=0
    for pts in GAPS:
        coords=([p if p>=pts[0] else p+A for p in pts] if pts[0]>pts[-1] else pts)
        last=-10**18
        for c,p in zip(coords,pts):
            if p in ex: continue
            if c-last>=3: total+=1; last=c
    return total

def resonance(a,ell):
    p2=1<<a; p3=3**ell
    return p2>p3 and 15*p2*p2 < 16*p3*p3

def det_solutions(a,ell):
    g=gcd(a,ell)
    if 2%g: return []
    aa=a//g; ll=ell//g; rhs=(-2)//g
    q0=(rhs*pow(ll,-1,aa))%aa; out=[]
    for j in range(g):
        q=q0+j*aa
        if 0<q<a:
            r=(q*ell+2)//a
            if a*r-q*ell==2: out.append((q,r))
    return out

def min_x_for_mass(b):
    x=1
    while (x*x)//4 < b+2: x+=1
    return x

def capacity_a_min(b): return 3*b+min_x_for_mass(b)-1

def selector_candidates(lo,hi):
    outs=[]
    for a in range(lo,hi+1):
        emin=(147*a+232)//233; emax=(12*a-1)//19
        for ell in range(max(1,emin),min(a-1,emax)+1):
            if not resonance(a,ell): continue
            z=a-ell
            for q,r in det_solutions(a,ell):
                B=q-r; H=19*z-7*a; n=19*B-7*q
                if H<=0: continue
                halving=H%2==0 and n%2==0
                bmin=260 if halving else 356
                if z < bmin+27 or a < capacity_a_min(bmin): continue
                if not halving and a-36*H<1068: continue
                outs.append((a,ell,z,q,r,H,n))
    return outs

def main():
    assert A*R-Q*ELL==2 and 19*Z-7*A==HSEL and 19*(Q-R)-7*Q==N
    assert [len(g) for g in GAPS]==[135,116,135,116,135,116,135]
    assert sum(map(len,GAPS))==888
    tail=excluded_roots(range(-28,0)); assert capacity(tail)==293
    rights=[]
    for t in product('01',repeat=9):
        bits=''.join(t)
        try: d,J,H,ys=forward_bits(bits)
        except AssertionError: continue
        cost=sum(w for w,ch in zip(range(9,0,-1),bits) if ch=='0')
        rights.append((d,J,H,bits,cost,ys))
    assert len(rights)==199
    assert min(x[4] for x in rights)==11
    assert [x[3] for x in rights if x[4]==11]==['110110111','110111010']
    lefts=[]
    for t in product('01',repeat=10):
        bits=''.join(t); cost=sum(w for w,ch in zip(range(1,11),bits) if ch=='0')
        lefts.append((bits,cost,inverse_suffix(bits,31)))
    raw=0; pairs=[]
    for rd,rJ,rH,rbits,rcost,rys in rights:
        rex=excluded_roots([3+i for i,ch in enumerate(rbits) if ch=='0'])
        for lbits,lcost,chains in lefts:
            E=rcost+lcost
            if E<=33:
                raw+=1
                lex=excluded_roots([-39+i for i,ch in enumerate(lbits) if ch=='0'])
                cap=capacity(tail|rex|lex)
                if 260+E<=cap: pairs.append((rd,rJ,rH,rbits,rcost,lbits,lcost,chains))
    assert raw==10183 and len(pairs)==8976
    owned=0; low=[]
    for rd,rJ,rH,rbits,rcost,lbits,lcost,chains in pairs:
        owned+=len(chains)
        for ed,eJ,Hsuf,ybits in chains:
            bridge=rd*(rd-1)//2+(ed-1)*(ed-2)//2
            if rH+Hsuf+bridge<=30:
                low.append((rd,rJ,30-rH-Hsuf,ed,eJ,rbits,lbits))
    assert owned==172633 and len(low)==8571
    assert len(set((x[5],x[6]) for x in low))==2778
    assert len(set((x[0],x[1]) for x in low))==28
    assert len(set((x[2],x[0],x[1]) for x in low))==306
    assert len(set((x[3],x[4]) for x in low))==1064
    assert min(x[4] for x in low)==3016492794 and max(x[4] for x in low)==244335916693
    rows='sd\tsJ\tbudget\ted\teJ\n'+''.join(f'{sd}\t{sJ}\t{b}\t{ed}\t{eJ}\n' for sd,sJ,b,ed,eJ,_,_ in low)
    Path('.rl260_low_cases.tsv').write_text(rows)
    nxt=selector_candidates(1120,1287)
    assert nxt==[(1287,812,475,485,306,16,6)]
    print('PASS RL260 core reconstruction')
    print('k31 flank pairs: 10183 budget-feasible -> 8976 capacity survivors')
    print('owned terminal chains = 172633')
    print('Gate-A-dangerous realizations = 8571; distinct flank pairs = 2778')
    print('canonical starts = 28; start/budget triples = 306; terminal target states = 1064')
    print('required terminal predecessor J range = 3016492794..244335916693')
    print('unique next selector for 1120<=a<=1287 = (1287,812,475,485,306,16,6)')

if __name__=='__main__': main()
