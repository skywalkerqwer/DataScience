import numpy as np
import matplotlib.pyplot as mp

mp.figure('Figure Title A',facecolor='lightgray')
"""
代码...
mp.plot()
画在A窗口里
"""
mp.figure('Figure Title B',facecolor='lightblue')

mp.figure('Figure Title A')
mp.title('Title A',fontsize=18)
mp.xlabel('Time',fontsize=14)
mp.ylabel('Price',fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.tight_layout()  # 窗口紧凑

mp.show()
