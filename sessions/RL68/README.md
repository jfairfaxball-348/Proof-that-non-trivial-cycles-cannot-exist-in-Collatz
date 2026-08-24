# Collatz R♯ / RL Research Repository

This repository houses the research bundles, mathematical proofs, verification code, and session-state ledgers for the **Collatz R♯ / RL** research program investigating nontrivial cycles in the Collatz (`3n + 1`) dynamical system.

---

## Repository Structure & Architecture

The repository is organized into three primary tiers:

```text
.
├── authoritative/   # Current authoritative three-file research handover
├── sessions/        # Frozen, searchable historical session mirrors (RL00, RL01, ...)
└── Archive/         # Original immutable historical ZIP bundles and sidecars
```

### 1. Current Authoritative Handover (`authoritative/`)

The [`authoritative/`](authoritative/) directory contains the **sole, current authoritative three-file research handover** for the ongoing investigation:

1. **Session Bundle (`.zip`)**: The primary archive containing all current mathematical theorems, verifiers, test runners, and certificates.
2. **Sidecar Checksum (`.zip.sha256`)**: The SHA-256 sidecar verifying the integrity of the ZIP bundle.
3. **Session State & Kickoff Ledger (`.md`)**: The Markdown ledger summarizing proven theorems, open gates, active invariants, dependency trees, and the kickoff prompt for the next research phase.

Any new research session begins directly from the three files present in `authoritative/`.

### 2. Searchable Historical Sessions (`sessions/`)

The [`sessions/`](sessions/) directory contains extracted, searchable mirrors of historical research iterations (`sessions/RL00/`, `sessions/RL01/`, etc.):

- Provides full-text and GitHub code search over historical mathematical notes, verifiers (`.py`, `.cpp`, `.sh`), and test outputs.
- Contains a `SOURCE_BUNDLE.md` in each session directory documenting the source archive, SHA-256 hashes, sidecar verification status, and git provenance.
- Serves as the long-term historical archive when handovers are rotated out of `authoritative/`.

> [!IMPORTANT]
> **Provenance Precedence**: Extracted session directories are convenience and search mirrors. When mathematical provenance or exact byte integrity matters, the canonical ZIP archives, their `.sha256` sidecars, internal checksum manifests (`SHA256SUMS.txt`), and verifier logs take precedence.

### 3. Canonical Historical Archives (`Archive/`)

The [`Archive/`](Archive/) directory contains original, immutable historical `.zip` handover bundles, standalone research notes, and historical SHA-256 sidecars. These files are permanent records of the research trajectory and are preserved without modification.

---

## Session Rollover Procedure

When an RL research session finishes and produces a new three-file handover, the handover transition is self-contained:

### 1. Before Rollover

`authoritative/` holds the previous session's three files:

```text
authoritative/
├── PREVIOUS_SESSION.zip
├── PREVIOUS_SESSION.zip.sha256
└── PREVIOUS_SESSION_STATE_AND_KICKOFF.md
```

### 2. Archiving the Previous Handover

Move the previous three authoritative files into the corresponding historical session directory:

```bash
mkdir -p sessions/RLXX/handover
mv authoritative/* sessions/RLXX/handover/
```

*(where `RLXX` is the session identifier being archived)*

### 3. Installing the New Handover

Place the newly completed session's three authoritative files directly into `authoritative/`:

```text
authoritative/
├── NEW_SESSION.zip
├── NEW_SESSION.zip.sha256
└── NEW_SESSION_STATE_AND_KICKOFF.md
```

### 4. Zero Repository-Wide Dependencies

Because `authoritative/` is the sole designated handover location:
- No `README.md`, index, pointer file, or top-level status document requires updating between sessions.
- No dynamic pointer files or symlinks are maintained.
- Downstream agents or researchers simply inspect `authoritative/` to resume work.
