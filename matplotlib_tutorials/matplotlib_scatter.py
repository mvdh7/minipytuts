import pandas as pd, numpy as np
from matplotlib import pyplot as plt

# import matplotlib.pyplot as plt  # exactly the same!

# Import dataset
glodap = pd.read_csv("data/GLODAPv2.2020_Indian_Ocean.csv", na_values=-9999)

#%% Scatter dissolved inorganic carbon (tco2) vs total alkalinity (talk)

# Make the blank figure canvas
fig, axs = plt.subplots(
    dpi=300, figsize=(5, 6), nrows=2
)  # figsize in inches (width, height)

# Add the data
ax = axs[0]
# glodap[glodap["depth"] < 20].plot.scatter("tco2", "talk", ax=ax, s=3)  # pandas-style
scatter_pts = ax.scatter(
    "tco2",
    "talk",
    data=glodap[glodap["depth"] < 20],
    s=3,
    c="temperature",
    cmap="plasma",  # colormap
)  # matplotlib-style

# Add colour bar
cb = plt.colorbar(scatter_pts, ax=ax)
cb.set_label("Temperature / °C")

# Control figure settings
ax.set_xlabel("DIC / μmol kg$^{-1}$")  # LaTeX-style formatting in $...$
yl0 = ax.set_ylabel("Alkalinity / μmol kg$^{-1}$")
ax.grid(alpha=0.3)
ax.text(0, 1.05, "(a)", transform=ax.transAxes)

# Do the second axis ===============================================================
# Add the data
ax = axs[1]
# glodap[glodap["depth"] < 20].plot.scatter("tco2", "talk", ax=ax, s=3)  # pandas-style
scatter_pts = ax.scatter(
    "salinity",
    "temperature",
    data=glodap[glodap["depth"] < 20],
    s="nitrate",
    c="latitude",
    cmap="viridis",  # colormap
)  # matplotlib-style

# Add colour bar
cb = plt.colorbar(scatter_pts, ax=ax)
cb.set_label("Latitude / °N")

# Control figure settings
ax.set_xlabel("Salinity")  # LaTeX-style formatting in $...$
yl1 = ax.set_ylabel("Temperature / °C")  # , labelpad=18)
ax.grid(alpha=0.3)
ax.text(0, 1.05, "(b)", transform=ax.transAxes)
ax.set_xticks(np.arange(25, 50, 1))
ax.set_xlim([31, 38])

# Adjust positioning
fig.align_ylabels()

# Save the figure
plt.tight_layout()
# plt.savefig("figures/mpl_scatter.png")
# plt.savefig("figures/mpl_scatter.pdf")
