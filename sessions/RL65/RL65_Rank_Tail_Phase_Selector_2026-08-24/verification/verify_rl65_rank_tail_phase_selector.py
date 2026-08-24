#!/usr/bin/env python3
from itertools import product

def is_power_of_two(n): return n > 0 and (n & (n-1)) == 0

def v3(n):
    c=0
    while n and n%3==0: n//=3; c+=1
    return c

def J_of(d,T): return T + 3**d - 2**d

def rl_step(d,T,H,x,y):
    num=(3**y)*T + x*3**(d+y-1) - y
    if num%2: return None
    d2=d+y-x
    if d2<1: return None
    return d2,num//2,H+d-1

def qpoly(w):
    ell=sum(w); rank=0; q=0
    for i,bit in enumerate(w):
        if bit:
            rank+=1; q += (1<<i)*3**(ell-rank)
    return q

def one_positions(w): return [i for i,b in enumerate(w) if b]

def rank_data(xw,yw):
    aa=one_positions(xw); bb=one_positions(yw); assert len(aa)==len(bb)
    delta=[a-b for a,b in zip(aa,bb)]; r=len(aa)
    Qx=sum((1<<a)*3**(r-j) for j,a in enumerate(aa,1))
    Qy=sum((1<<b)*3**(r-j) for j,b in enumerate(bb,1))
    return aa,bb,delta,Qx,Qy,Qx-Qy

def max_sync_suffix(xw,yw):
    n=0
    for x,y in zip(reversed(xw),reversed(yw)):
        if x!=y: break
        n+=1
    w=() if n==0 else xw[-n:]
    return w,sum(w)

def suffix_R(w):
    return sum((1<<q)*3**sum(w[q+1:]) for q,b in enumerate(w) if b)

def reverse_sync(k,w):
    J=1<<k
    for bit in reversed(w):
        if bit==0: J=2*J-1
        else:
            z=2*J-1
            if z%3: return None
            J=z//3
        if J<=0 or J%2==0: return None
    return J

peq=tp=rt=ps=fp=all11=0
states=[(1,-14,0,(),())]
MAX_M=16
for m in range(MAX_M+1):
    for d,T,H,xw,yw in states:
        if d==1:
            _,_,delta,_,_,_=rank_data(xw,yw)
            assert all(z>=0 for z in delta)
            assert H==sum(delta)
            peq+=1
        J=J_of(d,T)
        if d!=1 or not is_power_of_two(J): continue
        k=J.bit_length()-1
        if k<3 or T!=(1<<k)-1: continue
        r=sum(xw); assert r==sum(yw)
        a=m+k+1; ell=r+3; M=(1<<a)-3**ell
        if M<=0: continue
        _,_,delta,Qx,Qy,D=rank_data(xw,yw)
        assert H==sum(delta)
        assert 3*Qx-Qy == 14*3**r + (1<<(a-1)) - (1<<(a-k-1))
        u=(1,1,0)+xw+(1,)+(0,)*(k-3)
        v=(1,1,1)+yw+(0,)*(k-2)
        assert len(u)==len(v)==a and sum(u)==sum(v)==ell
        U,V=qpoly(u),qpoly(v); Y=3**ell
        assert U-V == 4*((1<<a)+Y)
        assert 2*M-(V+4*Y) == 12*D + (1<<(a-k+1)) - 237*3**r
        tp+=1
        w,s=max_sync_suffix(xw,yw)
        if w:
            if s: assert all(z==0 for z in delta[r-s:])
            assert D%(3**s)==0
            rt+=1
            mod=3**(s+1)
            Nres=((V+4*Y)%mod)*pow(M,-1,mod)%mod
            target=(2-pow(2,1-k,mod))%mod
            assert Nres==target
            Rw=suffix_R(w)
            target2=(-4 + pow(2,2-k-len(w),mod)*((1<<len(w))+3*Rw))%mod
            assert Nres==target2
            ps+=1
            n11=0
            for bit in reversed(w):
                if bit!=1: break
                n11+=1
            if n11:
                assert ((1<<k)+1)%(3**n11)==0
                assert k%2==1 and n11<=1+v3(k)
                all11+=1
        if (V+4*Y)%M==0:
            N=(V+4*Y)//M
            assert N>0 and N%8==3
            if w:
                mod=3**(s+1)
                assert N%mod==(2-pow(2,1-k,mod))%mod
            fp+=1
    if m==MAX_M: break
    nxt=[]
    for d,T,H,xw,yw in states:
        J=J_of(d,T); opts=((0,0),(1,1)) if J&1 else ((0,1),(1,0))
        for x,y in opts:
            if (x,y)==(1,0) and d<=1: continue
            out=rl_step(d,T,H,x,y)
            if out is None: continue
            d2,T2,H2=out
            nxt.append((d2,T2,H2,xw+(x,),yw+(y,)))
    states=nxt

# Historical RL47 long terminal witness at (a,ell,t)=(65,41,2).
EDGES='''11 11 01 11 11 10 01 01 11 11 00 11 11 01 10 01 11 10 01 10 11 10 01 11 10 01 01 10 11 00 11 11 00 10 01 11 11 01 11 10 01 11 10 11 01 00 10 10 01 10 11 00 10 01 11 11 01 10 10'''.split()
xw=tuple(int(e[0]) for e in EDGES); yw=tuple(int(e[1]) for e in EDGES)
d,T,H=1,-14,0
for x,y in zip(xw,yw):
    out=rl_step(d,T,H,x,y); assert out is not None; d,T,H=out
assert (d,T)==(1,31)
a,ell,k=65,41,5
_,_,delta,Qx,Qy,D=rank_data(xw,yw); assert H==sum(delta)==104
r=ell-3
assert 3*Qx-Qy==14*3**r+(1<<(a-1))-(1<<(a-k-1))
v=(1,1,1)+yw+(0,)*(k-2); M=(1<<a)-3**ell; V=qpoly(v)
assert 2*M-(V+4*3**ell)==12*D+(1<<(a-k+1))-237*3**r
hist=1

# Independent reverse audit of the even-k terminal synchronized theorem.
rev=0
for k in range(2,42,2):
    for n in range(1,11):
        legal=[]
        for w in product((0,1),repeat=n):
            z=reverse_sync(k,w)
            if z is not None:
                legal.append(w)
                assert all(b==0 for b in w)
                assert z==(1<<n)*((1<<k)-1)+1
            rev+=1
        assert legal==[(0,)*n]

# Finite CRT audit: the two residue selectors alone always leave one class.
crt=0
for k in range(1,100,2):
    vv=v3((1<<k)+1)
    for n in range(1,vv+1):
        m3=3**(n+1); r3=(2-pow(2,1-k,m3))%m3
        sols=[z for z in range(8*m3) if z%8==3 and z%m3==r3]
        assert len(sols)==1
        crt+=1

print('RL65 rank-tail/phase-selector verifier: PASS')
print('bounded equal-weight legal-path checks =',peq)
print('bounded terminal-power quotient checks =',tp)
print('bounded terminal rank-tail checks =',rt)
print('bounded modular phase-selector checks =',ps)
print('bounded full-phase divisibility hits =',fp)
print('bounded all-11 suffix checks =',all11)
print('historical RL47 long-witness checks =',hist)
print('even-k reverse synchronized-word checks =',rev)
print('CRT compatibility checks =',crt)
