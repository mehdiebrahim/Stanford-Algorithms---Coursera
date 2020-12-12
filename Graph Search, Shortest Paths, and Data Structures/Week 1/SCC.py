from datetime import datetime 
import pandas as pd
import sys
import os
import random
import copy
from collections import deque,defaultdict


os.chdir('/Users/mehdiebrahim/Desktop/Coding/Stanford Algorithms - Data')
data = pd.read_csv('SCC.txt',sep=' ',header=None)
data.columns = ['a','b','c']
del data['c'] #delete null col
edges = data.values.tolist() #put the data in a list 

def findSCCsizes(problem,V,minnode):


    class Graph:

        def __init__(self,edges):
            self.time = 0
            self.edges = edges
            self.explored = dict()
            self.finish_times_to_v = dict()
            self.v_to_finish_times = dict()
            self.explored2 = dict()
            self.new_graph = defaultdict(list)
            self.graph = defaultdict(list)
            self.revgraph = defaultdict(list)
            self.scc = []
            self.leaders = dict()
            self.source = None


        def RevGraphAdjList(self):
            #create adjacency list of edges with edges reversed in direction i.e. 
            #instead of u being the key and v the value in our dict, it is v being key and u being value
            for u,v in self.edges:
                self.revgraph[v].append(u)
    #         print(self.revgraph,'revgraph')
            return self.revgraph


        def dfs(self,node):
            '''Carry out the first DFS on the reversed graph to obtain finish times. Returns the 
            finish time dictionary, showing key being the node and value the finish time'''

            queue =deque([node])

            if not self.revgraph:
                #create the reversed graph
                self.RevGraphAdjList()

            while len(queue)!=0:
                head = queue.popleft()
                # removes this from queue
                if head not in self.explored:
                    #add this to explored

                    self.explored[head] = -1
                    frontier = self.revgraph[head]
                    queue.appendleft(head)  #we add this back to the top of stack to process finish times so we process the finish times in correct order
                                            # we do this before we push in the neighbouring nodes into the stack so that the neighbouring nodes are processed first so the search completes.
                                            # only at the end we process the finish times so when we see 'head' again, it has finished and we can pop it off again. 
                    for node in frontier:
                        if node not in self.explored:
                            queue.appendleft(node) #adds the frontier nodes to the top of stack            

                else:
                   #we process the finish times
                    if head not in self.finish_times_to_v:
                        self.time+=1
                        self.finish_times_to_v[head]=self.time
                        self.v_to_finish_times[self.time] = head

            return self.finish_times_to_v


        def finish(self):
            '''this method processes finish time for each node. We take value of maximum node'''
            for node in range(V,0,-1):

                if node not in self.explored:
                    self.dfs(node)
            print('finish first loop')
            print(len(self.finish_times_to_v),self.time,'finish time') #chhecks to see length of dictionary is equal to finish time, else the dfs ,method is wrong
    #         print(self.explored)
            return self.finish_times_to_v

        def NewGraph(self):

            '''Construct new graph replacing nodes with their respective finish times and reversing arrows again'''

            finish_times = self.finish()

            for u,v in self.edges:
                u1,v1 = finish_times[u],finish_times[v]
                self.new_graph[u1].append(v1)
    #         print('made new graph')
            return self.new_graph

        def dfs2(self,node):
            '''Second dfs loop to find the SCC components'''

            queue = deque([node])
            
            scc_lengths = []
            curr_length = len(self.explored2)
            lengths = []
            exp = []
            


            while len(queue) != 0:
                head = queue.popleft()

                if head not in self.explored2:
                    frontier = self.new_graph[head]
                    queue_length = len(queue)
                    self.explored2[head] = -1
                    exp.append(self.v_to_finish_times[head])

                    for node in frontier:
                        if node not in self.explored2:
                            queue.appendleft(node)
            self.leaders[self.v_to_finish_times[head]] = exp
            return len(self.explored2)-curr_length #updated explored dictionary once this dfs is completed contains added SCC. So the no. of vertices
                                                    #in this SCC is equal to the length of updated explored dict minus the length of dict prior to dfs

        def finish2(self):
            '''Run the second DFS search to find the SCCs on the new graph with the finish ties'''
            print('finish second loop')

            for node in range(V,0,-1):

                self.source = node 
                if node not in self.explored2:
                    length = self.dfs2(self.source)
                    self.scc.append(length)

            return self.scc

    start = datetime.now()
    g = Graph(problem) #create object graph with edges 
    print('starting')
    g.NewGraph() #construct new graph with the finishing times instead of of vertices. Max node number is 875714, hence we enter this. 
    clusters = sorted(g.finish2())[::-1] #sort the graph in decreasing number 
    print('finishing off')
    end = datetime.now()
    print(abs(end-start),'time taken')
    return clusters[:7]
findSCCsizes(edges,875714,0)