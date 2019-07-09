"""
绘制等高线图
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

mp.figure('Contour', facecolor='lightgray')
mp.title('Contour')
mp.grid(linestyle=':')
cntr = mp.contour(
    x,
    y,
    z,
    8,  # 把等高线绘制成8部分
    colors='black',
    linewidths=0.5,
)
mp.clabel(
    cntr,  # 等高线返回对象
    inline_spacing=1,
    fmt='%.1f',
    fontsize=10,
)  # 添加标签

mp.contourf(x,y,z,8,cmap='jet')  # 通过jet颜色映射填充等高线
mp.show()
