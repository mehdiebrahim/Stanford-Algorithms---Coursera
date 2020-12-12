
import pandas as pd
import sys
import os

os.chdir('/Users/mehdiebrahim/Desktop/Coding/Stanford Algorithms - Data')
data = pd.read_csv('numbers.txt',sep=' ',header=None)
data.columns = ['a']
L = list(data['a'])
n = len(L)
inv_count = 0

def Merge(L,R,mid):
    global inv_count
    result = [0]*(len(L)+len(R))
    #temporary list in which to merge L and R
    i=j=k=0
#     print(L,R)
    
#     below is the main loop for comparing two sorted arrays to merge into result
    while i < len(L) and j < len(R): 
        if L[i] < R[j]: 
            result[k] = L[i] 
          
            i+=1
        else: 
            result[k] = R[j]
            inv_count+=mid-(i)
            j+=1
        k+=1
        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        # this is necessary i.e if L=[1,2,4,9] R=[3,4,5,6] gives res 
        # [1,2,3,4,4,5,6,6] without the below step. 
        # In this case,i=3,j=4,k=7 so final element of L which is 9 
        # needs to be added. This step below would be necessary when
        # an element in L is bigger than all of elems in R
        # so the above loop breaks before 9 is copied in
    while i<len(L):
        result[k]=L[i]
        i+=1
        k+=1
        
    while j<len(R):
        result[k]=R[j]
        j+=1
        k+=1

    return result
    

def MergeSort(array):
      
    if len(array)==1:
        return array   #this way when the L or R inputted into Merge func has len=1 (after enough divides i.e array[:mid] and array[mid:], 
                       #MergeSort outputs the array which can be then sorted and merged by the Merge func. 
                       #Otherwise, MergeSort outputs None when the L or R has 
                       #which cannot be sorted and merged 
    mid = len(array)//2 
    L = array[:mid]
    R = array[mid:]
    

      
    return Merge(MergeSort(L),MergeSort(R),mid)
   

MergeSort(L)
print(inv_count)