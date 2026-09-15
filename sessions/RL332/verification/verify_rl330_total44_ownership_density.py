#!/usr/bin/env python3
"""Exact RL330 scratch verifier: total-44 ownership and carry contraction."""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache

A=217_976_794_617; ELL=137_528_045_312; D=A-ELL
LOW=1<<71; UP=(1<<76)+(1<<36)
H=32_551_214_632; CAP=H-1; OWNED_TOTAL=44
SHORT_MAX=OWNED_TOTAL-1

def log_interval_atanh(x,terms=280):
    x2=x*x; term=x; total=Fraction(0)
    for j in range(terms): total+=term/(2*j+1); term*=x2
    lo=2*total; return lo,lo+2*term/(2*terms+1)/(1-x2)

l2lo,l2hi=log_interval_atanh(Fraction(1,3))
l3lo,l3hi=log_interval_atanh(Fraction(1,2))
delta_up=A*l2hi-ELL*l3lo

@lru_cache(None)
def factors(length):
    cuts=sorted({0,ELL,*(((-D*j)%ELL) for j in range(length+1))}); out=set()
    for a,b in zip(cuts,cuts[1:]):
        for r in {a,min(a+1,b-1)}:
            prev=(r+ELL-1)//ELL; gaps=[]
            for j in range(1,length+1):
                cur=(r+D*j+ELL-1)//ELL; gaps.append(1+cur-prev); prev=cur
            out.add(tuple(gaps))
    assert len(out)==length+1
    return tuple(sorted(out))

def residue(gaps):
    c=0
    for j,g in enumerate(gaps): c=(1<<g)*c+3**j
    m=3**len(gaps)
    return c*pow(1<<sum(gaps),-1,m)%m,m

def reconstruct(x,gaps):
    states=[x]
    for g in gaps:
        y=(1<<g)*x-1
        assert y%3==0
        x=y//3; assert x&1; states.append(x)
    return tuple(states)

