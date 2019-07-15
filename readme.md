# 数据分析学习笔记大纲

------

## day01 -- Numpy

- 03_attr.py
  - 修改数据类型
  - 数组维度
  - 数组索引
- 04_obj.py
  - 自定义复合数据类型
  - 设置dtype 自定义别名
  - 多种设置dtype的方法
  - 时间类型
- 05_shape.py
  - 复制变维
  - 就地变维
- 06_slice.py
  - 数组切片
- 07_mask.py
  - 掩码操作
  - 得到数组中所有偶数
  - 用掩码进行排序
- 08_stack.py
  - 多维数组的拆分与组合
  - 垂直、水平、深度操作
- 09_constant.py
  - 填充数组
- 10_axis.py
  - axis作为关键字指定方向

## day02 -- matplotlib

- 01_plot.py
- 垂直水平线
- 02_plot_sin.py
  - 在制定区间拆分点
  - 绘制三角函数
  - mp.plot()关键字参数：线形、线宽、颜色、透明度、标签
  - 修改可视区域
  - 修改坐标刻度
  - latex语法
  - 设置坐标轴
  - 绘制两个特殊点
  - 绘制两个点的备注
  - 显示图例
- 03_figure.py
  - 绘制多个窗口
  - 窗口各个参数设定
- 04_subplot.py
  - 矩阵式子图
- 05_gridsubplot.py
  - 网格式子图布局
  - matplotlib.gridspec
- 06_free_layout.py
  - 自由式子图布局
  - mp.axes()
- 07_locators.py
  - 刻度定位器
  - 获取当前坐标轴
  - 隐藏除底轴以外的所有坐标轴
  - 将底坐标轴调整到子图中心位置
  - 设置主刻度定位器 与 次刻度定位器
  - 多点定位器
- 08_grid.py
  - 绘制刻度网格线
  - ax.grid()
- 09_semilogy.py
  - 绘制半对数坐标轴
  - mp.semilogy()
- 10_scatter.py
  - 生成呈正态分布的两组数据
  - np.random.normal(期望,标准差,容量)
  - 绘制散点图mp.scatter()

## day03 -- matplotlib

- 01_fill.py

  - 填充
  - mp.fill_between()

- 02_bar.py

  - 绘制柱状图
  - mp.bar()

- 03_pie.py

  - 绘制饼状图
  - mp.pie()

- 04_contour.py

  - 绘制等高线图
  - cntr = mp.contour()  等高线返回对象
  - mp.clabel( cntr,...)

- 05_imshow.py

  - 绘制热成像图
  - mp.imshow()

- 06_3d_scatter.py

  - 三维点阵图
  - ax3d = mp.gca(projection='3d')
  - ax3d.scatter()

- 07_3d_surface.py

  - 3d曲面图
  - ax3d = mp.gca(projection='3d')
  - ax3d.plot_surface()

- 08_3d_wirefarme.py

  - 3d曲面图
  - ax3d = mp.gca(projection='3d')
  - ax3d.plot_wireframe()

- 09_polar.py

  - 极坐标系
  - mp.gca(projection='polar')

- 10_bubble.py

  - 气泡动画
  - matplotlib.animation
  - anim = ma.FuncAnimation()

- 11_loadtxt.py

  - 加载文件

  - np.loadtxt()

## day04 -- 案例应用

- 01_k.py

  - 绘制K线图
  - 绘制实体  mp.bar()
  - 绘制影线  mp.vlines()

- 02_mean.py

  - 算术平均值  mean = np.mean()
  - 加权平均数  wap = np.average(..., weight=)
  - 中位数  median = np.median()

- 03_max.py

  - 最大值  np.max()
  - 最小值  np.min()
  - 最大最小值元素下标
    - maxi = np.argmax
    - mini = np.argmin
    - dates[maxi]
    - dates[mini]
  - 两个数组中每个对应元素的最大最小值
    - np.maximum(a,b)
    - np.minimum(a,b)

