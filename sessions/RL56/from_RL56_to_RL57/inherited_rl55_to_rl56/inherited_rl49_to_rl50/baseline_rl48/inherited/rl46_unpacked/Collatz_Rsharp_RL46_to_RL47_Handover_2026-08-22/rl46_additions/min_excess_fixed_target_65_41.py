from collections import defaultdict
A=65;ELL=41;P=39;Q=24;X=1<<A;Y=3**ELL
TARGET=(1,31,22,38) # d,T,z,pa preterminal; t=2

def cap_ok(n,pa): return (1<<(n+2))*Y*Y <= (3**(pa+2))*X*X
# layer by n=z+pa, no pump path because structural hit has pump=False
layers={1:{(1,-14,1,0):0}}
parent={}
for n in range(1,61):
    cur=layers.get(n,{})
    if not cur: break
    nxt={}
    for st,e in cur.items():
        d,T,z,pa=st
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd=d+y-x
            if nd<=0:continue
            # omit neutral selfloop: this is the no-pump branch
            if d==1 and T==-2 and x==1 and y==1:continue
            num=3**y*T+x*3**(d+y-1)-y
            if num&1:continue
            if x and not cap_ok(n,pa):continue
            z2=z+1-x;pa2=pa+x
            if z2>Q or pa2>P or pa2+nd>P:continue
            ns=(nd,num//2,z2,pa2)
            ne=e+d-x
            old=nxt.get(ns)
            if old is None or ne<old:
                nxt[ns]=ne; parent[(n+1,ns)]=(n,st,(x,y),e)
    layers[n+1]=nxt
print('layer60 states',len(layers.get(60,{})))
print('target present',TARGET in layers.get(60,{}),'min_e',layers.get(60,{}).get(TARGET))
if TARGET in layers.get(60,{}):
    path=[];key=(60,TARGET)
    while key[0]>1:
        prev=parent[key];pn,pst,edge,pe=prev
        path.append((pn,edge,key[1],layers[key[0]][key[1]]))
        key=(pn,pst)
    path.reverse()
    print('pathlen',len(path))
    print('edges',' '.join(f'{x}{y}' for _,(x,y),_,_ in path))
    for rec in path:
        print(rec)
