<!-- moved to be colocated with the paper -->
# Review: Appendix D — Entropy Estimation and Analysis Methodology

Audience: 1st–2nd year grad students (ML + basic info theory). Goal: make estimation choices explicit, statistically sound, and aligned with the paper’s variables so results are reproducible and defensible.

## Summary
- Defines metrics and provides estimation procedures for discrete and continuous cases, plus practical guidelines (see `src/research/papers/2024-slepian-wolf-marl.tsx:5616` onward).
- Implements plug‑in estimators with Miller–Madow/Panzeri‑Treves corrections for discrete (D.2.1), and k‑NN/KDE/Gaussian for continuous (D.2.2). Includes estimator selection tables and sample size guidance (D.5).

## Alignment With Paper Variables
- Use explicit random variables consistently: S (state), O_i = Ω_i(S), A_i* (teacher/optimal action), A_i (learned action). Compute H and I over A_i* and A_i, not distribution symbols 𝒁_i or π_i.
- State and hold fixed the base distribution ρ(S) for all expectations: e.g., stationary under the centralized teacher π*, or a specified behavior policy. Note where distribution shift (training vs evaluation) can bias estimates.

## Discrete Estimation (D.2.1)
- Strengths: Clear plug‑in implementation with multiple bias corrections and bootstrap path.
- Recommendations:
  - Add Dirichlet‑multinomial (add‑α) smoothing option for scarce categories; expose α.
  - For conditional entropy H(X|Y), guard against rare Y: require minimum per‑Y sample (e.g., ≥10 counts), or back off to pooled estimates; report fraction of mass covered.
  - For MI: compute via entropies (I = H(X)+H(Y)−H(X,Y)) with the same correction choice for all components; report bootstrap 95% CIs.
  - Consider NSB or Grassberger estimators for very small samples (optional), but keep plug‑in as default for simplicity.

## Continuous Estimation (D.2.2)
- Strengths: Includes KSG‑style k‑NN (via KL base), KDE, and Gaussian assumptions; acknowledges dimensionality.
- Recommendations:
  - Clarify units: differential entropy is in nats in current code; convert to bits where needed (divide by ln 2) and label consistently across the paper.
  - Prefer MI‑direct estimators (KSG for MI) over entropy‑difference approaches when estimating I(X;Y) in continuous cases.
  - Add boundary handling and standardize k selection (e.g., k ∈ {3, 5, 10} with sensitivity analysis) and bandwidth selection for KDE.
  - For >5D, discourage nonparametric estimators unless sample sizes are very large; suggest parametric or discretization schemes.

## Mutual Information Estimators (general)
- If using neural MI bounds (MINE/DV), keep them OUT of the training loss by default; use for offline analysis on logged trajectories with heavy smoothing and early stopping. Prefer InfoNCE/JSD for stability; always report that values are lower bounds (and temperature/negative pool details).

## Data Collection and Logging
- Log per‑time‑step tuples: (t, S_t hash or features, O_i^t, A_i^{*,t}, A_i^t, R_i^t). Ensure hashes are stable across runs and do not leak future information.
- Split data: use dedicated held‑out episodes for estimation to avoid circularity with training; record seeds and ρ(S) provenance (teacher vs behavior policy).
- Use bootstrapping across episodes (clustered by episode) to form 95% CIs for all reported H/I estimates and for derived metrics (e.g., performance vs capacity curves).

## Common Pitfalls and Fixes
- Sparse counts: unseen categories bias downwards; apply smoothing or Good–Turing corrections; report coverage (observed/possible categories).
- Conditional estimates: low counts for certain Y inflate bias; restrict to Y with sufficient support or pool similar Y.
- Distribution shift: estimates under training ρ(S) may not match evaluation ρ(S); either fix a reference ρ(S) or importance‑weight samples (with variance warnings).
- Mixed discrete/continuous: avoid naive binning for MI; either discretize with principled bins (e.g., Freedman–Diaconis) and report sensitivity, or use KSG‑type estimators.

## Reporting Standards
- Always report: estimator used (and parameters), number of samples, bias correction, and 95% CIs (bootstrap over episodes).
- For phase diagrams, overlay CIs on both axes (capacity proxies and information estimates) and annotate ρ(S).
- Release code: provide scripts/notebooks that recompute every figure from raw logs; include a test that replicates a tiny toy case with exact values.

## Minimal Edits To Appendix D Text/Code
- In D.1 and mapping, replace notation like H(𝒁_i) with H(A_i*), H(𝒁_i|𝒁_{−i}) with H(A_i*|A_{−i}*), and R_{π_i} with I(A_i*;A_i|S) when asserting MI. If using surrogates (e.g., KL), rename accordingly.
- In D.2.1, expose `alpha` for Dirichlet smoothing and add a `min_counts_per_y` guard in conditional entropy routines.
- In D.2.2, add unit conversion nats→bits, document k/bandwidth selection, and warn about high‑dimensional regimes.
- In D.5 tables, add a column for “CI method” and default to bootstrap (by episode) for discrete; note limitations for continuous.

## Line‑Level Notes
- Discrete estimator block: `src/research/papers/2024-slepian-wolf-marl.tsx:5630–5680`
- Continuous estimator block: `src/research/papers/2024-slepian-wolf-marl.tsx:5686–5740`
- Estimator selection and sample‑size guidance: `src/research/papers/2024-slepian-wolf-marl.tsx:5840–5920`
- D.1 metric notation references earlier: ensure consistency with A_i*, A_i, and ρ(S)
