"""
网格式子图布局
"""
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg
mp.figure('Grid Layout')
gs = mg.GridSpec(3,3)  # mg.GridSpec(rows, cols)拆分成3行3列
mp.subplot(gs[0,:2])  # 将第一行前2个元素合并
mp.text(0.5,0.5,1)
mp.xticks([])
mp.yticks([])

mp.subplot(gs[:2, 2])
mp.text(0.5,0.5, 2)
mp.xticks([])
mp.yticks([])

mp.subplot(gs[1,1])
mp.text(0.5,0.5, 3)
mp.xticks([])
mp.yticks([])

mp.subplot(gs[1:3,0])
mp.text(0.5,0.5, 4)
mp.xticks([])
mp.yticks([])

mp.subplot(gs[2,1:3])
mp.text(0.5,0.5, 5)
mp.xticks([])
mp.yticks([])

mp.tight_layout()
mp.show()