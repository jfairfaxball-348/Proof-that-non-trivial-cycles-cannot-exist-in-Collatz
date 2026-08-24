# RL59 exploratory computation status

These files are preserved for reproducibility and context. They are not all promoted proof certificates.

Notable items:

- `target_cut_reachability.*`: relaxed exact reachability hits `(73,47,1,3)`.
- `target_cut_defect_mitm_allcones.*`: targeted meet-in-the-middle exact DP finds minimum defect `~0.847046` at the same target; the standalone replay verifier is the cleaner promoted certificate.
- `terminal_q18_event_search.*`: early bounded terminal-Q exploration; superseded conceptually by the normalized-P theorem.
- `terminal_smallz_exact_verifier.out`: exact small-z terminal event capacity checks for z=41,43,45; superseded by the uniform normalized-P / final-tail approach.
- other height-one / reverse-terminal scripts: exploratory routes toward the final-tail event grammar.

Do not promote an exploratory output without reconstructing its hypotheses and role.
