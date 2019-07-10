"""
最值相关
"""
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

print('Max:', np.max(highest_prices))
print('Min:', np.min(lowest_prices))
maxi = np.argmax(highest_prices)
mini = np.argmin(lowest_prices)
print('Max date', dates[maxi])
print('Min date', dates[mini])

a = np.arange(1, 10)
b = a[::-1]
a = a.reshape(3, 3)
b = b.reshape(3, 3)
print(np.maximum(a,b))
print(np.minimum(a,b))