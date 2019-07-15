"""
频域滤波
"""
import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import matplotlib.pyplot as mp

"""
读取音频文件
sample_rate: 采样率
noised_sigs: 存储音频中每个采样点的采样位移
"""
sample_rate, noised_sigs = wf.read('../da_data/noised.wav')
# print(sample_rate,noised_sigs.shape)

times = np.arange(noised_sigs.size) / sample_rate

mp.figure('Filter', facecolor='lightgray')
mp.subplot(221)
mp.title('Time Domain', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:178], noised_sigs[:178],c='orangered', label='Noised')
mp.legend()
"""
基于傅里叶变换，获取音频频域信息，绘制音频频域的：频率/能量图像
"""
freqs = nf.fftfreq(times.size,times[1]-times[0])
complex_array = nf.fft(noised_sigs)
pows = np.abs(complex_array)
mp.subplot(222)
mp.title('Frequency Domain', fontsize=16)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.semilogy(freqs[freqs >= 0],pows[freqs >= 0], c='limegreen',label='Noised')
mp.legend()
"""
将低频噪声去除后绘制音频频域的：频率/能量图像。
"""
# 寻找能力最大的频率值
fund_freq = freqs[pows.argmax()]
# 寻找需要抹掉的复数的索引
noised_indices = np.where(freqs != fund_freq)
# 复制一个复数数组的副本,避免污染原始数据
filter_complex_array = complex_array.copy()
filter_complex_array[noised_indices] = 0
filter_pows = np.abs(filter_complex_array)

mp.subplot(224)
mp.xlabel('Frequency', fontsize=12)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(freqs[freqs >= 0], filter_pows[freqs >= 0],c='dodgerblue', label='Filter')
mp.legend()
"""
基于逆向傅里叶变换，生成新的音频信号，绘制音频时域的：时间/位移图像。
"""
filter_sigs = nf.ifft(filter_complex_array).real
mp.subplot(223)
mp.xlabel('Time', fontsize=12)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:178], filter_sigs[:178],c='hotpink', label='Filter')

mp.legend()
mp.show()

"""
生成新的音频
"""
wf.write('../da_data/filter.wav',sample_rate,(filter_sigs).astype(np.int16))
