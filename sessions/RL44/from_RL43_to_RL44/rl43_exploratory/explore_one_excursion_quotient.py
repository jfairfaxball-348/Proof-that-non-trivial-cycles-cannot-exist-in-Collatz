from collections import deque, defaultdict
from math import gcd, log2

def near(a,l):
    X=1<<a; Y=3**l
    return X>Y and 15*X*X < 16*Y*Y

def ell_candidates(q):
    # brute around q/log2(3/2); width near resonance tiny
    c=q/log2(1.5)
    lo=max(1,int(c)-10); hi=int(c)+11
    return [l for l in range(lo,hi+1) if near(l+q,l)]

def enumerate_families(maxe):
    # state d,e,T,z,pa,pump ; pump means arbitrary extra common-11 at T=-2,d=1 may be inserted
    T0=-14
    start=(1,0,T0,1,0,False)
    q=deque([start]); seen={start}; terms=[]
    while q:
        d,e,T,z,pa,pump=q.popleft()
        # Mark pumpability at neutral state without consuming a column.
        if d==1 and T==-2 and not pump:
            st=(d,e,T,z,pa,True)
            if st not in seen:
                seen.add(st); q.append(st)
        # terminal 10
        if d==1 and (T+1)%2==0:
            gout=(T+1)//2
            if gout>=4 and gout&(gout-1)==0:
                t=gout.bit_length()-3
                p0=pa+1
                terms.append((e,z,t,z+t,p0,pump,gout,T))
        for x,y,name in ((0,0,'00'),(1,1,'11'),(0,1,'01'),(1,0,'10')):
            nd=d+y-x
            if nd<=0: continue
            ne=e+d-x
            if ne>maxe: continue
            # omit neutral self-loop; pump flag handles arbitrary repetitions
            if d==1 and T==-2 and x==1 and y==1:
                continue
            num=(3**y)*T + x*3**(d+y-1)-y
            if num%2: continue
            Tn=num//2
            zn=z+(1-x)
            pan=pa+x
            st=(nd,ne,Tn,zn,pan,pump)
            if st not in seen:
                seen.add(st);q.append(st)
    return seen,terms

for E in [8,12,16,20,24,30,40,50,60]:
    seen,terms=enumerate_families(E)
    cand=[]
    for e,z,t,q,p0,pump,gout,T in terms:
        for l in ell_candidates(q):
            p=l-2
            if (pump and p>=p0) or ((not pump) and p==p0):
                a=l+q
                if gcd(a,l)==1:
                    cand.append((e,a,l,q,z,t,p0,pump,gout))
    cand=sorted(set(cand))
    print('E',E,'states',len(seen),'terms',len(set(terms)),'cands',len(cand),'first',cand[:10])
    if cand:
        break
