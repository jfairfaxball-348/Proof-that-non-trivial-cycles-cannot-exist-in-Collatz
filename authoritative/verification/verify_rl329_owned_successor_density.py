#!/usr/bin/env python3
"""Exact RL329 certificate: owned singleton successor pruning and carry contraction."""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from math import gcd
A=217_976_794_617; ELL=137_528_045_312; D=A-ELL
LAMBDA_UPPER=1+Fraction(1,1<<40); M_LOWER=1<<71; STATE_UPPER=(1<<76)+(1<<36)
THRESHOLD=32_562_630_354; NEW_CAP=THRESHOLD-1; RHO=60; T=ELL-RHO

def log_interval_atanh(x,terms=280):
    x2=x*x; term=x; total=Fraction(0)
    for index in range(terms): total+=term/(2*index+1); term*=x2
    lower=2*total; upper=lower+2*term/(2*terms+1)/(1-x2)
    return lower,upper
ln2_lower,ln2_upper=log_interval_atanh(Fraction(1,3)); ln3_lower,ln3_upper=log_interval_atanh(Fraction(1,2))
delta_upper=A*ln2_upper-ELL*ln3_lower; assert delta_upper>0

@lru_cache(maxsize=None)
def mechanical_factors(length):
    cuts=sorted({0,ELL,*(((-D*step)%ELL) for step in range(length+1))}); factors=set()
    for left,right in zip(cuts,cuts[1:]):
        for residue in {left,min(left+1,right-1)}:
            previous=(residue+ELL-1)//ELL; gaps=[]
            for step in range(1,length+1):
                current=(residue+D*step+ELL-1)//ELL; gaps.append(1+current-previous); previous=current
            factors.add(tuple(gaps))
    assert len(factors)==length+1; return tuple(sorted(factors))

def forced_residue(gaps):
    constant=0
    for step,gap in enumerate(gaps,1): constant=(1<<gap)*constant+3**(step-1)
    modulus=3**len(gaps); residue=constant*pow(pow(2,sum(gaps),modulus),-1,modulus)%modulus
    return residue,modulus

def reconstruct(endpoint,gaps):
    states=[endpoint]; state=endpoint
    for gap in gaps:
        numerator=(1<<gap)*state-1; assert numerator%3==0; state=numerator//3; assert state&1; states.append(state)
    return tuple(states)

