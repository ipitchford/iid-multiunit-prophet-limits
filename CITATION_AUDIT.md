# Citation and attribution audit

Audit date: 2026-10-15. Scope: source identity, applicable assumptions, theorem locators and attribution boundaries. This is not itself a correctness review or a blanket novelty declaration. The bounded source audit is summarized here for repository readers; the separate completed integrated-source assessment is recorded in [REVIEW_SUMMARY.md](REVIEW_SUMMARY.md).

## Claim-to-source map

| Claim or use | Exact inspected locator | Permitted conclusion / boundary |
|---|---|---|
| Exact fixed-n iid k-selection LP | JMZ v5 §4 Definition 4.1, Eq. (25), Theorem 4.2; BPV v2 §3 Theorem 1 | Prior finite-horizon characterization, distinct from the integrated continuum-limit proof. Cite versions because numbering may change. |
| Occupancy-weighted deterministic threshold recovery | JMZ v5 Lemma 2.11, Eq. (7), Appendix C proof; §4 Eq. (25) | Prior coverage/flow formulation already gives the finite-horizon principle. The continuous-time formula is a useful specialization, not a new discovery that randomized quantiles are unnecessary. |
| Concave-action mean-policy construction | PSM13 Lemma 3.2, PDF p.4; §4 Lemma 4.1 and Theorem 4.6 | Convex action sets and affine transition probabilities permit averaging while preserving visitation; concavity improves reward. Simultaneous coverage domination uses the special common family min(x,a), not just a deterministic optimum for one reward. |
| Nonlinear-system guarantee | BPV v2 §4 Theorem 2; §4.1; final discussion | A lower bound valid for sufficiently large n, hence a liminf bound. Not convergence/equality of optimal ratios. |
| Multiple-selection tightness conjecture | MGLP v2 §5 Proposition 5.4, Eq. (5.7), discussion after Table 2 | Boundary-value construction converges; optimal-ratio tightness remains conjectural there. Match k=ell for the present top-k-sum comparison. |
| Numerical finite-horizon comparisons | JMZ v5 §4.3 Proposition 4.8 and Table 1; BPV v2 Table 2 | Numbers at n=1000 are not asymptotic bounds merely by inspection. Distinguish discretization guarantees from solver numerical tolerances. |
| Thesis uncertainty about numerical gap | Brüstle thesis §1.2.3, Table 1.1, printed p.12 (PDF p.28) | Author discusses suboptimality versus slow convergence. It is not evidence of an optimal limit theorem; no quotation is required. |
| Quantile-kernel minimax precedent | LMPPV §3 Definition 1 and strong-duality proof; Appendix C.4; §5 extensions | Credit topology, endpoint handling and transfer methodology. Main models are single-selection/static-threshold, not unrestricted adaptive multiunit. |
| Fixed-distribution extreme-value asymptotics | KM26 v2 Theorem 3.1, Proposition 6.3 and Appendix A.1 | F is fixed and satisfies an extreme-value condition. Does not exchange infimum over F with limit over n. |
| Competition-complexity comparison | CPV26 v1 model and Theorem 1 | Single-threshold class with m observations against n-observation prophet. Not a characterization of optimal adaptive ordinary k-selection. |
| Single-threshold zero-sum games | GMZ published §4 | Methodological precedent only; different policy class from adaptive state-dependent thresholds. |
| Limited-flexibility LP | PST model and LP development | Count of prices/thresholds differs from acceptance budget. Avoid identifying the two parameters. |
| Optimal policy limit analysis in another model | PSV §3 | Selection over time involves commitment duration; cite as method context only. |
| Poisson approximation error | Le Cam §2 Theorem 1, printed pp.1183–1184; §3 Proposition 1 | Full variation norm is at most 2 sum p_i², so event-TV is at most sum p_i². The integrated proof supplies its Bernoulli/Poisson event-TV calculation, independent-sum coupling and mean-perturbation bound directly. |
| Minimax methodology | Fan Theorem 2, historical methodological reference | Original scan not recovered here. The integrated proof instead supplies finite-dimensional separation, nonnegative separating weights and compact finite-intersection reasoning explicitly; it does not depend on an unverified invocation of Fan's theorem. |
| Rigorous interval arithmetic | Johansson Arb paper | Identifies arithmetic methodology, not a certificate that these scripts implement the intended mathematics correctly. Version/run claims need local execution evidence. |