- 04_std.py

  - 中体标准差  np.std()
  - 平均值  m = np.mean(closing_prices)
  - 离差  d = closing_prices - m
  - 离差方  q = d**2
  - 方差  s = np.mean(q)
  - 标准差  v = np.sqrt(s)

- 05_wd.py

  - 时间处理

  - matplotlib.dates

  - ```
    d = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    wday = d.weekday()
    ave_price = np.zeros(5)
    for wday in range(ave_price.size):
        ave_price[wday] = np.mean(closing_prices[wdays==wday])
    ```

- 06_aaa.py
  - 轴向汇总
  - re = np.apply_along_axis()

- 07_sma.py
  - 移动平均线
  - 卷积  np.convolve(原数组,卷积核,'卷积类型')
  - 卷积实现移动平均线
  - 加权卷积
    - 通过指数函数寻求一组卷积核
    
    - kernel_e = np.exp(np.linspace(-1, 0, 5)
    
    - 翻转卷积核
    
    - kernel_e = kernel_e[::-1]
    
    - 让卷积核之和为1 保证卷积结果与源数据匹配
    
    - kernel_e /= kernel_e.sum()
    
    - sma_e = np.convolve()
    
## day05 -- 拟合分析
  - 01_brd.py
    - 绘制布林带
  - 02_lp.py
    - 线性预测
    - 计算矩阵的最小二乘解再通过矩阵点积得到预测值
  - 03_trend.py
    - 线性拟合 绘制股价趋势图
    - 通过最小二乘法求出所有结果中拟合误差最小的k与b的值
  - 04_cov.py
    - 计算协方差 评估两组数据相似度，值越大相似度越高
    - numpy协方差矩阵API np.cov() 结果为样本协方差
    - 计算相关系数[-1,1]  分析两组数据的相关性
    - numpy相关性矩阵API  np.corrcoef()
  - 05_poly.py
    - 多项式基本操作
    - 一组系数组成的数组可以代表一个多项式
    - 根据x求y值  np.polyval(P,X)  P--> 多项式系数
    - 多项式求导  np.polyder(P)
    - 求两个多项式差函数  Q = np.polysub(P1, P2)
    - 求根  xs = np.roots(P)  可带入差函数求两函数交点
  - 06_poly.py
    - 多项式拟合
    - 根据一组样本，并给出最高次幂，求出拟合多项式函数
    - P = np.polyfit(X, Y, 最高次幂)
  - 07_ph.py
    - 数据平滑
    - 卷积降噪
      - 利用convolve_core = hanning(n)产生一组卷积核
      - 卷积核归一
      - 曲线进行卷积运算  np.convolve(曲线,convole_core)
    - 拟合经过卷积降噪的曲线
      - P = np.polyfit(dates, 降噪曲线, 次幂)
      - 求出P函数每一点的y坐标
      - y = np.polyval(P, dates)
## day06 -- 数学运算
  - 01_obv.py
    - np.sign() 返回数组的符号数组
    - np.piecewise(源数组, 条件序列, 取值序列)
    - obv柱状图
  - 02_vec.py
    - 矢量化
    - 把处理标量的函数矢量化，使之可以处理矢量化数据
  - 03_vec.py
    - 定义一种投资策略，判断是否可以实施
  - 04_matrix.py
    - 两种创建矩阵的方法
      - np.matrix()  可选择是否共享数据
      - np.mat()  数据共享 可接受字符串形式的矩阵
    - 矩阵的点乘
    - 矩阵的逆矩阵 m * n = E
    - 应用于解多元方程的解
    - 实现斐波那契数列
    - 联合比较运算
  - 05_add.py
    - 加法乘法通用函数
  - 06_divide.py
    - 除法通用函数
  - 07_bitwise.py
    - 位运算
  - 08_fly.py
    - 根据傅里叶变换合成方波
## day07 -- 
  - 