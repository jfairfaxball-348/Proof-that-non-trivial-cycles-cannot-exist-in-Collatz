from fractions import Fraction
PATH='1101101011011011010110110101111111100111011011011111100111010111100010000'

def step(d,J,x):
    if x==0: y=0 if J%2 else 1
    else:
        if J%2: y=1
        elif d>1: y=0
        else: return None
    if x==0 and y==0: return d,(J+3**d-2**d)//2,y,'00'
    if x==1 and y==1: return d,(3*J+2**d-1)//2,y,'11'
    if x==0 and y==1: return d+1,(3*J+3**(d+1)-2**d-1)//2,y,'01'
    return d-1,J//2,y,'10'

i=p=0; d=1; J=-13
Z=Fraction(0); Y=Fraction(0); A=Fraction(0)
zeros=[]; aligned=[]
for n,ch in enumerate(PATH):
    x=int(ch); g=Fraction(2**i,3**p)
    s=step(d,J,x)
    if s is None: raise SystemExit(f'illegal at {n}')
    nd,nJ,y,edge=s
    if x==0:
        Z += g
        zeros.append((n+1,i,p,d,J,g,edge))
        if d==1 and y==0:
            A += g; aligned.append((n+1,g,J))
    if y==0: Y += g
    i += 1
    if x==1: p += 1
    d,J=nd,nJ

print('len',len(PATH),'ones',PATH.count('1'),'zeros',PATH.count('0'))
print('state',i,p,d,J)
print('gcut', Fraction(2**i,3**p), float(Fraction(2**i,3**p)))
print('Zx',Z, float(Z))
print('Zy',Y, float(Y))
print('D=Zx-Zy',Z-Y, float(Z-Y))
print('aligned A',A,float(A))
print('cap max',max(w for *_,w,e in zeros),float(max(w for *_,w,e in zeros)))
print('last zero',zeros[-1])
print('aligned count',len(aligned))
# four-pump metrics
m=4; g0=Fraction(2**i,3**p); G=g0*Fraction(4,3)**m
Ap=2*(G-g0)
print('4pump G',G,float(G),'A_pump',Ap,float(Ap),' >5/4?',Ap>Fraction(5,4))
print('pump zero weights', [g0*Fraction(4,3)**k*Fraction(2,3) for k in range(m)]) # 11 then 00 zero has g after 11=2/3*entry
# Actually x-zero weights within pumps: after 11: (2/3) g_k, g_k = g0*(4/3)^k
print('max pump zero', g0*Fraction(4,3)**(m-1)*Fraction(2,3), float(g0*Fraction(4,3)**(m-1)*Fraction(2,3)))
print('post Psi=2G',2*G,float(2*G))
# Type B forced zero after 11,11 has scalar 4G/9
print('typeB zero weight',Fraction(4,9)*G,float(Fraction(4,9)*G))
print('typeB exit g',Fraction(8,9)*G,float(Fraction(8,9)*G))
print('typeB exit Psi',Fraction(22,9)*G,float(Fraction(22,9)*G))
# Certificates
print('Zx<=77/10',Z<=Fraction(77,10))
print('A<=17/3',A<=Fraction(17,3))
print('D<5/3',Z-Y<Fraction(5,3))
