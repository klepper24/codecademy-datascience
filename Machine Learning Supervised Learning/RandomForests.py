def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

income_data = pd.read_csv('income.csv', header = 0, delimiter = ', ')
#print(income_data.iloc[0])
print(income_data['native-country'].value_counts())
income_data['sex_int'] = income_data['sex'].apply(lambda x: 0 if x == 'Male' else 1)
income_data['country_int'] = income_data['native-country'].apply(lambda x: 0 if x == 'United-States' else 1)
labels = income_data['income']
data = income_data[['age', 'capital-gain', 'capital-loss', 'hours-per-week', 'sex_int','country_int']]
train_data,test_data,train_labels,test_labels = train_test_split(data,labels,random_state = 1)
forest = RandomForestClassifier(random_state = 1)
forest.fit(train_data,train_labels)
print(forest.score(test_data,test_labels))
