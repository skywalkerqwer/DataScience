"""
时间处理
"""
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md


def dmy2wdays(dmy):
    """日月年 --> 年月日"""
    dmy = str(dmy, encoding='utf-8')
    d = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    wday = d.weekday()
    return wday


wdays,closing_prices = np.loadtxt(
    '../da_data/aapl.csv',
    delimiter=',',
    usecols=(1, 6),
    unpack=True,
    dtype='f8,f8',
    converters={1: dmy2wdays}
)

# 存储周一、周二、...的收盘价均值
ave_price = np.zeros(5)
for wday in range(ave_price.size):
    ave_price[wday] = np.mean(closing_prices[wdays==wday])

print(ave_price)
