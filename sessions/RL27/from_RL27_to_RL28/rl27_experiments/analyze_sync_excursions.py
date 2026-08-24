# enumerate viable residues to depth 24 using earlier tester, inspect aligned prefix-count resynchronizations
exec(open('/mnt/data/RL27_work/test_three_start_lifts.py').read().split('surv=[27]')[0])

def T(n): return (3*n+1)//2 if n&1 else n//2

def info(r,k):
    xs=[r,r+12,r+4]; ps=[0,0,0]; sync=[]
    for j in range(k+1):
        if ps[0]==ps[1]==ps[2]:
            # gap coords G=v-u, H=w-u and Eisenstein norm G^2-GH+H^2
            G=xs[1]-xs[0]; H=xs[2]-xs[0]
            norm=G*G-G*H+H*H
            sync.append((j,ps[0],G,H,norm))
        if j==k: break
        for i in range(3):
            b=xs[i]&1; ps[i]+=b; xs[i]=T(xs[i])
    return sync

surv=[27]
for k in range(6,25):
    old=1<<(k-1); ns=[]
    for r in surv:
        for rr in (r,r+old):
            ok,_=viable(rr,k)
            if ok: ns.append(rr)
    surv=ns
print('survivors',len(surv))
from collections import Counter,defaultdict
cnt=Counter(); examples={}
for r in surv:
    sy=info(r,24)
    key=tuple((j,G,H,norm) for j,p,G,H,norm in sy[1:])
    cnt[key]+=1; examples.setdefault(key,r)
print('sync pattern classes',len(cnt))
for key,n in cnt.most_common(20):
    print('count',n,'r',examples[key],'sync',key[:8])
