# Integrated claims and evidence map

Status: candidate version 0.1.0-candidate. Targeted integrated-source re-review completed with no mandatory mathematical revision remaining; see [review summary](REVIEW_SUMMARY.md) for exact input identities and limitations. Frozen-archive and publication gates remain pending. Labels below refer to the integrated LaTeX source, not obsolete theorem numbering.

| ID | Claim and hypotheses | Evidence | Boundary |
|---|---|---|---|
| A1 | For every fixed integer k≥1, γₙ,ₖ has a limit equal to the profile infimum and the closure-payoff maximin | paper.tex, `thm:general-k-game`; lower transfer, verification, upper transfer, compactness and two-endpoint approximation | Analytic, no numerical premise; no uniform-in-k statement or lim=infₙ conclusion |
| A2 | Quantile layer cake and fixed-policy lower transfer apply to every nonnegative iid law of finite positive mean, including atoms | `lem:general-k-lower-transfer`; conditional quantiles and stochastic telescoping | Zero-guarantee case handled separately; fixed mixture chosen before sufficiently large n |
| A3 | Profile ODE verifies optimal continuum reward; conservative barriers bound it; constructed finite-horizon laws transfer the upper bound | `lem:general-k-verification`, `prop:general-k-upper-transfer` | Layer measure is not an observation law; finite law includes zero mass |
| A4 | A bounded measurable occupancy-weighted deterministic quantile policy dominates any finite bounded-policy mixture | `prop:general-k-occupancy-domination` | Existing flow/concavity principle, not asserted novel; no equal-mesh or optimum-attainment claim |
| C1 | The 36-policy T=64 witness has cumulative payoff ≥0.83695 P₂ for all x≥0 | [mixture data](data/mix_fine.json), [certifier](code/cert_lower_mix.py); initial slope, all convex pieces, tail | Computer-assisted continuum statement plus A2 gives asymptotic lower bound |
| C2 | The 41-atom layer profile has optimal continuum ratio <0.8372914 | [profile data](data/inst_do450.json), [certifier](code/cert_upper2.py), 80000-step upward barriers | Plus A3 gives asymptotic upper bound, not a statement for every finite n |
| C3 | θ₁*+θ₂* < 5723787/6850000 < 0.835590 | [theta certifier](code/theta_cert.py), 2000-step barriers and interval integral | k=2 nonlinear system only; no causal attribution to the whole eta=0 restriction |
| C4 | γ₂ lies in [0.83695,0.8372914] and exceeds θ₁*+θ₂* by more than 18641/13700000 | A1–A3 and C1–C3, rational subtraction | Rounded headline upper endpoint 0.83730; not exact constant or midpoint |
| C5 | Supplied deterministic T=24 policy has cumulative payoff ≥0.8365 P₂ | [policy](data/policy_k2_T24.json), [certifier](code/certify_single.py), 400 subdivisions | Illustrative simpler witness, not proof of intrinsic mixture advantage |

The general-k backward-barrier formula is an analytic scheme, not a shipped numerical witness for k≥3. Historical k=3 checks and unsupported older upper estimates are not claims of this package. Floating-point double-oracle results and finite-n estimates are not certificate bounds.
