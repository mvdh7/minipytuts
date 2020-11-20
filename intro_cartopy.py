from cartopy import crs as ccrs, feature as cfeature
from matplotlib import pyplot as plt
import pandas as pd, xarray as xr, numpy as np
import cmocean

# Import data
rws = pd.read_excel(
    "data/RWS-NIOZ North Sea data v6-1 for SDG14-3-1.xlsx", na_values=-999,
)
gebco = xr.open_dataset("data/gebco_2020_noordzee.nc")

#%% Do per-station analysis
def per_station(station):
    return pd.Series({
        "latitude": station.LATITUDE.mean(),
        "longitude": station.LONGITUDE.mean(),
        "dic_count": np.sum(~np.isnan(station.dic)),
    })

# # Test our function
# walcrn2 = rws[rws.station == "WALCRN2"]
# stations_test = per_station(walcrn2)

stations = rws.groupby("station").apply(per_station)

#%% Initialise figure
fig = plt.figure(dpi=300)
ax = fig.add_subplot(projection=ccrs.Robinson(central_longitude=0))

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
# ax.scatter("LONGITUDE", "LATITUDE", data=rws, transform=ccrs.PlateCarree(), zorder=10)
splot = ax.scatter(
    "longitude",
    "latitude",
    c="dic_count",
    cmap="plasma",
    data=stations,
    transform=ccrs.PlateCarree(),
    zorder=10,
)
scbar = plt.colorbar(splot)
scbar.set_label("Number of DIC data")
ax.text(0, 1.05, "(a)", transform=ax.transAxes)
# transform kwarg sets what format the x and y numbers are in, not the projection that
# they are going to

# Plot bathymetry from data
gplot = (
    gebco.elevation  # take the elevation data
    .coarsen(lon=5, lat=5, boundary="trim").mean()  # reduce its resolution
    .plot(
        add_colorbar=False,
        ax=ax,
        # cmap="cmo.topo",
        cmap="gray",
        transform=ccrs.PlateCarree(),
        vmin=-200,
        vmax=0,
        zorder=-5,
    )  # plot it
)

gcbar = plt.colorbar(gplot)
gcbar.set_label("Depth / m")
gcbar.set_ticks(np.arange(-200, 1, 25))
gcbar.set_ticklabels(-gcbar.get_ticks())

# Plot settings
# ax.set_global()
ax.set_extent((0, 8, 50, 57))  # west, east, south, north limits
ax.gridlines(alpha=0.3)

plt.savefig("figures/intro_cartopy.png")
