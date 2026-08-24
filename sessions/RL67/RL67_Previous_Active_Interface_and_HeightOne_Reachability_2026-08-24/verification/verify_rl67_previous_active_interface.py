#!/usr/bin/env python3
from collections import Counter

def is_power_of_two(n): return n > 0 and (n & (n-1)) == 0

def v2(n):
    assert n != 0
    n=abs(n); c=0
    while n%2==0:
        n//=2; c+=1
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
    return aa,bb,delta,r

def max_sync_suffix(xw,yw):
    n=0
    for x,y in zip(reversed(xw),reversed(yw)):
        if x!=y: break
        n+=1
    w=() if n==0 else xw[-n:]
    return w,sum(w)

def replay(xw,yw):
    d,T,H=1,-14,0; out=[]
    for x,y in zip(xw,yw):
        z=rl_step(d,T,H,x,y); assert z is not None
        d,T,H=z; out.append((d,T,J_of(d,T),H))
    return out

def sync_bridge_constant(u):
    # If J_{i+1}=(3^{u_i}J_i+1)/2, then
    # 2^L J_L = 3^g J_0 + B(u).
    L=len(u); B=0
    suffix=0
    # direct formula: sum_i 2^i 3^{sum_{h>i}u_h}
    for i in range(L):
        suffix=sum(u[i+1:])
        B += (1<<i)*3**suffix
    return B

MAX_M=18
states=[(1,-14,0,(),())]
terminal=two_active=terminal_H3=isolated=gap_bridge=gap_prev_digit=phase_prev_digit=0
case_counts=Counter()
for m in range(MAX_M+1):
    for d,T,H,xw,yw in states:
        J=J_of(d,T)
        if d!=1 or not is_power_of_two(J) or J<8 or T!=J-1:
            continue
        terminal+=1
        k=J.bit_length()-1
        aa,bb,delta,r=rank_data(xw,yw)
        pos=[j for j,z in enumerate(delta) if z>0]
        # RL67 theorem: one active rank is impossible.
        assert len(pos)>=2
        two_active+=1
        assert H>=3
        terminal_H3+=1
        js=pos[-1]; p=pos[-2]
        ds=delta[js]; dp=delta[p]
        bstar=bb[js]; astar=aa[js]; ap=aa[p]
        rep=replay(xw,yw)
        R=rep[astar][2]
        wtail,s=max_sync_suffix(xw,yw); n=len(wtail)
        assert R>=3
        g=js-p-1
        assert all(delta[q]==0 for q in range(p+1,js))

        # Interface type of the previous active x-position relative to last y-position.
        if ap < bstar:
            kind='separated'
            # last active rank is isolated: 01, 00^(delta-1), 10 at height 1/2.
            P=rep[bstar-1][2] if bstar else -13
            dpre=rep[bstar-1][0] if bstar else 1
            assert dpre==1
            assert (xw[bstar],yw[bstar])==(0,1)
            assert all((xw[q],yw[q])==(0,0) for q in range(bstar+1,astar))
            assert (xw[astar],yw[astar])==(1,0)
            assert 3*P-4 == (1<<ds)*(2*R-5)
            assert v2(3*P-4)==ds
            assert P>=2
            isolated+=1
            # Between previous active completion and b*, the bridge is synchronized.
            A=rep[ap][2]
            assert rep[ap][0]==1
            u=tuple(xw[ap+1:bstar])
            assert u==tuple(yw[ap+1:bstar])
            L=len(u)
            assert L==bstar-ap-1
            assert sum(u)==g
            B=sync_bridge_constant(u)
            assert (1<<L)*P == 3**g*A + B
            # Since next y-rank occurs only after a_p, previous active exit obeys the same mod-3 selector.
            assert A%3 == (1+pow(2,dp,3))%3
            if g>=1:
                assert A>0
                norm=((1<<L)*P-B)//(3**g)
                assert norm==A
                if dp%2:
                    assert ((1<<L)*P-B)%(3**(g+1))==0
                else:
                    assert ((1<<L)*P-B)%(3**(g+1))==(2*3**g)%(3**(g+1))
                gap_bridge+=1
                gap_prev_digit+=1
            else:
                # g=0 separated bridge is all-00 and A=1+2^L(P-1).
                assert all(z==0 for z in u)
                assert A==1+(1<<L)*(P-1)
        elif ap == bstar:
            kind='cross'
            c=bstar
            C=rep[c-1][2] if c else -13
            dC=rep[c-1][0] if c else 1
            assert dC==2
            assert (xw[c],yw[c])==(1,1)
            assert 3*C-7 == (1<<ds)*(2*R-5)
            assert v2(3*C-7)==ds
            # Previous-rank displacement parity is encoded by C mod 3.
            assert C%3 == (pow(2,dp-1,3)+2)%3
            assert C%3 == (0 if dp%2 else 1)
        else:
            kind='nested'
            lam=ap-bstar
            assert 1<=lam<ds
            C=rep[ap-1][2]
            dC=rep[ap-1][0]
            assert dC==3
            assert (xw[ap],yw[ap])==(1,0)
            assert C-10 == (1<<(ds-lam))*(2*R-5)
            assert v2(C-10)==ds-lam
            assert C%3 == (1+pow(2,lam-1,3))%3
            assert C%3 == (2 if lam%2 else 0)
        case_counts[kind]+=1

        # One additional exact phase digit from the previous active rank.
        # This audits the simplified q=g+2 digit of the RL66 ladder.
        a_full=m+k+1; ell=r+3; M=(1<<a_full)-3**ell
        if M>0:
            v=(1,1,1)+yw+(0,)*(k-2)
            V=qpoly(v); Y=3**ell
            mod=3**(s+g+3)
            Nres=((V+4*Y)%mod)*pow(M,-1,mod)%mod
            lastcorr=(3**(s+1))*pow(2,-(k+n+ds),mod)*((1<<ds)-1)
            prior_digit=0
            if dp%2:
                prior_digit=(4*pow(2,bb[p]-a_full,mod))*3**(s+g+2)
            want=(2-pow(2,1-k,mod)-lastcorr-prior_digit)%mod
            assert Nres==want
            phase_prev_digit+=1

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


