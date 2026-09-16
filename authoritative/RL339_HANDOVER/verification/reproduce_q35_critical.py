"""Independent exhaustive q35 nonnegative high-high escape audit; PROMOTED; see RL339 certificate."""
from functools import lru_cache

A=217976794617
ELL=137528045312
D=A-ELL
LOW=1<<71
UP=(1<<76)+(1<<36)

def ceil_div(a,b):return -(-a//b)

@lru_cache(None)
def mechanical_words(length):
    cuts=sorted({0,ELL,*((-D*j)%ELL for j in range(length+1))})
    words=set()
    for start,stop in zip(cuts,cuts[1:]):
        for r in (start,min(start+1,stop-1)):
            words.add(tuple(1+ceil_div(r+D*j,ELL)-ceil_div(r+D*(j-1),ELL)
                            for j in range(1,length+1)))
    assert len(words)==length+1
    return tuple(words)

@lru_cache(None)
def profiles(p):
    result=[(1,)]
    for i in range(p-1,0,-1):
        result=[(value,)+tail for tail in result
                for value in range(1,min(p-i+1,tail[0]+1)+1)]
    return tuple(result)

def candidates(gaps):
    modulus=3**len(gaps)
    C=0
    three=1
    for gap in gaps:
        C=(1<<gap)*C+three
        three*=3
    residue=(C*pow(1<<sum(gaps),-1,modulus))%modulus
    x=residue+max(0,ceil_div(LOW-residue,modulus))*modulus
    while x<UP:
        if x&1:
            y=x
            for gap in gaps:
                numerator=(1<<gap)*y-1
                if numerator%3:break
                y=numerator//3
                if y%2==0:break
            else:yield x
        x+=modulus

def escape(x):
    for step in range(1001):
        if x<LOW:return step
        y=3*x+1
        x=y//(y&-y)
    raise AssertionError("unescaped critical source")

expected={5:(196,64120,299,154,39),6:(168,140992,20,14,28),
          7:(112,209938,2,1,4),8:(56,271326,0,0,0)}
for p in range(5,9):
    pair_count=template_count=candidate_count=0
    sources=set()
    for left in range(22,36):
        if 2*left-8*p<0:continue
        for right in range(22,36):
            pair_count+=1
            length=left+right+p-1
            for base in mechanical_words(length):
                for profile in profiles(p):
                    ext=(0,)+profile+(0,)
                    gaps=list(base)
                    for offset in range(p+1):
                        index=left-1+offset
                        gaps[index]+=ext[offset+1]-ext[offset]
                        if gaps[index]<1:break
                    else:
                        template_count+=1
                        for source in candidates(gaps):
                            candidate_count+=1
                            sources.add(source)
    maximum=max((escape(x) for x in sources),default=0)
    got=(pair_count,template_count,candidate_count,len(sources),maximum)
    assert got==expected[p],(p,got)
    print("red_team_layer",p,got,flush=True)
print("CRITICAL_Q35_RED_TEAM_GREEN")
