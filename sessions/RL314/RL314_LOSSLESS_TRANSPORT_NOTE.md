# RL314 lossless closeout transport note

Date: 2026-09-13

The semantic RL314 closeout tree was first promoted from incoming HEAD
`e443671d71b2320d42ba3d420bda33df55d7fb44` as commit
`51a14d452cf011b3b1fb1ad7f4098178dc26a49a`.

Post-push readback then showed that the repository's current
`verify-incoming-authority` workflow additionally requires the legacy conveyor
wrapper: one handover ZIP, its outer SHA-256 sidecar, and a predecessor-state
marker.  A second mechanical-only repair commit adds exactly that wrapper.  No
research result, route ranking, or RL315 target is changed by the repair.

The exact incoming authoritative files are archived by reusing their immutable
Git blob identities:

- incoming `authoritative/START_HERE.md` blob:
  `c62213e25d1b6c6367240c5f9edb49db3f0092be`;
- incoming `authoritative/RL314_FULL_STRATEGIC_AUDIT_TARGET.md` blob:
  `851805aca90e030dfb16060c3966ec7bdfa788b0`.

The mechanical handover wrapper is:

- `authoritative/RL314_SESSION_STATE_AND_RL315_KICKOFF.md`;
- `authoritative/RL314_to_RL315_Handover.zip`;
- `authoritative/RL314_to_RL315_Handover.zip.sha256`.

The ZIP contains a SHA256 manifest and portable fast verifier and is intended
only to satisfy fresh-unpack conveyor validation.  The canonical research state
remains the frozen `sessions/RL314/` audit plus the single RL315 target.
