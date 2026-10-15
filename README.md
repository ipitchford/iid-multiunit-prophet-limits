# Asymptotic i.i.d. prophet inequalities: fixed-capacity limits and certified two-unit bounds

Scholarly creator: Anonymous. **Candidate version 0.1.0-candidate.** Targeted AI-assisted mathematical re-review and bound-PDF QA are complete; frozen-archive and provider-publication gates remain pending. See the [review and revision summary](REVIEW_SUMMARY.md).

Version: 0.1.0-candidate. Reserved DOI: `10.5281/zenodo.23404235` (concept identifier `10.5281/zenodo.23404234`). Reservation is not publication. The intended repository is `https://github.com/ipitchford/iid-multiunit-prophet-limits`; creation and public readback are pending. See [citation metadata](CITATION.cff).

For every fixed integer k≥1, the manuscript develops existence of the worst-case i.i.d. k-selection limit and its continuum minimax characterization. For k=2, exact rational witnesses and interval arithmetic give

**0.83695 ≤ γ₂ ≤ 0.8372914**, hence the rounded headline interval **[0.83695, 0.83730]**.

The nonlinear-system value satisfies θ₁*+θ₂* < 5723787/6850000, so γ₂−(θ₁*+θ₂*) > 18641/13700000. This disproves asymptotic tightness of that construction for k=2, not its valid lower-bound theorem or the entire restricted dual program.

## Model and scope

Observations are independent and identically distributed, nonnegative, from a known law with finite positive mean. The online policy selects at most k observations irrevocably; the prophet takes the k largest. The worst-case law may vary with horizon n. First fix k, then let n tend to infinity. The limit is an infimum over bounded-support step profiles and a maximum over the pointwise closure of cumulative policy payoffs.

The theorem is analytic. Executable certificates localize only k=2. Neither equality with the all-horizon infimum, a convergence rate uniform in k, an exact optimal constant, an extremizing profile, nor attainment by a bounded policy is claimed. Finite mixtures are useful certificate representations; occupancy-weighted deterministic quantile thresholds dominate them, without necessarily retaining the original equal mesh. Randomizing within atoms to realize conditional quantiles is separate.

## Read and reproduce

* [Manuscript source](paper.tex) and [PDF](paper.pdf): mathematical definitions, proofs and certificate arguments. The 13-page PDF has completed text/rendering QA against the source identified in the [review summary](REVIEW_SUMMARY.md); this is not accessibility certification.
* [Claims map](claims.md): analytic versus computer-assisted dependencies and exclusions.
* [Replay instructions](REPLAY.md): a new output directory, python-flint 0.9.0, normal and optimized Python, semantic negative controls.
* [Assurance](ASSURANCE.md), [provenance](PROVENANCE.md), [status](STATUS.md), and [licence map](LICENSES.md).
* [Sources](SOURCES.md) and [citation audit](CITATION_AUDIT.md): predecessor comparisons and bounded search limits.
* [AI index](AI_INDEX.md): structured reader route through statements, witnesses and trust boundaries.

With python-flint 0.9.0 available in an isolated environment:

```sh
python -B code/replay.py /absolute/path/to/new-replay-directory
```

The parent directory must exist; the output directory must not. No original log is overwritten, no optimizer is run, and the runner does not install packages or use the network. See [replay receipt](REPLAY_RECEIPT.md) for actual pre-freeze executions and their limits.

## Witness inventory

| File | Role |
|---|---|
| [mix_fine.json](data/mix_fine.json) | 36 rational policies, k=2, T=64; mixture lower certificate |
| [inst_do450.json](data/inst_do450.json) | 41-atom positive layer measure generating an upper-witness value profile; not itself an observation probability law |
| [policy_k2_T24.json](data/policy_k2_T24.json) | Simpler deterministic 24-piece policy with guarantee 0.8365 |
| [certificates](certificates/README.md) | Retained historical outputs and numerical exploration, explicitly separated from fresh replay |

The integrated paper supersedes two overlapping unpublished notes. Old completion labels and provisional quality scores are not evidence for this changed manuscript. No human peer review, independent reproduction, formal verification, or predetermined quality rating is asserted.
