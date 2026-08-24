from fractions import Fraction
from itertools import product
from math import log
alpha=log(2)/log(3)

def Qword(bits):
    e=sum(bits); q=0; r=0
    for i,b in enumerate(bits):
        if b:
            q += (1<<i)*3**(e-1-r); r+=1
    return q

def parity_q(x):
    assert x.denominator%2
    return x.numerator&1

def Tq(x):
    return (3*x+1)/2 if parity_q(x) else x/2

def good(x,steps=2000):
    p2=p3=1; ones=0
    bits=[]
    seen={}
    for j in range(steps):
        b=parity_q(x); bits.append(b)
        if b: p3*=3; ones+=1
        p2*=2
        if p3<p2:
            return False,j+1,''.join(map(str,bits[-30:]))
        # optional detect exact rational state with deficit phase to establish cycle
        x=Tq(x)
    return True,steps,''.join(map(str,bits[-60:]))

pref=[1,1,0,1,1]
hits=[]
for p in range(5,25):
    rem=p-5
    for tail in product((0,1), repeat=rem):
        bits=pref+list(tail)
        e=sum(bits)
        # periodic average needs at least threshold
        if 3**e < 2**p: continue
        # also periodic ballot for R across repeated word: test one period prefixes
        p2=p3=1; ok=True
        for b in bits:
            if b:p3*=3
            p2*=2
            if p3<p2: ok=False;break
        if not ok: continue
        den=(1<<p)-3**e
        if den==0: continue
        R=Fraction(Qword(bits),den)
        # verify generated first 2p bits match periodic word twice
        x=R; gb=[]
        for j in range(2*p):
            gb.append(parity_q(x));x=Tq(x)
        if gb != bits*2: continue
        oks=[]
        for c in (0,12,4):
            oks.append(good(R+c,1200))
        if all(o[0] for o in oks):
            print('HIT p,e',p,e,'word',''.join(map(str,bits)),'R',R)
            print(' checks',oks)
            hits.append((p,e,bits,R,oks))
            raise SystemExit
    print('done p',p)
print('no hits')
