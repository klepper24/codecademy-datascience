import codecademylib3_seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the passenger data
passengers = pd.read_csv('passengers.csv')

# Update sex column to numerical
passengers['Sex'] = np.where(passengers['Sex'] == 'female', 1,0)

# Fill the nan values in the age column
passengers['Age'].fillna(value=passengers['Age'].mean(),inplace=True)
print(passengers['Age'].values)

# Create a first class column
passengers['FirstClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 1 else 0)
print(passengers.head(10))

# Create a second class column
passengers['SecondClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 2 else 0)

# Select the desired features
features = passengers[['Sex','Age','FirstClass','SecondClass']]
survival = passengers['Survived']

# Perform train, test, split
train_f, test_f, train_lab, test_lab = train_test_split(features,survival,test_size=0.8)

# Scale the feature data so it has mean = 0 and standard deviation = 1
scaler = StandardScaler()
train_f = scaler.fit_transform(train_f)
test_f = scaler.fit_transform(test_f)
# Create and train the model
reg = LogisticRegression()
reg.fit(train_f,train_lab)

# Score the model on the train data
print(reg.score(train_f,train_lab))

# Score the model on the test data
print(reg.score(test_f,test_lab))

# Analyze the coefficients
print(reg.coef_)
print(list(zip(['Sex','Age','FirstClass','SecondClass'], reg.coef_[0])))

# Sample passenger features
Jack = np.array([0.0,20.0,0.0,0.0])
Rose = np.array([1.0,17.0,1.0,0.0])
You = np.array([0.0,27,1.0,0.0])

# Combine passenger arrays
sample_passengers = np.array([Jack,Rose,You])

# Scale the sample passenger features
sample_passengers = scaler.transform(sample_passengers)
print(sample_passengers)

# Make survival predictions!
print(reg.predict(sample_passengers))
print(reg.predict_proba(sample_passengers))

