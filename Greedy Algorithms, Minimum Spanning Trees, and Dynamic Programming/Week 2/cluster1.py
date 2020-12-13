import os
import pandas as pd
import heapq


os.chdir('/Users/mehdiebrahim/Desktop/Stanford Algorithms - Data')
# data = pd.read_csv('greedyjobs.txt',sep=' ',header=None)
# data.columns = ['a','b']
# weight = data['a']
# length = data['b']
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

clusters = [[i] for i in range(1,500+1)]
k=1
# edges = [(1,2,1),(1,3,2),(2,3,2),(2,4,3),(4,3,4),(3,5,10),(5,6,7),(5,8,2),(6,7,3),(7,8,5),(5,7,4)]
# edges = [(1,2,5),(2,3,50),(3,4,6),(3,5,60),(5,6,7)]
edges = sorted(edges,key = lambda x: x[2])
# print(edges[-2])
# edges = [2,3,4,1]
# heap = heapq.heapify(edges)
# print(edges,'edg')
def find_cluster(clusters,point):
    
    for cluster in clusters:
        if point in cluster:
            return cluster

def merge(clusters,cluster1,cluster2):
    
    clusters.remove(cluster1)
    ind = clusters.index(cluster2)
    clusters[ind] = cluster1+cluster2
    
    return clusters
    
            
while len(clusters)>k: 
    
    smallest_edge = edges.pop(0)
    p,q,d = smallest_edge[0], smallest_edge[1],smallest_edge[2]
#     print(p,q,d,'pq')
#     print(smallest_edge)
    cluster1,cluster2 = find_cluster(clusters,p),find_cluster(clusters,q)
    if cluster1==cluster2:
        pass
    else:
#         print(d,len(clusters),'d')
        merge(clusters,cluster1,cluster2)
#         print(len(clusters))
    
#     if len(edges)!=0:
#         pass
#     else: 
#         break
print(len(clusters[0])==len(set(clusters[0])),'cluster length')
#     if len(edges)%1000==0:
#         print(len(edges))
#     if len(clusters)==2:
#         print(edges)
#     print(len(clusters))
    