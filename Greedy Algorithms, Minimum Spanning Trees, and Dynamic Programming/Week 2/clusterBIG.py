
import os
from collections import defaultdict

def hamdist2(x):
    x2 = x.split()
    L = []
    for i in range(24):
        for j in range(i+1,24):

            b= x2.copy()

            one_i = 1^int(b[i])
            zero_i = 0^int(b[i])

            one_j = 1^int(b[j])
            zero_j = 0^int(b[j])

            if one_i == 1:
                b[i] = '1'
            else:
                b[i] = '0'

            if one_j == 1:
                b[j] = '1'

            else:
                b[j] = '0'
            L.append(' '.join(b))
    return L

def hamdist1(x):
    x2 = x.split()
    L = []
    for i in range(24):
        
        b= x2.copy()
        one_i = 1^int(b[i])
        zero_i = 0^int(b[i])
        
        if one_i == 1:
            b[i] = '1'
            
        else:
            b[i] = '0'
        L.append(' '.join(b))

    return L

def merged(clusters,cluster):
    
 
    set_of_clusters= []
    merged = set()
    for point in cluster:
        cluster_f = find_cluster(clusters,point)


    #     print(cluster_f)
        if cluster_f:

            if set_of_clusters:

                last = set_of_clusters[-1]
                if cluster_f not in set_of_clusters:
                    set_of_clusters.append(cluster_f)
                merged = cluster_f.union(last,merged)

            else:
                set_of_clusters.append(cluster_f)

        else:
            merged = merged.union(set([point]))
    clusters.append(merged)
    for i in set_of_clusters:
        clusters.remove(i)
    return clusters

def find_cluster(clusters,point):
    
    for cluster in clusters:
        if point in cluster:
            return cluster
        
    return None

os.chdir('/Users/mehdiebrahim/Desktop/Stanford Algorithms - Data')
d = 'cluster2.txt'

with open(d, 'r') as infile:
    '''opens file and puts each row into adjMat'''
    no_of_nodes,no_of_bits,nodes = 0,0,defaultdict(list)
    for line in infile.readlines():
        line = line.split()

        line = ' '.join(line)
        
        if len(line.split())==2:
            no_of_nodes,no_of_bits = int(line[0]),int(line[1])
        else:
            nodes[line].append(line)

list_of_codes = [code for code in nodes]
clusters = []


while list_of_codes:
    code = list_of_codes.pop(0)
    initial = nodes[code]
    neighbours = hamdist1(code) + hamdist2(code)
    
    cluster = set(nodes[code])
    counts = []
    for neighbour in neighbours:
       
        if neighbour in nodes:
            
            cluster.add(neighbour)
    clusters = merged(clusters,cluster)


            
print(len(clusters))           
    
