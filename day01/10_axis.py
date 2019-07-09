"""
通过axis作为关键字参数指定的方向，取值如下：
    若数组都是二维数组：
    0: 垂直方向
    1: 水平方向

    若数组都是三维数组：
    0: 垂直方向
    1: 水平方向
    2: 深度方向
"""
import numpy as np

a = np.array([1,2,3,4]).reshape(2,2)
b = np.array([1,2,3,4]).reshape(2,2)

c = np.concatenate((a, b), axis=0)
d = np.concatenate((a, b), axis=1)

print(c)
print(d)

e = np.split(c,2,axis=1)
f = np.split(d,2,axis=0)

print('*'*30)
print(e)
print('*'*30)
print(f)