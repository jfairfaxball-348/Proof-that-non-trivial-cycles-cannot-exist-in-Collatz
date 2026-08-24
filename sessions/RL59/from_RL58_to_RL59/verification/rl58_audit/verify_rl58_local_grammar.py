from fractions import Fraction

def v2(n):
    assert n>0
    r=0
    while n%2==0:
        n//=2; r+=1
    return r

def v3(n):
    assert n>0
    r=0
    while n%3==0:
        n//=3; r+=1
    return r

# Height-one Q=J+1. Forward maps for synchronized edges.
def f00(Q):
    assert Q%2==0
    return (Q+2)//2

def f11(Q):
    assert Q%2==0
    return 3*Q//2

# Audit the all-00 continuation statement: the longest legal uninterrupted
# height-one 00 continuation from even Q != 2 is v2(Q-2).
for Q in range(4, 20000, 2):
    q=Q; m=0
    while q%2==0 and q!=2:
        q=f00(q); m+=1
    assert m==v2(Q-2), (Q,m,v2(Q-2))
print('r=0 all-00 continuation length = v2(Q-2): PASS')
print('wording repair: this is the longest all-00 continuation, not the length of every actual run')

# r=1 complete-return macro: 01 (00)^(n-1) 10.
# From height-one entry Q, after 01 the height-two variable obeys
# Q1-8=(3Q-7)/2. Each height-two 00 halves Q-8.
# The first legal return 10 occurs when Q_n is odd, hence n=v2(3Q-7).
# Check over the admissible odd entries with 3Q-7>0.
for Q in range(3, 20000, 2):
    a=3*Q-7
    if a<=0: continue
    n=v2(a)
    # Q after 01
    Qh=3*(Q+3)//2
    assert 2*(Qh-8)==a
    # n-1 internal d=2 00s
    for _ in range(n-1):
        assert Qh%2==0
        Qh=(Qh+8)//2
    assert Qh%2==1
    # and if n>1, previous one was even by construction.
    assert Qh-8 == a//(2**n)
print('r=1 complete-return entry valuation n=v2(3Q-7): PASS')

# Potential increment ratio for the complete r=1 macro.
# Zero masses: g,2g,...,2^(n-1)g, so M=g(2^n-1).
# Delta Psi/g = 1 + sum_{k=1}^{n-1} (13/12)2^k + (1/12)2^n.
for n in range(1,40):
    M=Fraction(2**n-1)
    dp=Fraction(1)
    for k in range(1,n):
        dp += Fraction(13,12)*2**k
    dp += Fraction(1,12)*2**n
    assert dp == Fraction(7,6)*M, (n,dp,M)
print('r=1 complete-return DeltaPsi=(7/6)M: PASS')

# Terminal LTE regression over odd K: v3(2^K+1)=1+v3(K).
for K in range(1,1001,2):
    assert v3(2**K+1)==1+v3(K), K
print('terminal v3(2^K+1)=1+v3(K) for odd K (finite regression): PASS')
