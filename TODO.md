# TODO — Slepian-Wolf MARL Research Program

## Paper 1 (slepian-wolf-marl.4) — DONE

Paper is READY (33/40) and live at rjwalters.info. No further revision needed
unless Paper 2 experimental results contradict claims in Paper 1.

---

## Paper 2 (slepian-wolf-marl-2.1) — DRAFTING

**Thesis:** Conditional entropy $\tilde{H}_i := H(A_i^*|A_{-i}^*)$ of the
heterogeneous Nash equilibrium predicts PPO trainability across the Bucket
Brigade phase diagram. PPO succeeds in low-$\tilde{H}_i$ (`symmetric_only`)
cells and fails structurally in high-$\tilde{H}_i$ (`asymmetric_only`) cells.
Asymmetry-aware training narrows the gap on the latter.

**Companion benchmark paper:** A parallel submission drafted in
`bucket-brigade/paper/anvil_pub.1/` (planned; see bucket-brigade issue #364)
presents the same phase diagram as a MARL environment benchmark without the
information-theoretic framing. The two papers share upstream artifacts and are
designed to be read independently.

### Upstream compute (tracked in bucket-brigade)

These are not work items in this repo. They are bucket-brigade roadmap items
whose outputs Paper 2 consumes.

| Issue | Title | Paper 2 consumes |
|---|---|---|
| [#357](https://github.com/rjwalters/bucket-brigade/issues/357) | Tracker | (overall roadmap) |
| [#358](https://github.com/rjwalters/bucket-brigade/issues/358) | Phase diagram across (β, κ, c) | Per-cell Nash classification + converged profiles |
| [#359](https://github.com/rjwalters/bucket-brigade/issues/359) | Analytical NE characterization | Theory section reference |
| [#360](https://github.com/rjwalters/bucket-brigade/issues/360) | PPO trainability sweep | Per-cell `gap_closed` (y-axis of headline figure) |
| [#361](https://github.com/rjwalters/bucket-brigade/issues/361) | Specialist exploitability for rest_trap | Validates the asymmetric anchor |
| [#362](https://github.com/rjwalters/bucket-brigade/issues/362) | Env spec doc | Cited; we use shared environment description |
| [#368](https://github.com/rjwalters/bucket-brigade/issues/368) | Estimate H(A_i*\|A_{-i}*) per cell | Per-cell $\tilde{H}_i$ (x-axis of headline figure) |

### Work items in this repo

#### A. Paper updates as bucket-brigade artifacts ship

- [ ] Two-anchor section (`minimal_specialization` + `rest_trap`): currently has the qualitative result; add per-position $\tilde{H}_i$ with bootstrap CIs once #368 produces them for the two anchors
- [ ] Phase diagram section: insert the figure produced by #358; insert the cell-count summary table
- [ ] Conditional entropy subsection (3.1): insert the scatter from #368
- [ ] Headline figure (Section 5): `gap_closed` from #360 vs. $\tilde{H}_i$ from #368, with Spearman ρ + permutation p-value
- [ ] Tier-1 sweep table is currently filled with 3-seed minspec data; extend or replace with the phase-diagram sweep when #360 ships

#### B. Asymmetry-aware training story

- [ ] Identify the specific method to credit (still TBD — bucket-brigade roadmap doesn't yet have an explicit issue for this; the existing JointPPOTrainer plus per-position parameter un-sharing may already be the candidate)
- [ ] Once the method is settled, write Section 4.2 (currently a TODO)
- [ ] Insert results on high-$\tilde{H}_i$ cells (likely `rest_trap` first, then phase-diagram extension)

#### C. Literature review — DONE this session

- [x] Targeted 5-area lit search → `literature.md` (20 ranked entries)
- [x] Bibliography integrated inline in `paper.tex` (18 `\bibitem` entries; matches v4 style; no separate `refs.bib`)
- [x] Theory subsection `sec:theory` added, grounded in Emmons et al. (ICML 2022) + Fey (2012) — reframed paper's contribution from "structural claim" to "quantitative predictor extending established prior art"
- [ ] *(deferred)* Targeted search for `HeterogeneousDoubleOracle` algorithmic prior art before claiming algorithm novelty
- [ ] *(deferred)* Read Strategic Risk Aversion (arXiv:2602.21515) — possible baseline or competing framing

#### D. Mechanical paper completion

- [x] PDF compiles cleanly (7 pages, 0 unresolved citations, 0 errors)
- [ ] Replace remaining `\TODO{...}` and `\RESULT{...}` markers (blocked on bucket-brigade #358, #360, #368)
- [ ] Run `/pub-review` to score (premature until A/B complete; would just flag missing data)
- [ ] Revision loop until score >= 32/40, 0 critical issues
- [ ] `/pub-audit`
- [ ] `/pub-website`

---

## Open Research Questions

- Is the failure of standard PPO on `asymmetric_only` cells truly structural
  (no symmetric basin) or does sufficient initialization noise + entropy bonus
  eventually break symmetry? (bucket-brigade #360 will inform.)
- Does the deceptive signaling layer (two-phase commitment mode, #236/#252)
  change the Nash classification of any cell?
- Can $\tilde{H}_i$ be estimated cheaply from a coarse symmetric-DO result,
  as a fast pre-screen before running the full heterogeneous DO?
- ~~Should Paper 2 cite a specific operationalization of "symmetric self-play
  cannot reach asymmetric NE" from the game-theory literature?~~ **Resolved:**
  Emmons et al. (ICML 2022) is the load-bearing prior art; cited and
  positioned in `sec:theory`.
