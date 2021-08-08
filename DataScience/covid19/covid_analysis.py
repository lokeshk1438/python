# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import matplotlib.pyplot as plt


# %%
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)


# %%
confirmed = pd.read_csv(r'covid19_confirmed_global.csv')
deaths = pd.read_csv(r'covid19_deaths_global.csv')
recorvered = pd.read_csv(r'covid19_recovered_global.csv')


# %%
# dropping the selected columns

confirmed = confirmed.drop(['Province','Lat','Long'], axis=1)
deaths = deaths.drop(['Province','Lat','Long'], axis=1)
recorvered = recorvered.drop(['Province','Lat','Long'], axis=1)


# %%
confirmed.isnull().sum()


# %%
len(confirmed['Country'].unique())


# %%
confirmed = confirmed.groupby(confirmed['Country']).aggregate('sum')
deaths = deaths.groupby(deaths['Country']).aggregate('sum')
recorvered = recorvered.groupby(recorvered['Country']).aggregate('sum')


# %%
confirmed = confirmed.T
deaths = deaths.T
recorvered = recorvered.T


# %%
new_cases = confirmed.copy()

print(new_cases)
'''
# %%
# calculating daily cases
for day in range(1,len(confirmed)):
    new_cases.iloc[day] = confirmed.iloc[day] - confirmed.iloc[day - 1]


# %%
growth_rate = confirmed.copy()


# %%
# calculating the growth rate
for day in range(1,len(confirmed)):
    growth_rate.iloc[day] = (new_cases.iloc[day] / confirmed.iloc[day-1]) * 100


# %%
active_cases = confirmed.copy()


# %%
for day in range(0, len(confirmed)):
    active_cases.iloc[day] = confirmed.iloc[day] - deaths.iloc[day] - recorvered.iloc[day]


# %%
actual_growth_rate = confirmed.copy()


# %%
for day in range(1,len(confirmed)):
    actual_growth_rate.iloc[day] = ((active_cases.iloc[day] - active_cases.iloc[day - 1]) / active_cases.iloc[day - 1]) * 100


# %%
actual_growth_rate['US'].tail(10)


# %%
death_rate = confirmed.copy()


# %%
# death_rate calculation
for day in range(0, len(confirmed)):
    death_rate.iloc[day] = (deaths.iloc[day] / confirmed.iloc[day]) * 100


# %%
hospitalisation_rate = 0.05


# %%
hospitalisation_needed = confirmed.copy()


# %%
for day in range(0, len(confirmed)):
    hospitalisation_needed.iloc[day] = active_cases.iloc[day] * hospitalisation_rate


# %%
# visualisation

countries = ['Italy', 'Austria', 'US', 'China', 'India', 'France', 'Spain']


# %%
for country in countries:
    confirmed[country].plot(label=country)
plt.legend(loc='upper left')
plt.show()


# %%
'''