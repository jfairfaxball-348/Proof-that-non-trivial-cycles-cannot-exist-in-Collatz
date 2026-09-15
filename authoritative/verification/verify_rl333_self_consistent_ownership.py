#!/usr/bin/env python3
"""RL333: rerun exact ownership reconstruction at the promoted lower bootstrap."""
from collections import Counter
from pathlib import Path

source_path = Path(__file__).with_name("verify_rl331_self_consistent_ownership.py")
source = source_path.read_text(encoding="utf-8")
old = "H=32_551_214_209; CAP=H-1; OWNED_TOTAL=44"
new = "H=32_548_554_425; CAP=H-1; OWNED_TOTAL=44"
assert source.count(old) == 1
# Remove inherited exact row/cardinality assertions which are expected to change,
# while retaining every construction and all other physical consistency checks.
source = source.replace("assert by_pair=={", "OLD_BY_PAIR = {")
source = source.replace("}\nleft_index=defaultdict(list)", "}\nleft_index=defaultdict(list)", 1)
source = source.replace("assert len(rows)==13556 and len(links)==14 and not self_links", "assert len(links)==14 and not self_links")
source = source.replace("assert Counter(r[0]+r[1] for r in large)=={45:4759,46:1634,47:556,48:173,49:46,50:14,51:6}", "pass")
source = source.replace("assert len(large)==7188 and len({r[:2] for r in large})==231", "assert len({r[:2] for r in large})==231")
source = source.replace(old, new)
exec(compile(source, str(source_path) + "[RL333-bootstrap]", "exec"), globals())
assert H == 32_548_554_425 and CAP == 32_548_554_424
assert len(rows) == 13_558
assert len(large) == 7_189
assert by_pair[(4,40)] == 260 and by_pair[(5,39)] == 379
for p,v in OLD_BY_PAIR.items():
    assert by_pair[p] == v + (1 if p in {(4,40),(5,39)} else 0)
assert Counter(r[0]+r[1] for r in large)=={45:4760,46:1634,47:556,48:173,49:46,50:14,51:6}
assert len(links)==14 and len(large_links)==14
assert len(large_to_t44)==7 and len(t44_to_large)==6
assert len(allowed_large_short)==282 and len(allowed_t44_short)==166
assert p2_counts == {45:2030,46:707,47:270,48:93,49:34,50:11,51:2}
assert len(states)==323 and len(edges)==26_514
assert min(pot)==0 and max(pot)==53 and b2==129
print("RL333_SELF_CONSISTENT_OWNERSHIP_GREEN")
print("bootstrap",H,"cap",CAP)
print("rows",len(rows),"large",len(large),"graph",len(states),len(edges))
