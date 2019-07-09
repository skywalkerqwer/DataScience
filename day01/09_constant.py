"""
填充数组
"""

import numpy as np

b = np.array([1,2,3,4])

b = np.pad(b, pad_width=(1, 1), mode='constant', constant_values=0)

print(b)