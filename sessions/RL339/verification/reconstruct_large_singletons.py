"""Gap-free in-band singleton scan for adjacent totals 44..70; PROMOTED; see RL339 certificate.

No high-carry filter is applied. Every odd residue lift in the inherited q=0
state band is checked, so the conclusion remains valid at a lower bootstrap.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

path=Path(__file__).resolve().parents[1]/"inherited/verify_rl338_q35_exhaustive.py"
spec=spec_from_file_location("rl338_exhaustive",path)
v=module_from_spec(spec)
spec.loader.exec_module(v)

def escape(x):
    seen=set()
    for step in range(10001):
        if x<v.LOW:return step,"below_floor"
        if x in seen:return step,"repeat"
        seen.add(x)
        y=3*x+1
        x=y//(y&-y)
    return 10000,"unresolved"

grand=Counter()
unresolved=[]
maximum=(0,0,0,0)
for total in range(44,71):
    pair_count=templates=candidates=0
    sources=set()
    for left in range(1,36):
        right=total-left
        if not 1<=right<=35:continue
        pair_count+=1
        for gaps,profile in v.templates((left,right),1):
            templates+=1
            for source,states in v.candidates(gaps):
                candidates+=1
                sources.add(source)
    for source in sources:
        steps,status=escape(source)
        if status!="below_floor":unresolved.append((total,source,steps,status))
        if status=="below_floor" and steps>maximum[0]:maximum=(steps,total,source,len(sources))
    print("total",total,"pairs",pair_count,"templates",templates,
          "candidates",candidates,"sources",len(sources),
          "unresolved",len(unresolved),flush=True)
    grand.update(pairs=pair_count,templates=templates,candidates=candidates)
print("aggregate",dict(grand),"maximum_escape",maximum,"unresolved",unresolved)
if unresolved:raise SystemExit(1)
print("LARGE_SINGLETON_ESCAPE_GREEN")
