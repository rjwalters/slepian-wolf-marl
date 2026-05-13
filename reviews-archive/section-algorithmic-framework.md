<!-- moved to be colocated with the paper -->
# Review: 6. Algorithmic Framework

Audience: 1st–2nd year grad students (ML + basic info theory). Goal: make the objective implementable and stable for Bucket Brigade, with clear estimators, schedules, and diagnostics.

## Summary
- Proposes an information-regularized objective and an adaptive capacity scaling scheme (see `src/research/papers/2024-slepian-wolf-marl.tsx:1813`).
- Objective: maximize reward while (i) penalizing inter-agent redundancy via I(π_i; π_j), and (ii) encouraging task-relevant information via I(o_i; π_i | 𝒁_i) (`:1816`).
- Adaptive capacity: expand/prune networks based on conditional-entropy estimates (`:1826`).
- Includes practical guidelines, diagnostics, complexity analysis, deployment notes, and best practices (`:1841`, `:1898`, `:2060`, `:2260`, `:2406`).

## Audience Fit
- Strengths: Concrete knobs (λ’s), actionable heuristics (expand/prune), helpful diagnostics and pitfalls table.
- Risks: MI terms are hard to estimate online and may destabilize training; I(o_i; π_i | 𝒁_i) is nonstandard IB; action-level redundancy penalty can fight coordination; capacity changes mid‑training can introduce nonstationarity.
- Opportunity: Use representation‑level IB with cheaper surrogates; clarify estimators and schedules; gate adaptive growth with robust triggers and cooldowns.

## Issues & Risks
1) Objective definition (third term)
- I(o_i; π_i | 𝒁_i) is unusual for an IB objective (mixes observations and policy distribution, conditioned on 𝒁_i). Standard IB/DIB uses a learned representation Ẑ_i with terms like I(Ẑ_i; O_i) and I(Ẑ_i; Y) (here Y could be A_i* or advantage labels).

2) Redundancy penalty
- Penalizing I(π_i; π_j) at the action level can harm tasks requiring synchronized actions. Prefer conditional or representation‑level redundancy, e.g., I(Ẑ_i; Ẑ_j) or I(π_i; π_j | S) / | A_i*, and apply only to nuisance/shared factors.

3) Estimation practicality
- Online MI estimators (e.g., MINE) are high‑variance and can introduce instability. For discrete Bucket Brigade settings, plug‑in estimators with bias correction are simpler and more stable; for continuous, prefer InfoNCE‑style lower bounds with temperature tuning and large negative banks.

4) Adaptive capacity scaling
- On‑the‑fly expand/prune can cause learning shocks and break optimizer state. Growing networks should use network morphisms (Net2Net) or warm‑started layers; pruning should be gradual (magnitude/L0 with cooldowns). Tie decisions to clear metrics with hysteresis to avoid oscillation.

5) Units and thresholds
- If using MI, keep everything in bits under a stated ρ(S). If using KL/Cross‑Entropy surrogates, do not call them “information rates”; rename and document their units.

## Suggestions (Objective and Estimators)
- Use a representation‑level IB:
  - Introduce Ẑ_i = encoder(O_i) and policy π_i(A_i | Ẑ_i).
  - Task relevance: either I(Ẑ_i; A_i*) with a variational bound, or supervised cross‑entropy to a teacher π* when available.
  - Compression: penalize I(Ẑ_i; O_i) via a stochastic encoder and KL to a factorized prior (VIB), or an HSIC/MMD surrogate for dependence.
- Redundancy: penalize I(Ẑ_i; Ẑ_j) (or CCA correlations) rather than I(π_i; π_j); optionally condition on state or teacher actions.
- Cheap, stable surrogates for Bucket Brigade (discrete):
  - Relevance: CE(π_i(·|O_i), 𝒁_i(·|S)) or advantage‑weighted log‑likelihood.
  - Redundancy: pairwise cosine/CCA penalties between Ẑ_i embeddings; HSIC with Gaussian kernels.
  - Compression: KL(q(Ẑ_i|O_i) || p(Ẑ_i)) with p standard normal.

Proposed loss (surrogate form):
- L = E[R] − λ_red Σ_{i<j} Corr(Ẑ_i, Ẑ_j) − β Σ_i CE(π_i(·|O_i), 𝒁_i(·|S)) + γ Σ_i KL(q(Ẑ_i|O_i) || p(Ẑ_i)).
- If no teacher 𝒁: replace CE term with advantage‑weighted log‑prob or imitation from centralized critic.

## Suggestions (Adaptive Capacity)
- Replace hard thresholds with a schedule and hysteresis:
  - Trigger expand if capacity_utilization > 0.85 for T epochs and validation reward plateaus; grow width/depth with Net2Net; freeze new layers briefly.
  - Trigger prune if utilization < 0.3 for T epochs; use gradual magnitude pruning (e.g., 10–30%) and recover with brief LR warmup.
  - Periodically re‑estimate conditional information on held‑out episodes; smooth with EMA to reduce noise.
- Consider alternative capacity controls: width multiplier, low‑rank adapters, parameter sharing, or quantization instead of structural changes mid‑run.

## Suggestions (Diagnostics and Complexity)
- Prefer offline MI estimation on logged episodes to stabilize training; use online only for light surrogates.
- Log bias‑corrected plug‑in estimates for H(A_i*), H(A_i*|A_{−i}*), I(A_i*; A_i | S), plus representation‑level redundancy metrics (CCA/HSIC) with bootstrap CIs.
- Cost control: limit pairwise computations to a rotating subset each epoch; maintain summary banks for negatives in InfoNCE.

## Optional Rewrite Snippet (Objective block)
We instantiate a practical InfoMARL objective around a learned representation Ẑ_i:
- Compression: encourage Ẑ_i to discard nuisance information with a VIB term KL(q(Ẑ_i|O_i) || p(Ẑ_i)).
- Relevance: align policy actions with a teacher signal (A_i* or centralized critic) via cross‑entropy or advantage‑weighted likelihood.
- Redundancy: reduce shared information between agents’ representations using correlation/HSIC penalties; when synchrony is required, condition penalties on state or disable them.
This yields a stable surrogate objective that approximates the intended information trade‑offs while remaining easy to estimate in discrete environments.

## Line‑Level Notes
- Section start and objective: `src/research/papers/2024-slepian-wolf-marl.tsx:1813`, `:1816`
- Adaptive capacity pseudocode: `src/research/papers/2024-slepian-wolf-marl.tsx:1826`
- Practical guidelines/pitfalls table: `src/research/papers/2024-slepian-wolf-marl.tsx:1841`
- Diagnostics scaffold: `src/research/papers/2024-slepian-wolf-marl.tsx:1898`
- Complexity analysis: `src/research/papers/2024-slepian-wolf-marl.tsx:2060`
- Deployment considerations and best practices: `src/research/papers/2024-slepian-wolf-marl.tsx:2260`, `:2406`
