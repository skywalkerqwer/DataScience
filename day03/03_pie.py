"""
绘制饼状图
"""
import numpy as np
import matplotlib.pyplot as mp

labels = ['Python', 'JavaScript', 'C++', 'Java', 'PHP']
values = [26, 17, 21, 29, 11]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
colors = ['dodgerblue', 'orangered', 'limegreen', 'violet', 'gold']

mp.figure('Pie Chart', facecolor='lightgray')
mp.title('Languages PR')
mp.pie(values, spaces, labels, colors, '%.1f%%', shadow=True, startangle=0, radius=1)
mp.legend()
mp.show()
