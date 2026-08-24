#!/usr/bin/env python3
from fractions import Fraction

EDGES='''11 11 01 11 11 10 01 01 11 11 00 11 11 01 10 01 11 10 01 10 11 10 01 11 10 01 01 10 11 00 11 11 00 10 01 11 11 01 11 10 01 11 10 11 01 00 10 10 01 10 11 00 10 01 11 11 01 10 10'''.split()

# Internal local coordinate: before EDGES[0], d=1,T=-14,p=0,i=0.
d,T,p=1,-14,0
apos=[]; bpos=[]
segments=[]
seg=None

for i,edge in enumerate(EDGES):
    x,y=map(int,edge)
    g=Fraction(1<<i, 3**p)
    # At height one and a same-bit edge, local g*T has the claimed behavior.
    if d==1 and x==y:
        before=g*T
        num=(3**y)*T + x*3**(d+y-1)-y
        assert num%2==0
        T2=num//2
        d2=d+y-x
        p2=p+x
        g2=Fraction(1<<(i+1),3**p2)
        after=g2*T2
        if edge=='00':
            assert after==before
            contrib=Fraction(0)
        else:
            # At d=1 counts are aligned, so this is a zero-displacement rank.
            j=p+1
            w=Fraction(1<<i,3**j)
            contrib=2*w
            assert after-before==contrib
        if seg is None:
            seg=[before, Fraction(0), i]
        seg[1]+=contrib
    else:
        if seg is not None:
            # Current edge starts after prior neutral segment; compute prior endpoint
            # from current local state.
            gnow=Fraction(1<<i,3**p)
            assert gnow*T-seg[0]==seg[1]
            segments.append((seg[2],i-1,seg[1]))
            seg=None

    # advance exact state
    num=(3**y)*T + x*3**(d+y-1)-y
    assert num%2==0
    T=num//2
    d=d+y-x
    p+=x

if seg is not None:
    i=len(EDGES)
    gnow=Fraction(1<<i,3**p)
    assert gnow*T-seg[0]==seg[1]
    segments.append((seg[2],i-1,seg[1]))

# Independent global rank check: all d=1 11 edges correspond to a_j=b_j and
# their rank-transport baseline contributions equal the segment totals.
a=[i for i,e in enumerate(EDGES) if e[0]=='1']
b=[i for i,e in enumerate(EDGES) if e[1]=='1']
assert len(a)==len(b)
zero_disp=sum(Fraction(2*(1<<aa),3**j) for j,(aa,bb) in enumerate(zip(a,b),1) if aa==bb)
seg_total=sum(s[2] for s in segments)
assert zero_disp==seg_total

print('RL49 height-one synchronized-mass telescoping verifier: PASS')
print('maximal height-one neutral segments =',len(segments))
print('total zero-displacement rank contribution =',zero_disp)
print('segment endpoints telescope exactly via local g*T')
