#!/usr/bin/env python3
from collections import Counter
from math import gcd

CANON={(0,1,2,3,4):'antipodal',(0,1,2,5,6):'long',(0,1,2,6,7):'short',(0,1,4,7,8):'interlaced'}
FAMS={
'antipodal':(0,1,2,3,4),
'long':(0,1,2,5,6),
'short':(0,1,2,6,7),
'interlaced':(0,1,4,7,8),
}
EXPECTED=Counter({'antipodal':3522,'interlaced':718,'short':204,'long':54})

def rotate(x,k):return x[k:]+x[:k]

def Q(bits):
    L=sum(bits);out=0;r=0
    for i,b in enumerate(bits):
        if b:
            r+=1;out+=(1<<i)*3**(L-r)
    return out

def optimal_flow(bits,m):
    y=rotate(bits,m);pref=[];s=0
    for a,b in zip(bits,y):s+=a-b;pref.append(s)
    med=sorted(pref)[(len(pref)-1)//2]
    return [v-med for v in pref]

def components(g):
    zeros=[i for i,v in enumerate(g) if v==0]
    if not zeros:return [g]
    k=zeros[0];z=rotate(g,k);out=[];cur=[]
    for v in z:
        if v==0:
            if cur:out.append(cur);cur=[]
        else:cur.append(v)
    if cur:out.append(cur)
    return out

def edge_formula(x,m):
    y=rotate(x,m);pref=[];s=0
    for a,b in zip(x,y):s+=a-b;pref.append(s)
    L=sum(x);R=0;E=0
    for i,(b,g) in enumerate(zip(x,pref)):
        R+=b
        if g==1:E+=(1<<i)*3**(L-R)
        elif g==-1:E-=(1<<i)*3**(L-R-1)
        else:assert g==0
    return E,pref

def classify_rotated(x,m,g):
    A=len(x);L=sum(x)
    assert g[0]==1 and g[-1]==0
    H=[g[(t*m)%A] for t in range(A)]
    X=[x[(t*m)%A] for t in range(A)]
    F=[sum(H[(t+j)%A] for j in range(L)) for t in range(A)]
    assert X==F and all(v in (0,1) for v in F)
    delta=[H[t]-H[(t+L)%A] for t in range(A)]
    B=[t for t,v in enumerate(delta) if v]
    assert len(B)==10 and B[0]==0
    assert all(delta[B[j]]==(1 if j%2==0 else -1) for j in range(10))
    S=tuple(j for j,t in enumerate(B) if H[t]!=0)
    r=[(B[(j+1)%10]-B[j])%A for j in range(10)]
    assert all(v>0 for v in r) and sum(r)==A
    for e in range(0,10,2):
        S2=tuple(sorted((j-e)%10 for j in S))
        if S2 in CANON:
            assert e in S
            return CANON[S2],r[e:]+r[:e]
    raise AssertionError(('unclassified',S))

def poly_residue(A,L,m,q,name,r):
    D=(1<<A)-3**L
    z=pow(2,m,D)*pow(pow(3,q,D),-1,D)%D
    b=[0]
    for j in range(9):b.append(b[-1]+r[j])
    S=FAMS[name];P=0;prefH=0
    for s in S:
        h=1 if s%2==0 else -1
        c=3**(prefH+1) if h==1 else -(3**prefH)
        P=(P+c*pow(z,b[s],D))%D
        prefH+=h
    assert prefH==1
    return P

def check_plus(bits,m,g):
    A=len(bits);L=sum(bits);D=(1<<A)-3**L
    i0=next(i for i,v in enumerate(g) if v==1)
    x=rotate(bits,i0);gr=rotate(g,i0)
    name,r=classify_rotated(x,m,gr)
    q=(m*L+1)//A
    assert q*A-m*L==1
    E,pref=edge_formula(x,m)
    assert pref==gr
    assert (E%D==0)==(poly_residue(A,L,m,q,name,r)%D==0)
    return name,E

def main():
    raw=kp=km=full=proper=detbad=0
    plusfam=Counter();negfam=Counter();pluspoly=negmap=negpoly=0
    for A in range(1,19):
      for mask in range(1<<A):
        bits=[(mask>>i)&1 for i in range(A)];L=sum(bits);D=(1<<A)-3**L
        if D<=1:continue
        q0=Q(bits)
        for m in range(1,A):
          g=optimal_flow(bits,m)
          if sum(abs(v) for v in g)!=5 or max(abs(v) for v in g)>1:continue
          if sorted((len(r) for r in components(g)),reverse=True)!=[1,1,1,1,1]:continue
          k=sum(g)
          if abs(k)!=1:continue
          raw+=1
          direct=Q(rotate(bits,m))-q0
          if direct%D==0:full+=1
          elif gcd(abs(direct),D)>1:proper+=1
          if (m*L+k)%A:detbad+=1
          if k==1:
            kp+=1
            name,E=check_plus(bits,m,g);plusfam[name]+=1
            if (E%D==0)!=(direct%D==0):pluspoly+=1
          else:
            km+=1
            y=rotate(bits,m);mp=A-m;gp=optimal_flow(y,mp)
            if sum(gp)!=1 or sorted((len(r) for r in components(gp)),reverse=True)!=[1,1,1,1,1]:
                negmap+=1;continue
            if Q(rotate(y,mp))-Q(y)!=-direct:negmap+=1
            name,E=check_plus(y,mp,gp);negfam[name]+=1
            if (E%D==0)!=((-direct)%D==0):negpoly+=1
    assert raw==8996 and kp==km==4498
    assert full==0 and proper==714 and detbad==0
    assert plusfam==EXPECTED and negfam==EXPECTED
    assert pluspoly==negmap==negpoly==0
    A,L=11,7;D=(1<<A)-3**L;assert D==-139 and 18904>0
    print('RL270 independent small replay: PASS')
    print('abs_kappa1 =',raw,'orientation =',kp,km)
    print('family_split_plus =',dict(plusfam))
    print('family_split_minus =',dict(negfam))
    print('full_D_hits =',full,'proper_factor_only =',proper)
    print('determinant_mismatches =',detbad,'orientation_mismatches =',negmap)
    print('sparse_polynomial_mismatches =',pluspoly+negpoly)
    print('negative_D_sentinel =',D)
    print('RL270_REDTEAM_PASS')
if __name__=='__main__':main()
