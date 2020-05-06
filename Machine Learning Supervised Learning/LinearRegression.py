import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")

print(df.head())

prod_per_year = df.groupby('year').totalprod.mean().reset_index()
x = prod_per_year['year']
x = x.values.reshape(-1,1)
y = prod_per_year['totalprod']
plt.scatter(x,y)

regr = linear_model.LinearRegression()
regr.fit(x,y)
print(regr.coef_[0])
print(regr.intercept_)
y_predict = regr.predict(x)
plt.plot(x,y_predict)
x_future = np.array(range(2013,2051))
x_future = x_future.reshape(-1,1)
future_predict = regr.predict(x_future)
plt.plot(x_future,future_predict)
plt.show()