"""fig4_capacity_sigmoid.py

Hypothesized team-reward vs.\\ capacity-proxy curve illustrating Prediction 1.
Marked clearly as illustrative; the experimental protocol of Section 7 tests
whether the knee actually exists near the conditional-entropy threshold.
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.bbox': 'tight',
})

# Capacity in some abstract proxy units; the threshold C^* corresponds to
# H(A_i^*|A_{-i}^*) / (alpha b) per Proxy A.6.
C = np.linspace(0, 4, 400)
C_star = 1.0  # threshold

def reward_curve(C, k=6.0, J_floor=0.35, J_ceil=0.92):
    """Sigmoid from J_floor to J_ceil with knee at C_star."""
    s = 1.0 / (1.0 + np.exp(-k * (C - C_star)))
    return J_floor + (J_ceil - J_floor) * s

# Three proxies giving slightly different empirical knees
proxies = [
    ("Parameter count $|\\theta_i|$",                "#1565C0", 1.00, 6.0),
    ("Compression bits (gzip)",                       "#2E7D32", 0.95, 5.5),
    ("PAC-Bayes KL",                                  "#EF6C00", 1.10, 5.0),
    ("Pruned effective params",                       "#8E24AA", 0.92, 6.5),
]

fig, ax = plt.subplots(figsize=(5.5, 3.8))

for label, color, knee, slope in proxies:
    J = 0.35 + (0.92 - 0.35) / (1.0 + np.exp(-slope * (C - knee)))
    ax.plot(C, J, label=label, color=color, linewidth=1.5)

# Annotate the regions (underlay)
ax.axvspan(0, C_star * 0.75, color="#FFCDD2", alpha=0.18, zorder=0)
ax.axvspan(C_star * 1.25, 4, color="#C8E6C9", alpha=0.18, zorder=0)

# Annotate the threshold (after axvspan so the line is on top)
ax.axvline(C_star, color="#444444", linestyle=":", linewidth=1.0, zorder=1)
ax.text(C_star + 0.06, 0.34,
        r"$C^* \approx H(A_i^* \mid A_{-i}^*) / (\alpha b)$",
        fontsize=8.5, color="#222")

# Region labels along the top
ax.text(0.4, 0.97, "under-capacity", ha="center", fontsize=8, color="#B71C1C",
        transform=ax.get_xaxis_transform())
ax.text(2.6, 0.97, "over-capacity (diminishing returns)", ha="center",
        fontsize=8, color="#1B5E20", transform=ax.get_xaxis_transform())

ax.set_xlabel(r"Capacity proxy $\;/\;$ predicted threshold $C^*$")
ax.set_ylabel(r"Team reward $\mathbb{E}[R]\,/\,R^\ast$")
ax.set_xlim(0, 4)
ax.set_ylim(0.3, 0.99)
ax.legend(loc="center right", fontsize=7.5, frameon=False,
          bbox_to_anchor=(0.98, 0.45))

# Hypothesis disclaimer (below plot)
fig.text(0.5, -0.02,
         "Hypothesized capacity sigmoid (Prediction 1). "
         "Falsifier: smooth growth with no knee across all four proxies.",
         ha="center", va="top", fontsize=8, style="italic", color="#444")

ax.set_title("Conjectured capacity sigmoid (Prediction 1)", fontsize=10, pad=10)

for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

fig.tight_layout()
fig.savefig("fig4_capacity_sigmoid.pdf")
fig.savefig("fig4_capacity_sigmoid.png")
print("Saved fig4_capacity_sigmoid.{pdf,png}")
