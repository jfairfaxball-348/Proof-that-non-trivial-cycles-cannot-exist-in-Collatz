"""Independent in-band singleton total 44..70 audit; PROMOTED; see RL339 certificate."""
from functools import lru_cache

A=217976794617
ELL=137528045312
D=A-ELL
LOW=1<<71
UP=(1<<76)+(1<<36)
def ceil_div(a,b):return -(-a//b)

@lru_cache(None)
def words(length):
    cuts=sorted({0,ELL,*((-D*j)%ELL for j in range(length+1))})
    result=set()
    for lo,hi in zip(cuts,cuts[1:]):
        for r in (lo,min(lo+1,hi-1)):
            result.add(tuple(1+ceil_div(r+D*j,ELL)-ceil_div(r+D*(j-1),ELL)
                             for j in range(1,length+1)))
    assert len(result)==length+1
    return result

def escape(x):
    for step in range(1001):
        if x<LOW:return step
        y=3*x+1
        x=y//(y&-y)
    raise AssertionError("unescaped singleton candidate")

expected={44:26432,45:8680,46:2852,47:934,48:306,49:103,50:39,
          51:11,52:3,53:1}
all_pairs=all_templates=all_candidates=maximum=0
for total in range(44,71):
    pair_count=template_count=candidate_count=0
    for left in range(1,36):
        right=total-left
        if not 1<=right<=35:continue
        pair_count+=1
        for base in words(total):
            gaps=list(base)
            gaps[left-1]+=1
            gaps[left]-=1
            if min(gaps)<1:continue
            template_count+=1
            modulus=3**total
            C=0
            power=1
            for gap in gaps:
                C=(1<<gap)*C+power
                power*=3
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
                    else:
                        candidate_count+=1
                        maximum=max(maximum,escape(x))
                x+=modulus
    assert candidate_count==expected.get(total,0),(total,candidate_count)
    all_pairs+=pair_count
    all_templates+=template_count
    all_candidates+=candidate_count
assert (all_pairs,all_templates,all_candidates,maximum)==(378,11865,39361,185)
print("LARGE_SINGLETON_RED_TEAM_GREEN",all_pairs,all_templates,all_candidates,maximum)
