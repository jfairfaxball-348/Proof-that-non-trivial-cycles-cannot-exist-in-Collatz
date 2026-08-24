from math import log

alpha=log(2)/log(3)

def T(x):
    return (3*x+1)//2 if x&1 else x//2

def good_prefix(x,steps=600):
    ones=0
    seen={}
    # exact integer comparison 3^ones >= 2^j, update powers incrementally bigints
    p3=1; p2=1
    for j in range(steps):
        # state before step j; bit at this step
        if x in seen:
            # cycle found; still continue enough to verify density numerically/exactly
            pass
        if x&1:
            ones+=1; p3*=3
        p2*=2
        if p3 < p2:
            return False,j+1,None
        x=T(x)
    return True,steps,x

def cycle_info(x,limit=5000):
    seen={}
    bits=[]
    for j in range(limit):
        if x in seen:
            i=seen[x]
            return (i,j-i,x,bits[i:j])
        seen[x]=j
        bits.append(x&1)
        x=T(x)
    return None

hits=[]
for R in range(-5,-2000001,-32): # -5 ==27 mod32
    ok=True
    for c in (0,12,4):
        g,_,_=good_prefix(R+c,400)
        if not g:
            ok=False; break
    if ok:
        infos=[cycle_info(R+c) for c in (0,12,4)]
        hits.append((R,infos))
        print('HIT',R)
        for c,inf in zip((0,12,4),infos):
            if inf:
                pre,per,state,bits=inf
                print(' c',c,'pre',pre,'period',per,'state',state,'ones',sum(bits),'bits',''.join(map(str,bits)))
            else: print(' c',c,'no cycle')
        if len(hits)>=20: break
print('total hits',len(hits))
