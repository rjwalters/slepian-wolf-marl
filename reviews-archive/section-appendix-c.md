<!-- moved to be colocated with the paper -->
# Review: Appendix C — Bucket Brigade Environment

Audience: 1st–2nd year grad students (ML + basic info theory). Goal: ensure the environment spec is precise, reproducible, aligned with the paper’s information‑theoretic quantities, and directly usable for the research program.

## Summary
- Provides a complete specification of Bucket Brigade: overview/motivation (src/research/papers/2024-slepian-wolf-marl.tsx:5238), world state and turn sequence (src/research/papers/2024-slepian-wolf-marl.tsx:5261, :5309), scenarios (src/research/papers/2024-slepian-wolf-marl.tsx:5369), mapping to information‑theoretic quantities (src/research/papers/2024-slepian-wolf-marl.tsx:5414), metrics/analysis and planned experiments (src/research/papers/2024-slepian-wolf-marl.tsx:5458, :5526), and implementation notes (src/research/papers/2024-slepian-wolf-marl.tsx:5562).
- Design emphasizes tunable correlation, measurable optimality, mixed incentives, and scalable complexity (src/research/papers/2024-slepian-wolf-marl.tsx:5243–5255).

## Strengths
- Clear, modular spec with phase breakdown and pseudocode; strong alignment with experimental goals.
- Scenarios span regimes needed to probe conditional information and redundancy.
- Direct mapping to metrics and planned experiments ties environment to theory.

## Issues & Gaps
1) “Measurable optimality” details
- Appendix claims oracle policies are computable, but the spec does not state how (exact DP/enumeration vs approximate centralized teacher). Provide a concrete method per regime (tiny enumerations; approximate centralized critic for larger).

2) Random variables and notation alignment
- Mapping uses 𝒁/π notation; for measurement, define explicit RVs: S, O_i, A_i* (teacher/optimal), A_i (learned). State that entropy/MI are computed over A_i* and A_i with a specified ρ(S).

3) Discrete vs continuous actions
- The overview mentions both discrete and continuous support (src/research/papers/2024-slepian-wolf-marl.tsx:5250), but examples and estimators are discrete. Either scope Appendix C to discrete for this release or add continuous‑action notes (differential entropy pitfalls; discretization; policy parameterization).

4) Reproducibility and determinism
- Implementation notes mention a Rust core (src/research/papers/2024-slepian-wolf-marl.tsx:5562), but the spec should define seeding (env RNG, fire spread/ignite, initial states), PRNG streams, and a determinism guarantee per build.

5) Observation model and partial observability
- Observation radius, features, and noise are shown; specify exact encoding (data types, normalization), and whether observations can be masked/noisy for correlation ablations.

6) Turn sequence precision
- The phase list is solid; add explicit equations for spread, ignite, extinguish success, burnout progression, and energy updates, including ordering and tie‑break rules to avoid ambiguity.

7) Scenario configs
- Provide canonical scenario YAML/JSON files (names used in paper), each with seeds and parameter ranges. Ensure these configs are versioned and referenced in experiments.

8) Metric computation details
- Metrics section lists quantities; define logging schema (per‑step tuples: t, S_t hash or features, O_i^t, A_i^t, A_i^{*,t}, R_i^t) and how to compute H(A_i*), H(A_i*|A_{−i}*), I(A_i*;A_i|S). Include estimator choice (plug‑in + Miller–Madow) and CI method (bootstrap).

9) Redundancy measurement
- I(π_i;π_j) at the action level can penalize necessary synchrony. Prefer representation‑level redundancy (e.g., I(Ẑ_i;Ẑ_j) or CCA/HSIC) or condition on state/teacher actions I(π_i;π_j | S) when measuring specialization.

10) Capacity and performance linkage
- When plotting capacity vs performance, accompany |θ| with additional proxies (weight compression bits, PAC‑Bayes KL, pruned parameter count) to avoid over‑interpreting parameter counts.

## Suggestions (Edits and Additions)
- Add “Oracle Policy Computation” subsection with:
  - Tiny regimes: exact enumeration/DP to derive A_i* and ρ(S);
  - Larger regimes: centralized teacher (π*) and estimator calibration against tiny regimes.
- Add “Seeding and Determinism” box: RNG sources, seed propagation, determinism guarantees, and reproducibility checklist.
- Expand “Mapping to Info Quantities” with explicit RVs and ρ(S) choice (stationary under π* or a fixed behavior); note that Appendix D covers estimators and CIs.
- Clarify discrete vs continuous scope here; defer continuous to Appendix A.10 and D with notes on differential entropy.
- Provide a public schema for scenario configs and log format (lightweight, human‑readable), and commit to releasing configs used in Section 7.

## Optional Rewrite Snippets
- Measurement paragraph: “We log per‑episode tuples (t, S_t hash, O_i^t, A_i^t, A_i^{*,t}, R_i^t). We estimate H(A_i*), H(A_i*|A_{−i}*), and I(A_i*;A_i|S) via plug‑in estimators with Miller–Madow correction, reporting bootstrap 95% CIs. For specialization, we report representation correlation (CCA/HSIC) between agents’ latents Ẑ_i.”
- Determinism note: “The Rust core ensures deterministic dynamics under fixed seeds (env, agents, spread/ignite RNGs). We expose seed fields in scenario configs and persist seeds in logs for reproducibility.”

## Line‑Level Notes
- Appendix header: src/research/papers/2024-slepian-wolf-marl.tsx:5238
- Overview/motivation: :5243–5255
- World state and turn sequence: :5261, :5309
- Scenarios: :5369
- Mapping to info quantities: :5414
- Metrics/analysis and planned experiments: :5458, :5526
- Implementation notes/significance: :5562, :5572
