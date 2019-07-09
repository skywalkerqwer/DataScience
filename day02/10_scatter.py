"""
散点图
"""

import numpy as np
import matplotlib.pyplot as mp

# 生成正态分布的两组数据
n = 5000
# np.random.normal(期望, 标准差, 样本容量)
x = np.random.normal(175, 15, n)
y = np.random.normal(65, 10, n)

mp.figure('Persons', facecolor='lightgray')
mp.title('Persons')
d = (x - 175)**2 + (y - 65)**2  # 计算每个点与中心点的相对远近
mp.scatter(
        x,  # x轴坐标数组
        y,  # y轴坐标数组
        s=60,  # 大小
        marker='.' ,  # 点型
        label='Person',
        c=d,  # 直接设置点的颜色
        cmap='jet_r')  # 根据选择的颜色映射表渲染点的颜色
mp.legend()
mp.show()
