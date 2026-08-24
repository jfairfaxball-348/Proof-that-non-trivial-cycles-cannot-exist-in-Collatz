from fractions import Fraction
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
import time
N=24; G=4; BUD=Fraction(31,4); X=1<<46; Y=3**29; MOD=X-Y; FULLRES=(4*X)%MOD
MAXA=42; MAXB=28; MAXAREA=23
# ten compressed preterminal target states from exact max-budget distortion DP
TARGETS={(10,3,33,22,0),(12,3,35,23,0),(12,3,35,24,0),(14,1,35,23,0),(15,1,36,24,0),
         (22,3,41,27,1),(23,21,40,28,1),(23,5,42,28,1),(23,11,41,28,1),(23,43,39,28,1)}

def v2(n):
    s=0
    while n%2==0:n//=2;s+=1
    return s,n

def qappend(q,n,h,p,qseg):
    return (pow(3,p,MOD)*q + pow(2,n,MOD)*qseg)%MOD
@lru_cache(None)
def sync_qvals(s,c):
    vals=[]
    for pos in combinations(range(s),c):
        # Q of common sync word
        mask=sum(1<<i for i in pos); seen=0;qq=0
        for i in range(s):
            if mask>>i&1:
                qq+=(1<<i)*3**(c-1-seen);seen+=1
        vals.append(qq)
    return tuple(sorted(set(vals)))
# physical dedup tables for structural graph
phys=defaultdict(dict)
with open('/mnt/data/rl41_work/small_types_17_fast_raw.tsv') as f:
    next(f)
    for ln in f:
        r,D,h,p,sn,sd=map(int,ln.split()); S=Fraction(sn,sd);k=(D,h,p)
        if k not in phys[r] or S>phys[r][k]:phys[r][k]=S
phys={r:[(D,h,p,S) for (D,h,p),S in d.items()] for r,d in phys.items()}
cphys=defaultdict(dict)
with open('/mnt/data/rl41_work/cross_types_24_fast_raw.tsv') as f:
    next(f)
    for ln in f:
        r,D,h,p,sn,sd,g,om=map(int,ln.split());S=Fraction(sn,sd);k=(D,h,p,om)
        if k not in cphys[(r,g)] or S>cphys[(r,g)][k]:cphys[(r,g)][k]=S
cphys={(r,g):[(om,h,p,S,D) for (D,h,p,om),S in d.items()] for (r,g),d in cphys.items()}
@lru_cache(None)
def nc_phys(g,r,sign):
    best={}
    for D,h,p,S in phys.get(r,()):
        den=1<<h
        for sigma in (+1,-1):
            num=3**p*(sign*g)-sigma*D
            if num%den:continue
            out=num//den
            if out==0 or (out>0)!=(sign>0):continue
            k=(abs(out),h,p)
            if k not in best or S>best[k]:best[k]=S
    return tuple((out,h,p,S) for (out,h,p),S in best.items())

def structural_next(area,state):
    g,A,B,cnt=state; sign=-1 if cnt else +1; out=[]
    # noncross, total noncross max 17 suffices for one-cross target paths
    for r in range(1,min(17,MAXAREA-area)+1):
        for om,h,p,S in nc_phys(g,r,sign):
            sv,odd=v2(om);A2=A+h+sv
            if A2>MAXA:continue
            for c in range(sv+1):
                B2=B+p+c
                if B2>MAXB:continue
                out.append((area+r,(odd*3**c,A2,B2,cnt)))
    if cnt==0:
        for r in range(7,MAXAREA-area+1):
            for om,h,p,S,D in cphys.get((r,g),()):
                sv,odd=v2(om);A2=A+h+sv
                if A2>MAXA:continue
                for c in range(sv+1):
                    B2=B+p+c
                    if B2>MAXB:continue
                    out.append((area+r,(odd*3**c,A2,B2,1)))
    return out
# Forward compressed reachability
reach=[set() for _ in range(MAXAREA+1)];reach[0].add((9,0,2,0))
for area in range(MAXAREA):
    for st in list(reach[area]):
        for a2,s2 in structural_next(area,st):
            if a2<=MAXAREA:reach[a2].add(s2)
print('compressed reach counts',[len(x) for x in reach])
# Backward mark states that can reach any target.
marked=[set() for _ in range(MAXAREA+1)]
for t in TARGETS:
    area,g,A,B,cnt=t
    if (g,A,B,cnt) in reach[area]:marked[area].add((g,A,B,cnt))
for area in range(MAXAREA-1,-1,-1):
    for st in reach[area]:
        for a2,s2 in structural_next(area,st):
            if a2<=MAXAREA and s2 in marked[a2]:
                marked[area].add(st);break
print('marked counts',[len(x) for x in marked],'start marked',(9,0,2,0) in marked[0])
# Load exact raw shapes for q residue and strong.
rawsmall=defaultdict(list)
with open('/mnt/data/rl41_work/small_shapes_17_fast_raw.tsv') as f:
    next(f)
    for ln in f:
        r,D,h,p,sn,sd,qa,qb=map(int,ln.split());rawsmall[r].append((D,h,p,Fraction(sn,sd),qa,qb))
rawcross=defaultdict(list)
with open('/mnt/data/rl41_work/cross_shapes_24_fast_raw.tsv') as f:
    next(f)
    for ln in f:
        r,D,h,p,sn,sd,g,om,qa,qb=map(int,ln.split());rawcross[(r,g)].append((D,h,p,Fraction(sn,sd),om,qa,qb))
