from collections import defaultdict
PAIRS=((0,0),(1,1),(0,1),(1,0))

def phase_residues(E,a,l,z_target,t,T_target):
    p=l-2; h=p+z_target; pa_target=p-1
    M=(1<<a)-3**l
    assert a==2+h+t
    def nxt(st,x,y,n):
        d,e,T,z,pa=st;pb=pa+d
        dd=d+y-x
        if dd<=0:return None
        ee=e+d-x
        if ee>E:return None
        num=(3**y)*T+x*3**(d+y-1)-y
        if num&1:return None
        zz=z+1-x; paa=pa+x; pbb=pb+y
        rem=(h-1)-(n+1)
        if zz>z_target or zz+rem<z_target:return None
        if paa>pa_target or paa+rem<pa_target:return None
        if pbb>p or pbb+rem<p:return None
        return (dd,ee,num//2,zz,paa)
    f={1:{(1,0,-14,1,0)}}
    for n in range(1,h-1):
        ns=set()
        for st in f[n]:
            for x,y in PAIRS:
                q=nxt(st,x,y,n)
                if q is not None:ns.add(q)
        f[n+1]=ns
    target=(1,E,T_target,z_target,pa_target)
    if target not in f[h-1]:return 0,False,[],0,0
    g={h-1:{target}}
    for n in range(h-2,0,-1):
        want=g[n+1];cur=set()
        for st in f[n]:
            for x,y in PAIRS:
                if nxt(st,x,y,n) in want:
                    cur.add(st);break
        g[n]=cur
    start=(1,0,-14,1,0)
    if start not in g[1]:return 0,False,[],sum(map(len,f.values())),sum(map(len,g.values()))
    # Full v has common prefix 11, then beta. Common zero suffix contributes nothing.
    initV=(3**(l-1) + 2*3**(l-2) + (1<<2)*3**(p-1))%M
    dp={start:{initV}}
    for n in range(1,h-1):
        ndp=defaultdict(set);allowed=g[n+1]
        for st,vals in dp.items():
            d,e,T,z,pa=st;pb=pa+d
            for x,y in PAIRS:
                q=nxt(st,x,y,n)
                if q not in allowed:continue
                add=0
                if y:
                    pbb=pb+y
                    # local beta rank pbb -> global rank 2+pbb
                    exp=l-(2+pbb)
                    if exp<0:continue
                    add=((1<<(2+n))*3**exp)%M
                if add:ndp[q].update((v+add)%M for v in vals)
                else:ndp[q].update(vals)
        dp=ndp
    vals=dp.get(target,set());need=(-4*3**l)%M
    return len(vals),need in vals,sorted(vals),sum(map(len,f.values())),sum(map(len,g.values()))

if __name__=='__main__':
 import time
 tests=[
 (26,65,41,24,0,7),(27,65,41,24,0,7),(28,65,41,24,0,7),(29,65,41,24,0,7),
 (30,65,41,24,0,7),(30,65,41,22,2,31),(31,65,41,24,0,7),(31,65,41,22,2,31),
 (32,65,41,24,0,7),(32,65,41,22,2,31)]
 for args in tests:
  t0=time.time();n,hit,vals,fs,gs=phase_residues(*args)
  print(args,'res',n,'hit',hit,'f/g',fs,gs,'time',round(time.time()-t0,3))
