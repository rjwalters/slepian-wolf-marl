<!-- moved to be colocated with the paper -->
# Review: 7. Experimental Validation

Audience: 1st–2nd year grad students (ML + basic info theory). Goal: deliver rigorous, reproducible experiments that directly test the conjecture with clear metrics, estimation procedures, and controls in Bucket Brigade.

## Summary
- Defines five RQs (capacity, sample complexity, specialization, communication, symmetry) and proposes experiments per RQ (see `src/research/papers/2024-slepian-wolf-marl.tsx:2477`).
- Uses Bucket Brigade with controllable correlation and discrete actions; includes capacity sweeps, sample complexity tables, and specialization/communication analyses (e.g., `src/research/papers/2024-slepian-wolf-marl.tsx:2542`, `src/research/papers/2024-slepian-wolf-marl.tsx:2667`).

## Audience Fit
- Strengths: Clear RQs, concrete experiment outlines, environment well matched to information‑theoretic measurements.
- Risks: Over‑confident numeric claims without uncertainty; capacity proxy (bits/param × α) used as if ground truth; MI/entropy estimation methods not fully specified; limited discussion of baselines and seed variance.
- Opportunity: Standardize protocols and reporting; add estimator validation; strengthen causal claims with ablations and controls.

## Issues & Risks
1) Estimation details missing
- Specify exactly how you estimate H(A_i*), H(A_i*|A_{−i}*), I(A_i*;A_i|S), and any action‑level MI. Include estimator choice (plug‑in with Miller–Madow; Bayesian; variational bound), sample size, and bias/variance handling.

2) Capacity proxy assumptions
- The mapping from bits to parameters via α and b is heuristic. Treat it as a proxy and report additional capacity measures (compression bits of weights, PAC‑Bayes KL, pruning‑based effective parameter count). Avoid treating |θ| as “true capacity.”

3) Statistical rigor
- Always report: number of seeds, mean ± 95% CI, effect sizes, and p‑values or permutation tests where relevant. Avoid single‑seed plots. Use fixed random seeds protocol and publish them.

4) Controls and confounders
- Vary correlation I(O_i;O_j) independently of capacity to test Communication and Capacity RQs separately. Control for optimizer, LR, and architecture across conditions. Include no‑regularizer and centralized‑teacher baselines.

5) Reproducibility
- Provide exact configs, versioned scenario files, and scripts to reproduce tables/plots. Save raw logs for metrics and make plotting notebooks available.

## Per‑RQ Recommendations
- RQ1 Capacity (phase transition)
  - What: Performance vs capacity curve; look for knee near conditional information threshold.
  - Measure: performance (team reward), estimated H(A_i*|A_{−i}*), and capacity proxies (|θ|, compression bits, PAC‑Bayes KL).
  - Controls: same optimization budget; vary width/depth separately; report across ≥20 seeds; include centralized teacher and overparameterized baselines.
  - Reporting: sigmoid fit with CI; annotate knee with estimated threshold and uncertainty.

- RQ2 Sample Complexity
  - What: Samples to reach ε‑performance vs estimated H(A_i*|A_{−i}*).
  - Measure: episodes to ε for multiple ε; fit scaling laws; compare linear‑in‑H vs alternatives.
  - Controls: fix policy class; vary conditional information by environment parameters only; ≥20 seeds.
  - Reporting: slope with CI; include estimator sanity checks and goodness‑of‑fit stats.

- RQ3 Specialization
  - What: Emergence of roles under redundancy penalties.
  - Measure: representation‑level redundancy (CCA/HSIC between Ẑ_i), role entropy, and task performance.
  - Controls: tasks requiring synchrony; turn penalty off/on; condition redundancy on state if needed.
  - Reporting: trajectories over training; ablate λ_red; show robustness to agent dropout.

- RQ4 Communication
  - What: Benefit of cheap‑talk vs predicted Δ_i = H(A_i*|O_i) − H(A_i*|O_i,M).
  - Measure: estimate Δ_i and realized reward deltas; sweep bandwidth/noise.
  - Controls: hold capacity and correlation; compare implicit signaling vs explicit channels.
  - Reporting: correlation with CI; threshold analysis; cost‑benefit curves (bits vs reward).

- RQ5 Symmetry
  - What: Invariance under agent permutations in symmetric settings.
  - Measure: performance distribution across permutations/seeds; permutation test.
  - Controls: inject slight asymmetries to map robustness; report when invariance fails.

## Estimation and Logging Checklist
- Log per‑episode tuples (S_t, O_i^t, A_i^t, A_i^{*,t}, R_t).
- Estimators: plug‑in with Miller–Madow (discrete), bootstrap CIs; optionally compare to variational MI bounds offline.
- Capacity proxies: store final weights for compression; compute PAC‑Bayes KL w.r.t. simple Gaussian priors; track pruned params.

## Baselines
- Centralized teacher (oracle) imitation policy.
- No‑regularizer MARL baseline.
- Overparameterized policy class to show ceiling performance.
- Communication oracle (high‑bandwidth) to bound achievable gains.

## Optional Rewrite Snippets
- “We report mean ± 95% CI over 20 seeds for all metrics. Entropy and MI are estimated with plug‑in estimators (Miller–Madow correction) on held‑out trajectories; we include bootstrap CIs and compare against a variational bound in an ablation.”
- “Capacity is measured via parameter count, weight compression bits (gzip), and a PAC‑Bayes KL estimate; conclusions are drawn only where all proxies agree within CI.”

## Line‑Level Notes
- Section start and RQs: `src/research/papers/2024-slepian-wolf-marl.tsx:2477`
- Experiment 1 capacity sweep outline: `src/research/papers/2024-slepian-wolf-marl.tsx:2542`
- Experiment 2 sample complexity table: `src/research/papers/2024-slepian-wolf-marl.tsx:2667`
- Specialization findings: `src/research/papers/2024-slepian-wolf-marl.tsx:2705`
- Communication correlation analysis: `src/research/papers/2024-slepian-wolf-marl.tsx:2745`
- Symmetry interchangeability setup: `src/research/papers/2024-slepian-wolf-marl.tsx:2762`
