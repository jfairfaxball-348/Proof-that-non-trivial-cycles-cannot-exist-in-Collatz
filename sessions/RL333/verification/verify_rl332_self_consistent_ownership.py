#!/usr/bin/env python3
"""RL332 dependency: rerun the inherited exact ownership reconstruction at the promoted lower bootstrap."""
from pathlib import Path

source_path = Path(__file__).with_name("verify_rl331_self_consistent_ownership.py")
source = source_path.read_text(encoding="utf-8")
old = "H=32_551_214_209; CAP=H-1; OWNED_TOTAL=44"
new = "H=32_550_361_322; CAP=H-1; OWNED_TOTAL=44"
assert source.count(old) == 1
source = source.replace(old, new)
exec(compile(source, str(source_path) + "[RL332-bootstrap]", "exec"), globals())
assert H == 32_550_361_322 and CAP == 32_550_361_321
assert len(rows) == 13_556
assert len(large) == 7_188
assert len(links) == 14 and len(large_links) == 14
assert len(large_to_t44) == 7 and len(t44_to_large) == 6
assert len(allowed_large_short) == 282 and len(allowed_t44_short) == 166
assert p2_counts == {45:2030,46:707,47:270,48:93,49:34,50:11,51:2}
assert len(states) == 323 and len(edges) == 26_514
assert min(pot) == 0 and max(pot) == 53 and b2 == 129
print("RL332_SELF_CONSISTENT_OWNERSHIP_GREEN")
print("bootstrap", H, "cap", CAP)
