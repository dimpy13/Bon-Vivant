import csv
import numpy as np
import pandas as pd
import scipy.spatial.distance

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import numpy as np
import pylab as pl
from sklearn import neighbors, datasets

train = pd.read_csv('D:/recipe_data/cluster/train_data.csv', nrows=1000)
X = np.array(train)

knn=neighbors.KNeighborsClassifier()
knn.fit(X)

h = 0.2

x_min, x_max = X[:,0].min() - .5, X[:,0].max() + .5

xx = np.meshgrid(np.arange(x_min, x_max, h))
Z = knn.predict(np.c_[xx.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
pl.figure(1, figsize=(4, 3))
pl.set_cmap(pl.cm.Paired)
pl.pcolormesh(xx, Z)

# Plot also the training points
pl.scatter(X)
pl.xlabel('Sepal length')
pl.ylabel('Sepal width')

pl.xlim(xx.min(), xx.max())

pl.xticks(())


pl.show()