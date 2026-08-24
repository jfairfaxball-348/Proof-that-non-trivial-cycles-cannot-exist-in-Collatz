from collections import defaultdict

def backward_layers(E,h=63,target=(1,None,7,24,38)):
    # target tuple d,e,T,z,pa at n=h-1 preterminal
    targ=(target[0],E,target[2],target[3],target[4])
    layers={h-1:{targ}}
    cur={targ}
    for n in range(h-1,1,-1):  # current at n, predecessor n-1 down to1
        prev=set()
        for dd,ee,Tp,zz,paa in cur:
            for x,y in ((0,0),(1,1),(0,1),(1,0)):
                d=dd-y+x
                if d<=0: continue
                e=ee-d+x
                if e<0: continue
                z=zz-1+x
                pa=paa-x
                if z<0 or pa<0: continue
                num=2*Tp - x*3**(d+y-1) + y
                den=3**y
                if num%den: continue
                T=num//den
                # forward parity/internals
                if d+y-x != dd or e+d-x != ee: raise AssertionError
                prev.add((d,e,T,z,pa))
        layers[n-1]=prev
        cur=prev
    return layers

def phase_residues(E):
    h=63;a=65;l=41;M=(1<<a)-3**l
    backs=backward_layers(E,h)
    start=(1,0,-14,1,0)
    if start not in backs[1]: return 0,False,[],[len(backs[n]) for n in range(1,h)]
    initV=(3**40 + 2*3**39 + (1<<2)*3**38)%M
    dp={start:{initV}}
    for n in range(1,h-1):
        ndp=defaultdict(set)
        allowed=backs[n+1]
        for (d,e,T,z,pa), vals in dp.items():
            pb=pa+d
            for x,y in ((0,0),(1,1),(0,1),(1,0)):
                dd=d+y-x
                if dd<=0:continue
                ee=e+d-x
                if ee>E:continue
                num=(3**y)*T+x*3**(d+y-1)-y
                if num&1:continue
                zz=z+1-x; paa=pa+x; pbb=pb+y
                key=(dd,ee,num//2,zz,paa)
                if key not in allowed:continue
                add=0
                if y:
                    if not (1 <= pbb <=39):continue
                    add=((1<<(2+n))*3**(39-pbb))%M
                if add:ndp[key].update((v+add)%M for v in vals)
                else:ndp[key].update(vals)
        dp=ndp
    target=(1,E,7,24,38)
    vals=dp.get(target,set());need=(-4*3**41)%M
    return len(vals), need in vals, sorted(vals), [len(backs[n]) for n in range(1,h)]

if __name__=='__main__':
  import sys,time
  for E in map(int,sys.argv[1:] or [26,27]):
    t=time.time(); n,hit,vals,counts=phase_residues(E)
    print('E',E,'residues',n,'hit',hit,'time',time.time()-t)
    print('back layer max',max(counts),'sum',sum(counts),'first',counts[:5],'last',counts[-5:])
    if n<=30:print(vals)
