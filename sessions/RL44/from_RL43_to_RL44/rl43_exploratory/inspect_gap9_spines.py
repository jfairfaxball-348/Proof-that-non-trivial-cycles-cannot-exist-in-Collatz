import sys
sys.setrecursionlimit(10000)
from fractions import Fraction

def frac_mod_pow2(fr,bits):
    mod=1<<bits
    return (fr.numerator*pow(fr.denominator,-1,mod))%mod

def comp(path):
    if not path:return ''
    out=[]; cur=path[0]; k=1
    for t in path[1:]:
        if t==cur:k+=1
        else: out.append(f'{cur[0]}{cur[1]}^{k}'); cur=t;k=1
    out.append(f'{cur[0]}{cur[1]}^{k}')
    return ' '.join(out)

def search(g=9,maxe=7,targetpa=40,maxn=60):
    S=Fraction(-1,3)
    hits=[]
    def rec(n,d,e,pa,pb,S,path):
        if pa>=targetpa:
            hits.append((n,d,e,pa,pb,comp(path)))
            return
        if n>=maxn:return
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd=d+y-x
            if nd<=0:continue
            ne=e+d-x
            np=pa+x; npb=pb+y
            if ne>maxe:continue
            Sn=S
            if x:Sn+=Fraction(1<<n,3**(pa+1))
            if y:Sn-=Fraction(1<<n,3**(pb+1))
            if frac_mod_pow2(Sn,n+1)!=g%(1<<(n+1)):continue
            rec(n+1,nd,ne,np,npb,Sn,path+[(x,y)])
    rec(1,1,0,0,1,S,[])
    return hits

for t in (10,20,40):
    H=search(targetpa=t,maxn=t+20)
    print('target',t,'hits',len(H))
    for h in H[:30]:print(h)
