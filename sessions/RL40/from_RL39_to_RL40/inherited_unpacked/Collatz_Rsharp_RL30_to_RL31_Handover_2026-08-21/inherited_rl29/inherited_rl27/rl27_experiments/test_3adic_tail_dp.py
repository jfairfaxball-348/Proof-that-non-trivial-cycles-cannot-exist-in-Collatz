from collections import defaultdict

# Explore tail valuation pairs satisfying E_h == 8 mod 3^h at every h.
# First tail valuations have endpoint ownership classes.

def invpow2(s,mod):
    return pow(pow(2,s,mod),-1,mod)

nodes={(0,0,0): ()} # (Su,Sv,total?) actually just cumulative sums; store seq pair
for h in range(1,13):
    mod=3**h
    new={}
    for (Su,Sv,_),seq in nodes.items():
        if h==1:
            us=[2,6,8,12,14,18]
            vs=[3,5,9,11,15,17]
        else:
            us=range(1,10)
            vs=range(1,10)
        # keep combined average <=4.5 per level to contain state growth
        for u in us:
          U=Su+u
          for v in vs:
            V=Sv+v
            if U+V > int(4.5*h+12):
                continue
            # compute E_h directly using seq cumulative + new
            # build cumulative arrays from stored valuations
            useq=seq[0]+(u,) if seq else (u,)
            vseq=seq[1]+(v,) if seq else (v,)
            cu=cv=0; E=0
            for i,(uu,vv) in enumerate(zip(useq,vseq),start=1):
                cu+=uu; cv+=vv
                E += 3**(i-1)*(invpow2(cu,mod)-invpow2(cv,mod))
            if (E-8)%mod: continue
            key=(U,V,U+V)
            if key not in new:
                new[key]=(useq,vseq)
    nodes=new
    if not nodes:
        print('dead at',h); break
    best=min(nodes.items(), key=lambda kv: kv[0][2])
    totals=[k[2] for k in nodes]
    print('h',h,'nodes',len(nodes),'min total',min(totals),'avg',min(totals)/h,'best sums',best[0][:2],'seq',best[1])
