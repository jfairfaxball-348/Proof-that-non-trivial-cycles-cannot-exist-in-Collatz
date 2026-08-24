# RL58 audit/divisibility session — start here

Date: 2026-08-23

This handover continues the Collatz R-sharp/RL research from RL57. It is deliberately framed as an **audit-first** session because RL57 produced one independently checked certificate and two stronger but still discovery-stage certificates.

## Immediate status

RL57 does **not** close the safe-CF survivor, Gate A, Gate B, RL, or Collatz.

The strongest promoted RL57 result is the independent C++ audit of the RL56 coupled-K viable-prefix certificate

`Zx_26 <= 33/4`.

Together with the inherited strict total requirement `Zx>143/12`, this promotes the survivor-local conclusion

`Zx_late > 11/3`.

RL57 also found two stronger exact computations:

- defect-aware viable prefix: `Zx_26 <= 77/10`;
- aligned (`r=0`) viable prefix: `M0_26 <= 17/3`.

These two are **independent-audit pending**. Do not promote them until a structurally independent implementation agrees.

If the `17/3` certificate survives, then the inherited defect budget forces

`M0_late > 5/4`,

where `M0` is x-zero mass with displacement `r=0`. This localizes the main suffix problem to height-one `00` runs and is sharper than the earlier mixed `r<=1` target.

## Run first

From the bundle root:

```bash
bash verification/run_all_rl57_to_rl58_verifiers.sh
```

This checks the inherited RL56->RL57 checksum, recompiles the new RL57 C++ verifiers from source, reruns the promoted `33/4` audit and the two audit-pending searches, and checks the exact target-8 defect diagnostic.

A full rerun of the inherited RL56->RL57 verifier chain remains available under

`inherited_rl56_to_rl57/Collatz_Rsharp_RL56_to_RL57_Audit_Handover_2026-08-23/verification/`.

Treat any verifier failure as a stop-and-repair event.

## Read next

1. `RL57_FINAL_PROOF_STATE_AND_RL58_AUDIT_ROADMAP.md`
2. `RL57_NEW_CERTIFICATES_AND_LOCAL_GRAMMAR_NOTES_2026-08-23.md`
3. `RL58_AUDIT_AND_TERMINAL_DIVISIBILITY_KICKOFF_PROMPT_2026-08-23.md`

The old RL56 roadmap is preserved inside `inherited_rl56_to_rl57/` and should remain the baseline for anything not explicitly superseded here.
