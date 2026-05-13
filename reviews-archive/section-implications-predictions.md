<!-- moved to be colocated with the paper -->
# Review: 5. Implications and Predictions

Audience: 1st–2nd year grad students (ML + basic info theory). Goal: turn the conjecture into actionable, testable guidance while keeping claims grounded and measurable in Bucket Brigade.

## Summary
- States five predictions: capacity threshold, sample complexity scaling, specialization via redundancy reduction, communication benefit threshold, and permutation invariance (see `src/research/papers/2024-slepian-wolf-marl.tsx:1423`).
- Provides derivations, intuition, and example protocols (capacity at `:1440`, sample complexity at `:1532`, specialization at `:1700`, communication at `:1666`, invariance at `:1810`).

## Audience Fit
- Strengths: Concrete, testable statements; practical checklists; visuals (capacity sigmoid); helpful taxonomy (specialization types, communication types).
- Risks: Over‑formal labels (e.g., “Fundamental Capacity Theorem”) for heuristic relations; unit mismatches (bits ↔ parameters); MI estimation pitfalls; redundancy penalty may suppress necessary coordination; symmetry claims ignore stochastic symmetry breaking.
- Opportunity: Standardize “What/Why/Measure/Controls” per prediction; add “Reporting checklist” boxes to make it programmatic.

## Issues & Risks
1) Capacity ≈ H(𝒁_i|𝒁_{−i})/(α·b)
- Bits‑per‑parameter mapping is a rough heuristic; effective capacity depends on function class complexity (e.g., MDL, PAC‑Bayes KL, flat minima) and data distribution. α and b are highly implementation‑dependent.
- Suggest renaming to “Heuristic capacity guideline” and offering alternatives: description length of weights (MDL), PAC‑Bayes bound terms, Fisher/effective dimension, pruning/quantization curves as empirical proxies.

2) Policy “information rate” vs capacity
- If R_{π_i} is MI, ensure same units (bits) and shared base distribution ρ(S). If you instead use KL fidelity, don’t call it an information rate. Keep one consistent definition across sections.

3) Sample complexity derivation
- Coupon‑collector style Step 1 is not standard for function learning and likely overstates dependence on 2^H. Prefer framing as a hypothesis with empirical support. Or tie to VC/Rademacher/covering‑number style terms plus conditional information to keep it honest.
- The proposed formula is useful as a scaling hypothesis; mark as such and validate with ablations.

4) Specialization via I(π_i;π_j)
- Penalizing action‑level MI can harm coordination when synchronized actions are required. Prefer conditional MI I(π_i;π_j | 𝒁) or representation‑level redundancy (I(Ẑ_i;Ẑ_j)). Consider tying λ to a measured redundancy‑benefit curve.

5) Communication threshold
- H(𝒁_i|o_i) vs H(𝒁_i|𝒁_{−i}) is a good intuition, but define what messages M can change: effective uncertainty H(𝒁_i|o_i, M). Then the benefit threshold is when E[H(𝒁_i|o_i)] − E[H(𝒁_i|o_i, M)] exceeds cost. Also clarify whether 𝒁_{−i} is approximated by teammates’ conveyed intentions/actions.

6) Symmetry and invariance
- State invariance “in expectation” under exchangeable settings; in practice report across seeds and small asymmetries. Include failure cases when exploration noise or initialization breaks symmetry.

## Suggestions (Per‑Prediction Template)
For each prediction, adopt a uniform mini‑spec:
- What it says: one or two plain‑language sentences.
- Why it matters: one sentence.
- How to measure: concrete metrics, estimators, and logging needed in Bucket Brigade.
- Controls: confounders to check (capacity proxy, estimator bias, correlation manipulation, seeds).
- Reporting: plots, CIs, and ablation knobs.

## Concrete Edits and Additions
- Capacity (5.1)
  - Rename “The Fundamental Capacity Theorem” → “Heuristic Capacity Guideline.”
  - Add alternative proxies: description length of weights (bits via compression), PAC‑Bayes KL from prior to posterior, effective dimension via Fisher trace, sparsity after pruning.
  - Replace hard formula with inequality band and confidence: plot performance vs measured capacity proxy; annotate conditional entropy estimates with error bars.

- Sample Complexity (5.2)
  - Label as “Scaling Hypothesis.” Add a note on estimator bias/variance and how you’ll compare fits (e.g., AIC/BIC across linear-in-H and alternative baselines).
  - Provide a minimal reproducible protocol: fixed policy class; vary conditional entropy by environment parameters; measure m_i at target ε; report seed‑wise distribution.

- Specialization (5.3)
  - Switch to conditional MI or representation‑level redundancy terms; add a caution box for tasks requiring synchrony.
  - Add diagnostics: pairwise policy divergence, role entropy over time, mutual‑information heatmaps between learned latents Ẑ_i.

- Communication (5.4)
  - Introduce a message RV M and define benefit Δ_i = H(𝒁_i|o_i) − H(𝒁_i|o_i, M). Frame threshold as Σ_i Δ_i > communication cost.
  - Suggest experiments toggling cheap‑talk bandwidth and noise; measure marginal value of bits.

- Symmetry (5.5)
  - Define invariance “on average across seeds.” Add tests under slight asymmetries to chart robustness boundaries.

## Optional Rewrite Snippets
- Capacity one‑liner: “An agent’s effective capacity should at least match the unique task information it must carry; we estimate both sides and look for the knee where performance takes off.”
- Sample complexity one‑liner: “Holding policy class fixed, the number of samples to reach ε‑optimality grows with the conditional information the agent must learn; we test this scaling across controlled correlation regimes.”
- Communication one‑liner: “Communication helps when messages can shrink each agent’s local uncertainty more than teammates’ behavior already does, and by more than the channel’s cost.”

## Measurement Notes (Bucket Brigade)
- Log tuples (S_t, O_i^t, A_i^t, A_i^{*,t}, R_t) to estimate H(A_i*), H(A_i*|A_{−i}*), I(A_i*;A_i|S), and redundancy metrics. Use plug‑in with Miller–Madow for discrete alphabets; bootstrap CIs.
- Capacity proxies: weight‑compression bits, PAC‑Bayes KL estimates, pruning‑based effective parameters, Fisher trace‑based dimension.
- Controls: vary observation correlation I(O_i;O_j), network width/depth/quantization, and communication bandwidth; run ≥20 seeds.

## Line‑Level Notes
- Section start: `src/research/papers/2024-slepian-wolf-marl.tsx:1423`
- Capacity guideline and derivation: `:1440–1510`
- Sample complexity block and derivation: `:1532–1560`
- Specialization prediction and metrics: `:1700–1760`
- Communication threshold: `:1666–1720`
- Symmetry and implications: `:1810–1885`
