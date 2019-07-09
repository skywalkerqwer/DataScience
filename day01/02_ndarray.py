import numpy as np

a1 = np.array([1,2,3,4,5])
print(a1,type(a1))

a2 = np.arange(0,10,2)
print(a2)

a3 = np.zeros(10)
print(a3,a3.dtype)

a4 = np.ones(10,dtype='int32')
print(a4,a4.dtype)
