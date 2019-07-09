# 数据分析学习笔记大纲

------

## day01 -- Numpy

- numpy概述

- 多维数组的创建

  - np.array()
  - np.arange()
  - np.zeros()
  - np.ones

- ndarry对象的属性操作

  - 数组的维度：np.ndarray.shape
  - 元素的类型：np.ndarray.dtype
  - 数组元素的个数：np.ndarray.size 
  - 数组元素索引

- 自定义Numpy的内部基本数据类型

- ndarray数组对象的维度操作

- ndarray数组的掩码操作

- 多维数组的组合与拆分

  - 垂直 np.vstack((a, b))  np.vsplit(c, 2)
  - 水平 np.hstack((a, b))  np.hsplit(c, 2)
  - 深度 np.dstack((a, b))  np.dsplit(i, 2)

- 通过axis作为关键字参数指定方向

  0: 垂直方向组合

  1: 水平方向组合

  2: 深度方向组合

- 简单的一维数组组合方案

  - 把两个数组摞在一起成两行 c = np.row_stack((a, b))
  - #把两个数组组合在一起成两列 d = np.column_stack((a, b))

- #### ndarray类的其他属性

  - shape - 维度
  - dtype - 元素类型
  - size - 元素数量
  - ndim - 维数，len(shape)
  - itemsize - 元素字节数
  - nbytes - 总字节数 = size x itemsize
  - real - 复数数组的实部数组
  - imag - 复数数组的虚部数组
  - T - 数组对象的转置视图
  - flat - 扁平迭代器

## day02 -- matplotlib

- matplotlib基本功能

- 绘图核心API

  - ```python
    mp.plot(xarray, yarray, linestyle='', linewidth=‘’, color='', alpha=‘’，label='')
    ```

    - linestyle: '-' 实线  '--' 虚线  ':' 点线
    - linewidth: 线宽
    - color: 英文颜色单词 或 常见颜色英文单词首字母 或 #495434 或 (1,1,1) 或 (1,1,1,1)
    - alpha:透明度

  - 绘制垂直线 mp.vlines(vval, ymin, ymax, ...)

  - 绘制水平线 mp.hlines(xval, xmin, xmax, ...)

- 设置坐标轴范围 

  - mp.xlim(x_limt_min, x_limit_max)
  - mp.ylim(y_limt_min, y_limit_max)

- 设置坐标刻度

  - mp.xticks(x_val_list , x_text_list )
  - mp.yticks(y_val_list , y_text_list )

- 刻度文本的特殊语法 LaTex排版语法字符串

- 设置坐标轴  

  - 获取当前坐标轴字典 ax = mp.gca()
  - 获取其中某个坐标轴 axis = ax.spines['坐标轴名']
  - 设置坐标轴的位置 axis.set_position((type, val))
    - type: <str> 移动坐标轴的参照类型  一般为'data' (以数据的值作为移动参照值)
    - val:  参照值
  - 设置坐标轴的颜色 axis.set_color(color)

- 图例

  - mp.plot(... label='', ...)
  - label: <关键字参数 str> 支持LaTex排版语法字符串
  - mp.legend(loc='')

- 特殊点

  ```python
    mp.scatter(xarray, yarray, 
               marker='', 		#点型 ~ matplotlib.markers
               s=60, 			#大小
               edgecolor='', 	#边缘色
               facecolor='',	#填充色
               zorder=3			#绘制图层编号 （编号越大，图层越靠上）
    )
  ```

- 备注

  ```python
    # 在图表中为某个点添加备注。包含备注文本，备注箭头等图像的设置。
    mp.annotate(
        r'$\frac{\pi}{2}$',			#备注中显示的文本内容
        xycoords='data',			#备注目标点所使用的坐标系（data表示数据坐标系）
        xy=(x, y),	 				#备注目标点的坐标
        textcoords='offset points',	#备注文本所使用的坐标系（offset points表示参照点的偏移坐标系）
        xytext=(x, y),				#备注文本的坐标
        fontsize=14,				#备注文本的字体大小
        arrowprops=dict()			#使用字典定义文本指向目标点的箭头样式
    )
  ```

  

- 图形对象（图形窗口）

  - 手动构建 matplotlib 窗口

    ```python
    # 手动构建 matplotlib 窗口
    mp.figure(
        '',					#窗口标题栏文本 
        figsize=(4, 3),		#窗口大小 <元组>
        dpi=120,			#像素密度
    	facecolor=''		#图表背景色
    )
    mp.show()
    ```

  - 设置当前窗口的参数

    ```python
    # 设置图表标题 显示在图表上方
    mp.title(title, fontsize=12)
    # 设置水平轴的文本
    mp.xlabel(x_label_str, fontsize=12)
    # 设置垂直轴的文本
    mp.ylabel(y_label_str, fontsize=12)
    # 设置刻度参数   labelsize设置刻度字体大小
    mp.tick_params(..., labelsize=8, ...)
    # 设置图表网格线  linestyle设置网格线的样式
    	#	-  or solid 粗线
    	#   -- or dashed 虚线
    	#   -. or dashdot 点虚线
    	#   :  or dotted 点线
    mp.grid(linestyle='')
    # 设置紧凑布局
    mp.tight_layout() 
    ```

- 子图

  - 矩阵式布局
  - 网格式布局
  - 自由式布局

- 刻度定位器

  ```python
  # 获取当前坐标轴
  ax = mp.gca()
  # 设置水平坐标轴的主刻度定位器
  ax.xaxis.set_major_locator(mp.NullLocator())
  # 设置水平坐标轴的次刻度定位器为多点定位器，间隔0.1
  ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
  ```

- 刻度网格线

  ```python
  ax = mp.gca()
  #绘制刻度网格线
  ax.grid(
      which='',		# 'major'/'minor' <-> '主刻度'/'次刻度' 
      axis='',		# 'x'/'y'/'both' <-> 绘制x或y轴
      linewidth=1, 	# 线宽
      linestyle='', 	# 线型
      color='',		# 颜色
  	alpha=0.5		# 透明度
  )
  ```

- 半对数坐标 

  ```python
  mp.semilogy(y)
  ```

- 散点图

  ```python
  mp.scatter(
      x, 					# x轴坐标数组
      y,					# y轴坐标数组
      marker='', 			# 点型
      s=10,				# 大小
      color='',			# 颜色
      edgecolor='', 		# 边缘颜色
      facecolor='',		# 填充色
      zorder=''			# 图层序号
  )
  
  ```

- 正态分布随机数 

  ```python
  np.random.normal(期望, 标准差, 容量)
  
  ```

- 设置点的颜色

  ```python
  mp.scatter(x, y, c='red')			#直接设置颜色
  d = (x-172)**2 + (y-60)**2
  mp.scatter(x, y, c=d, cmap='jet')	#以c作为参数，取cmap颜色映射表中的颜色值
  
  ```


