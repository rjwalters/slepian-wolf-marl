<!-- moved to be colocated with the paper -->
# Review: 4. The Distributed Learning Conjecture

Audience: 1st–2nd year grad students (ML + basic info theory). Goal: state the conjecture plainly, align math with estimable quantities, and anchor it to Bucket Brigade measurements.

## Summary
- Motivates information bounds via capacity allocation and a telephone‑game analogy (around `src/research/papers/2024-slepian-wolf-marl.tsx:1034`).
- States strong and approximate forms using a threshold: each agent’s “policy information rate” must meet its conditional optimal‑action information (`:1078` onward).
- Discusses assumptions, implications, potential failures, and connections to rate‑distortion, PAC/MDL, plus testable predictions (`:1207`, `:1270`, `:1362`).

## Audience Fit
- Strengths: Clear intuition; layered presentation (intuition → formal statements → implications); explicit “assumptions” and “failure modes.”
- Risks: Over‑strong “if and only if” in strong form; ambiguous definitions of R_{π_i} and 𝒁/𝒁_i; unit consistency (bits) vs parameter counts; using Slepian–Wolf terms outside the analogy can mislead.
- Opportunity: Add a one‑paragraph plain‑language version, a boxed “Units and Estimation” note, and a concrete 2×2 toy example before the formal block.

## Issues & Risks
- R_{π_i} semantics: The manuscript alternates between an MI‑like interpretation and an expected KL to 𝒁_i(·|s). These are different objects. Pick one:
  - Information view: R_{π_i} := I(A_i*; A_i | S) with A_i* ~ 𝒁_i(·|S), A_i ~ π_i(·|O_i). Estimable in discrete tasks via plug‑in tables (with bias correction).
  - Fidelity view: F_{π_i} := E_{S,O_i}[ D_KL(𝒁_i(·|S) || π_i(·|O_i)) ]. Not an information “rate”; rename accordingly.
- 𝒁 definition and scope: Clarify whether 𝒁 is induced by a centralized teacher π*(a|s) or an optimal decentralized equilibrium. This choice affects both meaning and measurement of H(𝒁_i|𝒁_{−i}).
- “If and only if” strength: Strong form likely false without stringent assumptions (infinite data, universal approximation, optimal optimization, stationarity). Lead with the approximate, practically useful form and demote the strong form to an idealization.
- Units and thresholds: H(𝒁_i|𝒁_{−i}) is in bits. Ensure R_{π_i} (if MI) is also in bits under the same base distribution ρ(S). Avoid mapping bits directly to “parameters × 32” without caveats.
- Distribution ρ(S): State explicitly which state distribution underlies all expectations (stationary, behavior‑induced, or oracle‑induced) to make quantities well‑defined and comparable.

## Suggestions (Structure)
- Add a “Conjecture (Plain Language)” box before math: “Each agent must carry enough unique, task‑relevant information about its optimal actions—the part others can’t infer. When each agent clears that threshold, coordination emerges.”
- Then present the Approximate Form first, with clear assumptions, followed by the Strong Form as an idealization.
- Insert a “Units and Estimation” callout: bits; how to estimate H(𝒁_i|𝒁_{−i}) and R_{π_i}/F_{π_i}; and the role of ρ(S).
- Include a tiny 2×2 coordination example that computes H(A_1*|A_2*) and shows the threshold visually.
- Keep “testable predictions” as a bridge to the next section, but reserve detailed algorithms there.

## Suggestions (Wording/Math)
- Prefer random‑variable notation: write entropies over A_i* (teacher/optimal action RV), not over distribution‑valued symbols 𝒁_i.
- If using MI: define R_{π_i} := I(A_i*; A_i | S) and note simple estimators for discrete actions (plug‑in with Miller–Madow; bootstrap CIs).
- If using KL: rename R_{π_i} to F_{π_i} (policy fidelity) and make the conjecture compare F_{π_i} to a distortion threshold tied to coordination performance, not directly to bits.
- Emphasize the distribution choice for expectations: “All expectations taken under the stationary state distribution ρ(S) induced by π or by a fixed reference policy.”
- Keep Slepian–Wolf terms in analogy callouts; otherwise say “environment evaluates joint actions.”

## Optional Rewrite (Conjecture box)
Conjecture (Approximate, plain language)
- Each agent needs to learn only the part of its optimal behavior that teammates can’t already infer from their own behavior.
- If every agent’s policy contains at least that much unique information, the team can achieve near‑optimal coordination.

One instantiation (Information view)
- Random variables: S ~ ρ; O_i = Ω_i(S); A_i* ~ 𝒁_i(·|S); A_i ~ π_i(·|O_i).
- Threshold: R_{π_i} := I(A_i*; A_i | S) ≥ H(A_i* | A_{−i}*), for all i.
- Intuition: The information agent i’s actions carry about the teacher’s optimal actions must beat the residual uncertainty left after seeing others’ optimal actions.

Measurement note (Bucket Brigade)
- Estimate H(A_i*|A_{−i}*) from a centralized teacher (π*) via rollouts; for small discrete tasks, compute exactly.
- Estimate I(A_i*; A_i | S) via contingency tables collected under π or a fixed behavior policy; report bias‑corrected estimates with error bars.

## Line‑Level Notes
- Section start and intuition: `src/research/papers/2024-slepian-wolf-marl.tsx:1026`, `:1034`
- Formal statements (strong/approx): `:1078` (block), subsequent blocks through ~`:1160`
- Slepian–Wolf relationship: `:1207`
- Implications/failure modes: `:1270`, `:1289`
- Testable predictions (bridge): `:1362`
