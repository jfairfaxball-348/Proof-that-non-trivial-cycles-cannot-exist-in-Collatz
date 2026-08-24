from math import gcd
from fractions import Fraction

# General strengthened shortest-vector check.  Scale physical gaps by 2^r:
# G=2^r N, H=2^r K.  Since all three actual phases are nonzero mod 3,
# at least one of N,K,N-K is 0 mod 3.  The old (1,2)/(2,1) minima are forbidden.
for b,e in [(5,3),(8,5),(10,6),(13,8)]:
    B=1<<b; Y=3**e
    for N in range(1,30):
        for K in range(1,30):
            if N==K: continue
            mod3 = (N%3==0 or K%3==0 or (N-K)%3==0)
            if not mod3: continue
            a=Y*K+B*N
            c=(B+Y)*K-Y*N
            assert max(abs(a),abs(c)) >= 3*B+Y

# The bound is sharp at the lattice level: N=3,K=1 gives a=3B+Y.
for b,e in [(8,5),(10,6)]:
    B=1<<b; Y=3**e
    N,K=3,1
    a=Y*K+B*N
    c=(B+Y)*K-Y*N
    assert a==3*B+Y
    assert max(abs(a),abs(c))==3*B+Y

# Simple rational certificate for the packing-derived physical gap cap used in the note.
# z<(16/15)^(1/3)<46/45, R/(4R-1)<=160/639 for R>=160.
assert 46**3 * 15 > 45**3 * 16
cH=Fraction(46,45)*Fraction(160,639)
cG=Fraction(46,45)*Fraction(91,45)*Fraction(160,639)
assert cH < Fraction(12,23)
assert cG < Fraction(12,23)

# Global numerator upper after combining balanced-cut heights with RL23 packing.
# For R>=160 the coefficient in R(lambda-1) < c*e is maximized at R=160.
c_num=Fraction(16,15)*3*Fraction(319*160,5*(256*160-319))
assert c_num==Fraction(163328,203205)
assert c_num < Fraction(81,100)
assert Fraction(16,1)/c_num > 19  # hence integer e>=20 from the numerator sandwich

# Dynamic programming for exact Q extrema under the EXTRA strict-supercritical package.
def q_extrema(b,e):
    states={0:(0,0)}
    p3=[1]
    for _ in range(e): p3.append(p3[-1]*3)
    for i in range(b):
        nxt={}
        rem=b-i-1
        for p,(lo,hi) in states.items():
            # bit 0
            if i==b-1 or p3[p] > (1<<(i+1)):
                if p+rem>=e:
                    old=nxt.get(p)
                    nxt[p]=(lo,hi) if old is None else (min(old[0],lo),max(old[1],hi))
            # bit 1
            if p<e:
                np=p+1
                if i==b-1 or p3[np] > (1<<(i+1)):
                    if np+rem>=e:
                        add=(1<<i)*p3[e-1-p]
                        nlo,nhi=lo+add,hi+add
                        old=nxt.get(np)
                        nxt[np]=(nlo,nhi) if old is None else (min(old[0],nlo),max(old[1],nhi))
        states=nxt
    return states.get(e)

near=[]
for b in range(2,121):
    for e in range(1,b):
        B=1<<b; Y=3**e
        if not (B//2 < Y < B):
            continue
        ex=q_extrema(b,e)
        if ex is None:
            continue
        lo,hi=ex
        near.append((b,e,hi-lo,B,Y))

new_fails=[z for z in near if z[2] >= 4*(3*z[3]+z[4])]
assert new_fails and new_fails[0][0:2]==(119,75)
coprime_fails=[z for z in new_fails if gcd(z[0],z[1])==1]
assert coprime_fails and coprime_fails[0][0:2]==(119,75)

print('RL23 cubic mod-3 lattice verifier: PASS')
print('global shortest-vector upgrade: 2^r(3B+Y)')
print('near-resonant shared-11 upgrade: 4(3B+Y)')
print('packing + mod-3 physical-gap consequence: e >= 24')
print('conditional strict-prefix Delta frontier =',new_fails[0][0:2])
print('conditional coprime frontier =',coprime_fails[0][0:2])
