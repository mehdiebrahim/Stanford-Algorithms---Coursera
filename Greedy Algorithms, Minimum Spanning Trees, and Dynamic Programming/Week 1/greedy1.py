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
ratio =  sorted(ratio,key = lambda x:(x[0],x[1]))[::-1]

count_diff = 0
final_diff = 0
for elem in diff:
    count_diff += elem[2]
    final_diff += count_diff*elem[1]


count_ratio = 0
final_ratio = 0
for elem in ratio:
    count_ratio += elem[2]
    final_ratio += count_ratio*elem[1]

print('Answer to 1:',str(final_diff))
print('Answer to 2:',str(final_ratio))