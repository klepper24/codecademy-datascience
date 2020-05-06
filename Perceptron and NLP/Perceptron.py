import codecademylib3_seaborn
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

data = [[0,0],[1,1],[1,0],[0,1]]
labels= [0,1,0,0]
#plt.scatter([point[0] for point in data],[point[1] for point in data], c = labels)
#plt.show()
x_values = np.linspace(0,1,100)
y_values = np.linspace(0,1,100)
point_grid = list(product(x_values,y_values))
classifier = Perceptron(max_iter = 40)
classifier.fit(data,labels)
print(classifier.score(data, labels))
distances = classifier.decision_function(point_grid)
abs_distances = [abs(d) for d in distances]
distances_matrix = np.reshape(abs_distances,(100,100))
heatmap = plt.pcolormesh(x_values,y_values,distances_matrix)
plt.colorbar(heatmap)
plt.show()