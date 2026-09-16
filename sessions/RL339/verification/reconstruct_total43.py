"""Exact total-43 singleton neutral-edge escape scan; PROMOTED; see RL339 certificate."""
from argparse import ArgumentParser
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ap=ArgumentParser()
ap.add_argument("low_lo",type=int)
ap.add_argument("low_hi",type=int)
a=ap.parse_args()
assert 8<=a.low_lo<=a.low_hi<=21
path=Path(__file__).resolve().parents[1]/"inherited/verify_rl338_q35_exhaustive.py"
spec=spec_from_file_location("rl338_exhaustive",path)
v=module_from_spec(spec)
spec.loader.exec_module(v)

def escape(start):
    x=start
    seen=set()
    for step in range(10001):
        if x<v.LOW:return step,"below_floor"
        if x in seen:return step,"repeat"
        seen.add(x)
        y=3*x+1
        x=y//(y&-y)
    return 10000,"unresolved"

summary=[]
for low in range(a.low_lo,a.low_hi+1):
    high=43-low
    for left,right in ((low,high),(high,low)):
        templates=candidates=owned=0
        sources=set()
        for gaps,profile in v.templates((left,right),1):
            templates+=1
            for source,states in v.candidates(gaps):
                candidates+=1
                sources.add(source)
                if v.delta_up*min(states)>=v.HC:
                    owned+=1
        outcomes={x:escape(x) for x in sources}
        unresolved=[x for x,(steps,status) in outcomes.items() if status!='below_floor']
        max_escape=max((steps for steps,status in outcomes.values() if status=='below_floor'),default=0)
        result=(left,right,templates,candidates,owned,len(sources),max_escape,len(unresolved))
        print("pair",result,flush=True)
        summary.append(result)
print("total_pairs",len(summary),"templates",sum(x[2] for x in summary),
      "candidates",sum(x[3] for x in summary),"owned",sum(x[4] for x in summary),
      "unresolved",sum(x[7] for x in summary))
print("RL339_PROMOTED")