# Exact first-mismatch synchronized-prefix cycle and first-isolated-active classification.
def F0(J): return (J+1)//2
def F1(J): return (3*J+1)//2
assert F1(-13)==-19 and F0(-19)==-9 and F1(-9)==-13
assert F0(-13)==-6 and F1(-19)==-28 and F0(-9)==-4
first_even_exits=(-6,-28,-4)
first_isolated=[]
for P0 in first_even_exits:
    dd=v2(3*P0-4)
    Rout=((3*P0-4)//(1<<dd)+5)//2
    first_isolated.append((P0,dd,Rout))
assert first_isolated==[(-6,1,-3),(-28,3,-3),(-4,4,2)]

# Analytic H=2 obstruction is mirrored exactly:
# isolated first rank with delta=1 exits at -3, whose possible synchronized even exits
# are -4 and 0, neither allowing an isolated delta=1 next rank; the overlapping
# delta=1,delta=1 case is the cross block 01,11,10 and stays nonpositive from P<=-4.
assert F0(-3)==-1 and F1(-3)==-4 and F1(-1)==-1 and F0(-1)==0
assert v2(3*(-4)-4)==4 and v2(3*0-4)==2
for P0 in first_even_exits:
    # cross delta1,delta1 output formula; if integral/legal it is certainly nonpositive.
    assert 9*P0+24 < 0

# Independent bounded falsification laboratory for the stronger, UNPROVED height-one reachability inequality.
# Compress by (d,T,H); no word/rank information is used here.
SCAN_DEPTH=22
S={(1,-14,0)}
positive_height1=0
height1_bound_checks=0
max_num=(0,1,None)  # ratio numerator/denominator, witness
for depth in range(SCAN_DEPTH+1):
    for d,T,H in S:
        J=J_of(d,T)
        if d==1 and J>0:
            positive_height1+=1
            assert J <= (1<<H)
            height1_bound_checks+=1
            if J*max_num[1] > max_num[0]*(1<<H):
                max_num=(J,1<<H,(depth,J,H))
    if depth==SCAN_DEPTH: break
    N=set()
    for d,T,H in S:
        J=J_of(d,T); opts=((0,0),(1,1)) if J&1 else ((0,1),(1,0))
        for x,y in opts:
            if (x,y)==(1,0) and d<=1: continue
            z=rl_step(d,T,H,x,y)
            if z is not None: N.add(z)
    S=N

# Explicit abstract macro counterexamples to the naive magnitude-only induction.
# These are legal local height-one synchronized+isolated macros but need not be canonically reachable at low H.
def f0(J): return (J+1)//2
def f1(J): return (3*J+1)//2
A=1; P=f1(A); dd=v2(3*P-4); Rout=((3*P-4)//(1<<dd)+5)//2
assert (A,P,dd,Rout)==(1,2,1,3) and Rout>(1<<dd)*A
A2=7; P2=f1(f1(f1(A2))); dd2=v2(3*P2-4); Rout2=((3*P2-4)//(1<<dd2)+5)//2
assert (A2,P2,dd2,Rout2)==(7,26,1,21) and Rout2>(1<<dd2)*A2

print('RL67 previous-active interface verifier: PASS')
print('bounded canonical terminal paths =',terminal)
print('terminal >=2-active-rank checks =',two_active)
print('terminal H>=3 checks =',terminal_H3)
print('first synchronized-prefix exits =',first_even_exits)
print('first isolated-active triples =',first_isolated)
print('isolated last-active transfer checks =',isolated)
print('g>=1 synchronized bridge checks =',gap_bridge)
print('g>=1 previous-active parity-digit checks =',gap_prev_digit)
print('previous-active phase-digit checks =',phase_prev_digit)
print('interface case counts =',dict(case_counts))
print('height-one reachability scan depth =',SCAN_DEPTH)
print('positive height-one bound checks =',height1_bound_checks)
print('max bounded J/2^H witness =',max_num[2])
print('abstract macro counterexamples = (1->2->3), (7->26->21)')
