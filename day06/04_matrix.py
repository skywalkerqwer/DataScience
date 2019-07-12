import numpy as np

data = np.array([
    [1, 2, 3],
    [3, 2, 1]
])


"""
创建方式一
可选择是否共享数据
"""
m1 = np.matrix(data, copy=True)  # 数据独立
# m1 = np.matrix(data, copy=False)  # 共享数据
print(m1, type(m1))
data[0][0] = 999
print(m1)


"""
创建方式二
一定共享数据
可以接受字符串形式的矩阵
"""
print('*' * 30)
m2 = np.mat(data)
print(m2, type(m2))
m2_str = np.mat('1 2 3; 4 5 6')
print(m2_str)

"""
矩阵的点乘
"""
print('*' * 30)
print(m1 * m2_str.T)

"""
矩阵的逆矩阵
np.linalg.inv(e) == e.I
"""
print('*' * 30)
e = np.mat('1,2,6;3,5,7;4,8,9')
# e = np.mat('1,2,3;4,5,6;7,8,9')  # 无法求逆矩阵
print(e)
print(e.I)
print(e * e.I)

print('-' * 10)
# 广义逆矩阵 --> 矩阵求逆过程推广到非方阵
e = np.mat('1,4,6;4,6,7')
print(e)
print(e.I)
print(e * e.I)

"""
应用
小孩票价为3元，家长票价为3.2元，共花了118.4
小孩票价为3.5元，家长票价为3.6元，共花了135.2
设小孩x 家长y
3x   + 3.2y = 118.4
3.5x + 3.6y = 135.2
--        --     -- --       --     --
| 3.0  3.2 |     | x |       | 118.4 |
|          |  *  |   |   =   |       |
| 3.5  3.6 |     | y |       | 135.2 |
--        --     -- --       --     --
     A             X             B
     A * X = B
     X = A^-1 * B
"""
print('*' * 30)
A = np.mat('3, 3.2; 3.5, 3.6')
B = np.mat('118.4; 135.2')
X = A.I * B  # 基于矩阵的逆矩阵求解
print(X)
print(np.linalg.lstsq(A, B)[0])  # 基于最小二乘法求得误差最小的最优解
print(np.linalg.solve(A, B))  # 解方程组

"""
矩阵实现斐波那契数列
"""
print('*' * 30)
F = np.mat('1 1; 1 0')
for n in range(10):
    print((F ** n)[0, 0], end='  ')

"""
返回数组中满足条件的元素组成的新数组
联合比较运算
a.commpress( 3<a<5)
a.compress([a>3,a<5], axis=0))
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a>3 [F, F, F, T, T, T, T, T, T]
a<5 [T, T, T, T, T, T, T, T, T]
按照纵向(axis=0)进行与运算
    [F, F, F, T, F, F, F, F, F]
             [4]
"""
print('*' * 30)
a = np.array([1, 2, 3, 5, 6, 7, 8, 9])
re = a.compress(np.all([a > 3, a < 5], axis=0))
print(re)
