import os
from collections import defaultdict
from heapq import heapify,heappop,heappush
import numpy as np
os.chdir('/Users/mehdiebrahim/Desktop/Coding/Stanford Algorithms - Data')
d = 'knapsack.txt'

with open(d, 'r') as infile:
    '''opens file and puts each row into adjMat'''
    no_of_nodes,value_weight = '1000',[[0,0]]
    count = 1
    for line in infile.readlines():
        line = line.split()
        if line ==['10000','100']:
            pass
            
        else:
            value_weight.append([int(line[0]),int(line[1])])

A =[[0]*10001 for i in range(101)]

for i in range(1,101):
    for x in range(10001):
        
        vi,wi = value_weight[i]
        if wi>x:
            A[i][x] = A[i-1][x]
            
        else:
            A[i][x] = max(A[i-1][x],A[i-1][x-wi]+vi)
print(A[-1][-1])