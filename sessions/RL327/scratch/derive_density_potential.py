#!/usr/bin/env python3
"""Find an integer potential proving the sharp singleton bridge mean bound."""

nodes = range(1, 50)
special = {(3, 49), (4, 48)}


def singleton_allowed(left, right):
    return left + right <= 51 or (left, right) in special


# Difference constraints phi[right] >= phi[left] + left + right - 51.
phi = {node: 0 for node in nodes}
for _ in range(1000):
    changed = False
    for left in nodes:
        for right in nodes:
            if singleton_allowed(left, right):
                candidate = phi[left] + left + right - 51
                if candidate > phi[right]:
                    phi[right] = candidate
                    changed = True
    if not changed:
        break
else:
    raise AssertionError("positive cycle in singleton graph")

for left in nodes:
    for right in nodes:
        if singleton_allowed(left, right):
            assert left + right <= 51 + phi[right] - phi[left]

print("iterations", _ + 1)
print("potential_range", min(phi.values()), max(phi.values()))
print("nonzero_potential", {node: value for node, value in phi.items() if value})

# Cost-two-or-more positive runs connect arbitrary zero runs.  Verify that
# their crude 49-per-positive-position pair bound also dominates the same
# 51-per-position target, including the potential correction.
worst_slack = None
worst = None
for left in nodes:
    for right in nodes:
        for cost in (2, 3):
            slack = 51 * cost + phi[right] - phi[left] - left - right
            if worst_slack is None or slack < worst_slack:
                worst_slack = slack
                worst = (left, right, cost)
assert worst_slack >= 0
print("long_run_worst_slack", worst_slack, "at", worst)
