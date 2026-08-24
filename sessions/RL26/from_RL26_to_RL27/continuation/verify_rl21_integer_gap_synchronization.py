from math import gcd

def T(n):
    return (3*n+1)//2 if n&1 else n//2

def v2(n):
    c=0
    while n%2==0:
        n//=2;c+=1
    return c

checks=0
sep_checks=0
for R in range(3,300,2):
  for G in range(2,100,2):
    x=R+G
    r=v2(G)
    a,b=R,x
    for t in range(r):
      assert (a&1)==(b&1)
      a,b=T(a),T(b)
    assert (a&1)!=(b&1)
    assert b-a>0 and (b-a)&1
    checks+=1
    # If both current and next states respect a common positive least floor R0,
    # verify the minimax separation inequality with that floor.
    a1,b1=T(a),T(b)
    floor=min(a,b,a1,b1)
    delta=b-a
    nextdelta=b1-a1
    assert max(delta,abs(nextdelta))*3 >= 2*floor+1
    sep_checks+=1
print('RL21 integer-gap synchronization verifier: PASS')
print('synchronization checks =',checks)
print('separation checks =',sep_checks)
