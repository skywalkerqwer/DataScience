"""
多项式基本操作
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-20, 20, 1000)
y = 4*x**3 + 3*x**2 - 1000*x +1

# 求导数
P = [4, 3, -1000, 1]
Q = np.polyder(P)
# 求根
xs = np.roots(Q)
# 将xs带入原函数得到驻点的y值
ys = np.polyval(P, xs)
mp.scatter(
    xs,
    ys,
    marker='o',
    color='red',
    zorder=3
)

mp.plot(x,y)
mp.show()
