import warnings

import pandas as pd
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings('ignore')

# Part 1
print(f"\n{'_' * 20}Part 1{'_' * 20}")
# create dataframe
df = pd.read_csv(r"CC GENERAL.csv")
# import scaler for later
scaler = StandardScaler()
# grab x and y vals
X = df.iloc[:, 1:12]
y = df.iloc[:, 0]

# scale values for part 3
X_Scale = scaler.fit_transform(X)
# create and fit to pca
pca2 = PCA(n_components=2)
principalComponents = pca2.fit_transform(X)

# add to dataframe to view
principalDf = pd.DataFrame(data=principalComponents, columns=['component 1', 'component 2'])

finalDf = pd.concat([principalDf, df[['CUST_ID']]], axis=1)
print(finalDf.head())

# PART 2
print(f"\n{'_' * 20}Part 2{'_' * 20}")
nclusters = 3  # this is the k in kmeans
# 3 clusters
km = KMeans(n_clusters=nclusters)
# fit the data
km.fit(principalDf)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(principalDf)
# score it and print
score = metrics.silhouette_score(principalDf, y_cluster_kmeans)
print(score)

# PART 3
print(f"\n{'_' * 20}Part 3{'_' * 20}")
# use the scaling with the PCA for k-means
pca = PCA(n_components=2)
principalComponents2 = pca.fit_transform(X_Scale)
km2 = KMeans(n_clusters=nclusters)
km2.fit(principalComponents2)
y_cluster_kmeans2 = km2.predict(principalComponents2)

score = metrics.silhouette_score(principalComponents2, y_cluster_kmeans2)
print(score)
