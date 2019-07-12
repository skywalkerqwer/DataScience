"""
矢量化
"""
import numpy as np
import math as m

def foo(x, y):
    return m.sqrt(x**2 + y**2)
    # return np.sqrt(x**2 + y**2)


# a = 3
# b = 4
a = np.array([3,4,5,6])
b = np.array([4,5,6,7])
# print(foo(a, b))

# 把foo函数矢量化，使之可以处理矢量化数据
foo_vec = np.vectorize(foo)
print(foo_vec(a, b))
