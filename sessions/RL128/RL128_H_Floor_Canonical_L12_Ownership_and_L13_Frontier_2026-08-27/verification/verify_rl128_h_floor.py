#!/usr/bin/env python3
L=12

def side_floor(n,t,base,zero=False):
    best=0
    for k in range(1,n+1):
        c=max(n-t*(k-1),0)
        if not c: break
        best=max(best,(c-1)*base**k+(1 if zero else 0))
    return best

def H(z):
    return min(max(side_floor(L,t,3),side_floor(z,t,2,True),6*(t-1))
               for t in range(1,min(L,z)+1))

def D(z): return 2**(L+z)-3**L
def B(z): return (2**z-1)*(3**L-2**L)

assert D(7)<0<D(8)
assert H(40)==121
assert H(41)==129
# 41 is the smallest positive-Z H/width contradiction.
for z in range(8,41):
    assert H(z)*D(z) <= B(z)
assert H(41)*D(41) > B(41)
# Exact tail identity. Since it is positive from z=16, it is positive throughout z>=41.
for z in range(16,80):
    assert 129*D(z)-B(z) == 1039*2**z-68_028_544
    assert 129*D(z)-B(z) > 0
# Diagnostic monotonicity over a range; the report gives the unbounded proof for z>=12.
assert all(H(z+1)>=H(z) for z in range(12,80))
print('RL128 H-floor verifier: PASS')
print('positivity threshold: Z=8')
print('H(12,40)=121; H(12,41)=129; tail Z>=41 excluded')
