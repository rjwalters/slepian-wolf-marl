<!-- moved to be colocated with the paper -->
# Review: Appendix B — Implementation Details

Audience: 1st–2nd year grad students (ML + basic info theory). Goal: make the InfoMARL implementation reproducible, stable, and aligned with the paper’s definitions so it can guide the Bucket Brigade research program.

## Summary
- Provides an end‑to‑end InfoMARL reference: framework scaffolding, entropy/MI/relevance estimators, PPO‑style agents, and a trainer (see `src/research/papers/2024-slepian-wolf-marl.tsx:4149`, `:4220`, `:4740`).
- Good coverage of practical concerns (buffers, logging stubs, clipping, batch norms) and instructive code blocks for readers.

## Key Issues (Fix First)
- Header/section mix‑up: Appendix B begins, then immediately shows A.* theorems before the actual B.* content (`src/research/papers/2024-slepian-wolf-marl.tsx:4150–4215`). This looks like a stray paste of Appendix A material. Suggest removing or moving those A.* blocks back under Appendix A.
- Conditional entropy estimation mismatch: `_estimate_conditional_entropies` uses random joint actions to estimate H(Z_i|Z_{−i}) (`src/research/papers/2024-slepian-wolf-marl.tsx:4263–4325`). By definition, Z_i is the optimal action distribution, not the behavior policy. Use oracle (A_i*) or a strong centralized teacher to compute entropies; for tiny tasks, enumerate; otherwise, approximate from teacher rollouts.
- R_{π_i} definition consistency: Later mapping and estimators refer to R_{π_i} ≈ I(𝒁_i; π_i). Ensure the code measures either MI between optimal and learned actions I(A_i*; A_i | S) or uses a named fidelity (KL) surrogate. Avoid mixing terms across sections.
- Relevance estimator mis‑specification: `RelevanceEstimator` aims for I(O;A|R) but implements a reward predictor with MSE and converts to MI via Gaussian noise assumptions (`src/research/papers/2024-slepian-wolf-marl.tsx:4858–4915`). This is not I(O;A|R). Prefer a clear surrogate: predictive R^2 (with caveats), cross‑entropy to a teacher, or a proper variational MI bound with explicit random variables.
- MINE stability and usage: The MINE‑style estimator (DV + f‑bound combo) is high variance; training it inside the RL loop can destabilize learning (`src/research/papers/2024-slepian-wolf-marl.tsx:4575–4718`). Use offline estimation on logged trajectories for metrics; if you must use MI in the loss, prefer stable surrogates (InfoNCE/JSD with large negative banks) and heavy smoothing.

## Suggestions (By Component)
- Conditional entropy pipeline
  - Replace random actions with teacher actions A_i* from a centralized oracle (or an enumerated optimal in small envs). Compute H(A_i*), H(A_i*|A_{−i}*) under a documented ρ(S): stationary under teacher or a fixed behavior policy.
  - For Bucket Brigade, first validate against exactly enumerable toy cases to calibrate estimator bias (plug‑in + Miller–Madow is fine for discrete alphabets).

- MI and relevance
  - If tracking “policy information rate,” use RVs: R_{π_i} := I(A_i*; A_i | S). For discrete actions, estimate via contingency tables; report bootstrap CIs.
  - If staying with surrogates, rename them clearly: F_{π_i} (KL fidelity), PredictiveRelevance (log‑variance ratio). Don’t label them MI.

- PPO/training loop
  - Ensure full PPO pieces exist (advantage estimation, GAE(λ), value loss, entropy bonus, clipped surrogate). The trainer stub currently shows action_probs capture but not value baselines (see update flow around `src/research/papers/2024-slepian-wolf-marl.tsx:4996–5100`).
  - BatchNorm in small, non‑i.i.d. on‑policy batches can be brittle; consider LayerNorm/none for stability.
  - Determinism: set seeds for numpy/torch/env; expose `seed` and log it.

- Capacity adaptation
  - Gate expand/prune with hysteresis and validation plateaus; update optimizer state cautiously (Net2Net for growth, gradual pruning). Log every change with before/after capacity proxies.

- Engineering and reproducibility
  - Config: centralize hyperparameters in a YAML/JSON config; emit a run manifest (git SHA, env, seeds, config).
  - Logging: track mean ± 95% CI over seeds; save raw trajectories for estimation; add simple CSV/Parquet sinks.
  - Performance: MI pairwise computations scale O(N^2); subsample pairs per epoch and rotate; cache negatives for NCE‑style bounds.

## Quick Code Risk Review
- One‑hot dimension inference in `RelevanceEstimator`: uses `self.predictor[0].in_features - obs_batch.shape[1]` (`src/research/papers/2024-slepian-wolf-marl.tsx:4880–4890`). This assumes a fixed network layout; safer to pass action_dim explicitly and build embeddings accordingly.
- Entropy estimator uses Miller–Madow with short episodes; bias can be large. Aggregate over many episodes and report error bars.
- MINE moving average `ma_et`: ensure it never hits 0; epsilon already used in DV path, but guard division/logs consistently.

## Minimal Changes To Align With Paper
- Rename/define metrics:
  - R_{π_i} → I(A_i*; A_i | S) (bits), or F_{π_i} (KL fidelity) if sticking to KL.
  - “Relevance” → PredictiveRelevance or I(Ẑ_i; A_i*) bound if using representation IB.
- Fix conditional entropy estimation to use A_i*.
- Add a note where MI is only logged (offline) vs used in loss (surrogate only).

## Line‑Level Notes
- Appendix B header with A.* duplication: `src/research/papers/2024-slepian-wolf-marl.tsx:4150–4215`
- Conditional entropy estimation routine: `:4220–4325`
- MINE estimator block: `:4575–4718`
- Relevance estimator block: `:4858–4915`
- Trainer skeleton and data flow: `:4922–5400`
