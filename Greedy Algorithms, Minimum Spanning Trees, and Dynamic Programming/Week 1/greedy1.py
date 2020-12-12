import os
import pandas as pd

os.chdir('/Users/mehdiebrahim/Desktop/Coding/Stanford Algorithms - Data')

f = 'greedyjobs.txt'
with open(f, 'r') as infile:
    '''opens file and puts each row into adjMat'''
    diff, ratio, edges = [], [], []
    for line in infile.readlines():
        line = line.split()
        edges.append(line)
        diff.append((int(line[0])-int(line[1]),int(line[0]),int(line[1])))
        ratio.append((int(line[0])/int(line[1]),int(line[0]),int(line[1])))


diff = sorted(diff,key = lambda x:(x[0],x[1]))[::-1]


count = 0
final = 0
for elem in diff:
    count += elem[2]
    final += count*elem[1]
final
