"""
attributes
属性
"""

import numpy as np

# 数组维度
ary = np.array([1, 2, 3, 4])
print(ary, ary.shape)
ary2 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
])
print(ary2, ary2.shape)
ary2.shape = (4, 2)
print(ary2)

print('*' * 50)

ary3 = np.array([1, 2, 3])
print(ary3.dtype)
# 修改数据类型
ary3_1 = ary3.astype('float32')
# 返回新数组
print(ary3_1.dtype)
ary3_2 = ary3.astype('str')
print(ary3_2, ary3_2.dtype)

print('*' * 50)

# 数组元素的个数
ary4 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
print(ary4.shape, ary4.size, len(ary4))

print('*' * 50)

# 数组索引
ary5 = np.arange(1, 9)  # [1,2,3,4,5,6,7,8]
ary5.shape = (2, 2, 2)
print(ary5, ary5.shape)
print(ary5[0])
print(ary5[0][0])
print(ary5[0][0][0])
print(ary5[0, 0, 0])  # 功能同上一行代码
