"""Independent total-43 singleton source/escape audit; PROMOTED; see RL339 certificate."""
from collections import Counter

A = 217976794617
ELL = 137528045312
D = A-ELL
LOW = 1 << 71
UP = (1 << 76) + (1 << 36)

def ceil_div(x,y):
    return -(-x//y)

def words(length):
    cuts=sorted({0, ELL, *((-D*j)%ELL for j in range(length+1))})
    result=set()
    for lo,hi in zip(cuts,cuts[1:]):
        for phase in (lo,min(lo+1,hi-1)):
            result.add(tuple(1+ceil_div(phase+D*j,ELL)-ceil_div(phase+D*(j-1),ELL)
                             for j in range(1,length+1)))
    assert len(result)==length+1
    return result

def trajectory(x):
    for step in range(1001):
        if x<LOW:return step
        triple=3*x+1
        x=triple//(triple&-triple)
    raise AssertionError("unresolved deterministic trajectory")

base_words=words(43)
all_candidates=0
all_templates=0
max_steps=0
per_pair=[]
for low in range(8,22):
    high=43-low
    for left,right in ((low,high),(high,low)):
        template_count=candidate_count=0
        for base in base_words:
            gaps=list(base)
            gaps[left-1]+=1
            gaps[left]-=1
            if min(gaps)<1:continue
            template_count+=1
            modulus=3**len(gaps)
            C=0
            power=1
            for gap in gaps:
                C=(1<<gap)*C+power
                power*=3
            residue=(C*pow(1<<sum(gaps),-1,modulus))%modulus
            x=residue+max(0,ceil_div(LOW-residue,modulus))*modulus
            while x<UP:
                if x&1:
                    state=x
                    for gap in gaps:
                        numerator=(1<<gap)*state-1
                        if numerator%3:break
                        state=numerator//3
                        if state%2==0:break
                    else:
                        candidate_count+=1
                        max_steps=max(max_steps,trajectory(x))
                x+=modulus
        per_pair.append((left,right,template_count,candidate_count))
        all_templates+=template_count
        all_candidates+=candidate_count
assert len(per_pair)==28
assert all_templates==721
assert all_candidates==80403
assert max_steps==186
print("TOTAL43_RED_TEAM_GREEN", "pairs",len(per_pair),"templates",all_templates,
      "candidates",all_candidates,"max_escape",max_steps)
print("per_pair",per_pair)
