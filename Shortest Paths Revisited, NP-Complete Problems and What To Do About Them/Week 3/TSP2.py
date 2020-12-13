import os
from collections import defaultdict
import matplotlib.pyplot as plt
from heapq import heapify,heappop,heappush
import numpy as np
from itertools import combinations
os.chdir('/Users/mehdiebrahim/Desktop/Coding/Stanford Algorithms - Data')
d = 'nn.txt'

with open(d, 'r') as infile:
    
    V,points = 0,[]
    count = 0
    for line in infile.readlines():
        line = line.split()
        
        if len(line)==1:
            V = int(line[0])
        
        else:
            points.append((float(line[1]),float(line[2])))
            count+=1


def euclidean_sq(X,Y):
    x1,y1 = X
    x2,y2 = Y
    
    dsq = (x1-x2)**2 + (y1-y2)**2
    return dsq

def iterate_points(point,points,S):
    
    distances_sq = [(euclidean_sq(points[point],points[p]),p) for p in range(len(points)) if p!=point]
    heapify(distances_sq)

    while distances_sq:
        d,p = heappop(distances_sq)
        if p not in S:
            break
            
    return d,p
    
S = {0}
point = 0
cost = 0
while len(S)!=len(points):
    
    d,p = iterate_points(point,points,S)
    S.add(p)
    d1 = euclidean_sq(points[0],points[p])
    cost += np.sqrt(d)
    point = p


print(cost+np.sqrt(euclidean_sq(points[point],points[0]))) 