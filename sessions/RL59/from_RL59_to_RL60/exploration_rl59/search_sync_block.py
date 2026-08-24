from fractions import Fraction
CAP=Fraction(17,30)
# zeta normalized to 1. Multiply final terminal-bound maxima by actual zeta where terminal bound active.

def eval_exit(J,g,M,maxz,bit):
    # bit is chosen exit same-bit from odd J; returns even Je, ge, M including exit 00 if any
    if bit==0:
        Je=(J+1)//2; ge=2*g; Me=M+g; mz=max(maxz,g)
    else:
        Je=(3*J+1)//2; ge=Fraction(2,3)*g; Me=M; mz=maxz
    assert Je%2==0
    # 01 follows: terminal inequality at d=2 gives ge*(Je+2) <= 3/2 (zeta=1)
    lam_term=Fraction(3,2)/(ge*(Je+2))
    lam_cap=10**100 if mz==0 else CAP/mz
    lam=min(lam_term,lam_cap)
    return lam*Me, (J,bit,Je,g,ge,M,Me,mz,lam_term,lam_cap,lam)

def cont_bit(J):
    # returns bit whose next J stays odd
    # J mod4=1: 00 continues odd, 11 exits even. J mod4=3: 11 continues odd, 00 exits even.
    return 0 if J%4==1 else 1

best=(Fraction(-1),None)
# brute starts odd positive up to 200k, follow deterministic continuation max 200
for Js in range(1,200000,2):
    J=Js; g=Fraction(1); M=Fraction(0); maxz=Fraction(0)
    for step in range(250):
        cb=cont_bit(J); eb=1-cb
        val,info=eval_exit(J,g,M,maxz,eb)
        if val>best[0]: best=(val,(Js,step,info))
        # continue
        if cb==0:
            maxz=max(maxz,g); M+=g; g*=2; J=(J+1)//2
        else:
            g*=Fraction(2,3); J=(3*J+1)//2
        if J<=0 or J%2==0: raise RuntimeError((Js,J,cb))
        # avoid massive rational numerator runtime if orbit huge, but 250 enough
print('best', float(best[0]), best[0])
print(best[1])
