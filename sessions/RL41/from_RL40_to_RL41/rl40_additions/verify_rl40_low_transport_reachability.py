from fractions import Fraction
from collections import defaultdict
from itertools import permutations

ZCAP=Fraction(16,15)
B4=Fraction(31,4)
B8=Fraction(31,2)


def Qword(w):
    L=sum(w); p=0; q=0
    for i,b in enumerate(w):
        if b:
            q += (1<<i)*3**(L-1-p)
            p += 1
    return q


def suffix_peak(beta):
    h=len(beta); ones=0; M=Fraction(1)
    for j in range(h-1,-1,-1):
        ones += beta[j]
        M=max(M,Fraction(3**ones,2**(h-j)))
    return M


def canonical_positive_excursions(maxarea):
    def rec(alpha,beta,d,area):
        area2=area+d
        if area2>maxarea:
            return
        if d==1:
            yield alpha+(1,),beta+(0,),area2
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd=d+y-x
            if nd>0:
                yield from rec(alpha+(x,),beta+(y,),nd,area2)
    yield from rec((0,),(1,),1,0)


def crossing_gap(D,h,p):
    mod=1<<h
    g=(D*pow(3**p,-1,mod))%mod
    if g==0:
        g=mod
    maxg=(D-1)//(3**p)
    if g<=maxg and (g&1):
        n=D-3**p*g
        assert n>0 and n%mod==0
        return g,n//mod
    return None


by=defaultdict(list)
E={}
C={}
for alpha,beta,r in canonical_positive_excursions(17):
    h=len(alpha); p=sum(alpha); D=Qword(alpha)-Qword(beta)
    M=suffix_peak(beta)
    strong=Fraction(D,1<<h)*min(Fraction(1),ZCAP/M)
    cross=crossing_gap(D,h,p)
    rec={'D':D,'h':h,'p':p,'strong':strong,'cross':cross,
         'alpha':alpha,'beta':beta}
    by[r].append(rec)
    if r not in E or strong>E[r]: E[r]=strong
    if cross is not None and (r not in C or strong>C[r]): C[r]=strong

counts={1:1,2:2,3:4,4:9,5:20,6:46,7:105,8:242,9:557,
        10:1285,11:2964,12:6842,13:15793,14:36463,15:84187,
        16:194388,17:448847}
assert {r:len(by[r]) for r in range(1,18)}==counts

E_expected={
 1:Fraction(1,4), 2:Fraction(16,27), 3:Fraction(13,16),
 4:Fraction(188,135), 5:Fraction(53,32), 6:Fraction(560,243),
 7:Fraction(377,135), 8:Fraction(401,128), 9:Fraction(5068,1215),
 10:Fraction(1321,270), 11:Fraction(1369,256), 12:Fraction(13552,2187),
 13:Fraction(8713,1215), 14:Fraction(8929,1080), 15:Fraction(9121,1024),
 16:Fraction(22300,2187), 17:Fraction(28361,2430),
}
assert E==E_expected
for r in range(1,7): assert r not in C


def parts(n,maxpart=None):
    if n==0:
        yield (); return
    if maxpart is None or maxpart>n: maxpart=n
    for p in range(maxpart,0,-1):
        for t in parts(n-p,p): yield (p,)+t


def cenv(part):
    vals=[]
    for i,r in enumerate(part):
        if r in C:
            vals.append(C[r]+sum(E[x] for j,x in enumerate(part) if j!=i))
    return max(vals) if vals else Fraction(0)

# rho=16 reduction
viable16=[p for p in parts(16) if cenv(p)>B4]
assert viable16==[(16,),(14,2),(14,1,1)]
assert max(sum(E[x] for x in p) for p in parts(16))==E[16] < B8

# G=4, prefix 11 -> first excursion gap 9.
first_gap=9

# Single area-16 candidate compatible with first gap has J<1.
c16=[x for x in by[16] if x['cross'] and x['strong']>B4]
assert sorted((x['D'],x['h'],x['p'],x['cross'][0],x['cross'][1]) for x in c16)==sorted([
    (27875,11,7,9,4),(9199,10,6,7,4),(44815,12,7,13,4)])
x=[x for x in c16 if x['cross'][0]==9][0]
assert Fraction((1<<x['h'])*4,3**x['p']*9)==Fraction(8192,19683)<1

# Unique viable area-14 crossing requires gap 13.
need=min(B4-E[2],B4-2*E[1])
c14=[x for x in by[14] if x['cross'] and x['strong']>need]
assert len(c14)==1 and (c14[0]['D'],c14[0]['h'],c14[0]['p'],c14[0]['cross'])==(17669,11,6,(13,4))


