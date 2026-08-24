from itertools import product
from math import gcd
from fractions import Fraction


def Qword(w):
    L=sum(w); p=0; q=0
    for i,b in enumerate(w):
        if b:
            q += (1<<i)*3**(L-1-p)
            p += 1
    return q

checks=0
even_sum_checks=0
order3_checks=0
# Small exact exhaustive sanity checks. We choose g,a,ell with X^g>Y^g,
# and all balanced canonical cuts j. Macroblocks are arbitrary words with
# the required lengths and weights.
for g in range(2,7):
  for a in range(1,4):
    for ell in range(1,a+1):
      X=1<<a; Y=3**ell
      if X**g <= Y**g: continue
      D=X**g-Y**g
      for j in range(1,g):
        n1=j*a; l1=j*ell
        n2=(g-j)*a; l2=(g-j)*ell
        # keep exhaustive domain small
        if n1+n2 > 10: continue
        for u in product((0,1), repeat=n1):
          if sum(u)!=l1: continue
          U=Qword(u)
          for v in product((0,1), repeat=n2):
            if sum(v)!=l2: continue
            V=Qword(v)
            d=u+v
            Q=Qword(d)
            assert Q == Y**(g-j)*U + X**j*V
            R=Fraction(Q,D)
            x=Fraction(X**(g-j)*U + Y**j*V, D)
            # Equivalent direct prefix state check.
            assert X**j*x - Y**j*R == U
            G=x-R
            S=x+R
            Mj=X**j-Y**j
            Mk=X**(g-j)-Y**(g-j)
            assert D*G == Mk*U - Mj*V
            h=gcd(g,j)
            Mh=X**h-Y**h
            assert Mj%Mh==0 and Mk%Mh==0 and D%Mh==0
            Cgap=D//Mh
            assert Cgap*G == (Mk//Mh)*U - (Mj//Mh)*V
            checks += 1
            n=g//h
            if n==3:
                C3=(X**(2*h)+X**h*Y**h+Y**(2*h))
                assert Cgap==C3
                order3_checks += 1
            if n%2==0:
                Ph=X**h+Y**h
                Aj=X**j+Y**j
                Ak=X**(g-j)+Y**(g-j)
                assert D%Ph==0 and Aj%Ph==0 and Ak%Ph==0
                Csum=D//Ph
                assert Csum*S == (Ak//Ph)*U + (Aj//Ph)*V
                # X^h-Y^h and X^h+Y^h are coprime because X even, Y odd.
                assert gcd(Mh,Ph)==1
                even_sum_checks += 1

print('RL21 balanced cyclotomic cofactor verifier: PASS')
print('gap-cofactor checks =', checks)
print('even-order sum-cofactor checks =', even_sum_checks)
print('order-3 cubic-cofactor checks =', order3_checks)
