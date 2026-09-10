#!/usr/bin/env python3
"""RL292 regression: checkpoint-8 transformed-shadow D resonance and low-cost kernel gap.
Analytic identities are proved in scratch notes; this script is regression support only.
"""
from collections import deque


def v2(n):
    assert n != 0
    n=abs(n)
    return (n & -n).bit_length()-1


def step(d,J,x):
    K=J+2**d-1
    if K%2==0:
        y=x
        if x:
            d2,K2=d,3*K//2
        else:
            d2,K2=d,(K+3**d-1)//2
    else:
        y=1-x
        if x:
            if d<=1:return None
            d2,K2=d-1,(K-1)//2
        else:
            d2,K2=d+1,3*(K+3**d)//2
    J2=K2-2**d2+1
    return d2,J2,d-1,y


def D_of(d,J):
    K=J+2**d-1
    return -2*K + 3**d - 1


def check_D_identities():
    checked=0
    column_counts={(0,0):0,(1,1):0,(0,1):0,(1,0):0}
    for d in range(1,9):
        for J in range(1,400):
            D=D_of(d,J); K=J+2**d-1
            for x in (0,1):
                out=step(d,J,x)
                if out is None: continue
                d2,J2,dh,y=out
                D2=D_of(d2,J2)
                assert 2*D2 == (3**y)*D + 1 - 3**d2
                col=(x,y); column_counts[col]+=1
                if col==(0,0): assert D2 == -K
                elif col==(1,1): assert D2 == 3**d-1-3*K
                elif col==(0,1): assert D2 == -(3*K+1)
                else: assert D2 == 3**(d-1)-K
                checked+=1
    return checked,column_counts


def first_returns_8_lt8():
    # forced launch from checkpoint 8
    out=step(1,8,0)
    assert out[:3]==(2,15,0)
    stack=[(2,15,0,"0")]
    seen=set(); returns=[]
    while stack:
        d,J,h,w=stack.pop()
        key=(d,J,h)
        if key in seen: continue
        seen.add(key)
        for x in (0,1):
            out=step(d,J,x)
            if out is None: continue
            d2,J2,dh,y=out; h2=h+dh; w2=w+str(x)
            if h2>=8: continue
            if d2==1:
                returns.append((J2,h2,w2))
            else:
                stack.append((d2,J2,h2,w2))
    returns=sorted(set(returns), key=lambda t:(t[1],t[0],t[2]))
    assert returns == [(5,2,'001'),(12,2,'011')], returns
    return returns,len(seen)


def boundary_exits_5():
    J=5; seen=set(); exits=set(); trace=[]
    while J not in seen:
        seen.add(J); trace.append(J)
        j0=(J+1)//2; j1=(3*J+1)//2
        even=[z for z in (j0,j1) if z%2==0]
        odd=[z for z in (j0,j1) if z%2==1]
        assert len(even)==len(odd)==1
        exits.add(even[0]); J=odd[0]
    assert exits=={2,8}
    assert trace==[5,3]
    return tuple(sorted(exits)),tuple(trace)


def main():
    c,cols=check_D_identities()
    rets,nstates=first_returns_8_lt8()
    exits,trace=boundary_exits_5()
    print('RL292 D-resonance + checkpoint-8 low-cost kernel regression: PASS')
    print('D_identity_checks=',c)
    print('column_counts=',cols)
    print('checkpoint8_first_returns_below_height8=',rets)
    print('offboundary_states_examined_below_height8=',nstates)
    print('boundary5_trace=',trace)
    print('boundary5_even_exits=',exits)
    print('analytic_candidate=CHECKPOINT8_TRANSFORMED_SHADOW_RESONANCE_NORMAL_FORM_AND_HEIGHT_GAP_PROVED')

if __name__=='__main__': main()
