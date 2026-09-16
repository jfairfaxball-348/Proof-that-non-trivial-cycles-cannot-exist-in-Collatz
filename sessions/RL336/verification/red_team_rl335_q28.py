#!/usr/bin/env python3
# Independent check of the promoted finite graph and q=28 all-length charge.
N=range(1,38)
edges=[]
for z in N:
    for nz in N:
        edges.append((z,nz,5))
        if z+nz<=43: edges.append((z,nz,1))
assert len(edges)==2242
p={v:0 for v in N}
for _ in range(100):
    ch=False
    for a,b,k in reversed(edges):
        w=2*b-43*k
        if p[a]+w>p[b]:p[b]=p[a]+w;ch=True
    if not ch:break
else:raise AssertionError
assert (min(p.values()),max(p.values()))==(0,31)
slack={(a,b,k):p[b]-p[a]-(2*b-43*k) for a,b,k in edges}
assert min(slack.values())>=0
q=28;c={v:0 for v in N}
for _ in range(100):
    ch=False
    for a,b,k in reversed(edges):
        w=q*(k-2*(b<=21))-slack[(a,b,k)]
        if c[a]+w>c[b]:c[b]=c[a]+w;ch=True
    if not ch:break
else:raise AssertionError
assert (min(c.values()),max(c.values()))==(0,28)
assert all(c[a]+q*(k-2*(b<=21))-slack[(a,b,k)]<=c[b] for a,b,k in edges)
s=slack[(37,37,5)]
assert s==141
assert 28*5-s==-1 and 29*5-s==4
for qq in range(1,43): assert qq-43<0
print('RL335_RED_TEAM_GREEN')
print('edges',len(edges),'density',min(p.values()),max(p.values()),'q28',min(c.values()),max(c.values()))
print('N37_self_slack',s,'q28',28*5-s,'q29',29*5-s)
