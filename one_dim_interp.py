import pandas as pd, numpy as np
from matplotlib import pyplot as plt, dates as mdates
from scipy import interpolate

# Import data
rws = pd.read_excel(
    "data/RWS-NIOZ North Sea data v6-1 for SDG14-3-1.xlsx",
    na_values=-999,
).rename(columns={
    "LATITUDE": "latitude",
    "LONGITUDE": "longitude",
    "DATE_UTC": "datetime",
})
rws["datenum"] = mdates.date2num(rws.datetime)

# Set which variables we're looking at
xvar = "datenum"
yvar = "temperature"
zvar = "pH_spectro_total_lab"

# Pick out first station
L = (rws.station == "WALCRN2") & ~np.isnan(rws[yvar]) & ~np.isnan(rws[zvar])

# Do some interpolation
data_x = rws[L][xvar]
data_y = rws[L][yvar]
data_z = rws[L][zvar]

ix = np.linspace(data_x.min(), data_x.max(), num=1000)
iy_numpy = np.interp(ix, data_x, data_y)

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html#scipy.interpolate.interp1d
fy_interp1d = interpolate.interp1d(data_x, data_y, kind='cubic')
iy_interp1d = fy_interp1d(ix)

fy_pchip = interpolate.PchipInterpolator(data_x, data_y)
iy_pchip = fy_pchip(ix)
fz_pchip = interpolate.PchipInterpolator(data_x, data_z)
iz_pchip = fz_pchip(ix)

# Make a plot
fig, axs = plt.subplots(nrows=2, dpi=300, figsize=(5, 8))
ax = axs[0]
ax.scatter(xvar, yvar, data=rws[L], label="Data")
ax.plot(xvar, yvar, data=rws[L], label="plot")
ax.plot(ix, iy_numpy, dashes=[4, 4], label="np.interp")
ax.plot(ix, iy_interp1d, label="interp1d")
ax.plot(ix, iy_pchip, label="PCHIP")
ax.legend()
ax.set_xlabel("Decimal days since 1970-01-01")
if yvar == "dic":
    ax.set_ylabel("DIC / micromol kg$^{-1}$")
elif yvar == "alkalinity":
    ax.set_ylabel("Alkalinity / micromol kg$^{-1}$")
else:
    ax.set_ylabel(yvar)
ax.grid(alpha=0.3)

ax = axs[1]
ax.scatter(data_y, data_z)
ax.plot(iy_pchip, iz_pchip)
