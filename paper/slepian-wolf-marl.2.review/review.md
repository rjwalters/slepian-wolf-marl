# Review: slepian-wolf-marl.2

**Reviewer:** Claude (automated paper review)
**Date:** 2026-05-13
**Paper reviewed:** `paper/slepian-wolf-marl.2/paper.tex`
**Previous review:** `paper/slepian-wolf-marl.1.review/review.md` (18/40 — NEEDS WORK)

---

## Overall Assessment: NEARLY READY

**Score: 26/40** (+8 vs. v1)

| Dimension | Score | Δ | Key Issue |
|-----------|-------|---|-----------|
| Technical Soundness | 4/5 | +2 | Theorems→Conjectures cleanly done in main body; 3 holdouts (A.3, E.4, E.5) still labeled "Theorem" with old notation. |
| Novelty & Contribution | 4/5 | +1 | Repositioned as unifying lens; ROMA/RODE/PMIC/IMAC engaged honestly. |
| Experimental Rigor | 3/5 | +2 | Protocol is solid and pre-registers falsifiers; no results yet, so rigor caps at 3. |
| Clarity & Writing | 3/5 | −1 | Abstract/body inconsistency (4 vs 5 predictions); $R_{\pi_i}$ used in main body without v2 definition; $H$ symbol clash. |
| Related Work Coverage | 4/5 | +2 | ~50 entries cover all inline citations. MIR3 (2024), MADPO (2024) missing. |
| Figures & Tables | 2/5 | +1 | Tables improved; figures/ still empty. |
| Reproducibility | 3/5 | +1 | Protocol is well-specified; statistical commitments stated up front. |
| Presentation & Structure | 3/5 | 0 | Closest Work + Protocol restructures help; Appendix A has numbering collisions. |

---

## v1 Critical Issues — Status

| v1 Critical Issue | Status | Notes |
|---|---|---|
| C1 Placeholder results as findings | **Fully fixed** | Section 7 now "Experimental Protocol"; all tables marked TBD; disclaimer prominent. |
| C2 Fano lower bound ill-defined | **Fully fixed** | Conjecture A.2 with Lipschitz-in-KL alternative; explicit explanation of v1's type error. |
| C3 Bits-per-parameter capacity | **Fully fixed (mostly)** | Heuristic A.1 with four proxies. Caveat: Definition A.13 still gives $C_\text{eff} = \alpha b m$ without v2 disclaimer. |
| C4 Sample complexity missing class term | **Fully fixed** | Scaling Hypothesis A.4 now has both $H$ and $\mathcal{C}(\Pi_i)$. |
| C5 Bibliography incomplete | **Fully fixed** | ~50 entries; every inline citation resolves. |
| C6 ROMA/RODE/PMIC/IMAC unengaged | **Fully fixed** | Closest Work subsection 2.7 with 2–4 sentences each; PMIC drives algorithmic redesign. |

All six v1 criticals addressed. The revision did substantive work — this is the main reason for the +8 score jump.

## v1 Important Issues — Status

| v1 Important Issue | Status | Notes |
|---|---|---|
| I1 Notation drift Z_i vs A_i^* | **Partial** | Main body (§1–9) clean; **Appendix A.10/A.13/A.14/A.15/A.17, Appendix C, D, E.1 still use $\mathcal{Z}_i$**. See remaining critical #2 below. |
| I2 Strong-form conjecture as iff | **Fully fixed** | Now "Strong Form (heuristic only)." |
| I3 Redundancy penalty contradicts PMIC | **Fully fixed** | Section 6 uses $I(\hat{Z}_i; \hat{Z}_j \mid R)$; rationale explicit. |
| I4 "Joint decoder" outside analogy | **Fully fixed** | Section 3.6/3.7 explicitly say environment is an evaluator, not a decoder. |
| I5 Title/scope mismatch | **Fixed via prose** | Section 1.3 says "conceptual rather than mathematical"; Section 3.7 is "The Analogy — and Its Limits." Title unchanged but no longer misleading. |
| I6 Appendix B (full PyTorch) | **Deferred (user choice)** | Retained at user request for future runs. Acknowledged. |
| I7 No figures | **Not addressed** | `figures/` is still empty. Carries over. |
| I8 NeurIPS Workshop footer | **Fixed** | Now "target venue under consideration." |

---

## Critical Issues (must fix in v3)

### 1. Abstract says "four testable predictions"; body has five (Dimension: 4)

