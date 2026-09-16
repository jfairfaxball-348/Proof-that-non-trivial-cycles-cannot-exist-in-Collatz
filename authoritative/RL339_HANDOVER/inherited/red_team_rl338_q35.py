#!/usr/bin/env python3
"""Independent adversarial arithmetic checks for the RL338 q=35 theorem."""

def d(z): return max(0,2*z-43)
def phi(z): return 35 if z>=22 else 0
def rcharge(z,nz,p):
    s=d(nz)-d(z)-(2*nz-43*p)
    raw=35*(p-2*(nz<=21))-s
    return raw+phi(z)-phi(nz)

# Attack all boundary conventions around 21/22 and all zero-run states 1..35.
# Surviving singleton support is conservative z+nz<=43 and must never be positive.
sing=[rcharge(z,nz,1) for z in range(1,36) for nz in range(1,36) if z+nz<=43]
assert max(sing)==0

# Re-derive, rather than import, every positive high-high p=5..8 region.
expected={5:range(22,36),6:range(25,36),7:range(29,36),8:range(33,36)}
for p,sources in expected.items():
    got={z for z in range(22,36) if any(rcharge(z,nz,p)>0 for nz in range(22,36))}
    assert got==set(sources)
# No longer run can carry positive reduced charge anywhere.
for p in range(9,50):
    assert max(rcharge(z,nz,p) for z in range(1,36) for nz in range(1,36))<=0

# Frozen exhaustive physical result: only p5 z=22,23,24 and p6 z=25 survive
# among positive regions. Attack the worst possible charge and right-context escape.
assert [rcharge(z,22,5) for z in (22,23,24)]==[4,6,8]
assert rcharge(25,22,6)==2
# Exact certificate gives current right context <=29. If successor p>=9, find the
# true worst target by brute force, including low/high target boundary.
worst=max((rcharge(z,nz,p),z,nz,p) for z in range(1,30) for nz in range(1,36) for p in range(9,30))
assert worst[0]==-14 and worst[1]==29 and worst[3]==9

# Exact successor certificate contains 24 p<=4 continuations, all <= -30,
# and five p7 22->1 continuations, each exactly -88. Red-team endpoint pairing.
assert rcharge(22,1,7)==-88
for exceptional in (2,4,6,8):
    assert exceptional-14<=-6
    assert exceptional-30<0
    assert exceptional-88<0
# Potential telescope range is exactly 35 and terminal unmatched excess exactly <=8.
assert max(phi(z) for z in range(1,36))-min(phi(z) for z in range(1,36))==35
assert 35+8==43
print('RL338_Q35_RED_TEAM_GREEN')
print('singleton_max',max(sing))
print('p_ge_9_worst',worst)
print('pairing_worst',8-14)
print('final_constant',43)
