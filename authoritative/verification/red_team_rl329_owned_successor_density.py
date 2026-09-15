#!/usr/bin/env python3
"""Independent structural red team for the RL329 owned-successor certificate."""
from collections import Counter,defaultdict
from fractions import Fraction
from functools import lru_cache
from math import gcd
A=217_976_794_617; ELL=137_528_045_312; D=A-ELL; LOW=1<<71; UP=(1<<76)+(1<<36)
LAM=1+Fraction(1,1<<40); H=32_562_630_354; CAP=H-1; T=ELL-60

def atanh_log(x,n=280):
    s=Fraction(0); t=x; x2=x*x
    for j in range(n): s+=t/(2*j+1); t*=x2
    lo=2*s; return lo,lo+2*t/(2*n+1)/(1-x2)
l2lo,l2hi=atanh_log(Fraction(1,3)); l3lo,l3hi=atanh_log(Fraction(1,2)); dup=A*l2hi-ELL*l3lo; assert dup>0

@lru_cache(None)
def factors(L):
    cuts=sorted({0,ELL,*(((-D*j)%ELL) for j in range(L+1))}); out=set()
    for a,b in zip(cuts,cuts[1:]):
        for r in (a,min(a+1,b-1)):
            prev=(r+ELL-1)//ELL; g=[]
            for j in range(1,L+1): cur=(r+D*j+ELL-1)//ELL; g.append(1+cur-prev); prev=cur
            out.add(tuple(g))
    assert len(out)==L+1; return tuple(sorted(out))
def residue_for(gaps):
    C=0
    for j,g in enumerate(gaps): C=(1<<g)*C+3**j
    M=3**len(gaps); return C*pow(1<<sum(gaps),-1,M)%M,M
def walk(x,gaps):
    xs=[x]
    for g in gaps:
        y=(1<<g)*x-1
        if y%3:return None
        x=y//3
        if x<=0 or x%2==0:return None
        xs.append(x)
    return tuple(xs)
