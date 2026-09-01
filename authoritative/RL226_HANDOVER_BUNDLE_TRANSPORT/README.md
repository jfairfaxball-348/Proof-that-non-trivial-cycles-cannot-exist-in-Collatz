# RL226 handover bundle transport

Transport mode: **Git-tree deterministic reconstruction**.

The completed RL225 payload is stored losslessly as Git tree
`16fd08b39d7d7369475f88fbb9427f2f0391d3d7` under
`RL225_E4_Exact_Root_Window_and_Candidate_Coupled_Height_Transfer_2026-09-01/`.

To reconstruct the canonical ZIP, materialize that tree exactly and run its
`reconstruct_rl225_bundle.py`. The expected ZIP SHA256 is
`cb918207949451619a81e01a596d9455763711ad80da30e082e1aec05c0c4185`.

The internal `SHA256SUMS.txt`, portable e=4 transfer verifier, proof-state
verifier, red-team report, proof/correction ledgers, provenance, and unique RL226
target are all inside the completed tree. The matching outer `.zip.sha256`
sidecar is top-level in `authoritative/`.

This transport is lossless: every Git blob SHA and the complete package tree SHA
were matched independently against the clean local candidate before promotion,
and the reconstruction script reproduces the clean-unpack-verified canonical ZIP.
