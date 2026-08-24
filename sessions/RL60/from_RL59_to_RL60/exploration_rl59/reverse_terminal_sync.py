from collections import defaultdict
from math import log2

def search(K, maxdepth=160):
    # represent g = 13.5 * 2^-K * 3^a / 2^b via float for diagnostic
    gend=13.5*(2.0**(-K))
    # state J,g, aligned mass backward accumulated = Psi_end-Psi_cur, max zero weight
    states={(1<<K, 0,0): (0.0,0.0)} # key J,a,b where g=gend*3^a/2^b; vals mass,maxz; a=back11, b=back00
    best=None
    psi_end=gend*((1<<K)+1)/2
    for dep in range(1,maxdepth+1):
        nxt={}
        for (J,a,b),(M,mz) in states.items():
            # inverse 00 always: Jp=2J-1, gp=g/2 => b+1, forward aligned zero gp
            Jp=2*J-1; ap=a; bp=b+1
            gp=gend*(3.0**ap)/(2.0**bp)
            M2=M+gp; mz2=max(mz,gp)
            key=(Jp,ap,bp)
            old=nxt.get(key)
            if old is None or M2>old[0]: nxt[key]=(M2,mz2)
            # inverse 11 if integral
            num=2*J-1
            if num%3==0:
                Jp=num//3; ap=a+1; bp=b
                gp=gend*(3.0**ap)/(2.0**bp)
                key=(Jp,ap,bp)
                old=nxt.get(key)
                if old is None or M>old[0]: nxt[key]=(M,mz)
        states=nxt
        # eligible entry after 10 return: J odd positive, X=Jg <=1.5; all zero weights<17/30
        local=[]
        for (J,a,b),(M,mz) in states.items():
            g=gend*(3.0**a)/(2.0**b)
            X=J*g
            if X<=1.5 and mz<17/30:
                psi=g*(J+1)/2
                local.append((M,psi,J,a,b,g,X,mz))
                if best is None or M>best[0]: best=(M,dep,psi,J,a,b,g,X,mz)
        if dep%10==0 or local:
            print('K',K,'dep',dep,'states',len(states),'eligible',len(local),'best',best)
        if len(states)>2_000_000:
            print('too many');break
    print('FINAL',K,'psi_end',psi_end,'best',best)

for K in [25,27,29,31]:
    search(K,120)