## Source issues raised by the supplied review

1. **Do not conflate a feasible construction with its entire restricted dual.** Beating the BPV nonlinear-system value does not establish that eta=0 itself is suboptimal or that eta must be nonzero. Attribute BPV's finite-n formulation and lower bound accurately.
2. **Keep limit existence separate from infimum equality.** JMZ's introductory attribution to subsequent work is not a replacement for BPV Theorem 2. State directly what that theorem proves. Do not reinterpret another author's intention as established fact.
3. **Do not label 0.853 a previous best certified unrestricted asymptotic bound.** The cited calculation belongs to the extreme-value framework. Its quantifiers differ from worst-case distributions allowed to vary with n.
4. **Credit kernel-minimax methods substantively.** Explain the changes in policy class, benchmark, compactification and boundary estimates rather than citing the kernel paper only in a bibliography list.
5. **Avoid novelty claims for purification.** The reviewer's formula is compatible with established occupancy/concavity arguments. It does not show a bounded policy attains a closure optimum or stays constant on the original time mesh; atom tie-breaking remains distinct.
6. **Separate numerical labels from literature claims.** Floating-point finite-n tables and approximate responses must not be upgraded to certificates. A layer measure is not the observation distribution. These are manuscript/reproducibility repairs, not facts validated by external references.
7. **Review is not proof or peer-review status.** The supplied report was used as a source-check lead, not as authority for novelty, correctness, rating, or publication readiness.

## Bibliographic reconciliation

`bibliography.bib` now records numbered 2026 MOR issues for BPV/JMZ/PST, retaining their 2025 online dates; the GMZ 2026 published First View article; MGLP's proceedings DOI and inspected v2; KM26 v2; the thesis's verified 2025 year and institutional DOI; and the PSM13 precedent. The unverified thesis “deposited 26 January 2026” statement was removed rather than guessed. Existing reference keys were preserved.

The final reviewed source uses a manual `thebibliography`, not BibTeX. Its printed entries now carry the reconciled BPV/JMZ/PST issue metadata, GMZ publication, MGLP proceedings DOI and verified 2025 thesis year without the unsupported deposit-month phrase. The introduction cites JMZ's Definition 4.1 / Eq. (25) / Theorem 4.2 and its occupancy-recovery precedent. PSM13 remains additional source-register background, not an asserted citation in the manuscript's printed bibliography. Bibliography entries alone are not proof of contextual support.

## Verification limits and bounded search

The principal primary texts were inspected at the locators above on 2026-10-15. Publisher and institutional records were used for publication metadata. Google-Scholar-restricted searches did not return usable confirmation; no citation counts were inferred. Direct retrieval of HK82 and Fan's original scan was unavailable, and their full proofs were not newly checked. These limitations should not be silently replaced by a “all citations fully verified” label.

The prior-art search used exact titles and combinations including `"prophet inequality" "limit exists" "k"`, `"prophet inequality" "limit existence" iid`, `"prophet inequalities" "liminf" "2026"`, `"multiunit" "prophet" "convergence" "worst" 2026`, continuum/minimax queries, and occupancy/concave-action searches. It covered the named primary papers and directly relevant discoveries, not every publication or unpublished manuscript. No equivalent all-fixed-k optimal-adaptive worst-case limit theorem was located. This is a bounded negative search result, not priority proof.

The integrated manuscript supplies the exact limiting characterization for each fixed k with both finite-horizon transfers; the separate targeted re-review accepted that argument within its stated scope. This does not strengthen the bounded priority search into exhaustive novelty verification. No citation licenses claims of uniformity in growing k, exact constants for k>=3, all-horizon infimum equality, or extremizer attainment.
