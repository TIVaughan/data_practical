''' Data Analyst - Practical Test (Charter)
    COVID-19 Cases and Deaths of the United States and Worldwide

    Data was obtained 6/3/2020 ~7:30 AM MST
'''

#Package Import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as sm
#import os
#os.chdir(r'C:\Users\TIVaw\Documents\Datacamp\Data Analyst - Practical Test (Charter)\Data-Analyst-Practical-Test-Covid--19-')

#Import Data Sets
bing = pd.read_csv('Data/Bing-COVID19-Data.csv')
pop = pd.read_csv('Data/population_by_country_2020.csv')
s_pop = pd.read_csv('Data/state_populations.csv')
pop.rename(columns={pop.columns[0]: 'Country_Region', pop.columns[1]: 'Country_Population'}, inplace = True)
pop2 = pop
pop2.drop(pop2.columns[2:], axis=1, inplace=True)

bing_pop = bing
bing_pop = bing_pop.merge(pop2, on='Country_Region', how = 'left')
bing_pop = bing_pop.merge(s_pop, left_on='AdminRegion1', right_on='State', how = 'left')

world_bing = bing_pop[bing_pop['Country_Region'] == 'Worldwide']
us_bing = bing_pop[bing_pop['Country_Region'] == 'United States']

world_cases = world_bing[['Updated', 'Confirmed']]
world_cases = world_cases.set_index('Updated')
world_cases_gb = world_cases.groupby('Updated').sum()

us_cases = us_bing[['Updated', 'Confirmed']]
us_cases = us_cases.set_index('Updated')
us_cases_gb = us_cases.groupby('Updated').sum()

world_cases_gb['Confirmed'].plot()
plt.xlabel('Date')
plt.ylabel('Millions of Cases')
plt.title('COVID-19 Cases Worldwide')

us_cases_gb['Confirmed'].plot()
plt.xlabel('Date')
plt.ylabel('Millions of Cases')
plt.title('COVID-19 Cases in the US')

world_deaths = world_bing[['Updated', 'Deaths']]
world_deaths = world_deaths.set_index('Updated')
world_deaths_gb = world_deaths.groupby('Updated').sum()

us_deaths = us_bing[['Updated', 'Deaths']]
us_deaths = us_deaths.set_index('Updated')
us_deaths_gb = us_deaths.groupby('Updated').sum()

world_deaths_gb['Deaths'].plot()
plt.xlabel('Date')
plt.ylabel('Deaths')
plt.title('COVID-19 Deaths Worldwide')

us_deaths_gb['Deaths'].plot()
plt.xlabel('Date')
plt.ylabel('Deaths')
plt.title('COVID-19 Deaths in the US')
