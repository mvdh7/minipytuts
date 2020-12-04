import pandas as pd, numpy as np, seaborn as sns
from matplotlib import pyplot as plt, dates as mdates
from scipy.stats import linregress

filename = "data/co2_mhd_surface-flask_1_ccgg_event.txt"

with open(filename, "r") as f:
    raw_data = f.read()
# Get the subset of this data that we want
raw_lines = raw_data.splitlines()
# header_line = raw_lines[67]  # not robust!
header_line = [line for line in raw_lines if line.startswith("# data_fields:")]
# ^ list comprehension
header_text = header_line[0]
header_list = header_text.split(" ")
headers = header_list[2:]
headers = [h for h in header_list if h not in ["#", "data_fields:"]]
# ^ list comprehension

# # One-line-of-code approach to above steps
# with open(filename, "r") as f:
#     headers = [
#         line for line in f.read().splitlines() if line.startswith("# data_fields:")
#     ][0].split(" ")[2:]

# # Don't do this, use `with ... as ... :` instead (see above)
# f = open(filename, "r")
# # your code
# f.close()

# Import with pandas
flask = pd.read_table(
    filename, sep="\s+", skiprows=68, names=headers,  # regular expression / regexp
)

# Get datetime
# dt_cols = {"sample_year": "year", "sample_month": "month"}  # long-winded alternative
dt_cols = {"sample_" + t: t for t in ["year", "month", "day", "hour", "minute"]}
# dict comprehension ^
dt_cols["sample_seconds"] = "second"  # annoying override

# Extract date-time columns
flask["datetime"] = pd.to_datetime(flask[dt_cols.keys()].rename(dt_cols, axis=1))
flask["datenum"] = mdates.date2num(flask.datetime)

# QC good data
flask["xco2_good"] = flask.analysis_flag == "..."
flask["xco2"] = flask.analysis_value.where(flask.xco2_good)

# Do a linear regression
slope, intercept, r, p, se = linregress(
    flask[flask.xco2_good].datenum, flask[flask.xco2_good].xco2
)

# Visualise
fig, axs = plt.subplots(ncols=2, dpi=300)
ax = axs[0]
flask.plot("datetime", "xco2", ax=ax)
fx = np.array([flask.datenum.min(), flask.datenum.max()])
fy = fx * slope + intercept
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy)
ax = axs[1]
sns.regplot(x="datenum", y="xco2", data=flask[::40], ax=ax, ci=99.9)