- **Problem**: Line 42 of the abstract enumerates four predictions (capacity, specialization, communication, symmetry). Section 5 has **five**, adding Prediction 2 (Sample Complexity). The predictions summary table (Section 5.6, lines 404–417) shows five rows. Section 1's "What This Paper Offers" item #3 also says "Five predictions." This is a direct abstract-vs-body contradiction that any conference reviewer will catch immediately.
- **Impact**: First impression of dishonesty or sloppiness. Easy to fix; reflects poorly while present.
- **Recommendation**: Edit the abstract to enumerate all five, or to say "five testable predictions" and group sample-complexity inside the capacity-scaling phrase. Personally I'd add it: "capacity should scale with conditional entropy $H(A_i^* \mid A_{-i}^*)$, sample complexity should grow monotonically in $H$, agents should specialize..."

### 2. Symbol $R_{\pi_i}$ used in main body without v2 definition (Dimension: 1, 4)

- **Problem**: Section 4.3 (line 319) writes "$\sum_i R_{\pi_i} \geq H(A_1^*, \ldots, A_N^*)$" but Sections 1–6 never define $R_{\pi_i}$. The v1 review (I1) asked to either rename to $F_{\pi_i}$ (KL fidelity) or define as $I(A_i^*; A_i \mid S)$ (MI fidelity). Section 3.4 of v2 defines $F_{\pi_i}$ (KL) and uses $I(A_i^*; A_i \mid S)$ (MI), but $R_{\pi_i}$ is introduced for the first time in Appendix A's Heuristic A.1 (line 851) and used in the Summary of Conjectures table (line 986) and Appendix C/D (lines 2057, 2085, 2155, etc.). A reader following Section 4.3 with no Appendix-A pre-loading will hit an undefined symbol.
- **Impact**: Same load-bearing equation that the v1 review flagged as needing clarification.
- **Recommendation**: Either (a) in Section 3.4, define $R_{\pi_i} := I(A_i^*; A_i \mid S)$ explicitly and reuse this consistently, or (b) replace line 319's $R_{\pi_i}$ with $I(A_i^*; A_i \mid S)$ and remove $R_{\pi_i}$ from the paper entirely. Option (a) is simpler.

### 3. Three "Theorems" not downgraded (Dimension: 1)

- **Problem**: Appendix A.3 (Achievability), Appendix E.4 (POMDP Capacity), and Appendix E.5 (Continuous-Time Capacity) are still labeled "Theorem" with v1-style "proof outlines" that admit "Full proof requires measure-theoretic arguments beyond our scope." Theorem A.3 also uses $R_{\pi_i}$ and $\mathcal{Z}_i$ — the old notation. The downgrade pattern from v2 was applied consistently to A.1, A.2, A.4, A.5, A.6, A.7, A.8, A.9, A.10, E.1, E.2, E.3 — only these three escaped.
- **Impact**: Inconsistent — a careful reviewer will ask why some "theorems" survived and others didn't. The honest answer is that they shouldn't have.
- **Recommendation**: Downgrade in v3: "Theorem A.3" → "Conjecture A.3 (Achievability)" with the proof outline reframed as motivating intuition. "Theorem E.4" → "Conjecture E.4 (POMDP Capacity)." "Theorem E.5" → "Conjecture E.5 (Continuous-Time Capacity)." Use $A_i^*$ throughout.

---

## Important Issues (should fix in v3)

### I1. Appendix A/C/D/E notation drift not fully fixed (Dimension: 1, 4)

- **Problem**: The v1 review flagged this as load-bearing, and v2 cleaned up the main body but left several appendix locations in v1 notation:
  - Definition A.10 (line 822–824): marginalization formula uses $\mathcal{Z}_i$ exclusively.
  - Lemma A.1 (line 826–830): chain rule applied to $\mathcal{Z}_i$ as if it were an RV.
  - Definition A.13 (line 896–903): effective capacity formula uses old $\alpha b m$ without v2 caveat.
  - Definition A.14 (line 917–918): inter-policy redundancy defined as **unconditional** $I(\pi_i; \pi_j)$, contradicting Section 6's conditional-MI design.
  - Definition A.15 (line 926–928): role clarity uses $\mathcal{Z}_i$ entropies.
  - Definition A.17 (line 970–972): time-varying optimal distribution uses $\mathcal{Z}_t$.
  - Theorem A.3 (line 870–880): $R_{\pi_i} = H(\mathcal{Z}_i \mid \mathcal{Z}_{-i})$.
  - Appendix C tables (lines 2083–2104): metrics written with $\mathcal{Z}_i$.
  - Appendix D (lines 2134–2158): "Marginal Entropy: $H(\mathcal{Z}_i)$" etc.
  - Appendix E.1 Linear-Gaussian proof (lines 2551, 2562, 2567, 2569): uses $\mathcal{Z}_i$, $\pi_i$ as RVs.
  - Appendix E POMDP / Continuous extensions (lines 2973, 2976, 2984): $\mathcal{Z}_i$.
