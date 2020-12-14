import os
import pandas as pd
import numpy.random as nr

os.chdir('/Users/mehdiebrahim/Desktop/Coding/Stanford Algorithms - Data')
f = 'edgesMST.txt'

with open(f, 'r') as infile:
    '''opens file and puts each row into adjMat'''
    V,E, edges_and_cost = 0, 0, []
    for line in infile.readlines():
        line = line.split()
        
        if len(line)==2:

            V = int(line[0])
            E = int(line[1])
        else:
            if (line[1],line[0],line[2]) not in edges_and_cost:
                edges_and_cost.append((int(line[0]),int(line[1]),int(line[2])))
                edges_and_cost.append((int(line[1]),int(line[0]),int(line[2])))
                   
X = [nr.randint(1,V+1)]
T = []

while len(X)<V:

    uv = []
    for u in X:
        for edge in edges_and_cost:
            if edge[0]==u and edge[1] not in X:
                uv.append(edge)

    min_val = min(uv, key= lambda x: x[2])
    T.append(min_val[2])
    X.append(min_val[1])

print(sum(T))