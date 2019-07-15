import numpy as np
import matplotlib.pyplot as mp
import scipy.misc as sm

img = sm.imread('../da_data/lily.jpg', True)
print(img.shape)

# 特征值提取
eigvals, eigvecs = np.linalg.eig(img)
U, sv, V = np.linalg.svd(img,full_matrices=False)

# 抹掉特征值与特征向量
eigvals[100:] = 0
img3 = np.mat(eigvecs) * np.mat(np.diag(eigvals)) * np.mat(eigvecs).I

sv[100:] = 0
img2 = np.mat(U) * np.mat(np.diag(sv)) * np.mat(V)

mp.figure('Img EIG')
# 原图
mp.subplot(221)
mp.imshow(img.real,cmap='gray')
mp.xticks([])
mp.yticks([])

# 奇异值分解图
mp.subplot(222)
mp.imshow(img2,cmap='gray')
mp.xticks([])
mp.yticks([])

# 特征值图
mp.subplot(223)
mp.imshow(img3.real,cmap='gray')
mp.xticks([])
mp.yticks([])

mp.tight_layout()
mp.show()