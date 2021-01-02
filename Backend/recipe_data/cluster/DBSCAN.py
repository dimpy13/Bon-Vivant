import csv
import numpy as np
import pandas as pd
import scipy.spatial.distance
import os
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
import matplotlib.pyplot as plt

train = pd.read_csv('D:/recipe_data/cluster/train_data.csv')
train = np.array(train)
print (train)


#model = DBSCAN(eps=0.300, min_samples=10, metric="hamming").fit(train)

#kmeans = KMeans(n_clusters=5, random_state=0, compute_labels=False).fit(train)
#batch_size = np.size(os.listdir(img_path)) * 3
kmeans = MiniBatchKMeans(n_clusters=8, batch_size=1000, verbose=1).fit(train)

print (kmeans.labels)_
#print model.labels_

df = pd.DataFrame(kmeans.labels_)
#df.to_csv("kmean_result2.csv")

plt.plot()
plt.show()
