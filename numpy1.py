import numpy as np
import numpy
#import timeit
import sys
x=np.array([2,3,4,5])
print(type(x))
print(x)

y=np.logspace(1,10,10,endpoint=True,base=10)
print(y)

w=range(1000)
print(type(w))
print(sum(w))
#timeit sum(w)
print(sys.getsizeof(1)*len(x))#memory
print(y.itemsize*len(y))#memory

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(np.sum(a,axis=0))#sumwillbecoloumnwise
c=np.sum(a,axis=1)
print(c)#sumwillberowwise
print(type(c))
b=np.arange(start=11,stop=20).reshape(3,3)
q=numpy.add(a,b)
print(q)
print("----------------------------------------")
print(np.add(a,b))
print("----------------------------------------")
#multiply
print(numpy.multiply(a,b))#elementwise
print("----------------------------------------")
#extract
print(a[0,1])
print("----------------------------------------")
print(a[:,0])#1stcoloumnkisarirow
print("----------------------------------------")
print(a[0,])
#subset of array
print("----------------------------------------")
print(a[:2,:2])
#transpose
print("----------------------------------------")
print(np.transpose(a))
print("----------------------------------------")
#append
col=np.array([21,22,23]).reshape(3,1)
print(col)
print("----------------------------------------")
#insert
print(numpy.insert(a,2,[2,3,4],axis=0))
print("----------------------------------------")
