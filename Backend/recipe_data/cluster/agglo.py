import csv
import numpy as np
import pandas as pd
import scipy.spatial.distance
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from time import time

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter

from sklearn import manifold, datasets


with open('training.csv', 'rb') as f:
    reader = csv.reader(f)
    train = list(reader)

train = np.array(train)

#model = DBSCAN(eps=0.066, min_samples=50, metric="hamming").fit(train)
n_neighbors = 10
n_components = 2

model = manifold.TSNE(n_components=n_components, init='pca', random_state=0).fit_transform(train)
print (model.labels_)

df = pd.DataFrame(model.labels_)
df.to_csv("DBSCAN_result3.csv")