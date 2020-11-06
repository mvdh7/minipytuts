import xarray as xr

# Import GEBCO dataset
gebco = xr.open_dataset("data/gebco_2020_n50.9_s41.7_w-12.7_e-0.1.nc")

# Change the axis label
gebco.elevation.attrs["long_name"] = "Elevation"

#%% Plot the data
gebco.elevation.plot()

#%% Select a single grid row and plot it
gebco.elevation.sel(lon=-8, method='nearest').plot()


#%% Import satellite data directly from online
oc = xr.open_dataset("https://oceandata.sci.gsfc.nasa.gov:443/opendap/MODISA/L3SMI/2020/0101/AQUA_MODIS.20200101.L3m.DAY.SST.sst.9km.nc")

#%% Coarsen the data then plot
oc.sst.coarsen(lat=5, lon=5, boundary="trim").mean().plot(vmin=0, vmax=30, cmap="magma")

#%% Select a subset of the data
# Get latitudes in northern hemisphere
northern_hem = oc.lat[oc.lat > 0]
lon_range = oc.lon[(oc.lon > -100) & (oc.lon < 0)]

# Plot it
oc.sst.sel(lat=northern_hem, lon=lon_range, method="nearest").plot(vmin=0, vmax=30, cmap="magma")

#%% Interpolate the gaps in an extremely basic way
(
    oc.sst
    .coarsen(lat=5, lon=5, boundary="trim").mean()
    .interpolate_na(dim="lon")
    .plot(vmin=0, vmax=30, cmap="magma")
)
