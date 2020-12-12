import os
from datetime import datetime
from heapq import heapify,heappush,heappop
from collections import defaultdict
os.chdir('/Users/mehdiebrahim/Desktop/Coding/Stanford Algorithms - Data')
# data = pd.read_csv('randomised_contractionAlgo.txt',sep='',header=None)
f = 'Dijkstra.txt'


s = datetime.now()

with open(f, 'r') as infile:
    '''opens file and puts each row into adjMat'''
    adjMat, edges, vertices = defaultdict(list), [], []
    for line in infile.readlines():
        line = line.split()
        l = []
        for elem_index in range(1,len(line)):
            l.append(tuple(line[elem_index].split(',')))
            edges.append([line[0]]+line[elem_index].split(','))
            list_form = line[elem_index].split(',')
            adjMat[int(line[0])].append([int(list_form[1]),int(list_form[0])])
                    

def greedy_criterion_helper(vertices_explored,distance,u,adjMatu):

    while len(adjMatu)!=0:
        
        d,v =  heappop(adjMatu)
        
        if v not in vertices_explored: 
            return [distance[u]+d,u,v]
        
        else:
            None
        
def dijkstra(start_node,end_node,edges,no_vertices):
    
    vertices_explored = [start_node]
    distance = dict()
    distance[start_node] = 0
    finished = dict()
    
    while len(vertices_explored) != no_vertices:

        greedy_criterion = []
        heapify(greedy_criterion)
        
        for u in vertices_explored:
            adj = edges[u].copy()
            heapify(adj)
            g = greedy_criterion_helper(vertices_explored,distance,u,adj)
            
            if g:
                heappush(greedy_criterion,g)
                
        if greedy_criterion:
            
            d,curr_node,next_node = heappop(greedy_criterion)
            vertices_explored.append(next_node)
            distance[next_node] = d

            if next_node==end_node:
                finished[curr_node] = d
                
    return finished

scores = [7,37,59,82,99,115,133,165,188,197]
length = []
for score in scores:
    length.append(dijkstra(1,score,adjMat,200))
f = datetime.now()
print(f-s,'time')
print(length)

