<!-- moved to be colocated with the paper -->
# Review: Policies as Encoders of Optimal Actions

Audience: 1st–2nd year grad students (ML + basic info theory). Goal: deliver the core conceptual framework clearly, resolve notation/definition pitfalls, and tie to Bucket Brigade measurements.

## Summary
- Builds the core metaphor: learning = compression; multi‑agent coordination = distributed encoding (start at `src/research/papers/2024-slepian-wolf-marl.tsx:617`).
- Defines the latent optimal action distribution 𝒵(s), per‑agent marginals 𝒵_i, and discusses partial observability and policies as encoders.
- Introduces information quantities: H(𝒵_i), H(𝒵_i|𝒵_{−i}), R_{π_i}, and I(π_i;π_j), and closes with practical examples (capacity limits, specialization, implicit signaling).

## Audience Fit
- Strengths: Intuitive single‑agent maze example; clear, progressive build from intuition → definitions → examples.
- Risks: Some definitions mix distributions and random variables (e.g., R_{π_i}); potential confusion between analogy and strict information‑theoretic semantics; many symbols before a concrete running example.
- Opportunity: Ground with a consistent set of random variables (S, O_i, A_i*, A_i), and unify notation. Introduce a simple running example (e.g., Bucket Brigade micro‑scenario) to instantiate each definition.

## Issues & Risks
- R_{π_i} definition: The text states R_{π_i} = I(𝒵_i; π_i), then “expands” to an expected KL E[ D_KL(𝒵_i(·|s) || π_i(·|o_i)) ] (`src/research/papers/2024-slepian-wolf-marl.tsx:897`). This KL is a fidelity/distillation loss, not mutual information between random variables. Suggest either:
  - Rename to “policy fidelity” and keep the KL expression, or
  - Define actual information quantities using random variables, e.g., R_{π_i} := I(A_i*; A_i | S) under ρ(S), where A_i* ~ 𝒵_i(·|S) and A_i ~ π_i(·|O_i).
- 𝒵 vs π* ambiguity: Clarify whether 𝒵 is induced by a centralized oracle π*(a|s) (teacher) or by optimal decentralized joint behavior. This affects measurability and interpretation.
- Joint decoder phrasing: Keep “environment evaluates joint actions (rewards/transitions)” unless explicitly referring to the compression analogy.
- Measuring H(𝒵_i|𝒵_{−i}): Be explicit that in practice you approximate via teacher rollouts, enumeration in tiny games, or variational estimators—call this out at first mention to set expectations.

## Suggestions (Structure)
- Add a “Random Variables at a Glance” box near the start:
  - S ~ ρ (state), O_i = Ω_i(S) (observation), A_i* ~ 𝒵_i(·|S) (teacher/optimal action), A_i ~ π_i(·|O_i) (learned action).
- Promote a simple running example (Bucket Brigade micro‑case) and reuse it in 3.2–3.4 to instantiate 𝒵, 𝒵_i, and H(𝒵_i|𝒵_{−i}).
- Separate “analogy” vs “formal”: Keep Slepian–Wolf language in shaded callouts, use RL/MDP language in definitions and claims.
- For inter‑policy redundancy, consider I(Ẑ_i; Ẑ_j) between learned representations, not necessarily I(π_i;π_j) at the action level, to avoid penalizing necessary synchronous actions.

## Suggestions (Wording/Math)
- If you keep MI: R_{π_i} := I(A_i*; A_i | S) (or unconditional I(A_i*; A_i)), with an estimator (e.g., plug‑in via joint contingency tables in discrete settings). Provide a 2–3 line estimation recipe.
- If you keep KL: rename R_{π_i} → F_{π_i} (policy fidelity), e.g., F_{π_i} := E_{S,O_i}[ D_KL(𝒵_i(·|S) || π_i(·|O_i)) ].
- For H(𝒵_i), define using A_i* as the RV: H(A_i*), likewise H(A_i*|A_{−i}*), to avoid mixing distribution‑valued objects in entropy notation.

## Optional Rewrite (excerpt, 3.1–3.4)
We’ll treat policies using standard random variables. Let S be the state, O_i = Ω_i(S) agent i’s observation, A_i* the action a centralized teacher would choose (sampled from 𝒵_i(·|S)), and A_i the action sampled from the learned policy π_i(·|O_i).

- Policy as encoder (informal): π_i compresses experience into parameters θ_i that produce actions A_i matching the teacher’s A_i* as closely as needed for good team performance.
- What needs encoding: the conditional information in A_i* that is not predictable from teammates’ optimal actions A_{−i}*. This is captured by H(A_i*|A_{−i}*).
- Measuring “how much was encoded” (choose one):
  - Information view: R_{π_i} := I(A_i*; A_i | S).
  - Fidelity view: F_{π_i} := E_{S,O_i}[ D_KL(𝒵_i(·|S) || π_i(·|O_i)) ].
- Redundancy: Prefer measuring redundancy between internal representations (e.g., I(Ẑ_i; Ẑ_j)) rather than between action distributions when synchronization is required.

## Line‑Level Notes
- Section start: `src/research/papers/2024-slepian-wolf-marl.tsx:617`
- Latent optimal action distribution def: `src/research/papers/2024-slepian-wolf-marl.tsx:694`
- Marginalization 𝒵_i: `src/research/papers/2024-slepian-wolf-marl.tsx:731`
- Policy as encoder claim box: `src/research/papers/2024-slepian-wolf-marl.tsx:860`
- R_{π_i} definitions: `src/research/papers/2024-slepian-wolf-marl.tsx:897`
