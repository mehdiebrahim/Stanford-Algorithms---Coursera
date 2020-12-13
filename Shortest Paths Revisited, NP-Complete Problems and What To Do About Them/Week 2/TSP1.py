import os
from collections import defaultdict
import matplotlib.pyplot as plt
from heapq import heapify,heappop,heappush
import numpy as np
from itertools import combinations
os.chdir('/Users/mehdiebrahim/Desktop/Stanford Algorithms - Data')
d = 'tsp.txt'


with open(d, 'r') as infile:
    
    V,points = 0,[]
    
    for line in infile.readlines():
        line = line.split()
        
        if len(line)==1:
            V = int(line[0])
        
        else:
            points.append((float(line[0]),float(line[1])))

points2 = points[:13]
points3 = points[11:]

#we split the graph. Investigate left half and right half. Find it for left half and add to right half subtract common edge
# edge. So edge (12,13) is common edge

def d_mat(V,points):
    '''Produces matrix d, with A[i][j] meaning distance from (i+1) to (j+1) vertex'''
    d = np.zeros((V,V))

    for point_ind in range(V):
        for point_ind2 in range(V):
            point1 = points[point_ind]
            point2 = points[point_ind2]
            d[point_ind][point_ind2] = distance_xy(point1,point2)
    return d
            
def subsets(m,k,s):
    '''Produces subset with start vertex 1. Return vertices with 1 in them '''
    
    l = list(combinations(list(range(1,m+1)),k))
    out = []
    for elem in range(len(l)):

        if s not in l[elem]:
            pass
        else:
            out.append(l[elem])


    return out

def find_min(A,d,subset,j):
    '''This allows us to update the dict A, with new vals for A[s,j], LEARN THIS BETTER'''
    l = list(subset)
    l.remove(j)
    #the minimum we calculated by iterating over k. but k!=j so its removed
    if len(l)>1:
        min_list = min([(A[(tuple(l),k)] + d[k-1][j-1]) for k in l])
    else:
        #we now populate the array A with new vals whereby A[s,j] and j is not just one. this allows us to recurse for all j for all s and thus all paths. 
        min_list = A[(1,1)]+d[0][j-1] 
    return min_list
            
def distance_xy(X,Y):
    
    x1,y1 = X
    x2,y2 = Y
    d = np.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    return d
    
def find_min_final(A,d,V):
    
    '''Gives final answer ((1,2,3,4,.....,25),j) where j is index and the
    (1,2,3,4,.....,25) is a subset, including all the vertices LEARN THIS BETTER'''
    
    f = [A[(tuple(range(1,V+1)),j)]+d[j-1][0] for j in range(2,V+1)]
    return min(f)

def create_paths(V,initial,points):
    '''Initialise with all subsets S, A[S,1]=1 is S=[1] else equal to inf'''
    A = dict()
    d = d_mat(V,points)
    # d gives the matrix of distances from i to j
  
    for m in range(1,V+1):
        #iterate over all subset sizes of 1 to V. when we reach V, subset is now a full set of all vertices from the start vertex being 1
        S = subsets(V,m,1)

        for subset in S:
            if len(subset)==1:
                A[(subset[0],initial)] = 0
            else:
                A[tuple(subset),1] = 1e300
    return A,d

         
def tsp(V,initial,points):
    '''Runs the algo LEARN THIS BETTER'''
    A,d = create_paths(V,initial,points)
    for m in range(2,V+1):

        S = subsets(V,m,1)
        #iterates over all the subets with 1 as starting point and below loops carry out recursion

        for s in S:
            for j in s:
                if j!=1:
                    #exclude 1, its the start vertex
                    A[(s,j)] = find_min(A,d,s,j)
    return find_min_final(A,d,V)


C = distance_xy(points[11],points[12])
A = tsp(13,1,points2)
B = tsp(14,1,points3)
print(A+B-2*C)