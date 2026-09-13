#!/usr/bin/env python3
from heapq import heappush,heappop
def st(s,x):
 d,J=s;K=J+2**d-1
 if K%2==0:d2,K2=(d,3*K//2) if x else (d,(K+3**d-1)//2)
 elif x:
  if d<=1:return None
  d2,K2=d-1,(K-1)//2
 else:d2,K2=d+1,3*(K+3**d)//2
 return (d2,K2-2**d2+1),d-1
def rp(s,w,soft=False):
 c=0
 for q in w:
  o=st(s,int(q))
  if o is None:return None if soft else (_ for _ in ()).throw(AssertionError((s,w,q)))
  s,z=o;c+=z
 return s,c
def fk(d,K):return d,K-2**d+1
def K(s):d,J=s;return J+2**d-1
def co(A,B):a,x=A;b,y=B;return a+b,3**b*x+y
def L(D):return fk(D,(5*3**D-3)//4)
def R(D):return fk(D,(9*3**D-3)//4)
def BL(D):return (D*D+D-6)//2
def BR(D):return (D*D+3*D-4)//2
R3=(3,20);C8=(1,8);P=(2,3);D0=(3,17)
z=0
for d in range(3,52):
 p="0"*(d-3);a=rp(R3,p+"10");b=rp(R3,p+"11")
 if d%2:
  assert a==(L(d),BL(d))
  if d==3:assert b==((1,5),3)
  else:
   assert b[0]==R(d-2) and b[1]-rp(R3,"0"*(d-4)+"11")[1]==d
 else:
  D=d-1;assert b==(R(D),BR(D))
  assert a[0]==L(D) and a[1]-rp(R3,"0"*(d-4)+"10")[1]==D+1
 z+=1
we=0
for D in range(3,52,2):
 w="001"+"0"*(D+1)
 assert rp(C8,w+"10")== (L(D),BL(D)+3)
 assert rp(C8,w+"011")== (R(D),BR(D)+3);we+=1
def F(d):return fk(d-1,(3**d-3)//2)
def S(d):return fk(d-1,(3**d-1)//2)
def A(d):return fk(d,(3**(d+1)-9)//2)
def CF(d):return d*d-d-2
def CA(d):return d*d-2*d-1
def C2(d):return d*(d-1)//2
for d in range(3,20):
 assert rp(D0,"00"*(d-3)+"1")== (A(d),CA(d))
 assert rp(D0,"00"*(d-3)+"01")== (F(d),CF(d))
om=ol=0
for d in range(3,18,2):
 for j in range(8):
  a=rp(F(d),"00"+"1"*j+"01",1);b=rp(S(d),"1"*(j+2)+"00",1)
  if a and b:
   assert a[0]==b[0] and a[1]-b[1]==j+3
   assert CF(d)+a[1]-C2(d)-b[1]==d*(d-1)//2+j+1>=4;om+=1
  D=d-2
  if D>=3:
   a=rp(F(d),"00"+"1"*j+"00",1);b=rp(L(D),"0"+"1"*j+"00",1)
   if a and b:
    assert a[0]==b[0]
    assert CF(d)+a[1]-BL(D)-b[1]==(D*D+7*D+8)//2>=19;ol+=1
em=0
for d in range(4,20,2):
 w="010" if d%4==2 else "011";a=rp(F(d),w);b=rp(S(d),w)
 assert a[0]==b[0] and a[1]-b[1]==2
 assert CF(d)+a[1]-C2(d)-b[1]==d*(d-1)//2>=6;em+=1
assert rp(D0,"01")==rp(C8,"011000")== (F(3),4)
for d in range(2,20):
 ad=(d,K(A(d)))
 if d==2:assert ad==(2,9)
 else:assert co((d-1,K(A(d-1))),(1,9))==ad
 assert co((d,K(S(d+1))),(0,-4))==ad
def sm(src,k):
 q=[(0,src)];b={src:0}
 while q:
  c,s=heappop(q)
  if c!=b[s]:continue
  d,J=s
  if d==1 and J>0 and J%(2**k)==0:return c,s
  if c>40:continue
  for x in (0,1):
   o=st(s,x)
   if o:
    t,v=o;n=c+v
    if n<b.get(t,10**99) and n<=40:b[t]=n;heappush(q,(n,t))
ma,ms=sm(A(4),2),sm(S(5),2);assert ma[0]==ms[0]==8
def fp(src):
 q=[(0,"",src)];b={src:(0,"")};e={}
 while q:
  c,w,s=heappop(q)
  if b.get(s)!=(c,w):continue
  for x in (0,1):
   o=st(s,x)
   if not o:continue
   t,v=o;n=c+v;u=w+str(x)
   if t[1]>0:
    if t not in e or (n,u)<e[t]:e[t]=(n,u)
   elif t not in b or (n,u)<b[t]:b[t]=(n,u);heappush(q,(n,u,t))
 return b,e
b28,e28=fp((3,-28));b17,e17=fp((2,-17))
E28={(2,3):(3,"110000"),(2,1):(4,"110100"),(3,2):(5,"1110100"),(4,21):(5,"100"),(5,104):(5,"00"),(3,6):(6,"111000"),(3,8):(7,"010"),(3,11):(7,"10100"),(3,9):(9,"0110")}
E17={(2,3):(2,"01000"),(3,2):(2,"00"),(2,1):(3,"01100"),(3,11):(5,"110000"),(3,8):(6,"1000"),(3,9):(7,"1101000"),(3,6):(8,"11011101000"),(4,25):(9,"10100")}
assert len(b28)==19 and e28==E28 and len(b17)==27 and e17==E17
sh=set(E28)&set(E17);assert len(sh)==7 and max(E17[s][0]-E28[s][0] for s in sh)==2
U=(4,21);V=(5,104);X=(4,43);Y=(6,504)
assert rp(U,"0")== (X,3) and rp(U,"1")==((4,39),3)
assert rp(V,"0")== (Y,4) and rp(V,"1")==((4,52),4) and rp((4,39),"0")==((4,52),3)
assert co((4,K((4,39))),(0,4))==(4,K(X))
assert co((2,K(P)),(4,81))==(6,K(Y))
print("RL307_CLOSEOUT_VERIFIER_GREEN")
print("r3_zipper_instances",z)
print("checkpoint8_wall_entry_instances",we)
print("d0_odd_merger_instances",om)
print("d0_odd_leadingP_instances",ol)
print("d0_even_merger_instances",em)
print("A4_shell_min",ma[0],"S5_shell_min",ms[0])
print("minus28_nonpositive_states",len(b28),"first_positive_exits",len(e28))
print("minus17_nonpositive_states",len(b17),"first_positive_exits",len(e17))
print("minus28_minus17_shared_exits",len(sh))
print("minus28_fixed_residues",X,Y)
