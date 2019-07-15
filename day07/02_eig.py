"""
提取图片特征值
"""

import numpy as np
import scipy.misc as sm
import matplotlib.pyplot as mp

img = sm.imread('../da_data/lily.jpg', True)
print(img.shape)

# 特征值提取
eigvals, eigvecs = np.linalg.eig(img)
print(eigvals.shape,eigvals.dtype)
print(eigvecs.shape,eigvecs.dtype)

# 抹掉特征值与特征向量
eigvals[100:] = 0
img2 = np.mat(eigvecs) * np.mat(np.diag(eigvals)) * np.mat(eigvecs).I
mp.figure('Img EIG')
mp.subplot(121)
mp.imshow(img,cmap='gray')
mp.xticks([])
mp.yticks([])

mp.subplot(122)
mp.imshow(img2.real,cmap='gray')
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.show()
