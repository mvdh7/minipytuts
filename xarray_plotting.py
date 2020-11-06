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
oc = xr.open_dataset("https://oceandata.sci.gsfc.nasa.gov:443/opendap/MODISA/L3SMI/2020/0601/AQUA_MODIS.20200601_20200630.L3m.MO.NSST.sst.9km.nc")

#%% Coarsen the data then plot
oc.sst.coarsen(lat=5, lon=5, boundary="trim").mean().plot(vmin=0, vmax=30, cmap="magma")

#%% Select a subset of the data
# Get latitudes in northern hemisphere
lat_range = oc.lat[(oc.lat > 40) & (oc.lat < 50)]
lon_range = oc.lon[(oc.lon > 25) & (oc.lon < 42)]

# Plot it
oc.sst.sel(lat=lat_range, lon=lon_range, method="nearest").plot(vmin=0, vmax=30, cmap="magma")

#%% Interpolate the gaps in an extremely basic way
(
    oc.sst
    .coarsen(lat=5, lon=5, boundary="trim").mean()
    .interpolate_na(dim="lon")
    .plot(vmin=0, vmax=30, cmap="magma")
)
