import numpy as np
x=np.matrix("4,5,16,7;2,-3,2,3;3,4,5,6;4,7,8,9")
print(x)
print("----------------------------------------")
#inverse
print("inverse:")
print(np.linalg.inv(x))
print("----------------------------------------")
#B=np.matrix("2,1,2;1,0,1;3,1,3")
#print("error")
#print(np.linalg.inv(B))#singularmatrixerroe
print("----------------------------------------")
#linear equation
A=np.matrix("3,1,2,3,2,5,6,7,8").reshape(3,3)
X=np.matrix("x,y,z").reshape(3,1)
B=np.matrix("2,-1,3").reshape(3,1)
print(A)
print("----------------------------------------")
print(X)
print("----------------------------------------")
print(B)
print("----------------------------------------")
