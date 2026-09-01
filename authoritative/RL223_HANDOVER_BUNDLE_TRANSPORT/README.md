# RL223 handover bundle transport

Transport mode: **Git-tree deterministic reconstruction**.

The completed RL222 payload is stored losslessly as the authoritative Git tree
`bd66f5e84994fcc4faaadecba21fda6e791354c0` under
`RL222_Full_Period_Quotient_Residue_Structural_Blindness_2026-09-01/`.

To reconstruct the canonical ZIP, materialize that tree exactly and run its
`reconstruct_rl222_bundle.py`.  The expected ZIP SHA256 is
`c06efedb92d1d46d15a93f7648a26bfedec6471609cde3d0b2318cd247661eb2`.

The internal `SHA256SUMS.txt`, portable verifiers, fresh-unpack review, proof state,
and unique RL223 target are all inside the completed tree.  This transport avoids
copying large base64 fragments while remaining lossless and independently hashable.
