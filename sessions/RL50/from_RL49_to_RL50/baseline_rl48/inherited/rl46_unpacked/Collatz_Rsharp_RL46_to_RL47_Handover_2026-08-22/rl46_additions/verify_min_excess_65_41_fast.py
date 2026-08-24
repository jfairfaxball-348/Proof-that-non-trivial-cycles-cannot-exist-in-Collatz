A=65; ELL=41; P=39; Q=24; X=1<<A; Y=3**ELL
TARGET=(1,31,22,38)

def cap_ok(n,pa):
    return (1<<(n+2))*Y*Y <= (3**(pa+2))*X*X

cur={(1,-14,1,0):0}
for n in range(1,60):
    nxt={}
    for (d,T,z,pa),e in cur.items():
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd=d+y-x
            if nd<=0: continue
            if d==1 and T==-2 and x==1 and y==1: continue
            num=3**y*T+x*3**(d+y-1)-y
            if num&1: continue
            if x and not cap_ok(n,pa): continue
            z2=z+1-x; pa2=pa+x
            if z2>Q or pa2>P or pa2+nd>P: continue
            ns=(nd,num//2,z2,pa2)
            ne=e+d-x
            old=nxt.get(ns)
            if old is None or ne<old:
                nxt[ns]=ne
    cur=nxt
v=cur.get(TARGET)
print('target present', v is not None, 'min_e', v)
assert v == 125
print('RL46 fast minimum-excess verifier: PASS')
