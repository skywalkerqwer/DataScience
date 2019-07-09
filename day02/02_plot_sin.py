"""
绘制三角函数
"""

import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-np.pi, np.pi, 1000)  # 在0到2π内拆分出1000个点
# x -> <class 'numpy.ndarray'>
y = np.sin(x)
# y -> <class 'numpy.ndarray'>

"""
# linestyle : '-'实线, '--'虚线, '-.'点虚线, ':'虚线
# linewidth : 线宽
# color : #xxxxxx (0,0,0) 或 (0,0,0,0.5) 不需设置alpha
# alpha : 透明度 0.0 -> 1.0
"""
mp.plot(
    x,
    y,
    linestyle='--',
    linewidth=2,
    color='#ff0000',
    label=r'$y=sin(x)$')

y = 0.5 * np.cos(x)
mp.plot(
    x,
    y,
    linestyle='-.',
    linewidth=2,
    color='orangered',
    alpha=0.7,
    label=r'$y=\frac{1}{2} cos(x)$')

# mp.vlines(0, -1, 1)
# mp.hlines(0, 1.2 * -np.pi, 1.2 * np.pi)

"""
# 修改可视区域
mp.xlim(0, np.pi)
mp.ylim(0, 1)
"""

# 修改坐标刻度
xvals = [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi]
# xtexts = ['-π', '-π/2', '0', 'π/2', 'π']
xtexts = [
    r'$-\pi$',
    r'$-\frac{\pi}{2}$',
    r'$0$',
    r'$\frac{\pi}{2}$',
    r'$\pi$'
]  # latex语法
mp.xticks(xvals, xtexts)  # (x_val_list,x_text_list): (x轴刻度值序列,x轴标签文本序列)
yvals = [-1, -0.5, 0, 0.5, 1]
ytexts = [r'$1$', r'$-\frac{1}{2}$', r'$0$', r'$\frac{1}{2}$', r'$1$']
mp.yticks(yvals, ytexts)

# 设置坐标轴
ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# 绘制两个特殊点
px = [np.pi / 2, np.pi / 2]
py = [0, 1]
mp.scatter(px, py, marker='o', s=70, color='#0000ff', label='Points', zorder=3)

# 绘制两个点的备注
mp.annotate(
    r'$[\frac{\pi}{2},1]$',  # 备注内容
    xycoords='data',  # 选择数据坐标系
    xy=(np.pi / 2, 1),  # 为π/2,1这个点添加备注
    textcoords='offset points',  # 相对偏移
    xytext=(30, 20),  # 偏移量
    fontsize=14,
    arrowprops=dict(
        arrowstyle='-|>',  # 连线样式
        connectionstyle='angle3'  # 箭头样式
    )
)
mp.annotate(
    r'$[\frac{\pi}{2},0]$',  # 备注内容
    xycoords='data',  # 选择数据坐标系
    xy=(np.pi / 2, 0),  # 为π/2,1这个点添加备注
    textcoords='offset points',  # 相对偏移
    xytext=(-50, -40),  # 偏移量
    fontsize=14,
    arrowprops=dict(
        arrowstyle='-|>',  # 连线样式
        connectionstyle='angle3'  # 箭头样式
    )
)

# 显示图例
# 需要先在mp.plot()内写好label参数
mp.legend()

mp.show()
