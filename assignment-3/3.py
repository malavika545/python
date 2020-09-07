'''3.	Compute outer product of 2 vectors.
Eg:
original matrix:
[[1, 0], [0, 1]]
[[1, 2], [3, 4]]
Outer product of the said two vectors:
[[1 2 3 4]
 [0 0 0 0]
 [0 0 0 0]
 [1 2 3 4]]
'''
import numpy as np
a=np.array([[1,0],[0,1]])
b=np.array([[1,2],[3,4]])
c=[[],[],[],[]]
x=0
for i in a:
    for j in i:
        for k in b:
            for l in k:
                c[x].append(j*l)
        x=x+1
c=np.array(c)
print(c)
