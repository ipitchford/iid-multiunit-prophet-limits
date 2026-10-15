# Integrated-version review and revision summary

Candidate version: **0.1.0-candidate**. Assessment date: **2026-10-15**. This is a sanitized public summary of coordinated AI-assisted review and PDF quality assurance, not the private reports, human peer review, journal acceptance or publication approval. No quality rating is used as public marketing.

## Bound inputs and completed scope

| Artifact | SHA256 |
|---|---|
| [Reviewed manuscript source](paper.tex) | `f1cd1e3a4450588acaae58a436eb5f24e4a2b2d62df5ffda74e96d103085d0a3` |
| [Checked 13-page PDF](paper.pdf) | `872b5afab8c7bed53995dfe2578a9790a08412389b37ccb5e011e0c6eb8d5aa7` |

The targeted re-review read the complete integrated source and reconstructed the principal lower/upper transfer, verification, compactness, endpoint approximation and occupancy arguments. It recommended acceptance of the revised mathematical manuscript for the intended research release, with no remaining mandatory mathematical revision identified. The reviewer inspected coordinated certificate receipts rather than independently reimplementing the arithmetic library or executing another replay. Its conclusion is bounded mathematical assessment, not formal proof or exhaustive priority determination.

The source's final bibliography-only change removed an unsupported thesis deposit-month phrase while retaining the verified year. The reviewer checked the resulting source identity. No mathematical statement changed in that final repair.

## Responses to substantive objections

| Concern | Integrated response checked in re-review |
|---|---|
| Nonlinear-system separation was attributed to the entire eta=0 restriction | The text now leaves open whether loss is in the restriction, the chosen feasible construction, or both; predecessor lower-bound/finite-horizon theorems remain intact. |
| Existence and lower transfer unnecessarily relied on numerical positivity | Both zero-value cases are handled by nonnegativity; positive-value arguments are invoked only afterward. |
| Limit confused with all-horizon infimum or attained optimal policy | Fixed-k quantifiers, horizon-dependent adversarial laws and closure-only attainment are explicit; no lim=infₙ or bounded-optimizer conclusion is claimed. |
| Mixture improvement could imply intrinsic randomization advantage | Occupancy-weighted deterministic domination is proved, including zero occupancy and discrete/continuous flows, with earlier threshold-recovery attribution. Same-mesh recovery and atom tie-breaking are distinguished. |
| Older numerical labels and upper estimates overstated evidence | The deterministic slope is a conservative inequality; unsupported older upper estimate and finite-n table are not carried into the paper. Floating-point search remains diagnostic. |
| Two overlapping notes and older audit could be counted as independent new contributions | One integrated paper supersedes both notes. New fixed-k proof and k=2 certificates are distinguished from historical checks; the missing later combined-audit archive is not claimed as available evidence. |
| Layer atoms and k≥3 scope were ambiguous | The profile-generating layer measure is distinguished from the finite-horizon observation law. The analytic theorem covers fixed k; no new numerical bracket or nonlinear-system separation for k≥3 is claimed. |

## PDF quality assurance

All 13 pages of the integrated diagnostic PDF were individually visually inspected. After the bibliography-only repair, exact source reconstruction and page-by-page extracted-text comparison isolated the change to page 12; that page was freshly rendered and inspected. Other page text was unchanged and pagination stayed at 13 pages. The final working-copy PDF was byte-compared with the checked output.

Renewed PDF/TeX preflight found zero raw-TeX findings. No missing glyphs, unresolved references, clipped equations/tables or overlapping content were reported. All 20 fonts are embedded/subsetted Type 1 with Unicode mappings. The PDF remains untagged and has empty descriptive metadata; this is not PDF/UA, comprehensive accessibility certification, mathematical proof validation or a separate font-rights clearance.

## Remaining release boundary

The reviewed source and checked PDF are identified above, but these hashes are not a frozen whole-package manifest. [Replay evidence](REPLAY_RECEIPT.md) remains producer-side and pre-freeze. Final whole-payload integrity, exact-version archive handoff, fresh-extraction gates, CI, provider asset parity and public readback remain pending. The DOI is reserved, not evidence of publication. Any material change to a bound artifact requires reassessment of affected evidence.
