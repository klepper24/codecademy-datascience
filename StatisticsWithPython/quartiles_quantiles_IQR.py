import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
quart = [0.25,0.5,0.75]
data = pd.read_csv("country_data.csv")
print(data.head())
life_expectancy = data['Life Expectancy']
life_expectancy_quartiles = np.quantile(life_expectancy,[0.25,0.5,0.75])
print(life_expectancy_quartiles)

gdp = data['GDP']
median_gdp = np.quantile(gdp,0.5)
print(median_gdp)
low_gdp = data[data['GDP'] <= median_gdp]
high_gdp = data[data['GDP'] >= median_gdp]
low_gdp_quartiles = np.quantile(low_gdp['Life Expectancy'],quart)
print(low_gdp_quartiles)
high_gdp_quartiles = np.quantile(high_gdp['Life Expectancy'],quart)
print(high_gdp_quartiles)

plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()