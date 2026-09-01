# RL225 handover bundle transport

Transport mode: **Git-tree deterministic reconstruction**.

The completed RL224 payload is stored losslessly as Git tree
`dcc255b3c10f15eea7ff8eb515355633eee83320` under
`RL224_Candidate_Coupled_Height_Closure_and_E16_Rank_Deletion_2026-09-01/`.

To reconstruct the canonical ZIP, materialize that tree exactly and run its
`reconstruct_rl224_bundle.py`. The expected ZIP SHA256 is
`fbd8eaf96f1ac75fd3fa21b5c036f514b282ccc3e1fa634a4036b1566065ac43`.

The internal `SHA256SUMS.txt`, portable reconstructive certificate, proof-state
verifier, red-team report, proof/correction ledgers, provenance, and unique RL225
target are all inside the completed tree. The matching outer `.zip.sha256`
sidecar is top-level in `authoritative/`.

This transport is lossless: the package tree SHA was independently reproduced
from the frozen local candidate before promotion, and the reconstruction script
reproduces the clean-unpack-verified canonical ZIP byte-for-byte.
