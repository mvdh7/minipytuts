import pandas as pd, numpy as np, seaborn as sns
from matplotlib import pyplot as plt, dates as mdates
from scipy.stats import linregress
from scipy.optimize import least_squares
from fitting_1 import get_flask_data

filename = "data/co2_mhd_surface-flask_1_ccgg_event.txt"
flask = get_flask_data(filename)

# Run the function
flask = get_flask_data(filename)

# Do a linear regression
slope, intercept, r, p, se = linregress(
    flask[flask.xco2_good].datenum, flask[flask.xco2_good].xco2
)


def xco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    xco2 = (
        datenum * slope 
        + intercept 
        + sine_stretch * np.abs(np.sin((datenum - sine_shift) * np.pi / 365.25))
    )
    return xco2


def lsq_xco2_fit(coeffs, datenum, xco2):
    return xco2_fit(coeffs, datenum) - xco2


opt_result = least_squares(lsq_xco2_fit, [0.005, 310, 5, 0], args=(
    flask[flask.xco2_good].datenum, flask[flask.xco2_good].xco2)
)
# fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, ax = plt.subplots(dpi=300)
flask.plot("datetime", "xco2", ax=ax)

fx = np.linspace(flask.datenum.min(), flask.datenum.max(), 10000)
fy = xco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy)

# # Visualise
# fig, axs = plt.subplots(ncols=2, dpi=300)
# ax = axs[0]
# flask.plot("datetime", "xco2", ax=ax)
# fx = np.array([flask.datenum.min(), flask.datenum.max()])
# fy = fx * slope + intercept
# fx_datetime = mdates.num2date(fx)
# ax.plot(fx, fy)
# ax = axs[1]
# sns.regplot(x="datenum", y="xco2", data=flask[::40], ax=ax, ci=99.9)
