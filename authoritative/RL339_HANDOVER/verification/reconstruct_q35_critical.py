"""Gap-free q35 nonnegative high-to-high candidate escape; PROMOTED; see RL339 certificate.

This scans all p=5..8 critical pair/profile/factor words and every odd
residue lift in the inherited q=0 source band. It intentionally omits the
high-carry ownership filter, so the scanned set is a superset of live rows.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

path=Path(__file__).resolve().parents[1]/"inherited/verify_rl338_q35_exhaustive.py"
spec=spec_from_file_location("rl338_exhaustive",path)
v=module_from_spec(spec)
spec.loader.exec_module(v)

expected={5:(196,64120,299),6:(168,140992,20),7:(112,209938,2),8:(56,271326,0)}
def escape(x):
    for step in range(1001):
        if x<v.LOW:return step
        y=3*x+1
        x=y//(y&-y)
    raise AssertionError("candidate did not escape below 2^71 within 1000 odd steps")

total=0
max_escape=0
for p in (5,6,7,8):
    pairs=templates=candidates=0
    sources=set()
    for left in range(22,36):
        if 2*left-8*p<0:continue
        for right in range(22,36):
            pairs+=1
            for gaps,profile in v.templates((left,right),p):
                templates+=1
                for source,states in v.candidates(gaps):
                    candidates+=1
                    sources.add(source)
    assert (pairs,templates,candidates)==expected[p]
    results=[escape(source) for source in sources]
    if results:max_escape=max(max_escape,max(results))
    total+=candidates
    print("layer",p,"pairs",pairs,"templates",templates,
          "candidates",candidates,"sources",len(sources),
          "max_escape",max(results,default=0),flush=True)
assert total==321
assert max_escape==39
print("CRITICAL_Q35_ESCAPE_GREEN","candidates",total,"maximum_escape",max_escape)
