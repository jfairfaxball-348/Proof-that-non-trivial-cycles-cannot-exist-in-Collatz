# Symbolic sanity verifier for RL40 single-state extremizer.
import sympy as sp

R,z,l,q=sp.symbols('R z l q', positive=True)
ln3=sp.log(3)
a=(z/R)*2**(-(l-1)/2)
b=ln3/l
u=a*sp.exp(-b*q)
C=-R*sp.log(1-u)

Cp=sp.simplify(sp.diff(C,q))
Cpp=sp.simplify(sp.diff(Cp,q))

expected1=sp.simplify(-R*b*u/(1-u))
expected2=sp.simplify(R*b**2*u/(1-u)**2)
assert sp.simplify(Cp-expected1)==0
assert sp.simplify(Cpp-expected2)==0

# Exact algebra behind 3^H = 3^(q/l) 2^((l-1)/2).
alpha=sp.log(2)/sp.log(3)
H=q/l+alpha*(l-1)/2
assert sp.simplify(sp.exp(sp.log(3)*H)/(sp.exp(sp.log(3)*q/l)*sp.exp(sp.log(2)*(l-1)/2))-1)==0

# High-precision numerical convexity / concentration sanity.
import mpmath as mp
mp.mp.dps=80

def cfun(R,z,l,q):
    R=mp.mpf(R); z=mp.mpf(z); q=mp.mpf(q)
    return -R*mp.log(1-(z/R)*(mp.mpf(2)**(-(l-1)/2))*(mp.mpf(3)**(-q/l)))

def derivs(R,z,l,q):
    aa=(mp.mpf(z)/R)*(mp.mpf(2)**(-(l-1)/2))
    bb=mp.log(3)/l
    uu=aa*mp.e**(-bb*q)
    d1=-R*bb*uu/(1-uu)
    d2=R*bb**2*uu/(1-uu)**2
    return d1,d2

for lv in (1,2,3,5,10):
    for qv in (2,5,20):
        d1,d2=derivs(mp.mpf(10)**6,mp.mpf('1.01'),lv,mp.mpf(qv))
        assert d1<0
        assert d2>0

# For identical l, convexity says concentrating fixed excess maximizes the sum.
R0=mp.mpf(10)**6; z0=mp.mpf('1.01'); lv=2; base=mp.mpf(4); excess=mp.mpf(8)
concentrated=cfun(R0,z0,lv,base+excess)+cfun(R0,z0,lv,base)
spread=2*cfun(R0,z0,lv,base+excess/2)
assert concentrated>spread

print('RL40 single-state extremizer verifier: PASS')
print('C_l is symbolically decreasing and convex in charge q')
print('fixed-total-charge concentration sanity verified')
