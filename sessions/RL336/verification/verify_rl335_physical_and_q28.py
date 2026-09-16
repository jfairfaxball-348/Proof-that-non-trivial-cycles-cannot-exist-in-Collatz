#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from collections import Counter
A=217_976_794_617; ELL=137_528_045_312; D=A-ELL
LOW=1<<71; UP=(1<<76)+(1<<36)
BOOT=32_546_289_531; CAP=BOOT-1; HC=20_390_252_058; ZMAX=37

def log_interval_atanh(x,terms=280):
    x2=x*x; term=x; total=Fraction(0)
    for j in range(terms): total += term/(2*j+1); term*=x2
    lo=2*total; return lo,lo+2*term/(2*terms+1)/(1-x2)
l2lo,l2hi=log_interval_atanh(Fraction(1,3)); l3lo,l3hi=log_interval_atanh(Fraction(1,2))
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
    return tuple(out)
def residue(gaps):
    c=0
    for j,g in enumerate(gaps): c=(1<<g)*c+3**j
    m=3**len(gaps); return c*pow(1<<sum(gaps),-1,m)%m,m
def reconstruct(x,gaps):
    st=[x]
    for g in gaps:
        y=(1<<g)*x-1
        if y%3:return None
        x=y//3
        if not(x&1):return None
        st.append(x)
    return tuple(st)
def realizations(gaps):
    r,m=residue(gaps); x=r+max(0,(LOW-r+m-1)//m)*m
    while x<UP:
        if x&1:
            st=reconstruct(x,gaps)
            if st: yield x,st
        x+=m
def escape_steps(x,limit=1000):
    for s in range(limit+1):
        if x<LOW:return s
        y=3*x+1; y//= y & -y; x=y
    raise AssertionError('no escape')
def profiles(p):
    out=[]
    def rec(pref):
        i=len(pref)
        if i==p-1:
            q=tuple(pref+[1])
            if all(q[j] <= q[j+1]+1 for j in range(p-1)): out.append(q)
            return
        for v in range(1,p-i+1): rec(pref+[v])
    rec([])
    return tuple(q for q in out if q[-1]==1 and all(q[i]>=1 and q[i]<=q[i+1]+1 for i in range(p-1)))
assert [len(profiles(p)) for p in range(1,5)]==[1,2,5,14]
def templates(pair,p):
    left,right=pair; ps=profiles(p); out=[]
    for base in factors(left+right+p-1):
        for q in ps:
            qq=(0,)+q+(0,); g=list(base); ok=True
            for off in range(p+1):
                pos=left-1+off; g[pos]+=qq[off+1]-qq[off]
                if g[pos]<1:ok=False; break
            if ok: out.append(tuple(g))
    return out
def scan_singletons():
    ct=Counter(); pairs=set(); maxesc=0; rows=0
    for l in range(7,38):
       r=44-l
       for g in templates((l,r),1):
        for x,st in realizations(g):
         if delta_up*min(st)>=BOOT:
          rows+=1;pairs.add((l,r));ct[44]+=1; maxesc=max(maxesc,escape_steps(x))
    assert (rows,len(pairs),maxesc)==(9836,31,185)
    rows=0; ct=Counter(); pairs=set(); maxesc=0
    for total in range(45,52):
      for l in range(max(1,total-ZMAX),min(ZMAX,total-1)+1):
       r=total-l
       for g in templates((l,r),1):
        for x,st in realizations(g):
         if delta_up*min(st)>=BOOT:
          rows+=1;pairs.add((l,r));ct[total]+=1;maxesc=max(maxesc,escape_steps(x))
    assert rows==4764 and len(pairs)==141 and ct==Counter({45:3236,46:1058,47:337,48:97,49:26,50:8,51:2}) and maxesc==184
def scan_p(p, expected_rows, expected_pairs, expected_ct, expected_esc):
    rows=0;pairs=set();ct=Counter();maxesc=0;tmpl=0;n3737=None
    for total in range(44,75):
      for l in range(max(1,total-ZMAX),min(ZMAX,total-1)+1):
       r=total-l;ts=templates((l,r),p);tmpl+=len(ts)
       if (l,r)==(37,37):n3737=len(ts)
       for g in ts:
        for x,st in realizations(g):
         if delta_up*min(st)>=HC:
          rows+=1;pairs.add((l,r));ct[total]+=1;maxesc=max(maxesc,escape_steps(x))
    assert rows==expected_rows and len(pairs)==expected_pairs and ct==Counter(expected_ct) and maxesc==expected_esc
    return tmpl,n3737
scan_singletons()
scan_p(2,11682,176,{44:7864,45:2561,46:841,47:284,48:94,49:30,50:7,51:1},151)
scan_p(3,7030,165,{44:4730,45:1544,46:511,47:165,48:53,49:19,50:6,51:2},133)
t4,n3737=scan_p(4,4986,141,{44:3347,45:1119,46:376,47:105,48:35,49:3,50:1},81)
assert t4==79820 and n3737==213
states=list(range(1,38)); edges=[]
for z in states:
 for nz in states:
  if z+nz<=43: edges.append((z,nz,1))
  edges.append((z,nz,5))
assert len(edges)==2242
pot={z:0 for z in states}
for _ in range(40):
 ch=False
 for z,nz,k in edges:
  w=2*nz-43*k
  if pot[z]+w>pot[nz]:pot[nz]=pot[z]+w;ch=True
 if not ch:break
else:raise AssertionError
assert (min(pot.values()),max(pot.values()))==(0,31)
sig=[]
for z,nz,k in edges:
 s=pot[nz]-pot[z]-(2*nz-43*k);assert s>=0;sig.append((z,nz,k,s))
q=28;pi={z:0 for z in states}
for _ in range(40):
 ch=False
 for z,nz,k,s in sig:
  w=q*(k-2*(nz<=21))-s
  if pi[z]+w>pi[nz]:pi[nz]=pi[z]+w;ch=True
 if not ch:break
else:raise AssertionError
assert (min(pi.values()),max(pi.values()))==(0,28)
assert all(pi[z]+q*(k-2*(nz<=21))-s<=pi[nz] for z,nz,k,s in sig)
self37=[x for x in sig if x[:3]==(37,37,5)][0];assert self37[3]==141
assert 28*5-141==-1 and 29*5-141==4
for qq in (28,29,42):assert qq-43<0
print('RL335_PHYSICAL_AND_Q28_GREEN')
print('T',9836,31,185,'L',4764,141,184)
print('P2',11682,176,151,'P3',7030,165,133,'P4',4986,141,81)
print('P4_templates',t4,'P4_37_37_templates',n3737)
print('graph',37,len(edges),'density_range',min(pot.values()),max(pot.values()),'q28_range',min(pi.values()),max(pi.values()))
print('anchor','28(K-2H)-S<=28','q29_residual_N37_self',4)
