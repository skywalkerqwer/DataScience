"""
轴向汇总
"""
import numpy as np

data = np.arange(1, 13).reshape(3, 4)
print(data)


def func(ary):
    return np.mean(ary)


re = np.apply_along_axis(
    func1d=func,  # 接收一维数组的函数
    axis=1,  # 轴向
    arr=data,  # ndarry数组
)
print(re)
