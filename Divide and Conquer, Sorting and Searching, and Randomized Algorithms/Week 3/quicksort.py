
import pandas as pd
import sys
import os

os.chdir('/Users/mehdiebrahim/Desktop/Coding/Stanford Algorithms - Data')
data = pd.read_csv('QuickSort.txt',sep=' ',header=None)
data.columns = ['a']
L = list(data['a'])
n = len(L)
count= 0

def find_middle(a,b):
    '''Finds the middle element between a and b '''

    if abs(b-a)%2==0:
        med = abs(b-a)//2 
        
        if a<=b:
            return a+med
        else:
            return b+med
        
    elif abs(b-a)%2!=0:
        
        med = abs(b-a)//2
        if a<=b:
            return a + med
        else:
            return b + med
        
def find_median(a,b,c):
    '''finds the median value of a,b,c'''
    
    if a>b:
        if c<b:
            return b
        
        elif a<c:
            return a
        
        else:
            return c
    else:
        
        if a > c:
            return a
        
        elif b < c:
            return b
        
        else:
            return c
    
def partition(A1,start,end,partition_type):
    
    '''Partitions the elements around the pivot so all elements
    <  pivot come before it and those > come after'''
    
    global count
    count += abs(end-start)-1
    
    if partition_type == 'first':
#        uses the first element of sub_array as pivot
        p = A1[start]
        
    elif partition_type == 'end':
        #uses the last element of sub_array as pivot
        
        p= A1[end-1] #end-1 necessary as end==len(A)
        A1[end-1],A1[start] = A1[start],A1[end-1] #swap the first elem with pivot, last elem
                                                    #this step is always necessary for any pivot
    elif partition_type == "median-of-three":
        
        #take the first, middle and last element and 
        # choose median value as pivot
        
        middle_ind = find_middle(start,end-1) #the middle index 
        start_val = A1[start] #value of starting element
        end_val = A1[end-1] #value of last element
        mid_val = A1[middle_ind] #value of middle index
        median = find_median(start_val,end_val,mid_val)
        
        if median == start_val:
#           #if median equals value at first index of subarray
            #set the pivot index to be index of first value of subarray
            piv_ind = start
            
        elif median == end_val:
            piv_ind = end-1
        
        else:
            piv_ind = middle_ind
        
        p = A1[piv_ind]
        A1[start], A1[piv_ind] = A1[piv_ind], A1[start] #swap start index of subarray
                                                        #with first elem
    i = start+1
    j = start+1
    
    while j < end:
        if A1[j] < p:
            A1[j],A1[i] = A1[i],A1[j]
            i += 1
        j += 1

    A1[start], A1[i-1] = A1[i-1], A1[start]
    return i

def QuickSort(A1,start,end,partition_type='median-three-pivot'):
    
    '''Implements the recursive QuickSort algorithm
    We want to continue working on the original array and so we do not
    need to create entirely new arrays and copy sorted elems into these arrays (unlike merge sort)
    We can work on original array but have to keep track of start and end indices of the array, hence 
    we have the start and end variables. The partition types are: first elem as pivot, last elem 
    as pivot and the median-three-pivot rule. 
    '''
    if start == end:
        #base condition necessary because when start index == end i.e. one element array, then we
        # want the recursion to stop 
        return A1

    new_piv = partition(A1,start,end,partition_type) #gives us the position of pivot
    QuickSort(A1,start,new_piv-1,partition_type) #partition to left of pivot 
    QuickSort(A1,new_piv,end,partition_type) #partition to the right of the pivot 

    return A1

QuickSort(L,0,len(L),partition_type='first')
print(count)
