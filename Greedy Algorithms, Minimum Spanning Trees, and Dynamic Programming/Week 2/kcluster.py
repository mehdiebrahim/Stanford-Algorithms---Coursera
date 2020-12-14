import os
import pandas as pd
import heapq


os.chdir('/Users/mehdiebrahim/Desktop/Coding/Stanford Algorithms - Data')

f = 'cluster1.txt'
with open(f, 'r') as infile:
    '''opens file and puts each row into adjMat'''
    edges,V = [],0
    for line in infile.readlines():
        line = line.split()
        
        if len(line)==1:
            V = int(line[0])
        else:
            edges.append((int(line[0]),int(line[1]),int(line[2])))

clusters = [[i] for i in range(1,V+1)]
edges = sorted(edges,key = lambda x: x[2])

def find_cluster(clusters,point):
    
    for cluster in clusters:
        if point in cluster:
            return cluster

def merge(clusters,cluster1,cluster2):
    
    clusters.remove(cluster1)
    ind = clusters.index(cluster2)
    clusters[ind] = cluster1+cluster2
    
    return clusters
    
no_clusters_at_end = 2    

def k_cluster(edges,clusters,no_clusters):
    k = 1
    while len(clusters)>k: 
        
        smallest_edge = edges.pop(0)
        p,q,d = smallest_edge[0], smallest_edge[1],smallest_edge[2]
        
        cluster1,cluster2 = find_cluster(clusters,p),find_cluster(clusters,q)
        if cluster1==cluster2:
            pass
        else:
            
            merge(clusters,cluster1,cluster2)
            if len(clusters)<no_clusters:

                return d
                

print(k_cluster(edges,clusters,no_clusters_at_end))