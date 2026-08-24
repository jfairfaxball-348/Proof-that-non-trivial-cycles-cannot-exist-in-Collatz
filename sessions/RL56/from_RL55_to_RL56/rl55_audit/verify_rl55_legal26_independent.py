#!/usr/bin/env python3
from fractions import Fraction

CAP=Fraction(17,30)
TARGET=Fraction(143,12)
EXPECTED=Fraction(34057930625026471931596,2954312706550833698643)
EXPECTED_ZEROS=(2,5,7,10,14,15,18,21,25,26,29,32,34,37,40,44,45,48,51,53,56,59,62,64,67,70)

def step(d,J,x):
    if x==0:
        y=0 if J&1 else 1
    else:
        if J&1: y=1
        elif d==1: return None
        else: y=0
    if (x,y)==(0,0):
        num=J+3**d-2**d; dn=d
    elif (x,y)==(1,1):
        num=3*J+2**d-1; dn=d
    elif (x,y)==(0,1):
        num=3*J+3**(d+1)-2**d-1; dn=d+1
    else:
        num=J; dn=d-1
    if num%2: raise AssertionError((d,J,x,y,num))
    return dn,num//2

best=Fraction(-1)
bestword=''
# memo: at identical future state, only greatest accumulated mass matters.
memo={}
nodes=0

def dfs(i,p,left,d,J,total,word):
    global best,bestword,nodes
    nodes+=1
    key=(i,p,left,d,J)
    prev=memo.get(key)
    if prev is not None and prev>=total:
        return
    memo[key]=total
    g=Fraction(2**i,3**p)
    if left==0:
        if total>best:
            best,totalword=total,word
            bestword=totalword
        return
    # optimistic future bound: each remaining zero is <= CAP, and even with no
    # intervening x=1 columns successive zero weights are g,2g,4g,...
    if total+min(left*CAP,(2**left-1)*g)<=best:
        return
    if g<=CAP:
        s=step(d,J,0)
        if s is not None:
            dfs(i+1,p,left-1,*s,total+g,word+'0')
    s=step(d,J,1)
    if s is not None:
        dfs(i+1,p+1,left,*s,total,word+'1')

dfs(0,0,26,1,-13,Fraction(0),'')
zeros=tuple(i for i,c in enumerate(bestword) if c=='0')
assert best==EXPECTED,(best,EXPECTED)
assert zeros==EXPECTED_ZEROS,(zeros,EXPECTED_ZEROS)
gap=TARGET-best
assert gap==Fraction(4590516512150518575599,11817250826203334794572)
print('RL55 independent legal-prefix maximization: PASS')
print('best =',best)
print('decimal =',float(best))
print('zeros =',list(zeros))
print('gap =',gap,'=',float(gap))
print('nodes =',nodes,'memo states =',len(memo))
