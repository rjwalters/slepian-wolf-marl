<!-- moved to be colocated with the paper -->
# Review: Appendix E — Extended Proofs and Supplementary Material

Audience: 1st–2nd year grad students (ML + basic info theory). Goal: ensure proofs are correct or clearly scoped, align with earlier notation, and make the supplementary experiments reproducible and statistically sound.

## Summary
- E.1 provides extended proofs, including a linear‑Gaussian special case of the conjecture (Theorem E.1) and a phase‑transition argument (Theorem E.2) (see `src/research/papers/2024-slepian-wolf-marl.tsx:6091–6185`).
- E.2 adds hyperparameter sensitivity analysis and result summaries with tables/code (around `:6260+`).

## Strengths
- Attempts to formalize a special case (linear networks + Gaussian assumptions) to build intuition.
- Offers concrete supplementary code snippets for hyperparameter sweeps and result reporting.

## Issues & Risks
1) Theorem E.1 (Linear Case) — correctness and units
- Current bound mixes discrete conditional entropy H(𝒁_i|𝒁_{−i}) with continuous Gaussian entropy forms and rank expressions involving log σ_min (`:6100–6150`). As written, dimensions/units do not align and steps invoking I(o_i; W_i o_i) ≤ rank(W_i) log σ_max(W_i) are non‑standard.
- DPI chain step I(𝒁_i; π_i) ≤ I(𝒁_i; o_i) ≤ I(o_i; W_i o_i) is not generally valid (the second inequality reverses the direction DPI would constrain). For Gaussian linear channels, mutual information terms should be expressed via log‑det covariance ratios.

2) Theorem E.2 (Phase Transition)
- The statistical mechanics analogy (partition function Z(β), order parameter m, mean‑field) is heuristic; it does not constitute a proof for broad environment classes without explicit model assumptions and limits. Label as “Heuristic Argument” or move to discussion unless concrete assumptions are added.

3) Notation alignment
- Reuse of 𝒁, π in MI/entropy within proofs is inconsistent with earlier corrections (A_i*, A_i random variables). Theorems should be restated with RVs and a fixed ρ(S).

4) Hyperparameter sensitivity analysis
- The grid search example reports “best parameters” on the same data used for selection; risk of optimistic bias. Parameter importance via simple variance of selected runs is not robust. Recommend factorial/ANOVA or Sobol sensitivity indices with proper cross‑validation and multiple seeds.

## Suggestions (Proofs)
- E.1 Linear‑Gaussian case
  - Assumptions: S, O_i, A_i*, A_i are jointly Gaussian; A_i = W_i O_i + ε_i with ε_i Gaussian, independent of O_i; linear teacher A_i* = L_i S + η_i. State ρ(S) and covariances explicitly.
  - Express MI via covariances:
    - I(A_i*; A_i | S) = 1/2 log det(Σ_{A_i*|S} Σ_{A_i*|S,A_i}^{−1}).
    - For linear Gaussian maps, derive Σ_{A_i*|S,A_i} in terms of W_i, L_i, and noise covariances. Rank enters through nullspaces (information lost if W_i projects onto subspaces orthogonal to teacher‑relevant components).
  - Provide a clean statement: minimal rank of W_i needed to preserve k informative directions about A_i* given A_{−i}*. Avoid ad‑hoc factors like log σ_min; use log‑det bounds (e.g., log det ≤ r log λ_max) with clear eigenvalue definitions, and state constants precisely (nats vs bits).
  - If full derivation is long, present it as a proposition with a proof sketch that references standard Gaussian MI identities.

- E.2 Phase transition
  - Label as “Heuristic mean‑field argument” and move to an Outlook box unless you can specify a teacher–student landscape and a thermodynamic limit where the argument is rigorous (e.g., random features, high‑dimensional limits). Clarify that it motivates the empirical “sigmoid knee,” not a theorem.

## Suggestions (Supplementary Experiments)
- Hyperparameter sensitivity
  - Use a proper experimental design: Latin hypercube or Sobol sequences; evaluate each setting over ≥N seeds; separate selection and evaluation folds to prevent selection bias.
  - Report aggregate metrics with 95% CIs across seeds; for importance, use ANOVA effects or Sobol indices; include interaction terms.
  - Release the exact grid/ranges, seed list, and results table; avoid single best‑run reporting.

- Reporting
  - For any supplementary plots/tables, annotate estimator choices, sample sizes, and base distribution ρ(S). If metrics involve MI/entropy, include error bars via bootstrap across episodes.

## Minimal Edits To Appendix E Text
- Rename Theorem E.2 → “Heuristic Phase‑Transition Argument” (or move to Discussion/Outlook).
- Restate E.1 with explicit linear‑Gaussian assumptions and random variables; replace the I(o; W o) bound with a log‑det covariance bound and remove the σ_min expression unless derived rigorously.
- Add a “Scope and Assumptions” box at the start of E.1 detailing Gaussianity, independence of noises, and invertibility/rank conditions.
- In E.2.1, add seeds, folds, and CI reporting; replace ad‑hoc “variance importance” with an established sensitivity method.

## Line‑Level Notes
- Appendix E header: `src/research/papers/2024-slepian-wolf-marl.tsx:6091–6098`
- Theorem E.1 statement and steps: `:6100–6160`
- Theorem E.2 statement and setup: `:6165–6230`
- Hyperparameter sensitivity code/table: `:6260–6400`
