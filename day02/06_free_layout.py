import matplotlib.pyplot as mp

mp.figure('FlowLayout', facecolor='lightgray')
"""
mp.axes([left_bottom_x, left_bottom_y, width, height])
left_bottom_x: 坐下角点x坐标
left_bottom_x: 坐下角点y坐标
width:		 宽度
height:		 高度
"""
mp.axes([0.1, 0.2, 0.5, 0.3])
mp.text(0.5, 0.5, 1, ha='center', va='center', size=36)
mp.show()