- **Recommendation**: A global pass: $\mathcal{Z}_i$ may appear only as a *distribution* (e.g., "$A_i^* \sim \mathcal{Z}_i(\cdot \mid S)$"); never inside $H(\cdot)$, $I(\cdot;\cdot)$, $D_\text{KL}(\cdot \| \cdot)$. Replace with $A_i^*$. ~15 minutes of find-and-replace plus a careful re-read.

### I2. Definition A.14 inconsistent with Section 6's algorithm (Dimension: 1)

- **Problem**: Section 6 uses conditional MI $I(\hat{Z}_i; \hat{Z}_j \mid R)$. Definition A.14 (line 917) defines "Inter-Policy Redundancy" as the **unconditional** $I(\pi_i; \pi_j)$. Proposition A.7 (line 920) then refers back to "$\mathcal{R}_{ij}$" from A.14 — perpetuating the inconsistency. PMIC's documented counterexample is exactly to *unconditional* MI penalties, so a reader who lands on A.14 first will see the wrong thing.
- **Recommendation**: Update A.14 to define $\mathcal{R}_{ij} := I(\pi_i; \pi_j \mid S)$ (or $I(\hat{Z}_i; \hat{Z}_j \mid R)$) consistent with Section 6. Note the v1 unconditional form was retained only for historical reference.

### I3. Numbering collisions in Appendix A (Dimension: 4, 8)

- **Problem**: The appendix uses parallel numbering across categories, leading to ambiguous citations:
  - "A.1": Definition A.1 (MAMDP) + Heuristic A.1 + Lemma A.1 + Proposition A.1.
  - "A.2": Definition A.2 (Observation Correlation) + Conjecture A.2 (Lower Bound) + Proposition A.2 (Specialization Metrics).
  - "A.3": Definition A.3 (Partial Observability Degree) + Theorem A.3 (Achievability) + Proposition A.3 (Continuous Capacity Bound).
- **Impact**: A future paper citing "Conjecture A.2" of this work could be read by a careless reader as the Observation Correlation definition.
- **Recommendation**: Either (a) cross-prefix numbering: Definition D.1, Proposition P.1, Conjecture C.1, etc.; or (b) keep a single sequence: Definition 1, Proposition 2, Conjecture 3, ... with `\theoremstyle` blocks. Latex `amsthm` makes this nearly free.

### I4. Missing recent (2023–2024) related work (Dimension: 5)

- **MIR3 (Liu et al., 2024)** — "Robust Multi-Agent Reinforcement Learning by Mutual Information Regularization" (arXiv:2310.09833, TNNLS 2025). Directly applies an information-bottleneck-style penalty between agents' histories and actions to improve robustness; cited as "remaining gap" in v2's `literature.md` but the v2 bibliography was expanded without adding it. Closely related to both Prediction 3 (specialization) and Prediction 5 (symmetry/robustness).
- **MADPO (Multi-Agent Divergence Policy Optimization, 2024)** — Quantifies policy discrepancies between episodes and between agents to enhance heterogeneity. Directly relevant to Prediction 3.
- **Recommendation**: Add both to the bibliography and reference in Section 2.7's Closest Work or 2.5's Information Theory in RL. Each gets a one-sentence treatment.

### I5. Symbol clash $H$ for entropy vs houses (Dimension: 4)

- **Problem**: Section 7.1 line 498 uses "$H{=}10$ houses" but $H$ is used everywhere else as entropy ($H(A_i^*)$, $H(A_i^* \mid A_{-i}^*)$).
- **Recommendation**: Rename to $K = 10$ houses or $n_\text{h} = 10$. Small but eliminates a real source of confusion when scanning Section 7.

### I6. Section 4.3 cross-reference to Section 7 (Dimension: 4, 8)

- **Problem**: Section 4.7 "Testable Predictions" closes with "We test these predictions in Section 7 using Bucket Brigade." But Section 7 is now a *protocol*, not a test. The wording is inconsistent with the experimental-deferral framing introduced in v2.
- **Recommendation**: "The protocol for testing these predictions appears in Section~\ref{sec:experiments}."

