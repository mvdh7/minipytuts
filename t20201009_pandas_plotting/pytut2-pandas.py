import pandas as pd

# Import GLODAP dataset
data = pd.read_csv('../data/GLODAPv2.2020_Indian_Ocean.csv', na_values=-9999)
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

data['example'] = 3
data['ts'] = data['temperature'] * data['salinity']

#%% Plot something
# data.plot.scatter("tco2", 'talk', s=2, c='xkcd:strawberry', alpha=0.05)
data.plot.scatter("tco2", 'talk', s=2, c='depth', alpha=0.9, cmap='viridis')
# https://xkcd.com/color/rgb/
# https://blog.xkcd.com/2010/05/03/color-survey-results/
# https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html

#%% map
surface = data['depth'] < 20
surface_data = data[surface]
data[surface].plot.scatter('longitude', 'latitude', s=2, c='temperature', cmap='magma')

#%% transect
data.plot.scatter('latitude', 'depth', s=2, c='temperature', cmap='magma')

#%% Import a different dataset
cocco = pd.read_csv('../data/Poulton-etal_2018.tab', sep='\t', skiprows=55)

# Make a renaming dict(ionary)
mapper = {'Coccolith [#/ml]': 'coccolith_count',
          'E. huxleyi [#/ml]': 'ehux_count'}
cocco = cocco.rename(columns=mapper)

# Plot a histogram of a subset of the data
cocco.loc[cocco['PI'] == 'Daniels', 'coccolith_count'].plot.hist()
# ^-- .loc for selecting both specific rows then specific column(s)

# Save a CSV
cocco.to_csv('../data/Poulton_v2.csv')

#%% Read an Excel file
msl = pd.read_excel('../data/csiro_alt_gmsl_yr_2015.xlsx', index_col=0, parse_dates=True)
msl['something_else'] = 100 - msl.GMSL
msl.plot()
