from itertools import product
B=15671092983
def Q(w):
 L=sum(w); p=[i for i,b in enumerate(w) if b]; return sum((1<<p[j])*3**(L-1-j) for j in range(L))
def T(n): return n//2 if n%2==0 else (3*n+1)//2
events=roots=strict=0
for A in range(2,15):
 for w in product((0,1),repeat=A):
  L=sum(w)
  if w[0]==1 and w[-1]==0:
   Z=A-L; q=Q(w); new=3**(L-1)+(1<<Z)*(3**(L-1)-2**(L-1)); old=(1<<(Z-1))*(3**L-2**L); assert q<=new<=old; roots+=1; strict+=new<old
  if L==0 or L==A: continue
  D=(1<<A)-3**L
  if D<=0 or Q(w)%D: continue
  n=Q(w)//D; x=n; orb=[]
  for _ in range(A): orb.append(x); x=T(x)
  assert x==n; m=min(orb); assert m&1 and m<=(L*(1<<A))//(3*D); events+=1
maxo=(-1,None); first=None; p3=3**40
for L in range(41,190538):
 p3*=3; A=p3.bit_length(); D=(1<<A)-p3; c=(L*(1<<A))//(3*D); o=c if c&1 else c-1
 if L<190537 and o>maxo[0]: maxo=(o,L)
 if first is None and o>B: first=(L,A,c,o)
assert maxo==(7216128937,158670); assert first==(190537,301994,984572842736,984572842735)
print('RL130 fast verifier: PASS'); print('divisible_events',events,'transition_roots',roots,'strict_improvements',strict); print('max_pre_wall',maxo,'first_failure',first)
