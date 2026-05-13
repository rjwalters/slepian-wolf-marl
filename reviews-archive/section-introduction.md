<!-- moved to be colocated with the paper -->
# Review: Introduction

Audience: 1st–2nd year grad students (ML + basic info theory). Goal: motivate, give intuition, set roadmap, and anchor the Bucket Brigade research program.

## Summary
- Opens with an accessible hook (jazz ensemble and application cases) and poses the central question about coordination without communication (src/research/papers/2024-slepian-wolf-marl.tsx:93).
- Introduces the information‑theoretic lens: policy as lossy encoder of a latent optimal strategy; environment as joint decoder/evaluator (src/research/papers/2024-slepian-wolf-marl.tsx:140).
- Uses Slepian–Wolf/weather‑station analogy and a table mapping distributed compression to MARL (src/research/papers/2024-slepian-wolf-marl.tsx:161–208).
- Lists contributions and previews predictions (src/research/papers/2024-slepian-wolf-marl.tsx:214–230).

## Audience Fit
- Strengths: Good real‑world examples, clear analogies, and a comparison table that grounds the mapping.
- Risks: “Joint decoder” may mislead; “latent optimal strategy,” “conditional entropy,” and “capacity” need concrete, informal definitions early. The table may feel heavy before a running example.
- Opportunity: Introduce Bucket Brigade earlier as the running example for the rest of the paper.

## Issues & Risks
- Decoder metaphor: Rephrase to emphasize evaluation, not reconstruction (src/research/papers/2024-slepian-wolf-marl.tsx:140).
- Leap from compression rate to neural network capacity: Flag as intuition/hypothesis here; reserve formal claims for later sections.
- Table before example: Readers may benefit from a tiny game (2×2 matrix) showing what “conditional information” means before the table.
- Term definitions scattered: Consolidate mini‑glossary close to first use (encoder, lossy, latent optimal strategy) (src/research/papers/2024-slepian-wolf-marl.tsx:131–152).

## Suggestions (Structure)
- Opening hook (keep), then add a 2×2 coordination game that shows how one agent’s action can be inferred from the other, introducing conditional information without equations.
- Informal claim box: “Agents only need to learn what others can’t infer.” Place right after the example.
- Short mini‑glossary callout for encoder/lossy/latent strategy and a one‑line note on conditional information.
- Replace “joint decoder” with “environment evaluates joint actions” across intro.
- Contributions tailored for broader audience: separate “What you get out of this paper” (intuition + practical rules of thumb) from “Technical contributions.”
- Early mention of Bucket Brigade as the program’s testbed and a figure preview.

## Suggestions (Wording)
- Prefer “environment evaluates joint actions” over “joint decoder.”
- Use “conditional information (what’s unpredictable given others)” instead of “conditional entropy” until the Background section.
- Qualify predictions as “we hypothesize and test.”

## Optional Rewrite (first ~6 paragraphs)
Coordination without reliable communication is a recurring challenge in robotics, sensing, and other multi‑agent systems. How can independent learners end up behaving in ways that fit together?

Our perspective is simple: learning a policy is a kind of compression. Each agent distills its experience into a compact internal representation (its network) that keeps just the information needed to act well. When several agents act together, the environment’s rewards tell us how well those compressed strategies fit.

Here’s the key intuition we’ll develop: each agent only needs to learn the parts of the strategy that teammates can’t infer on their own—the conditional information. When agents split up that information well, they coordinate; when they duplicate it, they waste capacity and struggle.

We make this intuition concrete by borrowing ideas from distributed compression, where separate observers can compress correlated data efficiently without talking. While our setting is learning and control, not lossless coding, the same “don’t send what others can predict” principle applies.

This lens leads to practical guidance: how large policies need to be in relation to the task’s conditional information, why specialization emerges, and when explicit communication helps. Throughout, we’ll use our Bucket Brigade environment as a running example to measure both performance and information.

Finally, we outline the contributions and a roadmap for the rest of the paper, keeping technical details in later sections and focusing here on intuition and examples.

## Line‑Level Notes
- “How can independent learners…” hook: src/research/papers/2024-slepian-wolf-marl.tsx:93
- Glossary block placement: src/research/papers/2024-slepian-wolf-marl.tsx:131–152
- “Joint decoder” to “evaluates joint actions”: src/research/papers/2024-slepian-wolf-marl.tsx:140
- Table placement consideration: src/research/papers/2024-slepian-wolf-marl.tsx:177–208
