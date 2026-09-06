#!/usr/bin/env python3
from collections import Counter
from itertools import product

A=1287; ELL=812; Z=475; Q=485; RSEL=306; HSEL=16; NSEL=6
RHO=ELL-3
M=(1<<A)-3**ELL
BLOCKS=[(129,161),(297,329),(446,478),(614,646),(782,814),(931,963),(1099,1131),(1248,1280)]
R_TAU={28:262,30:283,32:300,34:313,36:322,38:327,40:328}
EXPECTED_COUNTS={
  31:(198420,194960,36457,37,892),
  33:(43695,41814,7934,37,888),
  35:(7458,6634,1269,35,884),
  37:(784,724,121,17,880),
  39:(47,46,7,3,15),
}
EXPECTED_LONG={
37:[('100011100',715,1,875),('101000111',43,2,880),('110001000',571,1,876),('110010011',955,9,875)],
35:[('000010110',355,4,880),('000011110',1123,15,881),('000110001',931,9,880),('000111000',163,15,881),('001000010',643,3,879),('001100110',67,33,883),('100001100',331,23,880),('100011100',715,47,879),('101000111',43,50,884),('110001000',571,47,880),('110010011',955,61,879)],
33:[('000000100',739,57,882),('000010110',355,157,884),('000011110',1123,202,885),('000110001',931,181,884),('000111000',163,202,885),('001000010',643,144,883),('001100110',67,234,887),('100001100',331,220,884),('100011100',715,247,883),('101000111',43,249,888),('110001000',571,247,884),('110010011',955,255,883)],
31:[('000000100',739,740,886),('000010110',355,938,888),('000011110',1123,988,889),('000110001',931,965,888),('000111000',163,988,889),('001000010',643,920,887),('001100110',67,1011,891),('100001100',331,1002,888),('100011100',715,1019,887),('101000111',43,1021,892),('110001000',571,1019,888),('110010011',955,1024,887)],
}
EXPECTED_K39=[('101110100',235,1,10),('101110101',235,2,15),('110111010',763,4,13)]

def step_x(d,J,x):
    if J & 1:
        y=x
        if x==0: return d,(J+3**d-2**d)//2,y
        return d,(3*J+2**d-1)//2,y
    y=1-x
    if x==0: return d+1,(3*J+3**(d+1)-2**d-1)//2,y
    if d<=1: return None
    return d-1,J//2,y

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
        p%=A
        ex.add(p); ex.add((p-Q+1)%A)
    return ex

def capacity(ex):
    total=0
    for pts in GAPS:
        # All present gaps are non-wrapping in the chosen representative, but retain cyclic-safe code.
        coords=([p if p>=pts[0] else p+A for p in pts] if pts[0]>pts[-1] else pts)
        last=-10**18
        for c,p in zip(coords,pts):
            if p in ex: continue
            if c-last>=3:
                total+=1; last=c
    return total

def forward_bits(bits):
    d,J,H=1,-13,0; ys=''
    for ch in bits:
        o=step_x(d,J,int(ch))
        if o is None: return None
        d2,J2,y=o
        H+=d-1; d,J=d2,J2; ys+=str(y)
    return d,J,H,ys

RIGHTS=[]
for t in product('01',repeat=9):
    bits=''.join(t)
    o=forward_bits(bits)
    if o is None: continue
    d,J,H,ys=o
    cost=sum(w for w,ch in zip(range(9,0,-1),bits) if ch=='0')
    RIGHTS.append((d,J,H,bits,cost,ys))

def exact_pairs(k):
    tau=k-3; base=R_TAU[tau]-2; L=41-k
    tail=excluded_roots(range(-tau,0)); tailcap=capacity(tail)
    lefts=[]
    for t in product('01',repeat=L):
        bits=''.join(t)
        cost=sum(w for w,ch in zip(range(1,L+1),bits) if ch=='0')
        lefts.append((bits,cost))
    raw=0; pairs=[]
    for _d,_J,_H,rbits,rcost,_ys in RIGHTS:
        rex=excluded_roots([3+i for i,ch in enumerate(rbits) if ch=='0'])
        for lbits,lcost in lefts:
            E=rcost+lcost
            if base+E<=tailcap:
                raw+=1
                lex=excluded_roots([-39+i for i,ch in enumerate(lbits) if ch=='0'])
                if base+E<=capacity(tail|rex|lex):
                    pairs.append((rbits,lbits,rcost,lcost))
    return raw,pairs

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

def main():
    assert A*RSEL-Q*ELL==2
    assert 19*Z-7*A==HSEL
    assert 19*(Q-RSEL)-7*Q==NSEL
    assert [len(g) for g in GAPS]==[135,116,135,135,116,135,116,135]
    assert sum(map(len,GAPS))==1023
    assert len(RIGHTS)==199
    assert min(x[4] for x in RIGHTS)==11
    assert [x[3] for x in RIGHTS if x[4]==11]==['110110111','110111010']
    assert [capacity(excluded_roots(range(-t,0))) for t in (28,30,32,34,36,38,40)]==[338,337,337,336,335,335,334]

    # k>=41 is impossible from tail room versus right-prefix minimum cost.
    assert capacity(excluded_roots(range(-38,0)))-(R_TAU[38]-2)==10 < 11

    all_rows={}
    for k in (39,37,35,33,31):
        raw,pairs=exact_pairs(k)
        cnt=Counter(r for r,_l,_rc,_lc in pairs)
        classes=[]; phase_pairs=0
        for bits,paircnt in sorted(cnt.items()):
            nmax,vals=quotient_data(k,bits)
            assert nmax==1209
            if vals:
                phase_pairs+=paircnt
                for N,_D in vals: classes.append((bits,N,paircnt))
        deaths=[(bits,N,c,death_depth(k,bits,N)) for bits,N,c in classes]
        exp_raw,exp_cap,exp_phase,exp_classes,exp_max=EXPECTED_COUNTS[k]
        assert raw==exp_raw and len(pairs)==exp_cap
        assert phase_pairs==exp_phase and len(classes)==exp_classes
        assert max(d for *_x,d in deaths)==exp_max
        assert all(d>9 for *_x,d in deaths)
        if k==39:
            assert deaths==EXPECTED_K39
        else:
            assert [x for x in deaths if x[3]>27]==EXPECTED_LONG[k]
        all_rows[k]=(raw,len(pairs),phase_pairs,len(classes),max(d for *_x,d in deaths),sum(d<=27 for *_x,d in deaths))

    # Exact positive integral quotient set is the same 50 values for all live k.
    admiss=[]
    top=237*3**RHO - (1<<(A-31+1))
    for N in range(1,1210):
        if N%8!=3: continue
        num=top-(N-2)*M
        if num%12==0 and num//12>=0: admiss.append(N)
    assert admiss==list(range(19,1196,24)) and len(admiss)==50

    print('PASS RL261 third-selector full-phase elimination')
    print('selector=(1287,812,475,485,306,16,6); right prefixes=199; min right cost=11')
    print('pre-phase terminal frontier={31,33,35,37,39}; k>=41 impossible')
    for k in (39,37,35,33,31):
        raw,cap,pp,cl,mx,sh=all_rows[k]
        print(f'k={k}: {raw} budget -> {cap} capacity -> {pp} phase-pairs -> {cl} classes -> 0; max death={mx}; shallow<=27={sh}')
    print('admissible phase quotients: 50 values, 19..1195 step 24')
    print('RESULT: no genuine full-phase survivor at the third selector')

if __name__=='__main__': main()