def realizations(gaps):
    r,m=residue(gaps); x=r+max(0,(LOW-r+m-1)//m)*m
    while x<UP:
        if x&1: yield x,reconstruct(x,gaps)
        x+=m

rows=[]
for left in range(1,OWNED_TOTAL):
    right=OWNED_TOTAL-left
    for base in factors(OWNED_TOTAL):
        if base[left]!=2: continue
        gaps=list(base); gaps[left-1]+=1; gaps[left]-=1; gaps=tuple(gaps)
        for endpoint,states in realizations(gaps):
            if delta_up*min(states)>=H:
                rows.append((left,right,states[0],states[left+1],min(states),endpoint,gaps))

by_pair=Counter((r[0],r[1]) for r in rows)
assert by_pair=={
    (1,43):279,(2,42):336,(3,41):324,(4,40):259,(5,39):378,(6,38):252,
    (7,37):375,(8,36):307,(9,35):294,(10,34):352,(11,33):232,(12,32):403,
    (13,31):288,(14,30):325,(15,29):329,(16,28):248,(17,27):386,(18,26):258,
    (19,25):366,(20,24):313,(21,23):282,(22,22):360,(23,21):237,(24,20):395,
    (25,19):294,(26,18):313,(27,17):337,(28,16):237,(29,15):392,(30,14):263,
    (31,13):354,(32,12):323,(33,11):272,(34,10):371,(35,9):246,(36,8):385,
    (37,7):299,(38,6):305,(39,5):345,(40,4):225,(41,3):403,(42,2):268,(43,1):346,
}
left_index=defaultdict(list)
for j,r in enumerate(rows): left_index[(r[0],r[2])].append(j)
links=[]
for i,r in enumerate(rows):
    links.extend((i,j) for j in left_index[(r[1],r[3])])

pair_links=Counter(((rows[i][0],rows[i][1]),(rows[j][0],rows[j][1])) for i,j in links)
self_links=[(i,j) for i,j in links if i==j]
assert len(rows)==13556 and len(links)==14 and not self_links
assert set(pair_links)=={((1,43),(43,1)),((2,42),(42,2))}
print("rows",len(rows))
print("threshold",H)
print("owned_total",OWNED_TOTAL)
print("pair_support",len(by_pair),min(by_pair),max(by_pair))
print("pair_counts",dict(sorted(by_pair.items())))
print("physical_links",len(links))
print("pair_links",dict(sorted(pair_links.items())))
print("self_links",self_links)

# Reconstruct the inherited large-singleton layer in the same row format.
large=[]
for total in range(OWNED_TOTAL+1,99):
    for left in range(max(1,total-49),min(49,total-1)+1):
        right=total-left
        for base in factors(total):
            if base[left]!=2: continue
            gaps=list(base); gaps[left-1]+=1; gaps[left]-=1; gaps=tuple(gaps)
            for endpoint,states in realizations(gaps):
                if delta_up*min(states)>=H:
                    large.append((left,right,states[0],states[left+1],min(states),endpoint,gaps))
print("large_rows",len(large))
print("large_counts",dict(sorted(Counter(r[0]+r[1] for r in large).items())),"pairs",len({r[:2] for r in large}))
assert Counter(r[0]+r[1] for r in large)=={45:4759,46:1634,47:556,48:173,49:46,50:14,51:6}
assert len(large)==7188 and len({r[:2] for r in large})==231

large_pairs=sorted({r[:2] for r in large})
large_by_pair=defaultdict(list)
for i,r in enumerate(large): large_by_pair[r[:2]].append(i)
large_left=defaultdict(list)
for i,r in enumerate(large): large_left[(r[0],r[2])].append(i)
large_links=[]
for i,r in enumerate(large):
    large_links.extend((i,j) for j in large_left[(r[1],r[3])])
large_pair_links={ (large[i][:2],large[j][:2]) for i,j in large_links }
print("large_links",len(large_links),"pair_links",len(large_pair_links))
assert len(large_links)==14 and len(large_pair_links)==13

# Exact cross-links involving the total-44 layer.
t44_left=defaultdict(list)
for j,r in enumerate(rows): t44_left[(r[0],r[2])].append(j)
large_to_t44=[]
for i,r in enumerate(large):
    large_to_t44.extend((i,j) for j in t44_left[(r[1],r[3])])
t44_to_large=[]
for i,r in enumerate(rows):
    t44_to_large.extend((i,j) for j in large_left[(r[1],r[3])])
large_t44_pair_links={(large[i][:2],rows[j][:2]) for i,j in large_to_t44}
t44_large_pair_links={(rows[i][:2],large[j][:2]) for i,j in t44_to_large}
print("large_to_t44_physical",len(large_to_t44),"pair_links",sorted(large_t44_pair_links))
print("t44_to_large_physical",len(t44_to_large),"pair_links",sorted(t44_large_pair_links))
assert len(large_to_t44)==7 and large_t44_pair_links=={((2,43),(43,1)),((3,42),(42,2)),((3,43),(43,1)),((4,41),(41,3))}
assert len(t44_to_large)==6 and t44_large_pair_links=={((1,43),(43,2)),((2,42),(42,3))}

# Structural diagnostic on the exact-owned singleton transition projection.
owned_nodes=[("L",p) for p in large_pairs]+[("T",p) for p in sorted(by_pair)]
owned_edges=({(("L",a),("L",b)) for a,b in large_pair_links} |
             {(("L",a),("T",b)) for a,b in large_t44_pair_links} |
             {(("T",a),("L",b)) for a,b in t44_large_pair_links} |
             {(("T",a),("T",b)) for a,b in set(pair_links)})
owned_out=defaultdict(list); indegree={node:0 for node in owned_nodes}
for source,target in owned_edges:
    owned_out[source].append(target); indegree[target]+=1
queue=[node for node in owned_nodes if indegree[node]==0]; topo=[]
while queue:
    node=queue.pop(); topo.append(node)
    for target in owned_out[node]:
        indegree[target]-=1
        if indegree[target]==0: queue.append(target)
assert len(topo)==len(owned_nodes)
longest={node:0 for node in owned_nodes}
for node in topo:
    for target in owned_out[node]: longest[target]=max(longest[target],longest[node]+1)
print("owned_singleton_dag",len(owned_nodes),len(owned_edges),"longest_edges",max(longest.values()))

two_positive=[]
for total in range(OWNED_TOTAL+1,99):
    for left in range(max(1,total-49),min(49,total-1)+1):
        for base in factors(total+1):
            for height in (1,2):
                gaps=list(base)
                for off,change in enumerate((height,1-height,-1)):
                    gaps[left-1+off]+=change
                if min(gaps[left-1:left+2])<1: continue
                for _,states in realizations(tuple(gaps)):
                    if delta_up*min(states)>=H: two_positive.append(total)
p2_counts=Counter(two_positive); p2_max=max(p2_counts)
assert p2_counts=={45:2030,46:707,47:270,48:93,49:34,50:11,51:2}
print("two_positive_counts",dict(sorted(p2_counts.items())),"max",p2_max)

# Exact large->short support from RL329, retained for totals <=43.
@lru_cache(None)
def singleton_templates(pair):
    left,right=pair; out=[]
    for base in factors(left+right):
        if base[left]!=2: continue
        gaps=list(base); gaps[left-1]+=1; gaps[left]-=1; gaps=tuple(gaps)
        q,m=residue(gaps); out.append((q,m,gaps))
    return tuple(out)

def short_follows(x,pair):
    for q,m,gaps in singleton_templates(pair):
        if x%m!=q: continue
        states=reconstruct(x,gaps)
        if delta_up*min(states)>=H: return True
    return False

allowed_large_short=set()
for pair,inds in large_by_pair.items():
    current=pair[1]
    for nxt in range(1,OWNED_TOTAL-current):
        if any(short_follows(large[i][3],(current,nxt)) for i in inds):
            allowed_large_short.add((pair,nxt))

t44_by_pair=defaultdict(list)
for i,r in enumerate(rows): t44_by_pair[r[:2]].append(i)
allowed_t44_short=set()
for pair,inds in t44_by_pair.items():
    current=pair[1]
    for nxt in range(1,OWNED_TOTAL-current):
        if any(short_follows(rows[i][3],(current,nxt)) for i in inds):
            allowed_t44_short.add((pair,nxt))
print("allowed_t44_to_short",len(allowed_t44_short))
print("allowed_large_to_short_le43",len(allowed_large_short))
assert len(allowed_t44_short)==166 and len(allowed_large_short)==282

# Conservative pair projection of the exact owned graph.  Every T transition is
# first reconstructed with exact shared physical identity above; projecting to
# pairs can only add paths.  A potential here therefore lifts to every physical
# T realization while being much faster to find.
t44_pairs=sorted(by_pair)
states=[("N",z) for z in range(1,50)]+[("L",p) for p in large_pairs]+[("T",p) for p in t44_pairs]
idx={s:i for i,s in enumerate(states)}
large_pairs_by_left=defaultdict(list)
for p in large_pairs: large_pairs_by_left[p[0]].append(p)
edges=[]
for z in range(1,50):
    s=idx[("N",z)]
    for nz in range(1,50):
        if z+nz<=SHORT_MAX: edges.append((s,idx[("N",nz)],nz,1))
        if z+nz<=p2_max: edges.append((s,idx[("N",nz)],nz,2))
        edges.append((s,idx[("N",nz)],nz,3))
    for p in large_pairs_by_left[z]: edges.append((s,idx[("L",p)],p[1],1))
    for p in t44_pairs:
        if p[0]==z: edges.append((s,idx[("T",p)],p[1],1))

for p in large_pairs:
    s=idx[("L",p)]; current=p[1]
    for nz in range(1,50):
        if current+nz<=SHORT_MAX and (p,nz) in allowed_large_short: edges.append((s,idx[("N",nz)],nz,1))
        if current+nz<=p2_max: edges.append((s,idx[("N",nz)],nz,2))
        edges.append((s,idx[("N",nz)],nz,3))
    for q in large_pairs_by_left[current]:
        if (p,q) in large_pair_links: edges.append((s,idx[("L",q)],q[1],1))
    for source,target in large_t44_pair_links:
        if source==p: edges.append((s,idx[("T",target)],target[1],1))

t44_pair_links=set(pair_links)
for p in t44_pairs:
    s=idx[("T",p)]; current=p[1]
    for nz in range(1,50):
        if current+nz<=SHORT_MAX and (p,nz) in allowed_t44_short: edges.append((s,idx[("N",nz)],nz,1))
        if current+nz<=p2_max: edges.append((s,idx[("N",nz)],nz,2))
        edges.append((s,idx[("N",nz)],nz,3))
    for source,target in t44_pair_links:
        if source==p: edges.append((s,idx[("T",target)],target[1],1))
    for source,target in t44_large_pair_links:
        if source==p: edges.append((s,idx[("L",target)],target[1],1))

# Test/prove SCALE*Z <= COEFF*K + B by an exact integer potential.
SCALE=2 if SHORT_MAX%2 else 1
COEFF=SCALE*SHORT_MAX//2
pot=[0]*len(states)
pred=[None]*len(states); last=None
for iteration in range(len(states)+1):
    changed=False
    for s,t,z,k in edges:
        w=SCALE*z-COEFF*k
        if pot[s]+w>pot[t]: pot[t]=pot[s]+w; pred[t]=(s,z,k); last=t; changed=True
    if not changed: break
else:
    v=last
    for _ in states: v=pred[v][0]
    cycle=[]; seen={}
    while v not in seen:
        seen[v]=len(cycle); s,z,k=pred[v]; cycle.append((s,v,z,k)); v=s
    cycle=cycle[seen[v]:]
    print("positive_cycle",[(states[s],states[t],z,k) for s,t,z,k in reversed(cycle)])
    print("cycle_ratio",sum(z for _,_,z,_ in cycle),sum(k for _,_,_,k in cycle))
    raise SystemExit(2)
assert all(pot[s]+SCALE*z-COEFF*k<=pot[t] for s,t,z,k in edges)
b2=max(SCALE*z-pot[idx[("N",z)]] for z in range(1,50))+max(pot)
print("graph_states_edges",len(states),len(edges))
assert len(states)==323 and len(edges)==26514
print("potential_iterations",iteration+1,"range",min(pot),max(pot),"boundary2",b2)
assert iteration+1==2 and min(pot)==0 and max(pot)==53 and b2==129
print("density",f"{SCALE}Z <= {COEFF}K + {b2}")

# Inherited RL329 residue-weighted consumer at rho=60.
RHO=60; T=ELL-RHO; LAM=1+Fraction(1,1<<40)
num=SCALE*(T+1)-b2; den=SCALE+COEFF
K=(num+den-1)//den
assert K==6_112_357_564
x=l2lo/ELL
full=1/(2*(x+x*x/2))-Fraction(1,2)
omitted=sum((Fraction(1<<((A*r)//ELL),3**r) for r in range(1,RHO)),Fraction(0))/LAM
ideal=(full-omitted)/3
s1=K*(K+1)//2; s2=K*(K+1)*(2*K+1)//6; s3=s1*s1
s4=K*(K+1)*(2*K+1)*(3*K*K+3*K-1)//30
weighted=Fraction(K)+l2lo*s1/ELL+l2lo*l2lo*s2/(2*ELL*ELL)+l2lo**3*s3/(6*ELL**3)+l2lo**4*s4/(24*ELL**4)
rhs=1+ideal-weighted/(12*LAM)
print("positive_excess_min",K)
print("carry_rhs",float(rhs),"floor",rhs.numerator//rhs.denominator)
assert CAP<rhs<H
rho59=Fraction(5,6)+LAM*(1<<((D*59)//ELL))
assert rho59<CAP
max_x=l2lo*K/ELL
max_weight=1+max_x+max_x**2/2+max_x**3/6+max_x**4/24
assert max_weight<2 and max_weight/(12*LAM)<Fraction(1,6*LAM)
print("RL330_TOTAL44_OWNERSHIP_VERIFIER_GREEN")
print("new_carry_cap",CAP)
