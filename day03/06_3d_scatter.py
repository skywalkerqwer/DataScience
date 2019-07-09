"""
三维点阵图
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 500
x = np.random.normal(0, 1, n)  # 生成标准正态分布(期望=0,标准差=1)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)

mp.figure('3D Scatter')
ax3d = mp.gca(projection='3d')
d = x**2 + y**2 + z**2
ax3d.scatter(x, y, z, s=70, c=d, alpha=0.7)
ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')
mp.tight_layout()
mp.show()
