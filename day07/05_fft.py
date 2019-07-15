"""
傅里叶变换
"""
import numpy as np
import numpy.fft as nf
import matplotlib.pyplot as mp

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# 合成方波
n = 5000
y = np.zeros(x.size)
for i in range(1, n + 1):
    y += 4 * np.pi / (2 * i - 1) * np.sin((2 * i - 1) * x)

# 拆分合成波
complex_array = nf.fft(y)
print(complex_array.shape, complex_array.dtype, complex_array[0])

# 再次合成波
y_new = nf.ifft(complex_array)

mp.subplot(121)
mp.grid(linestyle=':')
mp.plot(x, y, label='y')
mp.plot(x, y_new, label='y_new', linewidth=7, color='orangered', alpha=0.4)
# 得到分解波的频率序列
freqs = nf.fftfreq(x.size, x[1] - x[0])

# 复数的模为信号的振幅（能量大小）
ffts = nf.fft(y)
pows = np.abs(ffts)

mp.subplot(122)
mp.title('Frequency Domain', fontsize=16)
mp.xlabel('Frequency', fontsize=12)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(freqs[freqs >= 0], pows[freqs >= 0], c='orangered', label='Frequency Spectrum')

mp.legend()
mp.tight_layout()
mp.show()
