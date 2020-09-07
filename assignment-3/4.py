'''4.	Write a NumPy program to compute the condition number of a given matrix.
5.	Original matrix:
6.	[[1 2]
7.	 [3 4]]
8.	Condition number of the said matrix:
9.	14.9330343737
'''
import numpy as np
import numpy.linalg as nl
a=np.array([[1,2],[3,4]])
x=nl.cond(a)
print(x)