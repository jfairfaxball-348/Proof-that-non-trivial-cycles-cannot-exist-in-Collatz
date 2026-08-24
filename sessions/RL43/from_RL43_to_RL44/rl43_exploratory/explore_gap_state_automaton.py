from collections import deque, defaultdict

def enumerate_gap(g,maxe=20):
    # initial canonical column alpha=0,beta=1: d=1,e=0, T=3(S-g)/2=-(1+3g)/2
    assert g%2==1
    T0=-(1+3*g)//2
    start=(1,0,T0)
    q=deque([start]); seen={start}; hits=[]; parent={start:None}; edge={}
    while q:
        d,e,T=q.popleft()
        # terminal canonical 10 from d=1
        if d==1 and (T+1)%2==0:
            gout=(T+1)//2
            if gout>0:
                hits.append((e,gout,(d,e,T)))
        for x,y,name in [(0,0,'00'),(1,1,'11'),(0,1,'01'),(1,0,'10')]:
            nd=d+y-x
            if nd<=0: continue # terminal handled separately
            ne=e+d-x
            if ne>maxe: continue
            num=(3**y)*T + (x*(3**(d+y-1))) - y
            if num%2: continue
            Tn=num//2
            st=(nd,ne,Tn)
            if st not in seen:
                seen.add(st); parent[st]=(d,e,T); edge[st]=name; q.append(st)
    # recover sample path
    out=[]
    for e,gout,st in sorted(hits):
        path=[]; cur=st
        while parent[cur] is not None:
            path.append(edge[cur]); cur=parent[cur]
        path.reverse(); path.append('10(term)')
        out.append((e,gout,path,st))
    return seen,out

for g in [1,3,5,7,9,11,13,15]:
    seen,hits=enumerate_gap(g,12)
    print('g',g,'states',len(seen),'minhit',hits[0][:2] if hits else None)
    if hits and g==9:
        for h in hits[:10]:print(' ',h)
