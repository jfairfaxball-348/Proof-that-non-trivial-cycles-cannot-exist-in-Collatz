from fractions import Fraction
from collections import defaultdict

def frac_mod_pow2(fr,bits):
    mod=1<<bits
    return (fr.numerator*pow(fr.denominator,-1,mod))%mod

def search(g=9,maxe=8,maxp=1000):
    types=defaultdict(set); nodes=0; maxn=0; maxpa=0; leaves=0
    S=Fraction(-1,3)
    beta_pos=(0,)
    def rec(Qa,Qb,n,d,e,pa,pb,S,beta_pos):
        nonlocal nodes,maxn,maxpa,leaves
        nodes+=1; maxn=max(maxn,n); maxpa=max(maxpa,pa)
        if d==1 and pa+1<=maxp:
            p=pa+1; h=n+1
            St=S+Fraction(1<<n,3**p)
            if frac_mod_pow2(St,h)==g%(1<<h):
                D=(3*Qa+(1<<n))-Qb
                rem=D-3**p*g
                if rem>0 and rem%(1<<h)==0:
                    gout=rem>>h
                    types[e].add((p,h,gout,D))
        extended=False
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd=d+y-x
            if nd<=0: continue
            ne=e+d-x
            np=pa+x; npb=pb+y
            if ne>maxe or np+1>maxp: continue
            Sn=S
            if x: Sn += Fraction(1<<n,3**(pa+1))
            if y: Sn -= Fraction(1<<n,3**(pb+1))
            if frac_mod_pow2(Sn,n+1) != g%(1<<(n+1)): continue
            Qa2=Qa if x==0 else 3*Qa+(1<<n)
            Qb2=Qb if y==0 else 3*Qb+(1<<n)
            bp=beta_pos+((n,) if y else ())
            extended=True
            rec(Qa2,Qb2,n+1,nd,ne,np,npb,Sn,bp)
        if not extended: leaves+=1
    rec(0,1,1,1,0,0,1,S,beta_pos)
    return types,nodes,maxn,maxpa,leaves

for E in range(4,9):
    types,nodes,maxn,maxpa,leaves=search(maxe=E,maxp=1000)
    print('E',E,'nodes',nodes,'maxn',maxn,'maxpa',maxpa,'leaves',leaves)
    for e in sorted(types):
        print(' e',e,'count',len(types[e]),'first',sorted(types[e])[:10], 'last', sorted(types[e])[-3:])
