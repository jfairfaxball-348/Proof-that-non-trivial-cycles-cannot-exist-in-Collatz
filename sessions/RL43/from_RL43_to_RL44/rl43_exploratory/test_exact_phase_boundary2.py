from collections import defaultdict
PAIRS=((0,0),(1,1),(0,1),(1,0))

def nxt(st,x,y,E,n,h=63):
    d,e,T,z,pa=st; pb=pa+d
    dd=d+y-x
    if dd<=0:return None
    ee=e+d-x
    if ee>E:return None
    num=(3**y)*T+x*3**(d+y-1)-y
    if num&1:return None
    zz=z+1-x; paa=pa+x; pbb=pb+y
    rem=(h-1)-(n+1) # preterminal target n=h-1
    if zz>24 or zz+rem<24:return None
    if paa>38 or paa+rem<38:return None
    if pbb>39 or pbb+rem<39:return None
    return (dd,ee,num//2,zz,paa)

def build_good(E,h=63):
    f={1:{(1,0,-14,1,0)}}
    for n in range(1,h-1):
        ns=set()
        for st in f[n]:
            for x,y in PAIRS:
                q=nxt(st,x,y,E,n,h)
                if q is not None:ns.add(q)
        f[n+1]=ns
    target=(1,E,7,24,38)
    if target not in f[h-1]:return f,{n:set() for n in f}
    g={h-1:{target}}
    for n in range(h-2,0,-1):
        want=g[n+1]; cur=set()
        for st in f[n]:
            for x,y in PAIRS:
                q=nxt(st,x,y,E,n,h)
                if q in want:
                    cur.add(st);break
        g[n]=cur
    return f,g

def phase_residues(E,h=63):
    a=65;l=41;M=(1<<a)-3**l
    f,g=build_good(E,h)
    start=(1,0,-14,1,0); target=(1,E,7,24,38)
    if start not in g.get(1,set()):return 0,False,[],f,g
    initV=(3**40+2*3**39+(1<<2)*3**38)%M
    dp={start:{initV}}
    for n in range(1,h-1):
        ndp=defaultdict(set); allowed=g[n+1]
        for st,vals in dp.items():
            d,e,T,z,pa=st;pb=pa+d
            for x,y in PAIRS:
                q=nxt(st,x,y,E,n,h)
                if q not in allowed:continue
                add=0
                if y:
                    pbb=pb+y
                    add=((1<<(2+n))*3**(39-pbb))%M
                if add:ndp[q].update((v+add)%M for v in vals)
                else:ndp[q].update(vals)
        dp=ndp
    vals=dp.get(target,set());need=(-4*3**41)%M
    return len(vals),need in vals,sorted(vals),f,g

if __name__=='__main__':
 import sys,time
 for E in map(int,sys.argv[1:] or [26,27]):
  t=time.time();n,hit,vals,f,g=phase_residues(E)
  print('E',E,'res',n,'hit',hit,'time',round(time.time()-t,3))
  print('f max/sum',max(map(len,f.values())),sum(map(len,f.values())),'good max/sum',max(map(len,g.values())),sum(map(len,g.values())))
  if n<=100:print(vals)
