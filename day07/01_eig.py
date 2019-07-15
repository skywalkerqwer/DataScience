"""
特征值与特征向量
"""

import numpy as np

m = np.mat('1 4 6; 3 6 8; 7 4 2')
print(m)

# 提取特征值与特征向量
eigvals, eigvecs = np.linalg.eig(m)  # n阶方阵有n组特征值与特征向量
print('特征值:\n',eigvals)
print('特征向量:\n',eigvecs)

# 逆向推倒原方阵
m2 = eigvecs * np.diag(eigvals) * eigvecs.I
print(m2)

# 抹掉部分特征再逆向还原方阵
eigvals[1:] = 0 # 抹掉末尾元素额特征信息
m3 = eigvecs * np.diag(eigvals) * eigvecs.I
print(m3)
