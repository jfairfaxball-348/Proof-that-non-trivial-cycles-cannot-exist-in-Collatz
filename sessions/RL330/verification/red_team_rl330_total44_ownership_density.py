#!/usr/bin/env python3
"""Independent RL330 scratch red team for total-44 ownership and density."""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache

A=217_976_794_617; L=137_528_045_312; D=A-L
LOW=1<<71; HIGH=(1<<76)+(1<<36)
BOOT=32_551_214_632; CAP=BOOT-1; RHO=60; T=L-RHO

def logarithm(x,n=280):
    y=x*x; term=x; partial=Fraction()
    for k in range(n):
        partial+=term/(2*k+1); term*=y
    lo=2*partial
    return lo,lo+2*term/(2*n+1)/(1-y)

log2_lo,log2_hi=logarithm(Fraction(1,3))
log3_lo,log3_hi=logarithm(Fraction(1,2))
delta_hi=A*log2_hi-L*log3_lo
assert delta_hi>0

@lru_cache(None)
def words(n):
    boundaries=sorted({0,L,*(((-D*j)%L) for j in range(n+1))})
    answer=set()
    for lo,hi in zip(boundaries,boundaries[1:]):
        for phase in {lo,min(lo+1,hi-1)}:
            old=(phase+L-1)//L; word=[]
            for j in range(1,n+1):
                new=(phase+D*j+L-1)//L
                word.append(1+new-old); old=new
            answer.add(tuple(word))
    assert len(answer)==n+1
    return tuple(sorted(answer))

def congruence(word):
    c=0
    for j,g in enumerate(word): c=(1<<g)*c+3**j
    modulus=3**len(word)
    return c*pow(1<<sum(word),-1,modulus)%modulus,modulus

def backward(x,word):
    orbit=[x]
    for g in word:
        numerator=(1<<g)*x-1
        if numerator%3: return None
        x=numerator//3
        if x<=0 or not x&1: return None
        orbit.append(x)
    return tuple(orbit)

