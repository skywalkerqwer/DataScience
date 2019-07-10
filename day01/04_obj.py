"""
自定义复合数据类型
"""

import numpy as np

data = [
    ('zs', [50, 51, 52], 15),
    ('ls', [60, 61, 62], 16),
    ('ww', [70, 71, 72], 17),
]
ary1 = np.array(data)
print(ary1)

print(ary1[0])
print(ary1[:, 1])

print('--' * 50)

# 设置dtype 自定义别名
ary2 = np.array(data, dtype=[
    ('name', 'str', 2),
    ('score', 'int32', 3),
    ('age', 'int64', 1),
])
print(ary2)
print(ary2[0]['age'])
print(ary2[:]['score'])

print('--' * 50)

# 设置dtype
c = np.array(data, dtype={
    'names': ['name', 'score', 'age'],
    'formats': ['U2', '3int32', 'int32'],
})
print(c)
print(c.dtype)

print('--' * 50)

# 设置dtype
d = np.array(data, dtype={
    'name': ('U2', 0),
    'score': ('3int32', 8),
    'age': ('int32', 20),
})  # 设置字节偏移量
print(d.dtype)

print('--' * 50)
# ndarry数组存放日期数据
dates = [
    '2011-01-01',
    '2012-01-01',
    '2011-02-01',
    '2012',
    '2011-01-01 12:30:05',
]
ary3 = np.array(dates)
print(ary3, ary3.dtype)
ary3_1 = ary3.astype('M8[D]')  # []内可填 M:月 h:小时...
print(ary3_1, ary3_1.dtype)
print(ary3_1[1]-ary3_1[0])  # 计算日期间隔时间
