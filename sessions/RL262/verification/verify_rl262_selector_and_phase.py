#!/usr/bin/env python3
from itertools import product
from math import gcd

A=1417; ELL=894; Z=523; Q=317; RSEL=200; HSEL=18; NSEL=4
RHO=ELL-3
M=(1<<A)-3**ELL
BLOCKS=[(129,161),(278,310),(446,478),(595,627),(763,795),(912,944),(1080,1112),(1229,1261),(1378,1410)]

# Inherited selector predicate from promoted RL260 verifier.
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

# Exact canonical transition used by RL260/RL261.
def step_x(d,J,x):
    if J & 1:
        y=x
        if x==0: return d,(J+3**d-2**d)//2,y
        return d,(3*J+2**d-1)//2,y
    y=1-x
    if x==0: return d+1,(3*J+3**(d+1)-2**d-1)//2,y
    if d<=1: return None
    return d-1,J//2,y

def forward_bits(bits):
    d,J,H=1,-13,0; ys=''
    for ch in bits:
        o=step_x(d,J,int(ch))
        if o is None: return None
        d2,J2,y=o; H+=d-1; d,J=d2,J2; ys+=str(y)
    return d,J,H,ys

def prefix_phase(bits):
    d,J=1,-13; rx=ry=0; S=0; ys=''
    for i,ch in enumerate(bits):
        x=int(ch); o=step_x(d,J,x)
        if o is None: return None
        d,J,y=o
        if x:
            rx+=1; S += 3**(RHO-rx)*(1<<i)
        if y:
            ry+=1; S -= 3**(RHO-ry)*(1<<i)
        ys+=str(y)
    return d,J,rx,ry,S,ys

RIGHTS=[]
for t in product('01',repeat=9):
    bits=''.join(t); o=forward_bits(bits)
    if o is None: continue
    d,J,H,ys=o
    cost=sum(w for w,ch in zip(range(9,0,-1),bits) if ch=='0')
    RIGHTS.append((d,J,H,bits,cost,ys))

def quotient_data(k,bits):
    top=237*3**RHO - (1<<(A-k+1))
    nmax=top//M+2
    pp=prefix_phase(bits); assert pp is not None
    S=pp[4]; mod=1<<len(bits); out=[]
    for N in range(1,nmax+1):
        if N%8!=3: continue
        num=top-(N-2)*M
        if num%12: continue
        D=num//12
        if D>=0 and (D-S)%mod==0:
            out.append((N,D))
    return nmax,out

def death_depth(k,bits,N):
    top=237*3**RHO - (1<<(A-k+1))
    num=top-(N-2)*M
    assert num%12==0
    D=num//12; assert D>=0
    m=A-k-1
    d,J,rx,ry,S,ys=prefix_phase(bits)
    p=len(bits); assert (D-S)%(1<<p)==0
    states=[(d,J,rx,ry,S)]
    while p<m:
        np=p+1; rem=m-np; mod=1<<np; nxt=[]
        for d,J,rx,ry,S in states:
            for x in (0,1):
                o=step_x(d,J,x)
                if o is None: continue
                d2,J2,y=o; rx2=rx+x; ry2=ry+y
                if rx2>RHO or ry2>RHO: continue
                if rx2+rem<RHO or ry2+rem<RHO: continue
                S2=S
                if x: S2 += 3**(RHO-rx2)*(1<<p)
                if y: S2 -= 3**(RHO-ry2)*(1<<p)
                if (D-S2)%mod: continue
                nxt.append((d2,J2,rx2,ry2,S2))
        p=np; states=nxt
        if not states: return p
    raise AssertionError('unexpected complete full-phase survivor')

def cyclic_runs(S,a):
    starts=[x for x in S if (x-1)%a not in S]; out=[]
    for st in sorted(starts):
        pts=[]; cur=st
        while cur in S:
            pts.append(cur); cur=(cur+1)%a
            if cur==st: break
        out.append(pts)
    return out

def main():
    # Arithmetic frontier and selector identities.
    nxt=selector_candidates(1288,1417)
    assert nxt==[(1417,894,523,317,200,18,4)]
    assert A*RSEL-Q*ELL==2
    assert 19*Z-7*A==HSEL
    assert 19*(Q-RSEL)-7*Q==NSEL
    assert 9*Q==2*A+19
    assert 9*(Q-RSEL)==2*Z+7

    # Frozen local geometry.
    U=set()
    for lo,hi in BLOCKS:
        assert hi-lo+1==33
        U.update(range(lo,hi+1))
    assert len(U)==9*33
    G=cyclic_runs(set(range(A))-U,A)
    assert [len(g) for g in G]==[116,135,116,135,116,135,116,116,135]
    assert sum(map(len,G))==1120
    assert sum((len(g)+2)//3 for g in G)==375

    # Canonical prefix facts.
    assert len(RIGHTS)==199
    assert min(x[4] for x in RIGHTS)==11
    assert [x[3] for x in RIGHTS if x[4]==11]==['110110111','110111010']

    # Complete full-phase feasible k-range follows from m>=rho.
    ks=list(range(31,Z+3,2))
    assert ks[0]==31 and ks[-1]==525 and len(ks)==248
    assert all(A-k-1>=RHO for k in ks)
    assert A-527-1<RHO

    total=0; maxdeath=0; maxclass=None
    for k in ks:
        classes=[]
        nmaxs=set()
        for _d,_J,_H,bits,_cost,_ys in RIGHTS:
            nmax,vals=quotient_data(k,bits); nmaxs.add(nmax)
            for N,D in vals:
                # Exact integrality sharpened by odd k.
                assert N%24==19
                m=A-k-1
                C=3**RHO*(9*N+61)//4
                T=(4+(N-2)*(1<<(k+1)))//3
                assert 4*C==3**RHO*(9*N+61)
                assert 3*T==4+(N-2)*(1<<(k+1))
                assert D==C-(1<<(m-2))*T
                assert (D-C)%(1<<(m-2))==0
                classes.append((bits,N))
        assert nmaxs=={288}
        assert len(classes)==9
        total+=len(classes)
        for bits,N in classes:
            d=death_depth(k,bits,N)
            if d>maxdeath:
                maxdeath=d; maxclass=(k,bits,N,d)
    assert total==2232
    assert maxdeath==988
    assert maxclass==(31,'101000111',43,988)

    print('PASS RL262 fourth-selector elimination')
    print('inherited scan 1288..1417 -> unique selector (1417,894,523,317,200,18,4)')
    print('geometry: 9 length-33 blocks; gaps 116,135,116,135,116,135,116,116,135; capacity 375')
    print('canonical right prefixes: 199; minimum weighted-zero cost 11')
    print('complete feasible odd terminal range: 31..525 (248 values)')
    print('phase quotient bound: N<=288; exact classes per k=9; N==19 mod24')
    print('total ordered full-phase classes=2232; survivors=0; maximum death depth=988')
    print("latest class=(k=31,prefix='101000111',N=43,death=988)")
    print('correct global reduction verified: Dcal=C-2^(m-2)T, hence Dcal==C mod 2^(m-2)')

if __name__=='__main__': main()
