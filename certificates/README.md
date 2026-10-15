# Retained certificate and exploration outputs

The four JSON files in this directory are retained outputs from the supplied later bundle. They are historical evidence, not newly generated receipts for the hardened code or integrated fixed-k manuscript. Their mathematical witnesses remain unchanged. Use [the clean replay](../REPLAY.md) and its fresh output hashes to assess the current certifiers.

* `cert_lower_mix.json`: 36-policy lower certificate.
* `cert_upper2.json`: 41-atom profile upper barrier.
* `theta_cert.json`: k=2 nonlinear-system comparison.
* `cert_det_T24.json`: simpler deterministic policy.

`numerical-context/do_k2.log` and `numerical-context/do2_k2_J320.log` are floating-point double-oracle exploration logs. A grid minimum may miss off-grid behavior; an ordinary ODE value is not a certified upper bound. None of these exploration estimates is a replacement for a rational witness and a verified enclosure. No new numerical k≥3 claim is supported here.
