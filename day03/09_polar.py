"""
极坐标系
"""
import numpy as np
import matplotlib.pyplot as mp

mp.figure('Polor',facecolor='lightgray')

mp.gca(projection='polar')  # 设置坐标系为极坐标系

mp.xlabel(r'$\theta$', fontsize=14)
mp.ylabel(r'$\rho$',fontsize=14)
mp.grid(linestyle=':')

t = np.linspace(0,4*np.pi,1000)
r = 0.8*t
mp.plot(t,r)

mp.show()
