"""
掩码 操作
"""
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a + 10)
print(a * 2.5)
print(a + a)

b = np.arange(1, 10)

# mask = [True,False,True,False,True,False,True,False,True]

# mask = b % 2 == 0  # 与上面的运算类似  b中每一个元素都会进行一次运算

mask = [2, 2, 3, 3, 6, 6, 4, 4]  # 掩码中元素对应b中元素下标
print(b[mask])

c = np.array([20,30,10,15])

mask0 = [2,3,0,1]  # 用掩码排序
print(c[mask0])
