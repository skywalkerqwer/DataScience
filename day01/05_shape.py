"""
维度操作
"""
import numpy as np

a = np.arange(1,10)
print(a)

b = a.reshape(3,3)
print(b)

a[0] = 999  # 视图变维共享数据
print(a)
print(b)
print(b.ravel())

# 复制变维
c = b.flatten()  # 将高维数组解为一维数组
c[0] = 111
print(b)
print(c)

# 就地变维
a = np.arange(1,9)
print('--'*50)
a.shape = (2,4)
print(a)
a.resize(2,2,2)
print(a)