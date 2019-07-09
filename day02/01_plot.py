import numpy as np
import matplotlib.pyplot as mp

# xarray 水平坐标序列
# yarray 垂直坐标序列

xarray = np.arange(1, 6)
yarray = np.array([16, 41, 55, 8, 32])

mp.plot(xarray, yarray)

# 垂直水平线
mp.vlines(2.5, 20, 80)  # (x坐标,起始位置,终止位置)
mp.hlines(50, 1.5, 3.5)  # (y坐标,起始,终止)


mp.show()