### I7. Section 4.5 / 4.6 still aspirational (Dimension: 1, 4)

- **Problem**: Section 4.5 "Implications" still says "Performance should show phase transitions near the conditional entropy threshold." — phrased as fact rather than conjecture. Section 4.6 "For practice" says "Size networks based on estimated conditional entropy" — but the heuristic in Heuristic A.1 / Proxy A.6 doesn't give an operational sizing rule; only a sweep center.
- **Recommendation**: Soften to "Performance is conjectured to show ..." and "Use the conditional-entropy estimate to set the *center* of a network-size sweep, not as a closed-form sizing prescription."

### I8. Still no figures (Dimension: 6)

- Carried over from v1.review. Conceptual figures (Slepian-Wolf rate region with MARL overlay, policy-as-encoder pipeline, Bucket Brigade topology, hypothesized sigmoid capacity curve) would substantially help. Run `/pub-figures slepian-wolf-marl.2` after the v3 cleanup.

---

## Suggestions (nice to have)

- **S1**: Section 4 ("Why Conditional Entropy?") and Section 5 each repeat the patrol-robot example. Pick one location.
- **S2**: The "Strong Form (heuristic only)" paragraph in Section 4 is now disclaimed but still ~80 words. Could be 30 words: "A natural idealization — infinite data, exact optimization — would suggest tight equality at $r_i = 1$. We do not pursue it because the necessity direction inherits the Conjecture-A.2 sketch."
- **S3**: The bibliography is organized by topic (good) but the categories overlap (e.g., MAVEN appears in "MARL roles / specialization / MI regularization" while it's more naturally an exploration paper). Minor.
- **S4**: Section 6's "Common Pitfalls" table has four rows. The PMIC-induced row "Coordination harm" → "Penalize representation, not actions" is now slightly out-of-date: v2 prescribes *conditional* MI at the representation level. Update to "Use conditional MI, not unconditional, at the representation level."
- **S5**: The Discussion ("On the 'this is just regularization' objection") is well-handled. Consider also pre-empting "this is just rate-distortion" — the answer is similar but reviewers who lean info-theory will ask.

---

## Missing Related Work

- **MIR3** — Liu, Y., Chen, S., Wang, Y., Mguni, D.H., Hao, J., An, B. (2024). Robust Multi-Agent Reinforcement Learning by Mutual Information Regularization. *IEEE TNNLS* / arXiv:2310.09833.
  - Relevance: IB on agent histories→actions; closest 2024 paper to the algorithmic prescription in Section 6. Connects to P3 + P5.
  - Recommendation: **Cite and discuss** in Section 2.5 or 2.7.
- **MADPO** — Multi-Agent Divergence Policy Optimization (OpenReview / NeurIPS 2024).
  - Relevance: Maximizes policy divergence between agents to enhance heterogeneity; directly addresses Section 5.3's prediction.
  - Recommendation: **Cite** in Section 2.7 alongside ROMA/RODE.

---

## Convergence Status

Per the `/pub-revise` rubric:

- **Score 26/40, with 3 critical-level issues** → technically "Needs Work" but the criticals are now *cleanup* (abstract typo, undefined symbol, three theorems not downgraded), not load-bearing math errors. The substance of the paper is solid.
- A focused v3 pass should resolve the criticals (≤1 hour) and the important issues (~2 hours), pushing the score to ~31–33/40 and triggering "Ready" if 0 criticals remain.

## Next Step

Run `/pub-revise slepian-wolf-marl.2` to create v3. The highest-leverage edits in priority order:

1. Abstract: "four testable predictions" → "five testable predictions" with all five listed.
2. Section 3.4: define $R_{\pi_i} := I(A_i^*; A_i \mid S)$ explicitly (then check the symbol resolves in Section 4.3 and Appendix A summary).
3. Theorem A.3 / E.4 / E.5 → Conjecture, with $A_i^*$ notation.
4. Appendix A/C/D/E global notation pass: $\mathcal{Z}_i$ only as distribution; replace with $A_i^*$ inside $H(\cdot)$ and $I(\cdot;\cdot)$.
5. Update Definition A.14 to conditional MI; update Section 6's "Common Pitfalls" row.
6. Add MIR3 and MADPO to bibliography.
7. (Optional) Renumber appendix to avoid A.1/A.2/A.3 collisions.

After v3, run `/pub-figures slepian-wolf-marl.3` to address the long-standing figures gap, then `/pub-review slepian-wolf-marl.3` for final scoring.
