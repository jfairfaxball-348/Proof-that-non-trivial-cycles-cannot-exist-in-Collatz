from collections import deque
from math import gcd, log2
from fractions import Fraction

def near(a,l):
    X=1<<a; Y=3**l
    return X>Y and 15*X*X < 16*Y*Y

def Hfrac(a,l):
    X=1<<a;Y=3**l
    return Fraction(12*Y*(X+Y), X*X)

def mmax(p,e):
    # maximize sum (1-2^-delta_i), delta_i>=1 ints, sum(delta_i-1)=e
    q,r=divmod(e,p)
    # r have delta=q+2, p-r delta=q+1
    return (p-r)*Fraction((1<<(q+1))-1,1<<(q+1)) + r*Fraction((1<<(q+2))-1,1<<(q+2))

def ell_candidates(q):
    c=q/log2(1.5)
    lo=max(1,int(c)-10); hi=int(c)+11
    return [l for l in range(lo,hi+1) if near(l+q,l)]

def enumerate_terms(maxe):
    # d,e,T,z,pa,pump
    start=(1,0,-14,1,0,False)
    dq=deque([start]); seen={start}; terms=set()
    while dq:
        d,e,T,z,pa,pump=dq.popleft()
        if d==1 and T==-2 and not pump:
            st=(d,e,T,z,pa,True)
            if st not in seen:seen.add(st);dq.append(st)
        if d==1 and T&1:
            gout=(T+1)//2
            if gout>=4 and gout&(gout-1)==0:
                t=gout.bit_length()-3
                terms.add((e,z,t,z+t,pa+1,pump,gout))
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd=d+y-x
            if nd<=0:continue
            ne=e+d-x
            if ne>maxe:continue
            if d==1 and T==-2 and x==1 and y==1:continue
            num=(3**y)*T+x*3**(d+y-1)-y
            if num&1:continue
            st=(nd,ne,num//2,z+(1-x),pa+x,pump)
            if st not in seen:seen.add(st);dq.append(st)
    return seen,terms

for E in [24,26,28,30,32,34,36,38,40]:
    seen,terms=enumerate_terms(E)
    cand=set()
    for e,z,t,q,p0,pump,gout in terms:
      for l in ell_candidates(q):
        p=l-2
        if p<=0:continue
        if not ((pump and p>=p0) or ((not pump) and p==p0)):continue
        a=l+q
        if gcd(a,l)!=1:continue
        rho=p+e
        if rho<50:continue
        if mmax(p,e) < Hfrac(a,l):continue
        cand.add((e,rho,a,l,q,z,t,p0,pump,gout,mmax(p,e),Hfrac(a,l)))
    cs=sorted(cand,key=lambda x:(x[0],x[1],x[2],x[5],x[7]))
    print('E',E,'states',len(seen),'terms',len(terms),'SURV',len(cs))
    for x in cs[:12]:
        print(' ',x[:10],'Mmax',float(x[10]),'H',float(x[11]))
    if cs:
        break
