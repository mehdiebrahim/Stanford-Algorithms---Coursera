
import os
from collections import defaultdict
from heapq import heapify,heappop,heappush
import numpy as np
os.chdir('/Users/mehdiebrahim/Desktop/Stanford Algorithms - Data')
d = 'g3.txt'


with open(d, 'r') as infile:
    '''opens file and puts each row into adjMat'''
    
    V,E,V_weights,edges_without_zero,edges_with_zero = 0,0,[],[],[]
    count = 1
    for line in infile.readlines():
        line = line.split()
        if len(line)==2:
            V = int(line[0])
            E = int(line[1])
            V_weights = [[i,0] for i in range(V+1)]
            edges2 = [[0,i,0] for i in range(1,V+1)]
            
        else:

            edges_without_zero.append([int(line[0]),int(line[1]),int(line[2])])
            edges2.append([int(line[0]),int(line[1]),int(line[2])])


def BellmanFord(start,v_pv,edges):
    A = [1e3000]*(len(v_pv))
    A[0] = 0

    for i in range(1,len(v_pv)):

        for w,v,c in edges :
            case1 = A[v]
            case2 = A[w]+c
            A[v] = min(case1,case2)
       
    for w,v,c in edges:
        if A[w]!=1e3000:
            if A[w]+c < A[v]:
                print('We hhave negative costs')
                break
                return

    return A

def newG(vertices,edges_withzero,edges2_original):
    v_pv = defaultdict(int)
    for v in range(vertices):
        v_pv[v] = 0
        
    out = BellmanFord(0,v_pv,edges_withzero)
    print(min(out),'FINAL ANSWER')
    for elem in range(len(out)):
        v_pv[elem] = out[elem]

    for ind in range(len(edges2_original)):
        
        edge = edges2_original[ind]
        v,w,c = edge
        pv,pw = v_pv[v],v_pv[w]
        edges2_original[ind] = v,w,c+pv-pw

    return edges2_original,v_pv

adjlist = defaultdict(list)
newGraph,v_pv = newG(V+1,edges2,edges_without_zero)

for elem in newGraph:
    adjlist[elem[0]].append((elem[2],elem[1]))
print('done')