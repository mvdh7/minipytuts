from cartopy import crs as ccrs, feature as cfeature
from matplotlib import pyplot as plt
import pandas as pd

# Import data
rws = pd.read_excel(
    "data/RWS-NIOZ North Sea data v6-1 for SDG14-3-1.xlsx", na_values=-999,
)

# Initialise figure
fig = plt.figure(dpi=300)
ax = fig.add_subplot(projection=ccrs.Mollweide(central_longitude=0))

# Quick visualisation of the coastlines
# ax.coastlines()

# Add more detailed features from NaturalEarthData.com
ax.add_feature(
    cfeature.NaturalEarthFeature("physical", "land", "10m"), facecolor="k",
)
ax.add_feature(
    cfeature.NaturalEarthFeature("physical", "lakes", "10m"), facecolor="w",
)
ax.add_feature(
    cfeature.NaturalEarthFeature("physical", "minor_islands", "10m"), facecolor="k",
)

# Scatter the data
ax.scatter("LONGITUDE", "LATITUDE", data=rws, transform=ccrs.PlateCarree())
ax.text(0, 1.05, "(a)", transform=ax.transAxes)
# transform kwarg sets what format the x and y numbers are in, not the projection that
# they are going to

# Plot settings
# ax.set_global()
ax.set_extent((0, 10, 50, 60))  # west, east, south, north limits
ax.gridlines(alpha=0.3)