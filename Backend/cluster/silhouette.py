import csv
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from datetime import datetime
startTime = datetime.now()

X = pd.read_csv('D:/Projects/RecipeRecommendation1/cluster/training_data.csv')

X = StandardScaler().fit_transform(X)

dbscan = DBSCAN(eps=0.046, min_samples=50, metric="hamming")

model = dbscan.fit(X)

labels= model.labels_

core_samples = np.zeros_like(labels, dtype=bool)
core_samples[dbscan.core_sample_indices_] = True
print(core_samples)

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print (n_clusters_)

print ("Silhouette Coefficiemt : %0.3f" % metrics.silhouette_score(X, labels))

df = pd.DataFrame(model.labels_)
df.to_csv("silhouetteDBSCAN046.csv")
print(datetime.now() - startTime)