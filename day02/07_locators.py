"""
刻度定位器
"""
import numpy as np
import matplotlib.pyplot as mp

mp.figure('Locators', facecolor='lightgray')
ax = mp.gca()  # 获取当前坐标轴

# 隐藏除底轴以外的所有坐标轴
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
mp.ylim(-1, 1)
mp.xlim(0, 10)

# 将底坐标轴调整到子图中心位置
ax.spines['bottom'].set_position(('data', 0))

# 设置主刻度定位器 与 次刻度定位器
maloc = mp.MultipleLocator(1)  # 多点定位器 每隔1单位划一刻度
ax.xaxis.set_major_locator(maloc)  # 设置主刻度
miloc = mp.MultipleLocator(0.1)  # 每隔0.1单位划一刻度
ax.xaxis.set_minor_locator(miloc)  # 设置次刻度
mp.show()
