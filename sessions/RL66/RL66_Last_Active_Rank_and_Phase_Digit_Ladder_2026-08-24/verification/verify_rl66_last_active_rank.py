#!/usr/bin/env python3
from itertools import product

def is_power_of_two(n): return n > 0 and (n & (n-1)) == 0

def v3(n):
    c=0
    while n and n%3==0:
        n//=3; c+=1
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

def reverse_sync(k,w):
    J=1<<k
    for bit in reversed(w):
        if bit==0:
            J=2*J-1
        else:
            z=2*J-1
            if z%3: return None
            J=z//3
        if J<=0 or J%2==0: return None
    return J

def terminal_replay_Js(xw,yw):
    d,T,H=1,-14,0
    after=[]
    for x,y in zip(xw,yw):
        out=rl_step(d,T,H,x,y); assert out is not None
        d,T,H=out
        after.append((d,T,J_of(d,T),H))
    return after

terminal=last_rank=valuation=lifted=nextdigit=ladder=gapselector=even_absence=all00=all11=0
states=[(1,-14,0,(),())]
MAX_M=17
seen_terminal_even=[]
for m in range(MAX_M+1):
    for d,T,H,xw,yw in states:
        J=J_of(d,T)
        if d!=1 or not is_power_of_two(J) or J<8 or T!=J-1:
            continue
        terminal+=1
        k=J.bit_length()-1
        assert k%2==1, (m,k,H,xw,yw)
        if k%2==0: seen_terminal_even.append((m,k,H))
        aa,bb,delta,Qx,Qy,D=rank_data(xw,yw)
        assert H==sum(delta)
        pos=[j for j,z in enumerate(delta) if z>0]
        assert pos, 'canonical terminal path cannot be mismatch-free'
        jstar=pos[-1]; ds=delta[jstar]
        a=aa[jstar]; b=bb[jstar]
        replay=terminal_replay_Js(xw,yw)
        # After b_j* there are no further y-ones through a_j*, and after a_j* all columns synchronize.
        assert all(y==0 for y in yw[b+1:a+1])
        assert all(x==y for x,y in zip(xw[a+1:],yw[a+1:]))
        assert xw[a]==1 and yw[a]==0
        Jtail=replay[a][2]
        assert Jtail%3 == (1+pow(2,ds,3))%3
        assert Jtail%3 in (0,2)
        last_rank+=1
        # The maximal synchronized tail begins exactly after a_j*.
        wtail,s=max_sync_suffix(xw,yw)
        n=len(wtail); r=len(aa)
        assert a==m-n-1
        assert s==r-(jstar+1)
        assert b==m-n-1-ds
        assert D%(3**s)==0
        Dstar=D//(3**s)
        last_term=(1<<b)*((1<<ds)-1)
        assert Dstar%3==last_term%3
        if ds%2:
            assert Dstar%3!=0
            assert v3(D)==s
        else:
            assert Dstar%3==0
            assert v3(D)>=s+1
        valuation+=1
        # Rational full-phase residue audit; if full divisibility holds this is integer N.
        r=sum(xw); a_full=m+k+1; ell=r+3
        M=(1<<a_full)-3**ell
        if M>0:
            v=(1,1,1)+yw+(0,)*(k-2)
            V=qpoly(v); Y=3**ell
            mod=3**(s+1)
            target=(2-pow(2,1-k,mod))%mod
            Nres=((V+4*Y)%mod)*pow(M,-1,mod)%mod
            assert Nres==target
            mod2=3**(s+2)
            base2=(2-pow(2,1-k,mod2))%mod2
            Nres2=((V+4*Y)%mod2)*pow(M,-1,mod2)%mod2
            eps=ds&1
            target2=(base2-eps*pow(2,n,3)*3**(s+1))%mod2
            assert Nres2==target2
            nextdigit+=1
            if ds%2==0:
                assert Nres2==base2
                lifted+=1
            # Exact rank-tail phase-digit ladder, audited for the first four retained ranks.
            Aterms=[(1<<bb[j])*((1<<delta[j])-1) for j in range(len(delta))]
            j1=jstar+1  # one-based last active index; equals r-s
            g=0
            qidx=jstar-1
            while qidx>=0 and delta[qidx]==0:
                g+=1; qidx-=1
            modg=3**(s+g+2)
            gotg=((V+4*Y)%modg)*pow(M,-1,modg)%modg
            corr=(3**(s+1))*pow(2,-(k+n+ds),modg)*((1<<ds)-1)
            wantg=(2-pow(2,1-k,modg)-corr)%modg
            assert gotg==wantg
            gapselector+=1
            for q in range(1,min(j1,4)+1):
                Cq=sum((3**h)*Aterms[jstar-h] for h in range(q))
                modq=3**(s+q+1)
                gotq=((V+4*Y)%modq)*pow(M,-1,modq)%modq
                wantq=(2-pow(2,1-k,modq)-4*3**(s+1)*pow(2,-a_full,modq)*Cq)%modq
                assert gotq==wantq
                ladder+=1
        # Odd-k all-00 tail parity selector.
        if all(bit==0 for bit in wtail):
            assert n%2==ds%2
            if ds%2==0:
                assert v3(D)>=1
            all00+=1
        # All-11 tail refinement.
        if n and all(bit==1 for bit in wtail):
            nu=v3((1<<k)+1)
            assert n<=nu
            q=((1<<k)+1)//(3**n)
            if n<nu:
                assert q%3==0
                assert Jtail%3==2
                assert ds%2==0
                assert v3(D)>=n+1
            else:
                assert q%3!=0
                e=v3(k); m0=k//(3**e)
                # normalized LTE quotient digit
                assert q%3==m0%3
                assert q%3==pow(2,n,3)
                assert ds%2==1
            all11+=1
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

# Independent finite audit of the normalized LTE quotient digit and maximal all-11 selector.
lte=0; maximal_allowed=0; maximal_forbidden=0
for k in range(1,1000,2):
    e=v3(k); nu=e+1
    z=(1<<k)+1
    assert v3(z)==nu
    q=z//(3**nu); m0=k//(3**e)
    assert q%3==m0%3
    if m0%3==pow(2,nu,3): maximal_allowed+=1
    else: maximal_forbidden+=1
    lte+=1

# Independent reverse audit of inherited even-k all-00 synchronized theorem and RL66 contradiction residue.
for k in range(2,42,2):
    for n in range(0,11):
        w=(0,)*n
        J0=reverse_sync(k,w) if n else (1<<k)
        assert J0 is not None
        assert J0==(1<<n)*((1<<k)-1)+1
        assert J0%3==1
        even_absence+=1

print('RL66 last-active-rank verifier: PASS')
print('bounded canonical terminal paths =',terminal)
print('bounded last-active normal-form checks =',last_rank)
print('bounded defect-valuation checks =',valuation)
print('bounded next-digit phase-selector checks =',nextdigit)
print('bounded even-delta lifted-selector checks =',lifted)
print('bounded rank-tail digit-ladder checks =',ladder)
print('bounded last-active zero-gap selector checks =',gapselector)
print('bounded odd-k all-00 tail checks =',all00)
print('bounded all-11 refinement checks =',all11)
print('normalized LTE quotient checks =',lte)
print('maximal all-11 normalized classes allowed =',maximal_allowed)
print('maximal all-11 normalized classes forbidden =',maximal_forbidden)
print('even-k all-00 reverse contradiction checks =',even_absence)