def band_realizations(gaps):
    residue,modulus=forced_residue(gaps); lift=max(0,(M_LOWER-residue+modulus-1)//modulus); endpoint=residue+lift*modulus
    while endpoint<STATE_UPPER:
        if endpoint&1: yield endpoint,reconstruct(endpoint,gaps)
        endpoint+=modulus

singleton_rows=[]
for total in range(45,99):
    for left_zero in range(max(1,total-49),min(49,total-1)+1):
        right_zero=total-left_zero
        for baseline in mechanical_factors(total):
            if baseline[left_zero]!=2: continue
            gaps=list(baseline); gaps[left_zero-1]+=1; gaps[left_zero]-=1
            for endpoint,states in band_realizations(tuple(gaps)):
                if delta_upper*min(states)>=THRESHOLD:
                    singleton_rows.append((tuple(states[:left_zero]),tuple(states[left_zero+1:]),left_zero,right_zero,endpoint))
singleton_counts=Counter(row[2]+row[3] for row in singleton_rows)
assert singleton_counts=={45:4755,46:1633,47:556,48:173,49:46,50:14,51:6}
pair_counts={total:len({(row[2],row[3]) for row in singleton_rows if row[2]+row[3]==total}) for total in singleton_counts}
assert pair_counts=={45:44,46:45,47:46,48:47,49:29,50:14,51:6}; assert len(singleton_rows)==7183

left_index=defaultdict(list)
for index,row in enumerate(singleton_rows): left_index[(row[2],row[0][0])].append(index)
physical_links=[]
for first_index,first in enumerate(singleton_rows):
    for second_index in left_index[(first[3],first[1][0])]: physical_links.append((first_index,second_index))
pair_links={((singleton_rows[first][2],singleton_rows[first][3]),(singleton_rows[second][2],singleton_rows[second][3])) for first,second in physical_links}
assert len(physical_links)==14
assert pair_links=={((1,44),(44,1)),((1,45),(45,1)),((1,45),(45,2)),((1,45),(45,3)),((1,45),(45,4)),((2,43),(43,2)),((2,44),(44,1)),((2,45),(45,1)),((2,45),(45,2)),((2,45),(45,3)),((2,45),(45,4)),((3,42),(42,3)),((3,43),(43,2))}

two_positive=[]
for zero_total in range(45,99):
    gap_length=zero_total+1
    for left_zero in range(max(1,zero_total-49),min(49,zero_total-1)+1):
        for baseline in mechanical_factors(gap_length):
            for first_height in (1,2):
                gaps=list(baseline)
                for offset,change in enumerate((first_height,1-first_height,-1)): gaps[left_zero-1+offset]+=change
                if min(gaps[left_zero-1:left_zero+2])<1: continue
                for _,states in band_realizations(tuple(gaps)):
                    if delta_upper*min(states)>=THRESHOLD: two_positive.append(zero_total)
assert Counter(two_positive)=={45:2029,46:707,47:270,48:93,49:34,50:11,51:2}; p2_max=max(two_positive); assert p2_max==51

@lru_cache(maxsize=None)
def singleton_gap_candidates(pair):
    left_zero,right_zero=pair; total=left_zero+right_zero; candidates=[]
    for baseline in mechanical_factors(total):
        if baseline[left_zero]!=2: continue
        gaps=list(baseline); gaps[left_zero-1]+=1; gaps[left_zero]-=1; gaps=tuple(gaps); residue,modulus=forced_residue(gaps); candidates.append((residue,modulus,gaps))
    return tuple(candidates)
def short_successor_possible(left_state,pair):
    for residue,modulus,gaps in singleton_gap_candidates(pair):
        if left_state%modulus!=residue: continue
        states=reconstruct(left_state,gaps)
        if delta_upper*min(states)>=THRESHOLD: return True
    return False
rows_by_pair=defaultdict(list)
for row in singleton_rows: rows_by_pair[(row[2],row[3])].append(row)
allowed_short_after_large=set()
for pair,rows in rows_by_pair.items():
    current_zero=pair[1]
    for next_zero in range(1,45-current_zero):
        target_pair=(current_zero,next_zero)
        if any(short_successor_possible(row[1][0],target_pair) for row in rows): allowed_short_after_large.add((pair,next_zero))
assert len(allowed_short_after_large)==286

large_pairs=sorted(rows_by_pair); states=[("N",zero) for zero in range(1,50)]+[("L",pair) for pair in large_pairs]; state_index={state:index for index,state in enumerate(states)}; pairs_by_left=defaultdict(list)
for pair in large_pairs: pairs_by_left[pair[0]].append(pair)
edges=[]
for state in states:
    source=state_index[state]; current_zero=state[1] if state[0]=="N" else state[1][1]
    for next_zero in range(1,50):
        if current_zero+next_zero<=44 and (state[0]=="N" or (state[1],next_zero) in allowed_short_after_large): edges.append((source,state_index[("N",next_zero)],next_zero,1))
    for pair in pairs_by_left[current_zero]:
        if state[0]=="N" or (state[1],pair) in pair_links: edges.append((source,state_index[("L",pair)],pair[1],1))
    for next_zero in range(1,50):
        if current_zero+next_zero<=p2_max: edges.append((source,state_index[("N",next_zero)],next_zero,2))
        edges.append((source,state_index[("N",next_zero)],next_zero,3))
assert len(states)==280; assert len(edges)==22991

potential=[0]*len(states)
for iteration in range(len(states)+1):
    changed=False
    for source,target,zero_gain,positive_cost in edges:
        weight=zero_gain-22*positive_cost
        if potential[source]+weight>potential[target]: potential[target]=potential[source]+weight; changed=True
    if not changed: break
else: raise AssertionError("positive max-plus cycle at coefficient 22")
assert iteration+1==2
assert all(potential[source]+zero_gain-22*positive_cost<=potential[target] for source,target,zero_gain,positive_cost in edges)
assert min(potential)==0 and max(potential)==26
boundary=max(zero-potential[state_index[("N",zero)]] for zero in range(1,50))+max(potential); assert boundary==66
K=(T+1-boundary+22)//23; assert K==5_979_480_226

x_lower=ln2_lower/ELL; full_sum_upper=1/(2*(x_lower+x_lower*x_lower/2))-Fraction(1,2)
def omitted_lower(last_r): return sum((Fraction(1<<((A*r)//ELL),3**r) for r in range(1,last_r+1)),Fraction(0))/LAMBDA_UPPER
ideal_partial_upper=(full_sum_upper-omitted_lower(RHO-1))/3; assert gcd(A,ELL)==1
def weighted_residue_lower(count):
    sum_r=count*(count+1)//2; sum_r2=count*(count+1)*(2*count+1)//6; sum_r3=sum_r**2; sum_r4=count*(count+1)*(2*count+1)*(3*count**2+3*count-1)//30
    return Fraction(count,1)+ln2_lower*sum_r/ELL+ln2_lower**2*sum_r2/(2*ELL**2)+ln2_lower**3*sum_r3/(6*ELL**3)+ln2_lower**4*sum_r4/(24*ELL**4)
weighted_sum_lower=weighted_residue_lower(K); loss_lower=weighted_sum_lower/(12*LAMBDA_UPPER); carry_rhs_upper=1+ideal_partial_upper-loss_lower
assert NEW_CAP<carry_rhs_upper<THRESHOLD
rho59_carry_upper=Fraction(5,6)+LAMBDA_UPPER*(1<<((D*59)//ELL)); assert rho59_carry_upper<NEW_CAP
max_x=ln2_lower*K/ELL; max_weight_polynomial=1+max_x+max_x**2/2+max_x**3/6+max_x**4/24
assert max_weight_polynomial<2; assert max_weight_polynomial/(12*LAMBDA_UPPER)<Fraction(1,6*LAMBDA_UPPER)
print("RL329_OWNED_SUCCESSOR_DENSITY_VERIFIER_GREEN")
print("singleton_counts",dict(sorted(singleton_counts.items())))
print("pair_counts",dict(sorted(pair_counts.items())))
print("large_large_physical_links",len(physical_links))
print("large_large_pair_links",len(pair_links))
print("allowed_large_to_short_pair_transitions",len(allowed_short_after_large))
print("two_positive_counts",dict(sorted(Counter(two_positive).items())))
print("states_edges",len(states),len(edges))
print("density_boundary",boundary)
print("positive_excess_min_at_rho60",K)
print("carry_rhs_upper_lt",float(carry_rhs_upper))
print("new_carry_cap",NEW_CAP)
