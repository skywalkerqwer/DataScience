"""
矩阵式子图
"""
import matplotlib.pyplot as mp

mp.figure('Matrix', facecolor='lightgray')
for i in range(1,10):
    mp.subplot(3,3,i)
    mp.text(0.5, 0.5, i, ha='center', va='center', size=36, alpha=0.7)
    mp.xticks([])
    mp.yticks([])
mp.tight_layout()

import matplotlib.gridspec as mg
mp.figure('Grid Layout')
gs = mg.GridSpec(3,3)
mp.subplot(gs[0,:2])  # 将第一行前2个元素合并
mp.show()
