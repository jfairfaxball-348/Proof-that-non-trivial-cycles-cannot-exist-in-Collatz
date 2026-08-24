CAP=17/30
best=(-1,None)
for Js in range(1,2000000,2):
    J=Js; g=1.0; M=0.0; maxz=0.0
    for step in range(120):
        cb=0 if J%4==1 else 1
        eb=1-cb
        if eb==0:
            Je=(J+1)//2; ge=2*g; Me=M+g; mz=max(maxz,g)
        else:
            Je=(3*J+1)//2; ge=(2/3)*g; Me=M; mz=maxz
        lam_term=1.5/(ge*(Je+2))
        lam_cap=1e300 if mz==0 else CAP/mz
        lam=lam_term if lam_term<lam_cap else lam_cap
        val=lam*Me
        if val>best[0]: best=(val,(Js,step,J,eb,Je,g,ge,M,Me,mz,lam_term,lam_cap,lam))
        # continue
        if cb==0:
            maxz=max(maxz,g); M+=g; g*=2; J=(J+1)//2
        else:
            g*=2/3; J=(3*J+1)//2
        if J<=0 or J%2==0: raise RuntimeError((Js,J,cb))
print('best',best)
