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

l = [(10,2),(10,1),(10,3),(20,3),(40,5),(100,2)]
print(sorted(l,key= lambda x: (x[0],x[1])))
diff = sorted(diff,key = lambda x:(x[0],x[1]))[::-1]
ratio =  sorted(ratio,key = lambda x:(x[0],x[1]))[::-1]

count = 0
final = 0
for elem in diff:
    count += elem[2]
    final += count*elem[1]

print(final)
count = 0
final = 0
for elem in ratio:
    count += elem[2]
    final += count*elem[1]

print(final)