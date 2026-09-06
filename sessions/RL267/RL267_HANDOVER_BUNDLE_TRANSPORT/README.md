# RL267 canonical bundle transport

This directory is a lossless text transport of the canonical RL267 ZIP for connector/Git-object workers.

Canonical bundle:
`RL267_Radius5_Kappa1_311_221_Closure_2026-09-06.zip`

Canonical SHA256:
`412a96aa16b58db5184a5e263a424668bc8bb453a1b9a2711ad8c09e95fca0d9`

Reconstruction:

```sh
sha256sum -c PART_SHA256SUMS.txt
python3 reconstruct_rl267_bundle.py
```

The reconstruction script concatenates the numbered base64 parts, decodes them, and requires the canonical ZIP SHA256 above. The canonical ZIP itself contains the internal `SHA256SUMS.txt`, proof-state reports, successor authority, portable primary verifiers, and independent red-team sources/outputs.
