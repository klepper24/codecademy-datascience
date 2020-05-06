import codecademylib3_seaborn
import pandas as pd
import numpy as np
import pickle

london_data = pickle.load( open( "weather.p", "rb" ) )

temp = london_data['TemperatureC']
average_temp = np.average(temp)
print('Mean: '+str(average_temp))
temperature_var = np.var(temp)
print('Var: '+str(temperature_var))
temperature_standard_deviation = np.std(temp)
print('Std: '+str(temperature_standard_deviation))
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
july = london_data.loc[london_data['month'] == 7]["TemperatureC"]
print('Mean in june: '+str(np.average(june)))
print('Mean in july: '+str(np.average(july)))
print('Std in june: '+str(np.std(june)))
print('Std in july: '+str(np.std(july)))

for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")