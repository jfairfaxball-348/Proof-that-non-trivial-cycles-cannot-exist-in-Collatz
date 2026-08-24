from fractions import Fraction

def v2(n):
    c=0
    while n%2==0:
        n//=2;c+=1
    return c

def F(x): return Fraction(3*x+1,3*x)

for t in list(range(0,60))+[1000,1000000]:
    R=361+486*t
    x0=379+512*t
    y0=569+768*t
    x1=427+576*t
    y1=641+864*t
    z=481+648*t
    H=Fraction(4*R-1,3)
    assert H==z
    assert R < x0 < H and R < x1 < H
    assert y0>H and y1>H and z>=H
    vals=[x0,y0,x1,y1,z]
    nus=[v2(3*x+1) for x in vals]
    assert nus==[1,2,1,2,2]
    nxt=[(3*x+1)//(1<<nu) for x,nu in zip(vals,nus)]
    assert nxt==[y0,x1,y1,z,R]
    q=(2*R+1)//3
    assert 2*R+1==3*q and z==2*q-1
    assert q%2==1 and q%3!=0
    prod=Fraction(1)
    for x in vals: prod*=F(x)
    assert prod==Fraction(256*R,256*R-319)
    # For t != 1 mod 3, every displayed phase is nonzero mod 3.
    if t%3!=1:
        assert all(x%3 for x in [R]+vals)

# Infinite hard-root-compatible subfamily: t == 3 or 11 (mod 24)
# gives R == 91 (mod 144), R == 11 (mod 16), and avoids t == 1 (mod 3).
for t in [3,11,27,35,51,59]:
    R=361+486*t
    assert t%24 in (3,11)
    assert R%144==91
    assert R%16==11
    assert t%3!=1
    vals=[R,379+512*t,569+768*t,427+576*t,641+864*t,481+648*t]
    assert all(x%3 for x in vals)

print('RL23 local packing saturation verifier: PASS')
print('family R=361+486t realizes exact type-II k=2 core equality')
print('all displayed phases are nonzero mod 3 for t mod 3 != 1')
print('hard-root-compatible infinite subfamilies: t mod 24 in {3,11}')
