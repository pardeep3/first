#ques 1

import numpy as np
a=np.random.random((1,10))
print(a)
print(a.shape)
b=np.mean(a) #mean
print(b)

#ques 2

c=np.random.random((20,1))
print(c)
d=np.var(c)  #variation
print(d)
e=np.std(c)
print(e)

#ques 3

A=np.random.random((10,20))
B=np.random.random((20,25))
print(A)
print(B)
f=np.matmul(A,B)   #martix multiplication
print(f)
print(f.shape)
g=np.sum(f)       #sum of elements of matrix
print(g)

#question4

import  numpy as np
import math
a=np.random.random((10,1))
print(a)
b=[]
for i in range (0,10):
    x=1/(1+math.exp(-(a[i,0])))
    b.append(x)
print(b)
