
Question 1
Download the following text file:

Median.txt
The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. Letting x_ix 
i
​	
  denote the iith number of the file, the kkth median m_km 
k
​	
  is defined as the median of the numbers x_1,\ldots,x_kx 
1
​	
 ,…,x 
k
​	
 . (So, if kk is odd, then m_km 
k
​	
  is ((k+1)/2)((k+1)/2)th smallest number among x_1,\ldots,x_kx 
1
​	
 ,…,x 
k
​	
 ; if kk is even, then m_km 
k
​	
  is the (k/2)(k/2)th smallest number among x_1,\ldots,x_kx 
1
​	
 ,…,x 
k
​	
 .)

In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That is, you should compute (m_1+m_2+m_3 + \cdots + m_{10000}) \bmod 10000(m 
1
​	
 +m 
2
​	
 +m 
3
​	
 +⋯+m 
10000
​	
 )mod10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations of the algorithm.
