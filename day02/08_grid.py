"""
刻度网格线
"""
import numpy as np
import matplotlib.pyplot as mp

y = [1, 10, 100, 1000, 100, 10, 1]

ax = mp.gca()
xmaloc = mp.MultipleLocator(1)
ax.xaxis.set_major_locator(xmaloc)
xmiloc = mp.MultipleLocator(0.1)
ax.xaxis.set_minor_locator(xmiloc)
ymaloc = mp.MultipleLocator(250)
ax.yaxis.set_major_locator(ymaloc)
ymiloc = mp.MultipleLocator(50)
ax.yaxis.set_minor_locator(ymiloc)

# 绘制刻度网格线
ax.grid(
    which='major',  # 选择主刻度或次刻度
    axis='both',  # 绘制x轴或y轴 x/y/both
    color='orangered',
    alpha=0.6,
    linewidth=0.75)
ax.grid(
    which='minor',
    axis='both',
    color='orangered',
    alpha=0.5,
    linewidth=0.25)

mp.plot(y, 'o-')
mp.show()