@lru_cache(None)
def nc_raw(g,r,sign):
    # exact shape transitions, retain qu and S; dedup identical action data keeping max S
    best={}
    for D,h,p,S,qa,qb in rawsmall.get(r,()):
        den=1<<h
        for sigma in (+1,-1):
            num=3**p*(sign*g)-sigma*D
            if num%den:continue
            out=num//den
            if out==0 or (out>0)!=(sign>0):continue
            qu=qa if sigma==+1 else qb
            k=(abs(out),h,p,qu,D,sigma)
            if k not in best or S>best[k]:best[k]=S
    return tuple((om,h,p,S,qu,D,sigma) for (om,h,p,qu,D,sigma),S in best.items())
# qmod DP only on marked compressed states. state key includes q residue; value=max strong.
qstates=[{} for _ in range(MAXAREA+1)];qstates[0][(9,0,2,0,5)]=Fraction(0)
target_maps=defaultdict(dict); start=time.time(); trans=0
for area in range(MAXAREA+1):
    if qstates[area]:print('q area',area,'states',len(qstates[area]),'elapsed',round(time.time()-start,2),flush=True)
    # record target residues at boundary
    for (g,A,B,cnt,q),S in qstates[area].items():
        if (area,g,A,B,cnt) in TARGETS:
            old=target_maps[(area,g,A,B,cnt)].get(q)
            if old is None or S>old:target_maps[(area,g,A,B,cnt)][q]=S
    if area==MAXAREA:continue
    for (g,A,B,cnt,q),S in list(qstates[area].items()):
        if (g,A,B,cnt) not in marked[area]:continue
        sign=-1 if cnt else +1;n=2+A
        for r in range(1,min(17,MAXAREA-area)+1):
            for om,h,p,Sx,qu,D,sigma in nc_raw(g,r,sign):
                sv,odd=v2(om);A2=A+h+sv
                if A2>MAXA:continue
                q1=qappend(q,n,h,p,qu);S2=S+Sx
                for c in range(sv+1):
                    B2=B+p+c
                    if B2>MAXB:continue
                    st2=(odd*3**c,A2,B2,cnt)
                    if st2 not in marked[area+r]:continue
                    for qs in sync_qvals(sv,c):
                        q2=qappend(q1,n+h,sv,c,qs);k=st2+(q2,);trans+=1
                        old=qstates[area+r].get(k)
                        if old is None or S2>old:qstates[area+r][k]=S2
        if cnt==0:
            for r in range(7,MAXAREA-area+1):
                for D,h,p,Sx,om,qa,qb in rawcross.get((r,g),()):
                    sv,odd=v2(om);A2=A+h+sv
                    if A2>MAXA:continue
                    q1=qappend(q,n,h,p,qa);S2=S+Sx
                    for c in range(sv+1):
                        B2=B+p+c
                        if B2>MAXB:continue
                        st2=(odd*3**c,A2,B2,1)
                        if st2 not in marked[area+r]:continue
                        for qs in sync_qvals(sv,c):
                            q2=qappend(q1,n+h,sv,c,qs);k=st2+(q2,);trans+=1
                            old=qstates[area+r].get(k)
                            if old is None or S2>old:qstates[area+r][k]=S2
print('qDP done elapsed',time.time()-start,'trans',trans)
# Generate all exact final shape options from each target and test required pre-residue.
def req_pre(npre,h,p,qu):
    rhs=(FULLRES-pow(2,npre,MOD)*qu)%MOD
    return rhs*pow(pow(3,p,MOD),-1,MOD)%MOD
survivors=[]
for T in sorted(TARGETS):
    area,g,A,B,cnt=T; r=N-area; mp=target_maps[T]; opts=[]
    sign=-1 if cnt else +1
    if cnt==0:
        # final crossing positive->negative
        for D,h,p,Sx,om,qa,qb in rawcross.get((r,g),()):
            if om%4:continue
            qpow=om//4
            if qpow<=0 or qpow&(qpow-1):continue
            sv,_=v2(om)
            if A+h+sv!=46 or B+p!=29:continue
            req=req_pre(2+A,h,p,qa);best=mp.get(req)
            opts.append((D,h,p,Sx,om,qa,req,best))
            if best is not None and best+Sx>BUD:survivors.append((T,'C',D,req,best,Sx))
    else:
        # final sign-preserving negative excursion: exact raw shapes/orientations
        for D,h,p,Sx,qa,qb in rawsmall.get(r,()):
            den=1<<h
            for sigma in (+1,-1):
                num=3**p*(-g)-sigma*D
                if num%den:continue
                out=num//den
                if out>=0:continue
                om=-out
                if om%4:continue
                qpow=om//4
                if qpow<=0 or qpow&(qpow-1):continue
                sv,_=v2(om)
                if A+h+sv!=46 or B+p!=29:continue
                qu=qa if sigma==+1 else qb
                req=req_pre(2+A,h,p,qu);best=mp.get(req)
                opts.append((D,h,p,Sx,om,qu,req,best,sigma))
                if best is not None and best+Sx>BUD:survivors.append((T,'N',D,req,best,Sx,sigma))
    matches=sum(1 for x in opts if ((x[-1] is not None and x[-1]+x[3]>BUD) if cnt==0 else (x[-2] is not None and x[-2]+x[3]>BUD)))
    print('TARGET',T,'residues',len(mp),'final opts',len(opts),'budget-compatible req matches',matches)
print('ABSOLUTE SURVIVORS',len(survivors))
for s in survivors[:50]:print(s)
