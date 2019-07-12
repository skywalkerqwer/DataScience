"""
定义一种投资策略，判断是否可以实施
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

def profit(oprice, hprice, lprice, cprice):
    """
    定义一种买入卖出策略
    :param oprice: 开盘价
    :param hprice: 最高价
    :param lprice: 最低价
    :param cprice: 收盘价
    :return:
    """
    buy_price = oprice * 0.99
    if lprice <= buy_price <= hprice:
        return (cprice - buy_price) / buy_price
    else:
        return np.nan


# 计算使用该策略30天中每天的收益
profits = np.vectorize(profit)(opening_price, highest_prices, lowest_prices, closing_prices)
# 获取profits中是nan的掩码数组
nan_mask = np.isnan(profits)
dates = dates[~nan_mask]  # ~代表按位取反
profits = profits[~nan_mask]
mp.plot(
    dates,
    profits,
    'o-'
)


mp.legend()
mp.gcf().autofmt_xdate()  # 自动格式化x轴的日期文本
mp.show()
