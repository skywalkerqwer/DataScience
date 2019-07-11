"""
多项式拟合
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

# 绘制差价价
diff_price = bhp_closing_prices - vale_closing_prices
mp.plot(
    dates,
    diff_price,
    color='red',
    alpha=0.4,
)

# 多项式拟合
days = dates.astype('M8[D]').astype('int32')
P = np.polyfit(days, diff_price, 4)  # 最高次幂设为4
# 计算每一天的预测值
y = np.polyval(P, days)  # 把days带入
mp.plot(
    dates,
    y,
    color='green',
    alpha=0.4,
    label='polyfit'
)

mp.legend()
mp.gcf().autofmt_xdate()  # 自动格式化x轴的日期文本
mp.show()
