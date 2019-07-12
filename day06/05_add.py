"""
加法乘法通用函数
"""
import numpy as np

a = np.arange(1,7)
print(a)

print(np.add(a, a))  # 两数组相加
print(np.add.reduce(a))  # 累加和
print(np.add.accumulate(a))  # 累加和过程数组
print(np.prod(a))  # 累乘
print(np.cumprod(a))  # 累乘过程数组
print(np.add.outer([10,20,30], a))  # 求两个数组的外和
print(np.outer([10,20,30], a))  # 求两个数组的外积
