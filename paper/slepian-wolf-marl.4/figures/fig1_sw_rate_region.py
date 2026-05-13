"""fig1_sw_rate_region.py

Slepian-Wolf rate region with MARL analog labels.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.bbox': 'tight',
})

# Pick representative values
H_X = 3.0          # H(X)
H_Y = 2.5          # H(Y)
H_X_given_Y = 1.8  # H(X|Y)
H_Y_given_X = 1.3  # H(Y|X)
H_XY = H_X_given_Y + H_Y  # = H_Y_given_X + H_X by chain rule (here 4.3)

fig, ax = plt.subplots(figsize=(4.8, 3.6))

# Plot the achievable region: R_X >= H(X|Y), R_Y >= H(Y|X), R_X + R_Y >= H(X,Y)
# Shade the achievable region with a light blue patch.
R_max = 5.0
xs = np.linspace(0, R_max, 400)

# Boundary curve R_X + R_Y = H(X,Y) for R_X >= H(X|Y)
boundary_x = np.array([H_X_given_Y, H_X_given_Y, H_X,            R_max])
boundary_y = np.array([R_max,        H_Y,         H_Y_given_X,   H_Y_given_X])

# Polygon vertices for shaded region
verts = [
    (H_X_given_Y, R_max),
    (H_X_given_Y, H_Y),
    (H_X,         H_Y_given_X),
    (R_max,       H_Y_given_X),
    (R_max,       R_max),
]
poly = mpatches.Polygon(verts, closed=True, facecolor="#BBDEFB", edgecolor="none", alpha=0.7, zorder=1)
ax.add_patch(poly)

# Sum-rate boundary segment R_X + R_Y = H(X,Y)
ax.plot([H_X_given_Y, H_X], [H_Y, H_Y_given_X], color="#1565C0", linewidth=1.8, zorder=3)
# Vertical lower edge
ax.plot([H_X_given_Y, H_X_given_Y], [H_Y, R_max], color="#1565C0", linewidth=1.8, linestyle="--", zorder=3)
# Horizontal lower edge
ax.plot([H_X, R_max], [H_Y_given_X, H_Y_given_X], color="#1565C0", linewidth=1.8, linestyle="--", zorder=3)

# Tick markings for the key entropies
ax.axvline(H_X_given_Y, ymin=0, ymax=H_Y_given_X / R_max, color="#888", linewidth=0.6, linestyle=":")
ax.axhline(H_Y_given_X, xmin=0, xmax=H_X_given_Y / R_max, color="#888", linewidth=0.6, linestyle=":")

# Annotate corner points
ax.plot(H_X_given_Y, H_Y, "o", color="#1565C0", markersize=4, zorder=4)
ax.plot(H_X, H_Y_given_X, "o", color="#1565C0", markersize=4, zorder=4)

ax.annotate(r"$(H(X|Y),\,H(Y))$", xy=(H_X_given_Y, H_Y),
            xytext=(H_X_given_Y - 1.6, H_Y + 0.35), fontsize=8,
            arrowprops=dict(arrowstyle="-", color="#666", lw=0.6))
ax.annotate(r"$(H(X),\,H(Y|X))$", xy=(H_X, H_Y_given_X),
            xytext=(H_X - 1.3, H_Y_given_X - 0.55), fontsize=8,
            arrowprops=dict(arrowstyle="-", color="#666", lw=0.6))

# Axis ticks
ax.set_xticks([0, H_X_given_Y, H_X, R_max])
ax.set_xticklabels(["0", r"$H(X|Y)$", r"$H(X)$", ""])
ax.set_yticks([0, H_Y_given_X, H_Y, R_max])
ax.set_yticklabels(["0", r"$H(Y|X)$", r"$H(Y)$", ""])

# Region label
ax.text(3.4, 3.5, "Achievable\n(Slepian-Wolf)", fontsize=10, color="#0D47A1",
        ha="center", style="italic", zorder=5)

# Axis labels
ax.set_xlabel(r"Rate $R_X$  $\;\sim\;$  per-agent capacity for agent 1", fontsize=9)
ax.set_ylabel(r"Rate $R_Y$  $\;\sim\;$  per-agent capacity for agent 2", fontsize=9)

# MARL analog box (top of plot)
analog_text = (
    "MARL analog: "
    r"$R_X \to R_{\pi_1}$, $R_Y \to R_{\pi_2}$, "
    r"$H(X|Y) \to H(A_1^* \mid A_{-1}^*)$"
)
ax.text(0.5, 1.04, analog_text, transform=ax.transAxes, fontsize=7.5,
        ha="center", va="bottom",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFFDE7",
                  edgecolor="#FBC02D", linewidth=0.6))

ax.set_xlim(0, R_max)
ax.set_ylim(0, R_max)
ax.set_aspect('equal')
ax.set_title("Slepian-Wolf rate region (lossless distributed source coding)",
             fontsize=10, pad=24)

for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

fig.tight_layout()
fig.savefig("fig1_sw_rate_region.pdf")
fig.savefig("fig1_sw_rate_region.png")
print("Saved fig1_sw_rate_region.{pdf,png}")
