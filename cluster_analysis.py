# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 15:51:44 2018

@author: alexy
"""

import pandas as pd
import numpy as np
import statistics as st
import sklearn.cluster as sklc
import sklearn.metrics as sklm
import scipy.cluster.hierarchy as spch
import matplotlib.pyplot as plt
import sklearn.metrics as sklm


df = pd.read_csv('tremor_data.csv')

for col in [1,2,3]:
    sd = []
    for x in df.iloc[:,col]:
        z = (x-st.mean(df.iloc[:,col])/np.std(df.iloc[:,col]))
        sd.append(z)
    df[str(col)] = pd.Series(sd)
df.rename(columns={'1':'sd_time','2':'sd_dist','3':'sd_size'},inplace=True)
df.to_csv('new_tremor_data.csv')

cluster_data = df.iloc[:,3:6]

# Perform a k-means clustering on the tremors data for k (number of clusters) ranging from 1 to 20.
silhouette_score_kmeans = []
sse_kmeans = []
for i in range(2,21): 
    # Note that you can choose the number of clusters (n_clusters) and the number of repetitions of the algorithm (n_init).
    # The output (stored to kmeans_output here) is a special object which contains all the information about the clustering.
    kmeans_output = sklc.KMeans(n_clusters = i, n_init = 1).fit(cluster_data)

    # A list giving the final cluster number of each point:
    clustering_ids_kmeans = kmeans_output.labels_
    
    # The SSE of the clustering and store it
    clustering_sse = kmeans_output.inertia_
    sse_kmeans.append(clustering_sse)
    
    # A list of the centroids, ordered by cluster number:
    clustering_centroids  = kmeans_output.cluster_centers_
    
    # calculate the silhouette score of this clustering and store it
    silhouette_kmeans = sklm.silhouette_score(cluster_data,clustering_ids_kmeans)
    silhouette_score_kmeans.append(silhouette_kmeans)

opt = silhouette_score_kmeans.index(max(silhouette_score_kmeans))
kmeans_output = sklc.KMeans(n_clusters = opt+2, n_init = 1).fit(cluster_data)

# add clustering ids of each point to the dataframe
df['clustering_id'] = pd.Series(kmeans_output.labels_)

# create a dataframe of the results
kmeans_results = pd.DataFrame()
kmeans_results['cluster_number'] = range(2,21)
kmeans_results['silhouette_score'] = silhouette_score_kmeans
kmeans_results['sse'] = sse_kmeans
kmeans_results = kmeans_results.set_index('cluster_number')


# perform hierarchical agglomerative clustering
silhouette_score_hierag = []
radii = []
for r in range(1200,3600,100):
    radii.append(r)
    clustering_ids_hierag = spch.fclusterdata(cluster_data, r, criterion='distance', method='single')
    silhouette_hierag = sklm.silhouette_score(cluster_data,clustering_ids_hierag)
    silhouette_score_hierag.append(silhouette_hierag)
opt_index = silhouette_score_hierag.index(max(silhouette_score_hierag))
clustering_ids_hierag = spch.fclusterdata(cluster_data, radii[opt_index], criterion='distance', method='single')

# add clustering ids of each point to the dataframe
df['clustering_id_hierag'] = pd.Series(clustering_ids_hierag)

# plot a dendrogram and save as a 
# =============================================================================
# Z = spch.linkage(cluster_data, method='single', metric='euclidean')
# plt.figure(figsize=(20,30))
# spch.dendrogram(Z,orientation='right')
# plt.show()
# plt.savefig('my_dendrogram.png')
# =============================================================================


# print a dataframe of stat sum of each of the clusters generated from kmeans clustering
for i in range(5):
    cluster = df.loc[df['clustering_id'] == i]
    mean = [cluster.iloc[:,col].mean() for col in [0,1,2]]
    stdev = [cluster.iloc[:,col].std() for col in [0,1,2]]
    minimum = [cluster.iloc[:,col].min() for col in [0,1,2]]
    maximum = [cluster.iloc[:,col].max() for col in [0,1,2]]
    df_k_c = pd.DataFrame({'mean':mean,'stdev':stdev,'min':minimum,'max':maximum},index=['time','dist','size'])
    print(df_k_c)

# print a dataframe of stat sum of each of the clusters generated from hierag clustering
for i in range(1,8):
    cluster = df.loc[df['clustering_id_hierag'] == i]
    mean = [cluster.iloc[:,col].mean() for col in [0,1,2]]
    stdev = [cluster.iloc[:,col].std() for col in [0,1,2]]
    minimum = [cluster.iloc[:,col].min() for col in [0,1,2]]
    maximum = [cluster.iloc[:,col].max() for col in [0,1,2]]
    df_h_c = pd.DataFrame({'mean':mean,'stdev':stdev,'min':minimum,'max':maximum},index=['time','dist','size'])
    print(df_h_c)



