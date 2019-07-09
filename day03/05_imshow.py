"""
绘制热成像图
"""
import numpy as np
import matplotlib.pyplot as mp

n = 1000
x, y = np.meshgrid(
    np.linspace(-3, 3, n),
    np.linspace(-3, 3, n),
)

# 根据公式计算出每个坐标的高度值
z = (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 - y**2)
mp.figure('Imshow', facecolor='lightgray')
mp.title('Imshow')
mp.grid(linestyle=':')
mp.imshow(z, cmap='jet', origin='lower')
mp.show()
