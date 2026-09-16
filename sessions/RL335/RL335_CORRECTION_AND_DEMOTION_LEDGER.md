# RL335 correction and demotion ledger

Date: 2026-09-16
Status: FROZEN

## C1 — p=4 scratch count correction

An early scratch tally reported 72,091 p=4 templates. The corrected exhaustive enumeration gives 79,820. The earlier number was never promoted.

## C2 — `(37,37)` scratch count correction

An early scratch tally reported 237 p=4 templates for `(37,37)`. The corrected exhaustive enumeration gives 213, with zero physical realizations. The earlier number was never promoted.

## C3 — self-loop slack correction

An early spoken scratch value 144 for the `N37->N37`, p=5 fallback slack was arithmetic error. The exact value is `43*5-2*37=141`. Only 141 is promoted.

## C4 — inherited authority

No inherited authoritative theorem is demoted. RL334's q=22 theorem remains valid but is superseded in this branch by the stronger q=28 theorem after RL335's additional exact physical pruning.

## C5 — connector closeout transaction repair

During closeout, a mistaken contents-API call created a transient empty root file named `nonexistent` in commit `9123a0aedca799cb3d6d02517e21b83abc8e245b`, whose parent was the untouched RL334 base. No mathematical or authoritative file was changed in that transient commit. The final RL335 promotion commit replaces the whole root with the verified candidate tree, so the stray file is absent from final authority. Classification: mechanical closeout repair; no proof-state change.
