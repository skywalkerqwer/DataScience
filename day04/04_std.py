import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md


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

std = np.std(closing_prices)
print('std:',std)

m = np.mean(closing_prices)
d = closing_prices - m  # 离差
q = d**2  # 离差方
s = np.mean(q)  # 方差
v = np.sqrt(s)  # 标准差
print(v)
