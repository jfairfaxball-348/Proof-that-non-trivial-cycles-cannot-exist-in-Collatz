# RL236 mandatory red-team report — 2026-09-02

Status: **PASS AFTER CLOSEOUT REPAIR**.

Checks:

1. **Necessary versus physical state:** retained cells remain a necessary-state superset; no physical realization is inferred from retention.
2. **Invariant-specific cap:** spacing `>=3032` is applied only to exact H20 `T=250157725494998535`, owners `{32,33,34,35}`.
3. **Coverage sweep:** every RL235 generic-overage candidate was rechecked at the final RL236 charge.  Only exact H20 `{32,33,34,35}`, H21 `{33,34,35}`, and H21 `{34,35,36,37}` exceed local budgets; each has its own exact occurrence cap.  H20 `T=216803362095665397`, owners `{32,33,34}` is exactly binding, not over budget.
4. **K-pricing:** local budget only; never converted into an occurrence theorem.
5. **Scratch stop-and-repair:** proposed `a≈7.8091U` / flow `>763` failed coverage because the distinct H20 `{32,33,34}` cell was uncapped.  Those claims are withdrawn.
6. **H21 scratch recurrence:** spacing `>=6251` is not promoted without final portable reproduction.
7. **Variation versus excursion:** promoted signed/K results are total variation only.
8. **Chronological versus rank order:** recurrence certificate uses chronological separation; no p-rank ordering substitution.
9. **Gate scope:** Gate A and Gate B remain independently open.

After the repair, no uncovered charged cell remains in the promoted schedule.
