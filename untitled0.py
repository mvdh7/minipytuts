import pandas as pd

# Import data
df = pd.read_csv('data/GLODAPv2.2020_Indian_Ocean.csv', na_values=-9999)

#%% Draw the plot
df.plot.scatter('tco2', 'talk', s=2, c='depth', alpha=0.8, cmap='viridis_r')





#%%
# df[df['depth'] < 20].plot.scatter('latitude', 'depth', s=2, c='temperature', cmap='magma')
surface = df['depth'] < 20
mesopelagic = (df['depth'] > 800) & (df['depth'] < 1000)
s27 = (df['sigma0'] > 26.95) & (df['sigma0'] < 27.05)
df[s27].plot.scatter(
    'longitude', 'latitude', s=2, c='nitrate', cmap='magma')

#%%
df2 = pd.read_csv('data/Poulton-etal_2018.tab', sep='\t', skiprows=55)
df2.loc[df2['PI'] == 'Daniels', ['Coccolith [#/ml]', 'E. huxleyi [#/ml]']].hist()

#%%
df3 = pd.read_excel('data/csiro_alt_gmsl_yr_2015.xlsx', index_col=0, parse_dates=True)
df3['other thing'] = 100 - df3['GMSL']
df3.plot()
