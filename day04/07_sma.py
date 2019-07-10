import numpy as np
import datetime as dt
import matplotlib.dates as md
import matplotlib.pyplot as mp

def dmy2ymd(dmy):
    """日月年 --> 年月日"""
    dmy = str(dmy, encoding='utf-8')
    d = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    ymd = d.strftime('%Y-%m-%d')
    return ymd


dates, opening_price, highest_prices, lowest_prices, closing_prices = np.loadtxt(
    '../da_data/aapl.csv',
    delimiter=',',
    usecols=(1, 3, 4, 5, 6),
    unpack=True,
    dtype='M8[D],f8,f8,f8,f8',
    converters={1: dmy2ymd}
)

# 把dates的数据类型改为matplotlib的日期类型
dates = dates.astype(md.datetime.datetime)

# 绘制收盘价的折线图
mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.grid(linestyle=':')
mp.tick_params(labelsize=10)

# 设置刻度定位器
ax = mp.gca()
maloc = md.WeekdayLocator(byweekday=md.MO)  # 以每周周一为主刻度
ax.xaxis.set_major_locator(maloc)
# 设置主刻度日期格式
ax.xaxis.set_major_formatter(md.DateFormatter('%Y-%m-%d'))
miloc = md.DayLocator()  # 以每天为次刻度
ax.xaxis.set_minor_locator(miloc)

mp.plot(
    dates,
    closing_prices,
    label='Closing Prices',
    linewidth=2,
    color='dodgerblue',
    linestyle='--',
    alpha=0.3
)

# 移动平均线
sma = np.zeros(closing_prices.size - 4)  # 5日移动平均线
for i in range(sma.size):
    sma[i] = closing_prices[i:i + 5].mean()
mp.plot(
    dates[4:],  # 从第四天开始绘制
    sma,
    label='SMA-5',
    linewidth=2,
    color='orangered',
    linestyle='-',
    alpha=0.9
)

"""
使用卷积实现5日平均线
"""
kernel = np.ones(5) / 5  # 生成5个 1/5
sma_2 = np.convolve(
    closing_prices,
    kernel,
    'valid',  # 有效卷积
)
mp.plot(
    dates[4:],  # 从第四天开始绘制
    sma_2,
    label='SMA-5_2',
    linewidth=7,
    color='orangered',
    linestyle='-',
    alpha=0.3
)

# 卷积实现10日移动平均线
kernel_10 = np.ones(10) / 10  # 生成5个 1/5
sma_3 = np.convolve(
    closing_prices,
    kernel_10,
    'valid',  # 有效卷积
)
mp.plot(
    dates[9:],  # 从第四天开始绘制
    sma_3,
    label='SMA-10',
    linewidth=2,
    color='green',
    linestyle='-',
    alpha=0.9,
)

# 实现加权卷积
# 通过指数函数寻求一组卷积核
kernel_e = np.exp(np.linspace(-1, 0, 5))  # 从e^-1 到 1 取5个点
kernel_e = kernel_e[::-1]
kernel_e /= kernel_e.sum()  # 让卷积核之和为1 保证卷积结果与源数据匹配
sma_5e = np.convolve(
    closing_prices,
    kernel_e,
    'valid',  # 有效卷积
)
mp.plot(
    dates[4:],  # 从第四天开始绘制
    sma_5e,
    label='SMA-e',
    linewidth=7,
    color='green',
    linestyle='-',
    alpha=0.3,
)


mp.legend()
mp.gcf().autofmt_xdate()  # 自动格式化x轴的日期文本
mp.show()
