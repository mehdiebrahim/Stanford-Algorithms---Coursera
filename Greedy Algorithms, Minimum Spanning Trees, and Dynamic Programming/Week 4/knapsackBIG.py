import os
from collections import defaultdict
from heapq import heapify,heappop,heappush
import numpy as np
os.chdir('/Users/mehdiebrahim/Desktop/Stanford Algorithms - Data')
d = 'knapsack_big.txt'


with open(d, 'r') as infile:
    '''opens file and puts each row into adjMat'''
    N,W,value_weight,weight,val = 0,0,[[0,0]],[],[]
    count = 1
    for line in infile.readlines():
        line = line.split()
        if line ==['2000000','2000']:
            W= int(line[0])
            N = int(line[1])
            pass
            
        else:
            value_weight.append([int(line[0]),int(line[1])])
            weight.append(int(line[1]))
            val.append(int(line[0]))
            
t = [[-1 for i in range(W + 1)] for j in range(N + 1)] 
   
def knapsack(wt, val, W, n):     
  
    # base conditions
#     print(n,'n')
    if n == 0 or W == 0: 
        return 0
    if t[n][W] != -1: 
        return t[n][W] 
  
    # choice diagram code 
    if wt[n-1] > W :
        t[n][W] = knapsack(wt,val,W,n-1)
       
    elif wt[n-1] <= W:
        t[n][W] = max(knapsack(wt,val,W,n-1),knapsack(wt,val,W-wt[n-1],n-1)+val[n-1])
    
    return t[n][W]  
        
knapsack(weight,val,W,N)