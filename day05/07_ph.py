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


dates, bhp_closing_prices = np.loadtxt(
    '../da_data/bhp.csv', delimiter=',', usecols=(
        1, 6), dtype='M8[D], f8', converters={
            1: dmy2ymd}, unpack=True)
vale_closing_prices = np.loadtxt(
    '../da_data/vale.csv',
    delimiter=',',
    usecols=(6),
    dtype='f8',
    converters={
        1: dmy2ymd},
    unpack=True)

bhp_returns = np.diff(bhp_closing_prices) / bhp_closing_prices[:-1]
vale_returns = np.diff(vale_closing_prices) / vale_closing_prices[:-1]
dates = dates[:-1]

#卷积降噪
convolve_core = np.hanning(8)
convolve_core /= convolve_core.sum()
bhp_returns_convolved = np.convolve(bhp_returns, convolve_core, 'valid')
vale_returns_convolved = np.convolve(vale_returns, convolve_core, 'valid')

# 绘制这条曲线
mp.figure('BHP VALE RETURNS', facecolor='lightgray')
mp.title('BHP VALE RETURNS', fontsize=20)
mp.xlabel('Date')
mp.ylabel('Price')
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%Y %m %d'))
dates = dates.astype('M8[D]')
# 绘制收益线
mp.plot(
    dates,
    bhp_returns,
    color='dodgerblue',
    linestyle='-',
    label='bhp_returns',
    alpha=0.3)
mp.plot(
    dates,
    vale_returns,
    color='orangered',
    linestyle='-',
    label='vale_returns',
    alpha=0.3)

mp.show()
