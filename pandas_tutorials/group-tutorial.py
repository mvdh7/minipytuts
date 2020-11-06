import pandas as pd, numpy as np
from matplotlib import pyplot as plt
from scipy import stats

# Import data
data = pd.read_csv("data/MgCa_data_field.csv")

# Rename columns to make them easier to work with
data.rename(columns={"Del-CO32-": "del_CO3", "T": "temperature"},
            inplace=True)

# Make linear regression function
def get_linear_regression(data, x_var="temperature", y_var="MgCa"):
    """Get linear regression."""
    l = ~np.isnan(data[x_var]) & ~np.isnan(data[y_var])
    if sum(l) > 1:
        slope, intercept, r, p, se = stats.linregress(
            data[l][x_var].values,
            data[l][y_var].values
        )
        
        # data.temperature  # yes
        # data["temperature"]  # yes
        # data[x_var]  # yes
        # data.x_var  # no
        # data["x_var"]  # no
        
    else:
        slope = np.nan
        intercept = np.nan
        r = np.nan
        p = np.nan
        se = np.nan
    mean_temperature = np.nanmean(data.temperature)
    
    # Make a plot
    fig, ax = plt.subplots(dpi=300)
    ax.scatter(x_var, y_var, data=data)

    return pd.Series({
        "slope": slope,
        "intercept": intercept,
        "r": r,
        "p": p,
        "se": se,
        "mean_temperature": mean_temperature,
    })

# Apply the linear regression function
results = get_linear_regression(data)

# Apply to groups by genus
grouped_genus = data.groupby(by="Genus", axis=0).apply(get_linear_regression)

# Get data for each group
cib_slope = grouped_genus.loc["Cibicides"].slope

# Group by genus AND species
grouped_gs = data.groupby(by=["Genus", "species"], axis=0).apply(
    get_linear_regression)

# Access multi-index data from above
cib_slope_gs = grouped_gs.loc["Cibicides", "mundulus"].slope
