"""Independent finite-edge and rational check for candidate 42-phase theorem.

PROMOTED; see RL339 certificate. The analytic block-count argument is recorded in checkpoint text.
"""
from fractions import Fraction

a=217976794617
ell=137528045312
Lambda=1+Fraction(1,1<<40)
c=Fraction(198849,1000000)
CAP=32537248343

zero_edges=[]
for left in range(1,36):
    for right in range(1,36):
        for p in range(1,10):
            if p==1 and left+right>=43:continue
            slack=42*p-left-right
            assert slack>=0
            if slack==0:
                assert p==1 and left+right==42
                zero_edges.append((left,right))
            else:
                assert slack>=p
assert len(zero_edges)==29
assert all(right==42-left for left,right in zero_edges)

r44=(44*a)%ell
alpha44=Fraction(r44,ell)
assert Fraction(1,2)<alpha44<1

# Each full group of four zero-slack edges contains two low targets separated
# by exactly 44 physical ranks, both for 21->21 and alternating z<->42-z.
for length in range(101):
    self_pairs=((length+1)//2)//2+(length//2)//2
    alternating_pairs=(length//2)//2
    assert self_pairs>=length//4
    assert alternating_pairs>=length//4

# Different log-series from the primary verifier.
ln2=sum((Fraction(1,n*(1<<n)) for n in range(1,301)),Fraction())
y=(1-alpha44)*ln2
exp_lower=sum((y**j / __import__('math').factorial(j) for j in range(7)),Fraction())
assert exp_lower-1>c

K=(ell-60+1-35+21)//22
s=44*K-2*(ell-60+1)+70
assert (K,s)==(6251274783,16)
x=ln2/ell
sum1=K*(K+1)//2
sum2=K*(K+1)*(2*K+1)//6
sum3=sum1*sum1
sum4=K*(K+1)*(2*K+1)*(3*K*K+3*K-1)//30
W=K+x*sum1+x*x*sum2/2+x**3*sum3/6+x**4*sum4/24
full=1/(2*x+x*x)-Fraction(1,2)
om=sum((Fraction(1<<((a*j)//ell),3**j)/Lambda for j in range(1,60)),Fraction())

def g(h):
    S=44*h+s
    structural=K+h+c*max(Fraction(0),Fraction(K+h-4*S-3,4))
    return max(Fraction(h),structural-W)
values=[(h,g(h)) for h in (0,24281913,24281914,24281915,35721569)]
assert min(values,key=lambda item:item[1])[0]==24281914
gain=g(24281914)
rhs=1+(full-om)/3-W/(12*Lambda)-gain/(12*Lambda)
assert CAP<rhs<CAP+1
assert c<1
assert Fraction(22,21)/(12*Lambda)<1/(6*Lambda)
print("PHASE42_RED_TEAM_GREEN","zero_edges",len(zero_edges),
      "h",24281914,"floor",rhs.numerator//rhs.denominator)