def local_step(delta,t,sigma):
    # sigma=+1 positive prefix-count excursion; sigma=-1 negative.
    num=3**t['p']*delta-sigma*t['D']
    den=1<<t['h']
    if num%den: return None
    return num//den

# Exact area-1/2 transitions used in rho=16 proof.
def positive_integral_transitions(g,r):
    out=[]
    for t in by[r]:
        for sigma in (+1,-1):
            q=local_step(g,t,sigma)
            if q is not None and q>0:
                out.append((t['D'],t['h'],t['p'],sigma,q))
    return out
assert positive_integral_transitions(9,1)==[(1,2,1,-1,7)]
assert positive_integral_transitions(7,1)==[(1,2,1,+1,5)]
assert positive_integral_transitions(9,2)==[(3,3,1,+1,3)]
assert 13 not in {9,7,5,3}

# rho=17 partition pruning
assert max(sum(E[x] for x in p) for p in parts(17))==E[17] < B8
viable17=[p for p in parts(17) if cenv(p)>B4]
expected17=[(17,),(16,1),(15,2),(15,1,1),(14,3),(14,2,1),
            (14,1,1,1),(12,5),(12,4,1)]
assert viable17==expected17


def sync_next(delta):
    sign=1 if delta>0 else -1
    n=abs(delta); s=0
    while n%2==0:
        n//=2; s+=1
    # Safe over-approximation: c common odd columns may be any 0..s.
    return [sign*n*3**c for c in range(s+1)]


def terminal_ok(delta):
    if delta>=0 or (-delta)%4: return False
    q=(-delta)//4
    return q>0 and (q&(q-1))==0

# For each viable partition, crossing is its largest part.  Keep only crossing
# types that can still clear B4 even if every small part attains E(r).
large_candidates={}
for part in viable17:
    R=part[0]; comp=part[1:]
    threshold=B4-sum(E[r] for r in comp)
    large_candidates[part]=[x for x in by[R] if x['cross'] and x['strong']>threshold]

small={r:by[r] for r in range(1,6)}
physical=[]
for part in viable17:
    R=part[0]
    for order in sorted(set(permutations(part))):
        ci=order.index(R)
        for cross_t in large_candidates[part]:
            def dfs(i,delta,strongsum,path):
                if i==len(order):
                    if strongsum>B4 and terminal_ok(delta):
                        physical.append((part,order,cross_t,delta,strongsum,tuple(path)))
                    return
                r=order[i]
                types=[cross_t] if i==ci else small[r]
                for t in types:
                    for sigma in (+1,-1):
                        out=local_step(delta,t,sigma)
                        if out is None or out==0: continue
                        if i<ci and not (delta>0 and out>0): continue
                        if i==ci and not (delta>0 and out<0): continue
                        if i>ci and not (delta<0 and out<0): continue
                        rec=(r,t['D'],t['h'],t['p'],sigma,delta,out)
                        if i==len(order)-1:
                            dfs(i+1,out,strongsum+t['strong'],path+[rec])
                        else:
                            for nxt in sync_next(out):
                                dfs(i+1,nxt,strongsum+t['strong'],path+[rec+(nxt,)])
            dfs(0,first_gap,Fraction(0),[])

# Two word-shapes share the same area-17 local numeric data, so there are four
# raw records but only three distinct physical transition patterns.
def numeric_signature(sol):
    part,order,cross_t,delta,strong,path=sol
    return (part,order,tuple((x[0],x[1],x[2],x[3],x[4],x[5],x[6]) for x in path))
sigs=sorted(set(numeric_signature(s) for s in physical),key=str)
assert len(sigs)==3

# Identify and certify the three distortion products.
products=[]
for sig in sigs:
    part,order,path=sig
    prod=Fraction(1)
    for r,D,h,p,sigma,din,dout in path:
        J=Fraction((1<<h)*abs(dout),3**p*abs(din))
        prod*=J
    products.append((part,order,prod,path))

assert sorted(p[2] for p in products)==sorted([
    Fraction(32768,59049),
    Fraction(16384,19683),
    Fraction(524288,531441),
])
assert all(prod<1 for _,_,prod,_ in products)

print('RL40 low-transport crossing reachability verifier: PASS')
print('canonical positive excursions through area 17 =',sum(counts.values()))
print('crossing-aware viable rho=16 partitions =',viable16)
print('crossing-aware viable rho=17 partitions =',viable17)
print('rho=17 distinct endpoint-compatible physical patterns =',len(sigs))
for part,order,prod,path in products:
    print('  pattern',part,'order',order,'distortion product',prod)
print('certified strengthened consequence: rho >= 18')
