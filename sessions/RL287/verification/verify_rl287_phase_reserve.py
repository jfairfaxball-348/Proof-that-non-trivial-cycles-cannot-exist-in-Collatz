#!/usr/bin/env python3
"""RL287 portable regression verifier."""
from fractions import Fraction
RHO=Fraction(2,3)
def k_step(d,K,x):
    if K%2==0:
        return (d,3*K//2) if x else (d,(K+3**d-1)//2)
    if x:
        return None if d<=1 else (d-1,(K-1)//2)
    return d+1,3*(K+3**d)//2
def y_from(d,K,x): return x if K%2==0 else 1-x
def generate_excursions(K0,max_len=12):
    d,K=k_step(1,K0,0); frontier=[(d,K,0,(0,),(1,),Fraction(2,1))]; out=[]
    while frontier:
        d,K,H,xw,yw,q=frontier.pop()
        if len(xw)>1 and d==1:
            out.append((K0,K,H,xw,yw,q)); continue
        if len(xw)>=max_len: continue
        for x in (0,1):
            st=k_step(d,K,x)
            if st is None: continue
            d2,K2=st; y=y_from(d,K,x)
            frontier.append((d2,K2,H+d-1,xw+(x,),yw+(y,),q*Fraction(2,3**x)))
    return out
def zero_ranks(w):
    o=[]; a=0
    for b in w:
        if b:a+=1
        else:o.append(a)
    return o
def W(w):
    c=-6
    for i,b in enumerate(w): c=3*c if b else c+2**i
    return c
def metrics(ex):
    _,_,H,xw,yw,_=ex; u=zero_ranks(xw); v=zero_ranks(yw); hs=[b-a for a,b in zip(u,v)]
    c=[Fraction(2**j,1)*RHO**u[j] for j in range(len(u))]
    S=sum(c,Fraction(0)); D=sum((cj*(1-RHO**hj) for cj,hj in zip(c,hs)),Fraction(0))
    assert sum(hs)==H
    return hs,c,S,D
def replay_x(J0,xw):
    d=1; K=J0+1; ys=[]; H=0
    for x in xw:
        ys.append(y_from(d,K,x)); st=k_step(d,K,x); assert st is not None
        d2,K2=st; H+=d-1; d,K=d2,K2
    return d,K-1,tuple(ys),H
def nu2(n):
    n=abs(n); assert n; s=0
    while n%2==0:s+=1;n//=2
    return s
def boundary_stay_exit(n):
    return (n//2,3*n+2,0) if n%2==0 else ((3*n+1)//2,n+1,1)
def check_excursions():
    checked=one=cyl=0
    for K0 in range(-199,200,2):
      for ex in generate_excursions(K0,12):
        K0,K1,H,xw,yw,q=ex; J0=K0-1; J1=K1-1; hs,c,S,D=metrics(ex); z=len(c); L=len(xw); r=sum(xw)
        CE=W(xw)-W(yw); assert Fraction(CE,1)==3**r*D
        Pin=Fraction(2*J0+3,5); Pout=q*Fraction(2*J1+3,5); dP=Pout-Pin
        assert 5*dP==4*S+2*D+q-1 and dP>=S and dP>=D+q/2
        rhs=sum(c[1:],Fraction(0))/5+Fraction(3,5)*sum((c[j]*RHO**hs[j] for j in range(max(0,z-1))),Fraction(0))
        assert dP-D-q/2==rhs
        if z==1: one+=1; assert dP==S==1
        else: assert dP>S and rhs>0
        d2,J2,ys2,H2=replay_x(J0+2**L,xw); assert d2==1 and ys2==yw and H2==H and J2-J1==3**r
        checked+=1; cyl+=1
    assert checked==13909 and one==199
    return checked,one,cyl
def check_boundary_affine():
    n=0
    for J in range(1,10000,2):
        Q=Fraction(7,11); P=Q*Fraction(2*J+3,5)
        J0=(J+1)//2; Q0=2*Q; assert Q0*Fraction(2*J0+3,5)-P==Q
        J1=(3*J+1)//2; Q1=Fraction(2,3)*Q; assert Q1*Fraction(2*J1+3,5)-P==-Q/Fraction(15,1)
        n+=2
    return n
def check_direct_terminal():
    c=0
    for k in range(3,80,2):
        z=4 if k%6==3 else 2; num=2**(k+z+1)-5*2**z+4; assert num%3==0; Jin=num//3
        assert Jin>0 and Jin%2==0 and Jin%3 in (0,2)
        d,Jout,ys,H=replay_x(Jin,(0,)*z+(1,)); assert d==1 and Jout==2**k and H==z and ys==(1,)+(0,)*z; c+=1
    return c
def find_s(N):
    mod=9**N; x=1
    for s in range(1,2*3**(2*N-1)+1):
        x=(2*x)%mod
        if x==(-5)%mod:return s
    raise AssertionError(N)
def check_boundary_family():
    fam=0
    for N in range(1,6):
        s=find_s(N); u=(2**s+5)//9**N; assert u>0 and u%2==1
        cur=2**(3*N)*u-5; bits=[]; vals=[]
        for _ in range(3*N):
            cur2,ex,b=boundary_stay_exit(cur); bits.append(b); vals.append(nu2(ex)); cur=cur2
        assert tuple(bits)==(1,1,0)*N and max(vals)<=2 and cur==2**s
        seen=set()
        while cur not in seen:
            seen.add(cur); cur2,ex,b=boundary_stay_exit(cur); vals.append(nu2(ex)); cur=cur2
        assert max(vals)==3; fam+=1
    return fam
def main():
    ex,oz,cyl=check_excursions(); b=check_boundary_affine(); dt=check_direct_terminal(); bf=check_boundary_family()
    print('RL287 fast verifier: PASS'); print(f'first_return_excursions={ex}'); print(f'one_zero_excursions={oz}'); print(f'cylinder_isometry_excursions={cyl}'); print(f'boundary_affine_checks={b}'); print(f'direct_terminal_odd_k_cases={dt}'); print(f'boundary_110_beta3_families={bf}'); print('failures=0')
if __name__=='__main__': main()
