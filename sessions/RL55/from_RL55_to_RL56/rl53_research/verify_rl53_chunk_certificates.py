#!/usr/bin/env python3
import pathlib,re,sys
ROOT=pathlib.Path(__file__).resolve().parent
checks=[
 ('z39_exact11_chunks.txt',128,67),
 ('z39_exact12_chunks.txt',512,67),
]
for fn,n,expect in checks:
    p=ROOT/fn
    lines=p.read_text().splitlines()
    seen=[]; maxima=[]
    for line in lines:
        m=re.search(rf'chunk=(\d+)/{n}\b',line)
        mm=re.search(r'\bmax=(-?\d+)\b',line)
        if not m or not mm:
            raise SystemExit(f'{fn}: malformed line: {line}')
        seen.append(int(m.group(1))); maxima.append(int(mm.group(1)))
    missing=sorted(set(range(n))-set(seen))
    dup=len(seen)-len(set(seen))
    if missing or dup or len(lines)!=n:
        raise SystemExit(f'{fn}: coverage failure lines={len(lines)} missing={missing[:10]} duplicates={dup}')
    got=max(maxima)
    if got!=expect:
        raise SystemExit(f'{fn}: max {got}, expected {expect}')
    if any(v>=900000 for v in maxima):
        raise SystemExit(f'{fn}: ambiguity/error sentinel present')
    print(f'{fn}: PASS chunks={n}/{n} global_max={got}')
print('RL53 chunk certificate audit: PASS')
