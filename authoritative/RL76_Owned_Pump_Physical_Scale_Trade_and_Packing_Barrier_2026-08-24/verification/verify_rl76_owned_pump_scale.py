from fractions import Fraction
from itertools import product


def phys_step(x,b):
    return x/2 if b==0 else (3*x+1)/2

def quot_step(J,b):
    return (J+1)/2 if b==0 else (3*J+1)/2

def affine_phys(word):
    a=Fraction(1); b=Fraction(0)
    for bit in word:
        if bit==0:
            a,b=a/2,b/2
        else:
            a,b=3*a/2,(3*b+1)/2
    return a,b

def affine_quot(word):
    a=Fraction(1); b=Fraction(0)
    for bit in word:
        if bit==0:
            a,b=a/2,(b+1)/2
        else:
            a,b=3*a/2,(3*b+1)/2
    return a,b

def legal_word_from_state(x,word):
    y=Fraction(x)
    for bit in word:
        if y.denominator != 1: return False
        n=y.numerator
        if (n&1) != bit: return False
        y=phys_step(y,bit)
    return y.denominator==1

closed=0
pair_checks=0
scale_checks=0
determinant_checks=0
for n in range(1,8):
    P=2**n
    for word in product([0,1], repeat=n):
        R=3**sum(word)
        ap,bp=affine_phys(word)
        aq,bq=affine_quot(word)
        assert ap==aq==Fraction(R,P)
        alpha=bp/(1-ap)
        J=bq/(1-aq)
        # exact conjugacy of synchronized quotient dynamics to physical shortcut map
        assert J == 2*alpha+1
        if J.denominator!=1 or J.numerator%2==0: continue
        JJ=Fraction(J)
        ok=True
        for bit in word:
            if JJ.denominator!=1 or JJ.numerator%2==0:
                ok=False; break
            JJ=quot_step(JJ,bit)
        if not ok or JJ!=J: continue
        assert alpha.denominator==1
        alpha=int(alpha); J=int(J)
        closed += 1
        C=int(bp*P)
        assert C==(P-R)*alpha
        for q in range(1,5):
            for m in [1,2,5,11]:
                A0=alpha + (P**q)*m
                B0=alpha + 3*(P**q)*m
                Aq=alpha + (R**q)*m
                Bq=alpha + 3*(R**q)*m
                assert 3*A0-B0+1==J
                assert 3*Aq-Bq+1==J
                ww=word*q
                if A0>0 and B0>0:
                    assert legal_word_from_state(A0,ww)
                    assert legal_word_from_state(B0,ww)
                    a=Fraction(A0); b=Fraction(B0)
                    for bit in ww:
                        a=phys_step(a,bit); b=phys_step(b,bit)
                    assert a==Aq and b==Bq
                    pair_checks += 1
                g=Fraction(7,13)
                gq=g*Fraction(P,R)**q
                assert g*(A0-alpha)==gq*(Aq-alpha)
                assert g*(B0-alpha)==gq*(Bq-alpha)
                scale_checks += 1

                # RL75 determinant factor after substituting x=B0.
                # Choose arbitrary positive context powers X0,Y0 with Mq>0 when possible.
                X0=2**5; Y0=3**2
                Mq=X0*(P**q)-Y0*(R**q)
                if Mq!=0:
                    delta=R-P
                    lhs=(delta*B0+C)*Mq//(P**q)
                    rhs=3*m*(R-P)*Mq
                    assert lhs==rhs
                    determinant_checks += 1

# For P>R, full denominator M_q grows faster than P under fixed context.
growth_checks=0
for P,R in [(4,3),(16,9),(32,27)]:
    X0=2**12; Y0=3**3
    prev=None
    for q in range(1,10):
        M=X0*P**q-Y0*R**q
        if M>0 and prev is not None:
            assert M > P*prev
            growth_checks += 1
        if M>0: prev=M

# Special c=10 reciprocal-mass barrier.
R0=2**71
harmonic_checks=0
for q in range(1,30):
    minm=(R0-1 + 3**q - 1)//(3**q)
    for mult in [1,2,7,101]:
        m=max(1,minm*mult)
        A=[];B=[]
        for j in range(q):
            A.append(1 + (4**(q-j))*(3**j)*m)
            B.append(1 + 3*(4**(q-j))*(3**j)*m)
        Aq=1+3**q*m
        assert Aq>=R0
        recip=sum(Fraction(1,x) for x in A+B)
        bound=Fraction(4, R0-1)*(1-Fraction(3,4)**q)
        assert recip < bound
        assert recip/3 < Fraction(4,3*(R0-1))
        harmonic_checks += 1

# Full-cycle resonance budget from RL73 is 2 log(zeta) < 158/[9(R0-2)].
assert Fraction(4,3*(R0-1)) < Fraction(158,9*(R0-2))

print('RL76 owned-pump physical-scale verifier: PASS')
print('closed synchronized words checked =', closed)
print('positive paired legality checks =', pair_checks)
print('scale-invariance checks =', scale_checks)
print('determinant-normal-form checks =', determinant_checks)
print('fixed-context denominator-growth checks =', growth_checks)
print('c=10 reciprocal-mass checks =', harmonic_checks)
print('R0 =', R0)
print('c10 full-cycle log-product contribution ceiling <', float(Fraction(4,3*(R0-1))))
print('RL73 full-cycle resonance ceiling scale <', float(Fraction(158,9*(R0-2))))
