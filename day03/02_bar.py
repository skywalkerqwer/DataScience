"""
绘制柱状图
"""

import numpy as np
import matplotlib.pyplot as mp

apples = np.array([93, 45, 76, 39, 66, 52, 39, 46, 52, 34, 48, 61])
oranges = np.array([98, 14, 45, 63, 54, 52, 34, 85, 63, 51, 74, 66])

x = np.arange(apples.size)

mp.figure('Bar', facecolor='lightgray')
mp.title('Bar')
mp.xlabel('Month', fontsize=14)
mp.ylabel('Volumn', fontsize=14)
mp.bar(
    x - 0.2,
    apples,
    0.4,
    color='dodgerblue',
    label='Apple')  # 0.8代表每个柱子宽度占80%
mp.bar(x + 0.2, oranges, 0.4, color='orangered', label='Orange',)

mp.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

mp.legend()
mp.show()