def realizations(gaps):
    r,m=residue_for(gaps); k=max(0,(LOW-r+m-1)//m); x=r+k*m
    while x<UP:
        if x&1:
            xs=walk(x,gaps)
            if xs is not None: yield xs
        x+=m

rows=[]
for total in range(45,99):
    for l in range(max(1,total-49),min(49,total-1)+1):
        rr=total-l
        for base in factors(total):
            if base[l]!=2: continue
            g=list(base); g[l-1]+=1; g[l]-=1
            for xs in realizations(tuple(g)):
                if dup*min(xs)>=H: rows.append((tuple(xs[:l]),tuple(xs[l+1:]),l,rr))
counts=Counter(l+r for _,_,l,r in rows); assert counts=={45:4755,46:1633,47:556,48:173,49:46,50:14,51:6}; assert len(rows)==7183
pairs=sorted({(r[2],r[3]) for r in rows}); assert len(pairs)==231
left=defaultdict(list)
for i,r in enumerate(rows): left[(r[2],r[0][0])].append(i)
phys=[]
for i,r in enumerate(rows): phys.extend((i,j) for j in left[(r[3],r[1][0])])
assert len(phys)==14
plinks={((rows[i][2],rows[i][3]),(rows[j][2],rows[j][3])) for i,j in phys}; assert len(plinks)==13

@lru_cache(None)
def short_templates(pair):
    l,r=pair; out=[]
    for base in factors(l+r):
        if base[l]!=2: continue
        g=list(base); g[l-1]+=1; g[l]-=1; g=tuple(g); q,m=residue_for(g); out.append((q,m,g))
    return tuple(out)
def follows(x,pair):
    for q,m,g in short_templates(pair):
        if x%m!=q: continue
        xs=walk(x,g)
        if xs is not None and dup*min(xs)>=H:return True
    return False
by_pair=defaultdict(list)
for r in rows: by_pair[(r[2],r[3])].append(r)
allowed=set()
for p,rs in by_pair.items():
    cur=p[1]
    for nxt in range(1,45-cur):
        if any(follows(r[1][0],(cur,nxt)) for r in rs): allowed.add((p,nxt))
assert len(allowed)==286
assert ((45,4),39) not in allowed
for source_pair,next_zero in [((13,38),6),((6,42),2),((45,1),43),((43,7),37),((37,14),29),((29,20),24),((24,25),19),((19,31),13)]: assert (source_pair,next_zero) not in allowed

p2=[]
for total in range(45,99):
    for l in range(max(1,total-49),min(49,total-1)+1):
        for base in factors(total+1):
            for h in (1,2):
                g=list(base)
                for o,c in enumerate((h,1-h,-1)): g[l-1+o]+=c
                if min(g[l-1:l+2])<1: continue
                for xs in realizations(tuple(g)):
                    if dup*min(xs)>=H:p2.append(total)
assert Counter(p2)=={45:2029,46:707,47:270,48:93,49:34,50:11,51:2}; assert max(p2)==51

states=[('N',z) for z in range(1,50)]+[('L',p) for p in pairs]; idx={s:i for i,s in enumerate(states)}; by_left=defaultdict(list)
for p in pairs: by_left[p[0]].append(p)
edges=[]
for st in states:
    s=idx[st]; cur=st[1] if st[0]=='N' else st[1][1]
    for nz in range(1,50):
        if cur+nz<=44 and (st[0]=='N' or (st[1],nz) in allowed): edges.append((s,idx[('N',nz)],nz,1))
    for p in by_left[cur]:
        if st[0]=='N' or (st[1],p) in plinks: edges.append((s,idx[('L',p)],p[1],1))
    for nz in range(1,50):
        if cur+nz<=51: edges.append((s,idx[('N',nz)],nz,2))
        edges.append((s,idx[('N',nz)],nz,3))
assert len(states)==280 and len(edges)==22991
pot=[0]*len(states)
for it in range(len(states)+1):
    ch=False
    for s,t,z,k in edges:
        if pot[s]+z-22*k>pot[t]: pot[t]=pot[s]+z-22*k; ch=True
    if not ch: break
else: raise AssertionError('positive cycle')
assert it+1==2 and max(pot)==26
B=max(z-pot[idx[('N',z)]] for z in range(1,50))+max(pot); assert B==66
assert any(s==idx[('N',22)] and t==s and z==22 and k==1 for s,t,z,k in edges)
assert any(s==idx[('N',21)] and t==idx[('N',23)] and z==23 and k==1 for s,t,z,k in edges)
assert any(s==idx[('N',23)] and t==idx[('N',21)] and z==21 and k==1 for s,t,z,k in edges)
K=(T+1-B+22)//23; assert K==5_979_480_226
x=l2lo/ELL; full=1/(2*(x+x*x/2))-Fraction(1,2); om=sum((Fraction(1<<((A*r)//ELL),3**r) for r in range(1,60)),Fraction(0))/LAM; ideal=(full-om)/3
s1=K*(K+1)//2; s2=K*(K+1)*(2*K+1)//6; s3=s1*s1; s4=K*(K+1)*(2*K+1)*(3*K*K+3*K-1)//30
W=Fraction(K)+l2lo*s1/ELL+l2lo**2*s2/(2*ELL**2)+l2lo**3*s3/(6*ELL**3)+l2lo**4*s4/(24*ELL**4); rhs=1+ideal-W/(12*LAM)
assert CAP<rhs<H; assert gcd(A,ELL)==1
print('RL329_OWNED_SUCCESSOR_RED_TEAM_GREEN')
print('rows_pairs_links',len(rows),len(pairs),len(phys))
print('allowed_large_to_short',len(allowed))
print('states_edges',len(states),len(edges))
print('density_boundary',B)
print('sharp_total44_cycle_ratio',22)
print('carry_cap',CAP)
