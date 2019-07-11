"""
协方差
"""
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


dates, bhp_closing_prices = np.loadtxt(
    '../da_data/bhp.csv',
    delimiter=',',
    usecols=(1, 6),
    unpack=True,
    dtype='M8[D],f8',
    converters={1: dmy2ymd}
)
vale_closing_prices = np.loadtxt(
    '../da_data/vale.csv',
    delimiter=',',
    usecols=(6,),
    unpack=True,
)


# 把dates的数据类型改为matplotlib的日期类型
dates = dates.astype(md.datetime.datetime)

# 绘制收盘价的折线图
mp.figure('COV', facecolor='lightgray')
mp.title('COV', fontsize=18)
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
# 绘制收盘价
mp.plot(
    dates,
    bhp_closing_prices,
    label='BHP Closing Prices',
    linewidth=2,
    color='dodgerblue',
    linestyle='-',
)
mp.plot(
    dates,
    vale_closing_prices,
    label='VALE Closing Prices',
    linewidth=2,
    color='orangered',
    linestyle='-',
)

# 计算两只股票的协方差
# 先计算均值
bhp_mean = bhp_closing_prices.mean()
vale_mean = vale_closing_prices.mean()
# 离差
d1 = bhp_closing_prices - bhp_mean
d2 = vale_closing_prices - vale_mean
# 协方差
cov = np.mean(d1 * d2)
print(cov)

# 计算相关系数
s = cov / (np.std(bhp_closing_prices) * np.std(vale_closing_prices))
print(s)

# 获取相关性矩阵
m = np.corrcoef(bhp_closing_prices, vale_closing_prices)[0, 1]
print(m)

# 获取协方差矩阵
cm = np.cov(bhp_closing_prices, vale_closing_prices)[0, 1]  # 结果为样本协方差
print(cm)

mp.legend()
mp.gcf().autofmt_xdate()  # 自动格式化x轴的日期文本
mp.show()
