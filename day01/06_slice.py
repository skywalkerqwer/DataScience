"""
数组切片
"""
import numpy as np

a = np.arange(1, 10)
# 二维数组
a = a.reshape(3, 3)
print(a)
print('--' * 50)

print(a[:2, :])  # 切出前两行
print(a[:, :2])  # 切出前两列
print(a[::2,:])  # 列按步长2进行切片
