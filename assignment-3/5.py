'''5. write a NumPy program to compute the sum of the diagonal element of a given array(matrix).'''
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
sum1=0
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        if (i==j):
            sum1=sum1+a[i][j]
            
print(sum1)