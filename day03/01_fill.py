import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(0, 8*np.pi, 1000)
sinx = np.sin(x)
cosx = np.cos(x/2)/2
mp.figure('Fill',facecolor='lightgray')
mp.title('Fill')
mp.plot(x,sinx,color='dodgerblue', label='sinx', linewidth=2)
mp.plot(x,cosx,color='orangered', label='cosx', linewidth=2)

mp.fill_between(x, sinx, cosx, sinx>cosx, color='dodgerblue', alpha=0.5)
mp.fill_between(x, sinx, cosx, sinx<cosx, color='orangered', alpha=0.5)
mp.legend()
mp.show()