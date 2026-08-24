from fractions import Fraction
from math import gcd


def Qword(w):
    e=sum(w); p=0; q=0
    for i,b in enumerate(w):
        if b:
            q += (1<<i)*3**(e-1-p)
            p += 1
    return q

# Exact state/lattice/norm algebra.
for b,e in [(5,3),(7,4),(8,5)]:
    B=1<<b; Y=3**e; C=B*B+B*Y+Y*Y
    base=[1]*e+[0]*(b-e)
    words=[base]
    if b-e>=1 and e>=2:
        z=base[:]
        z[e-1],z[e]=0,1
        words.append(z)
    while len(words)<3: words.append(base)
    u,v,w=words[:3]
    U,V,W=map(Qword,(u,v,w))
    Dfull=B**3-Y**3
    Q=Y*Y*U+B*Y*V+B*B*W
    R=Fraction(Q,Dfull)
    x=Fraction(Y*R+U,B)
    y=Fraction(Y*x+V,B)
    G=x-R; H=y-R
    assert B*R-Y*y==W
    assert U-W==B*G+Y*H
    assert V-W==-Y*G+(B+Y)*H
    lhs=(U-W)**2-(U-W)*(V-W)+(V-W)**2
    rhs=C*(G*G-G*H+H*H)
    assert lhs==rhs

# Lattice equivalence and shortest-vector bounds on small integer boxes.
for b,e in [(5,3),(8,5),(10,6)]:
    B=1<<b;Y=3**e;C=B*B+B*Y+Y*Y
    for k in range(-8,9):
        for n in range(-8,9):
            a=k*Y+n*B
            c=k*(B+Y)-n*Y
            assert Y*a+B*c==k*C
            assert Fraction(Y*a+B*c,C)==k
            assert Fraction((B+Y)*a-Y*c,C)==n
            if (k,n)!=(0,0):
                assert max(abs(a),abs(c))>=B
            if k>0 and n>0 and k!=n:
                assert max(abs(a),abs(c))>=2*B+Y

# Dynamic programming for exact Q extrema under the EXTRA strict-supercritical package.
def q_extrema(b,e):
    states={0:(0,0)}
    p3=[1]
    for _ in range(e): p3.append(p3[-1]*3)
    for i in range(b):
        nxt={}
        for p,(lo,hi) in states.items():
            # bit 0
            if i==b-1 or p3[p] > (1<<(i+1)):
                if p+(b-i-1)>=e:
                    old=nxt.get(p)
                    nxt[p]=(lo,hi) if old is None else (min(old[0],lo),max(old[1],hi))
            # bit 1
            if p<e:
                np=p+1
                if i==b-1 or p3[np] > (1<<(i+1)):
                    if np+(b-i-1)>=e:
                        add=(1<<i)*p3[e-1-p]
                        nlo,nhi=lo+add,hi+add
                        old=nxt.get(np)
                        nxt[np]=(nlo,nhi) if old is None else (min(old[0],nlo),max(old[1],nhi))
        states=nxt
    return states.get(e)

near=[]
for b in range(2,101):
    for e in range(1,b):
        B=1<<b; Y=3**e
        if not (B//2 < Y < B):
            continue
        ex=q_extrema(b,e)
        if ex is None:
            continue
        lo,hi=ex; Delta=hi-lo
        near.append((b,e,Delta,B,Y))

for b,e,Delta,B,Y in near:
    if b<=31:
        assert Delta < 4*B

weak_fails=[z for z in near if z[2]>=4*z[3]]
assert weak_fails and weak_fails[0][0:2]==(35,22)

primitive_fails=[z for z in near if z[2]>=4*(2*z[3]+z[4])]
assert primitive_fails and primitive_fails[0][0:2]==(92,58)

coprime_fails=[z for z in primitive_fails if gcd(z[0],z[1])==1]
assert coprime_fails and coprime_fails[0][0:2]==(100,63)

print('RL22 cubic prefix-lattice verifier: PASS')
print('weak Delta>=4B frontier =',weak_fails[0][0:2])
print('primitive positive-gap frontier =',primitive_fails[0][0:2])
print('coprime primitive frontier =',coprime_fails[0][0:2])
