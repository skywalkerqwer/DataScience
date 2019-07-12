"""
位运算
"""
import numpy as np

a = np.array([0, -1, 2, -3, 4, -5])
b = np.array([0, 1, 2, 3, 4, 5])
# 按位异或　不同为１
print(np.where(a^b < 0))  # 返回a,b对应异号元素的下标
