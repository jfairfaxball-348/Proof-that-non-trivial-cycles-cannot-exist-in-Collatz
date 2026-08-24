from collections import deque
from fractions import Fraction

def build(maxe=26):
    start=(1,0,-14,1,0,False)
    dq=deque([start]); seen={start}; par={start:None}; edge={}
    terms=[]
    while dq:
        st=d,e,T,z,pa,pump=dq.popleft()
        if d==1 and T==-2 and not pump:
            ns=(d,e,T,z,pa,True)
            if ns not in seen:
                seen.add(ns);par[ns]=st;edge[ns]='PUMP';dq.append(ns)
        if d==1 and T&1:
            gout=(T+1)//2
            if gout>=4 and gout&(gout-1)==0:
                t=gout.bit_length()-3
                if e==26 and z+t==24 and gout==4:
                    terms.append((st,pa+1,t))
        for x,y,name in ((0,0,'00'),(1,1,'11'),(0,1,'01'),(1,0,'10')):
            nd=d+y-x
            if nd<=0:continue
            ne=e+d-x
            if ne>maxe:continue
            if d==1 and T==-2 and name=='11':continue
            num=(3**y)*T+x*3**(d+y-1)-y
            if num&1:continue
            ns=(nd,ne,num//2,z+(1-x),pa+x,pump)
            if ns not in seen:
                seen.add(ns);par[ns]=st;edge[ns]=name;dq.append(ns)
    return terms,par,edge

def recover(st,par,edge):
    out=[]
    while par[st] is not None:
        out.append(edge[st]);st=par[st]
    return out[::-1]

def score_path(path,loops):
    # initial col 0/1, then path with PUMP marker replaced by loops 11, then terminal 10
    pairs=[(0,1)]
    for s in path:
        if s=='PUMP': pairs += [(1,1)]*loops
        else:pairs.append((int(s[0]),int(s[1])))
    pairs.append((1,0))
    apos=[i for i,(x,y) in enumerate(pairs) if x]
    bpos=[i for i,(x,y) in enumerate(pairs) if y]
    assert len(apos)==len(bpos)
    ds=[a-b for a,b in zip(apos,bpos)]
    assert all(d>=1 for d in ds)
    sc=sum(Fraction((1<<d)-1,1<<d) for d in ds)
    return pairs,ds,sc
terms,par,edge=build()
print('terms',len(terms))
for st,p0,t in sorted(terms,key=lambda q:q[1])[:30]:
    path=recover(st,par,edge)
    loops=39-p0
    if loops<0:continue
    pairs,ds,sc=score_path(path,loops)
    print('p0',p0,'loops',loops,'lenpath',len(path),'M',float(sc),'exact',sc,'deltas',ds)
    print(' path',' '.join(path))
