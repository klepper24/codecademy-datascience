import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import codecademylib3_seaborn
import glob

df = glob.glob('states*.csv')
df_list = []
for i in df:
  d = pd.read_csv(i)
  df_list.append(d)
  
us_census = pd.concat(df_list)
#print(us_census.columns)
#print(us_census.dtypes)
#print(us_census.head())
us_census['Income'] = us_census['Income'].str.replace('\$','',regex=True) 
print(us_census.head())
gender = us_census['GenderPop'].str.split('_',expand=True)
us_census['Men'] = pd.to_numeric(gender[0].str.replace('M','', regex=True))
us_census['Women'] = pd.to_numeric(gender[1].str.replace('F','', regex=True))
pyplot.scatter(us_census['Women'],us_census['Income']) 
pyplot.show()
us_census=us_census.fillna(value={'Women':us_census['TotalPop']-us_census['Men']})
print(us_census.head())
us_census = us_census.drop_duplicates()
pyplot.scatter(us_census['Women'],us_census['Income']) 
pyplot.show()
print(us_census.columns)