def band(word):
    r,m=congruence(word)
    x=r+max(0,(LOW-r+m-1)//m)*m
    while x<HIGH:
        if x&1:
            orbit=backward(x,word)
            if orbit is not None: yield orbit
        x+=m

def singleton_rows(first_total,last_total):
    out=[]
    for total in range(first_total,last_total+1):
        for left in range(max(1,total-49),min(49,total-1)+1):
            right=total-left
            for baseline in words(total):
                if baseline[left]!=2: continue
                word=list(baseline); word[left-1]+=1; word[left]-=1
                for orbit in band(tuple(word)):
                    if delta_hi*min(orbit)>=BOOT:
                        out.append((left,right,orbit[0],orbit[left+1]))
    return out

owned=singleton_rows(44,98)
t44=[r for r in owned if r[0]+r[1]==44]
large=[r for r in owned if r[0]+r[1]>=45]
assert len(t44)==13556
assert Counter(l+r for l,r,_,_ in large)=={45:4759,46:1634,47:556,48:173,49:46,50:14,51:6}
t_pairs=sorted({r[:2] for r in t44}); l_pairs=sorted({r[:2] for r in large})
assert len(t_pairs)==43 and len(l_pairs)==231

def physical_links(source,target):
    incoming=defaultdict(list)
    for j,r in enumerate(target): incoming[(r[0],r[2])].append(j)
    return [(i,j) for i,r in enumerate(source) for j in incoming[(r[1],r[3])]]

tt=physical_links(t44,t44); ll=physical_links(large,large)
lt=physical_links(large,t44); tl=physical_links(t44,large)
tt_pairs={(t44[i][:2],t44[j][:2]) for i,j in tt}
ll_pairs={(large[i][:2],large[j][:2]) for i,j in ll}
lt_pairs={(large[i][:2],t44[j][:2]) for i,j in lt}
tl_pairs={(t44[i][:2],large[j][:2]) for i,j in tl}
assert len(tt)==14 and tt_pairs=={((1,43),(43,1)),((2,42),(42,2))}
assert len(ll)==14 and len(ll_pairs)==13
assert len(lt)==7 and lt_pairs=={((2,43),(43,1)),((3,42),(42,2)),((3,43),(43,1)),((4,41),(41,3))}
assert len(tl)==6 and tl_pairs=={((1,43),(43,2)),((2,42),(42,3))}
owned_projected=({(('L',a),('L',b)) for a,b in ll_pairs} |
                 {(('L',a),('T',b)) for a,b in lt_pairs} |
                 {(('T',a),('L',b)) for a,b in tl_pairs} |
                 {(('T',a),('T',b)) for a,b in tt_pairs})
assert len(owned_projected)==21
assert {a for a,_ in owned_projected}.isdisjoint({b for _,b in owned_projected})

@lru_cache(None)
def singleton_templates(pair):
    left,right=pair; out=[]
    for baseline in words(left+right):
        if baseline[left]!=2: continue
        word=list(baseline); word[left-1]+=1; word[left]-=1; word=tuple(word)
        r,m=congruence(word); out.append((r,m,word))
    return tuple(out)

def can_follow(x,pair):
    for r,m,word in singleton_templates(pair):
        if x%m!=r: continue
        orbit=backward(x,word)
        if orbit is not None and delta_hi*min(orbit)>=BOOT: return True
    return False

def exact_short_support(rows):
    grouped=defaultdict(list)
    for row in rows: grouped[row[:2]].append(row)
    support=set()
    for pair,items in grouped.items():
        for nxt in range(1,44-pair[1]):
            if any(can_follow(row[3],(pair[1],nxt)) for row in items):
                support.add((pair,nxt))
    return support

large_short=exact_short_support(large); t44_short=exact_short_support(t44)
assert len(large_short)==282 and len(t44_short)==166

p2=[]
for total in range(45,99):
    for left in range(max(1,total-49),min(49,total-1)+1):
        for baseline in words(total+1):
            for height in (1,2):
                word=list(baseline)
                for offset,change in enumerate((height,1-height,-1)):
                    word[left-1+offset]+=change
                if min(word[left-1:left+2])<1: continue
                for orbit in band(tuple(word)):
                    if delta_hi*min(orbit)>=BOOT: p2.append(total)
p2_counts=Counter(p2)
assert p2_counts=={45:2030,46:707,47:270,48:93,49:34,50:11,51:2}
p2max=max(p2_counts)

states=[('N',z) for z in range(1,50)]+[('L',p) for p in l_pairs]+[('T',p) for p in t_pairs]
index={state:i for i,state in enumerate(states)}
large_by_left=defaultdict(list)
for p in l_pairs: large_by_left[p[0]].append(p)
edges=[]

def common_edges(source,current):
    for nxt in range(1,50):
        if current+nxt<=p2max: edges.append((source,index[('N',nxt)],nxt,2))
        edges.append((source,index[('N',nxt)],nxt,3))

for z in range(1,50):
    source=index[('N',z)]; common_edges(source,z)
    for nxt in range(1,50):
        if z+nxt<=43: edges.append((source,index[('N',nxt)],nxt,1))
    for p in large_by_left[z]: edges.append((source,index[('L',p)],p[1],1))
    for p in t_pairs:
        if p[0]==z: edges.append((source,index[('T',p)],p[1],1))

for p in l_pairs:
    source=index[('L',p)]; current=p[1]; common_edges(source,current)
    for nxt in range(1,44-current):
        if (p,nxt) in large_short: edges.append((source,index[('N',nxt)],nxt,1))
    for q in large_by_left[current]:
        if (p,q) in ll_pairs: edges.append((source,index[('L',q)],q[1],1))
    for a,b in lt_pairs:
        if a==p: edges.append((source,index[('T',b)],b[1],1))

for p in t_pairs:
    source=index[('T',p)]; current=p[1]; common_edges(source,current)
    for nxt in range(1,44-current):
        if (p,nxt) in t44_short: edges.append((source,index[('N',nxt)],nxt,1))
    for a,b in tt_pairs:
        if a==p: edges.append((source,index[('T',b)],b[1],1))
    for a,b in tl_pairs:
        if a==p: edges.append((source,index[('L',b)],b[1],1))

assert len(states)==323 and len(edges)==26514
potential=[0]*len(states)
for iteration in range(len(states)+1):
    changed=False
    for s,t,z,k in edges:
        candidate=potential[s]+2*z-43*k
        if candidate>potential[t]: potential[t]=candidate; changed=True
    if not changed: break
else: raise AssertionError("positive cycle at 43/2")
assert iteration+1==2 and min(potential)==0 and max(potential)==53
assert all(potential[s]+2*z-43*k<=potential[t] for s,t,z,k in edges)
boundary=max(2*z-potential[index[('N',z)]] for z in range(1,50))+max(potential)
assert boundary==129

K=(2*(T+1)-boundary+44)//45
assert K==6_112_357_564
lam=1+Fraction(1,1<<40); x=log2_lo/L
full=1/(2*(x+x*x/2))-Fraction(1,2)
omitted=sum((Fraction(1<<((A*r)//L),3**r) for r in range(1,RHO)),Fraction())/lam
ideal=(full-omitted)/3
s1=K*(K+1)//2; s2=K*(K+1)*(2*K+1)//6; s3=s1*s1
s4=K*(K+1)*(2*K+1)*(3*K*K+3*K-1)//30
weighted=Fraction(K)+log2_lo*s1/L+log2_lo**2*s2/(2*L**2)+log2_lo**3*s3/(6*L**3)+log2_lo**4*s4/(24*L**4)
rhs=1+ideal-weighted/(12*lam)
assert CAP<rhs<BOOT
rho59=Fraction(5,6)+lam*(1<<((D*59)//L))
assert rho59<CAP
max_x=log2_lo*K/L
max_weight=1+max_x+max_x**2/2+max_x**3/6+max_x**4/24
assert max_weight<2 and max_weight/(12*lam)<Fraction(1,6*lam)

print("RL330_TOTAL44_RED_TEAM_GREEN")
print("total44_rows_links",len(t44),len(tt))
print("large_rows_links",len(large),len(ll))
print("cross_links",len(lt),len(tl))
print("owned_singleton_dag_edges_longest",len(owned_projected),1)
print("owned_short_support",len(large_short),len(t44_short))
print("two_positive_counts",dict(sorted(p2_counts.items())))
print("states_edges",len(states),len(edges))
print("density","2Z<=43K+129")
print("positive_excess_min",K)
print("carry_rhs_upper_lt",float(rhs))
print("new_carry_cap",CAP)
