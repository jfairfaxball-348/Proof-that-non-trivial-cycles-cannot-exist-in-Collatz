# Collatz R♯ / RL Research Archive

This repository houses the historical research bundles, verification scripts, and session state ledgers for the **Collatz R♯ / RL** program investigating nontrivial cycles in the Collatz (`3n + 1`) dynamical system.

---

## Current Authoritative Research State

The current authoritative incoming research state is **RL64** (2026-08-24):

- **Authoritative Handover Bundle**: [`authoritative/RL64/RL64_Full_Phase_Recovery_and_All_Word_Cylinder_Selector_2026-08-24.zip`](file:///authoritative/RL64/RL64_Full_Phase_Recovery_and_All_Word_Cylinder_Selector_2026-08-24.zip)
- **Matching Sidecar**: [`authoritative/RL64/RL64_Full_Phase_Recovery_and_All_Word_Cylinder_Selector_2026-08-24.zip.sha256`](file:///authoritative/RL64/RL64_Full_Phase_Recovery_and_All_Word_Cylinder_Selector_2026-08-24.zip.sha256)
- **Authoritative State Ledger**: [`RL64_SESSION_STATE_AND_KICKOFF_2026-08-24.md`](file:///RL64_SESSION_STATE_AND_KICKOFF_2026-08-24.md)
- **Current State Summary**: [`CURRENT_RESEARCH_STATE.md`](file:///CURRENT_RESEARCH_STATE.md)
- **Gate A Status**: **Open** (*"Gate A remains open"*). No result in RL64 proves Gate A, Gate B, RL closure, nontrivial-cycle exclusion, or the Collatz conjecture.

---

## Repository Structure & Navigation

```text
/
├── README.md                          # Repository overview & navigation guide (this file)
├── CURRENT_RESEARCH_STATE.md          # Pointer to current authoritative research state (RL64)
├── RESEARCH_INDEX.md                  # Comprehensive chronological index across all RL sessions
├── RL64_SESSION_STATE_AND_KICKOFF_... # Authoritative RL64 state ledger
│
├── authoritative/                     # Verified convenience copies of latest authoritative bundles
│   └── RL64/                          # Current authoritative RL64 ZIP + .sha256 sidecar
│
├── sessions/                          # Searchable extracted mirrors of historical RL iterations
│   ├── RL00/                          # Pre-RL Odometer / Packet Potential Handover
│   ├── RL02/                          # Suffix Obstruction & XiProbe
│   ├── RL05/                          # Seed & Ancestors RL3/RL4
│   ├── RL07/                          # Handover & Ancestor RL6
│   ├── ...
│   ├── RL63/                          # Even Exit Selector & Ownership Target
│   └── RL64/                          # Full Phase Recovery & All-Word Cylinder Selector
│
└── Archive/                           # Immutable historical ZIP archives, sidecars, and standalone notes
```

---

## Architecture & Provenance Rules

### 1. Canonical Archives (`Archive/` and root bundles)
All original `.zip` handover bundles and their corresponding `.sha256` sidecars are **immutable archival artifacts**. Their byte contents and sidecars are never modified, rewritten, or regenerated.

### 2. Searchable Extracted Mirrors (`sessions/`)
To enable full-text and GitHub code search across historical mathematical proofs, theorem statements, and verifiers, all historical handover bundles have been extracted into predictable session directories under `sessions/RLXX/`. Each session directory contains:
- The extracted source files (`.py`, `.cpp`, `.sh`, `.md`, certificates, logs);
- A `SOURCE_BUNDLE.md` documenting exact source archive paths, SHA-256 hashes, sidecar validation results, and Git commit provenance.

> [!IMPORTANT]
> **Extracted session directories are convenience/search mirrors.** When provenance matters, the corresponding ZIP, `.sha256` sidecar, internal checksum manifest (`SHA256SUMS.txt`), and verifier results take precedence.

### 3. Authoritative Pointer (`authoritative/` & `CURRENT_RESEARCH_STATE.md`)
The `authoritative/` directory provides a verified convenience pointer to the current latest handover bundle. Downstream research sessions should verify the authoritative sidecar and internal checksum manifest before trusting workspace files.

### 4. Complete Research Index (`RESEARCH_INDEX.md`)
For a complete chronological index of all research iterations from RL00 through RL64, see [`RESEARCH_INDEX.md`](file:///RESEARCH_INDEX.md).
