import numpy as np

products = np.array(['Apple', 'Huawei', 'Mi', 'Oppo', 'Vivo'])

prices = [8888, 5555, 1999, 2999, 2999]
volumns = np.array([100, 400, 150, 300, 260])

indices = np.lexsort((volumns,prices))  # 先对价格排序再对销量排序
print(indices)
