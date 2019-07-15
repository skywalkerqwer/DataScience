"""
插值器
"""

import scipy.interpolate as si
import numpy as np
import matplotlib.pyplot as mp

# 生成11组原始数据
min_x = -50
max_x = 50
dis_x = np.linspace(min_x, max_x, 9)
dis_y = np.sinc(dis_x)
mp.scatter(dis_x, dis_y, marker='o', s=70, color ='red', label ='sinc')


# 通过一系列的散点设计出符合一定规律插值器函数，使用线性插值（kind缺省值）
linear = si.interp1d(dis_x, dis_y)
lin_x = np.linspace(min_x, max_x, 1000)
lin_y = linear(lin_x)
mp.plot(lin_x, lin_y, color='dodgerblue', label='linear')

# 三次样条插值 （Cubic Spline Interpolation） 获得一条光滑曲线
cubic = si.interp1d(dis_x, dis_y, kind='cubic')
cub_x = np.linspace(min_x, max_x, 1000)
cub_y = cubic(cub_x)
mp.plot(cub_x, cub_y, color='orangered', label='cubic')

mp.legend()
mp.show()
