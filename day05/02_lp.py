"""
线性预测
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

mp.plot(
    dates,
    closing_prices,
    label='Closing Prices',
    linewidth=2,
    color='dodgerblue',
    linestyle='--',
    alpha=0.3
)

# 基于线性预测理论 通过6天股价预测第7天股价
N = 3  # 三元一次方程组

# 构建一个数组存储所有的预测结果
pred_price = np.zeros(closing_prices.size - 2*N + 1)

for j in range(pred_price.size):
    A = np.zeros((N, N))  # A = N*N 的矩阵
    for i in range(N):
        A[i, ] = closing_prices[i+j: i+N+j]
    # print(A)
    B = closing_prices[N+j: N*2+j]
    X = np.linalg.lstsq(A,B)[0]
    print(X)
    pred = B.dot(X)  # 向量点乘
    pred_price[j] = pred
    # print('第%d天预测：'%j,pred)
    # print('第%d天实际：'%j,closing_prices[6+j])

# 绘制预测价格曲线
mp.plot(
    dates[2*N:],
    pred_price[:-1],
    label='Predict Prices',
    linewidth=2,
    color='orangered',
    linestyle='-',
    alpha=0.3
)

mp.legend()
mp.gcf().autofmt_xdate()  # 自动格式化x轴的日期文本
mp.show()

