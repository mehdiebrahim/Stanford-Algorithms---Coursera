
import pandas as pd
import os
from collections import defaultdict

os.chdir('/Users/mehdiebrahim/Desktop/Coding/Stanford Algorithms - Data')
data = pd.read_csv('twoSum.txt',sep=' ',header=None)
data.columns = ['a']
nums = data['a']
num_dist = set(nums)


def two_sum(d,t):
    for key in d:
        if t-key in d:
            return True
    return False

def two_sum_all(d):
    total = 0
    
    for t in range(-10000,10001):
    	print(t)
    	if two_sum(d,t) is True:
            total+=1
            print(total)
    return total

print(two_sum_all(num_dist))