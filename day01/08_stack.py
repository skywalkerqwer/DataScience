"""
多维数组的组合与拆分
"""
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
print(a)
print(b)

print('-' * 30)

# 垂直方向操作
c = np.vstack((a, b))
print(c)
a, b = np.vsplit(c, 2)  # 要用与切分数量相同数量的变量接受
print(a)
print(b)

print('-' * 30)

# 水平方向操作
d = np.hstack((a, b))
print(c)
a, b = np.hsplit(d, 2)
print(a)
print(b)

print('-' * 30)

# 深度方向操作
"""
俯视视角
"""
e = np.dstack((a, b))
print(e)
