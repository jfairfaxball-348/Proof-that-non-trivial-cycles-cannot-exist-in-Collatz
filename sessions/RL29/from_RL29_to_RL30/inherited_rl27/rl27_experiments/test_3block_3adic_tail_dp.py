# Exact 3-adic tail constraints for U,V,W in G=12,H=4 geometry.
# F_X(m)=sum_{h=1}^m 3^(h-1) 2^{-S_X(h)} mod 3^m.
# Need F_U-F_W=12, F_V-F_W=4 (mod 3^m).
# Endpoint ownership: u1=2 mod6 or 0 mod6; v1=3 or5 mod6; w1=2 exactly.

def invpow2(s,m):
    mod=3**m
    return pow(pow(2,s,mod),-1,mod)

def F(seq,m):
    mod=3**m
    s=0; z=0
    for h,v in enumerate(seq,1):
        s+=v
        z += 3**(h-1)*invpow2(s,m)
    return z%mod

# state keyed by cumulative sums triple, keep one sequence witness.
nodes={(0,0,0):((),(),())}
for h in range(1,16):
    mod=3**h
    new={}
    for (su,sv,sw),seqs in nodes.items():
        if h==1:
            us=[2,6,8,12,14]
            vs=[3,5,9,11,15]
            ws=[2]
        else:
            us=range(1,9); vs=range(1,9); ws=range(1,9)
        for u in us:
          U=su+u
          for v in vs:
            V=sv+v
            for w in ws:
              W=sw+w
              # only retain totals in plausible vicinity so state space stays finite
              if U+V+W > int(6.2*h+15):
                  continue
              useq=seqs[0]+(u,); vseq=seqs[1]+(v,); wseq=seqs[2]+(w,)
              fu=F(useq,h); fv=F(vseq,h); fw=F(wseq,h)
              if (fu-fw-12)%mod or (fv-fw-4)%mod:
                  continue
              key=(U,V,W)
              if key not in new:
                  new[key]=(useq,vseq,wseq)
    nodes=new
    if not nodes:
        print('DEAD',h); break
    best=min(nodes.items(), key=lambda kv: sum(kv[0]))
    s=sum(best[0])
    print('h',h,'nodes',len(nodes),'minsum',s,'avg',s/h,'sums',best[0],'seqs',best[1])
