import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

digits = datasets.load_digits()
print(digits.target[100])
# Figure size (width, height)

#fig = plt.figure(figsize=(6, 6))
# Adjust the subplots 

#fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# For each of the 64 images

#for i in range(64):

    # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position

   # ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])

    # Display an image at the i-th position

  #  ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')

    # Label the image with the target value

 #   ax.text(0, 7, str(digits.target[i]))

#plt.show()

model = KMeans(n_clusters = 10, random_state = 42)
model.fit(digits.data)
fig = plt.figure(figsize=(8, 3))
fig.suptitle('Cluster Center Images', fontsize = 14, fontweight = 'bold')

for i in range(10):

  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)

  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
  
plt.show()