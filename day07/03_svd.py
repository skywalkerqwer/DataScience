import numpy as np
import matplotlib.pyplot as mp

M = np.mat('1,5,9;6,8,1')
U,sv,V = np.linalg.svd(M,full_matrices=False)  # 需要逆向回推参数设为False
print(U)
print(sv)
print(V)
print(U * np.diag(sv) * V)

sv[1] = 0
print(U * np.diag(sv) * V)
