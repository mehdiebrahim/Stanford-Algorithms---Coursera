from heapq import heapify,_heapify_max,heappop,heappush
import pandas as pd
import os

os.chdir('/Users/mehdiebrahim/Desktop/Stanford Algorithms - Data')
data = pd.read_csv('Median.txt',sep=' ',header=None)
data.columns = ['a']
nums = data['a']

def median_maintenance(nums):
    curr_median = 0
    sum_median = 0

    for num_ind in range(1,len(nums)+1):

        curr_arr = nums[:num_ind]
        heap = []
        heapify(heap)

        for number in curr_arr:
            heappush(heap,number)
        lenheap = 0
        
        if (num_ind)%2==0:
            lenheap = len(heap)//2
        else:
            lenheap = len(heap)//2 +1

        for _ in range(lenheap):
            median = heappop(heap)
        sum_median += median
        
    return "Sum of Median modulo 10000 is: " + str(sum_median%10000)
median_maintenance(nums)