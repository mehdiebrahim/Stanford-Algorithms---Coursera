
import pandas as pd
import sys
import os
import random
import copy
os.chdir('/Users/mehdiebrahim/Desktop/Coding/Stanford Algorithms - Data')
# data = pd.read_csv('randomised_contractionAlgo.txt',sep='',header=None)
f = 'KragersMinCut.txt'
count = 0        
with open(f, 'r') as infile:
    '''opens file and puts each row into adjMat'''
    adjMat, edges, vertices = [], [], []
    for line in infile.readlines():
        adjMat.append(line)   

def produceVerticesEdges(adjMat):
    '''return list of nodes and edges from adjMat'''
    edges = []
    global count
    vertices = []
    for vertex in adjMat:
        vertex= vertex.split()
        vertices.append(vertex[0])
        count+=len(vertex)
#         print(vertex)
        for i in range(1,len(vertex)):
            edge = (vertex[0],vertex[i])
            if (vertex[i],vertex[0]) not in edges: #this is necessary since its undirected graph in file so we have
                edges.append(edge)
            else:
                pass                             # 1->9 and also 9->1. This is directed representation. So we don't 
                                                #include both in the edges list as this double counts and gives directed graph result
                                                #in essence, if the adjacency list give 1->9, it will also give 9->1 which pertains to the
                                               # same edge. This is why (1,9) and (9,1) can't both be in the list since they are the same edge
                                                #so we get final answer being double what it should be.         
    return edges,vertices

# print(produceVerticesEdges(adjMat))
#lists below give produce a test case

edges2, vertices2 = produceVerticesEdges(adjMat)

def contractEdge(vertices,edges,edge_contr):
    
    '''edge contraction algo
    - takes edge (u1,v1) and collpases the v1 into u1. For another edge (u2,v2), if v2==v1 then
    the new edge is (u2,u1) as v1=>u1 and so v2=>u1. If u2==v1, then v1=>u1 and so u2=>u1 and so new edge
    is (u1,v2).
    - we remove v1 from the vertices and create new list of edges (inefficient, try a better implementation?)
    - we double count edges at the end so the answer has to be divided by two.
    edge_contr is the index of the edge that is randomly picked. '''
    
   
    edge1= edges[edge_contr]
    u1,v1 =edge1
    edges.remove(edge1)
    vertices.remove(v1)
    New_Edge = []
    n = len(edges)
    

    for i in range(n):
    
        edge = edges[i]
        u2,v2 = edge


        if v2==v1:
            edges[i]= (u2,u1)

        elif u2==v1:

            edges[i] = (u1,v2)

        if edges[i][0]!=edges[i][1]:
            New_Edge.append(edges[i])
    
    return vertices, New_Edge


def Kragers(vertices,edges):
    
    while len(vertices)>2:
        #iterate till we have only two vertices left in the list
        
        ind = random.randrange(0, len(edges))
        vertices, edges = contractEdge(vertices,edges,ind) #returns new list of vertices and 
                                                            #edges after contraction
          
    return len(edges)

result = []

    
for i in range(100):
        random.seed(i)
        #seed the random number generator differently each time 
        v = vertices2.copy()
        e = edges2.copy()
        r = Kragers(v, e)
        result.append(r)
        print('result=',min(result))

print(min(result))
