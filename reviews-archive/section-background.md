<!-- moved to be colocated with the paper -->
# Review: Background and Related Work

Audience: 1st–2nd year grad students (ML + basic info theory). Goal: introduce essentials without overwhelming, and clearly bridge to your MARL framing and Bucket Brigade program.

## Summary
- Provides an information theory primer (entropy, conditional entropy, mutual information) with simple examples and equations (see `src/research/papers/2024-slepian-wolf-marl.tsx:300`).
- Explains Slepian–Wolf via an Alice/Bob scenario and motivates “conditional information” (around `src/research/papers/2024-slepian-wolf-marl.tsx:360`).
- Maps distributed compression to multi‑agent learning with a comparison table; motivates specialization and communication thresholds.

## Audience Fit
- Strengths: Good intuitive primers and real‑world analogies; minimal prerequisites beyond basic probability and KL.
- Risks: The primer is long and may delay the main narrative; the comparison table appears before a concrete MARL micro‑example; terms like “joint decoder” may prime reconstruction rather than evaluation.
- Opportunity: Use a tiny MARL example (2×2 coordination game) to anchor “conditional information” before formal definitions. Introduce Bucket Brigade early as the running example for the program.

## Issues & Risks
- Jargon drift: “Joint decoder” risks misunderstanding. Prefer “environment evaluates joint actions” except when explicitly discussing the compression analogy.
- Primer length: The multi‑page primer may feel heavy for readers who already know the basics; move proofs and extended math to an appendix, keep the main thread tight.
- Table before example: The mapping table is clearer after a simple example showing how one agent’s action reduces uncertainty about another’s.
- Missing bridge notes: After each concept (H, H|, I), add a one‑line “Why this matters for MARL.”

## Suggestions (Structure)
- Add a short “What to remember” callout after each concept:
  - Entropy H(X): how unpredictable a variable is → task complexity for an agent’s optimal actions.
  - Conditional entropy H(X|Y): unpredictable after seeing Y → what each agent uniquely needs to learn.
  - Mutual information I(X;Y): shared information → redundancy between agents or observations.
- Insert a 2×2 coordination game before the table to illustrate conditional information without equations.
- Reorder: Primer (short) → 2×2 example → Slepian–Wolf story (analogy + differences) → Mapping table → Early Bucket Brigade mention.
- Keep equations, but gate keep details in expandable callouts or defer to Appendix A.

## Suggestions (Wording)
- Use “environment evaluates joint actions” when not explicitly within the compression analogy.
- Say “we use Slepian–Wolf as inspiration” and list key differences (lossy policies, non‑i.i.d., sequential, non‑stationary) in a small box.
- Replace shorthand “conditional entropy of optimal actions” with “conditional information (what remains unpredictable given teammates), quantified later as conditional entropy.”

## Optional Rewrite (opening of Background)
Many multi‑agent problems can be illuminated with a few ideas from information theory. We’ll keep this section brief and focus on the concepts we use throughout the paper; fuller details and proofs are in the appendix.

- Entropy H(X) measures unpredictability. Higher entropy means more “variety” in what you need to be ready for. In our setting, it tracks how complex an agent’s optimal actions can be.
- Conditional entropy H(X|Y) captures what remains unpredictable after seeing Y. For us, it’s what agent i still needs to learn once it can observe (or infer) what other agents are doing.
- Mutual information I(X;Y) is the overlap in information between X and Y. Between agents, high overlap can mean redundant learning; low overlap suggests useful specialization.

We’ll use these concepts to connect multi‑agent learning with an idea from distributed compression (Slepian–Wolf): when two observers see correlated data, they can compress efficiently without talking by focusing on the parts the other can’t predict. We’ll show how the same “don’t learn what others can already infer” intuition helps explain specialization, capacity needs, and when explicit communication is worth adding.

## Line‑Level Notes
- Background start and primer context: `src/research/papers/2024-slepian-wolf-marl.tsx:281`
- Slepian–Wolf story block: `src/research/papers/2024-slepian-wolf-marl.tsx:360`
- Mapping table location: `src/research/papers/2024-slepian-wolf-marl.tsx:392`
