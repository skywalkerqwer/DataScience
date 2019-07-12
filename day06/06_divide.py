"""
除法相关函数
"""
import numpy as np
a = np.array([20, 20, -20, -20])
b = np.array([3, -3, 6, -6])

print(a / b)
print(np.floor_divide(a, b))  # 向下取整
print(np.ceil(a / b))  # 向上取整
print(np.trunc(a / b))  # 截断小数点取整
print(np.round(a / b))  # 四舍五入

