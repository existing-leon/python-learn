import numpy as np

# 沿指定轴的最大最小值
a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print(f'原始数组为：\n{a}')
print(f'调用 amin() 函数：{np.amin(a, 1)}')
print(f'再次调用 amin() 函数：{np.amin(a, 0)}')
print(f'调用 amax() 函数：{np.amax(a)}')
print(f'再次调用 amax() 函数：{np.amax(a, axis=0)}')

# 最大与最小值的差
a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print(f'\n我们的数组是：\n{a}')
print(f'调用 ptp() 函数：{np.ptp(a)}')
print(f'沿轴 1 调用 ptp() 函数：{np.ptp(a, axis=1)}')
print(f'沿轴 0 调用 ptp() 函数：{np.ptp(a, axis=0)}')

# 百分位数
a = np.array([[10, 7, 4], [3, 2, 1]])
print(f'\n我们的数组是：\n{a}')
# 50% 的分位数, 就是 a 里排序之后的中位数
print(f'调用 percentile() 函数：{np.percentile(a, 50)}')
# axis 为 0 , 在纵列上求
print(np.percentile(a, 50, axis=0))
# axis 为 1 , 在横列上秋
print(np.percentile(a, 50, axis=1))
# 保持维度不变
print(np.percentile(a, 50, axis=1, keepdims=True))

# 中位数
a = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])
print(f'\n原数组为：\n{a}')
print(f'调用 median() 函数：\n{np.median(a)}')
print(f'沿轴 0 调用 median() 函数：\n{np.median(a, axis=0)}')
print(f'沿轴 1 调用 median() 函数：\n{np.median(a, axis=1)}')

# 算术平均值
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(f'\n原数组为：\n{a}')
print(f'调用 mean() 函数：\n{np.mean(a)}')
print(f'沿轴 0 调用 mean() 函数：\n{np.mean(a, axis=0)}')
print(f'沿轴 1 调用 mean() 函数：\n{np.mean(a, axis=1)}')

# 加权平均数
a = np.array([1, 2, 3, 4])
print(f'\n原数组为：{a}')
# 不指定权重相当于 mean 函数
print(f'调用 average() 函数：{np.average(a)}')
wts = np.array([4, 3, 2, 1])
print(f'再次调用 average() 函数：{np.average(a, weights=wts)}')
# 如果 returned 参数设为 true, 则返回权重的和
print(f'权重的和：{np.average([1, 2, 3, 4], weights=[4, 3, 2, 1], returned=True)}')

# 标准差
print(f'\n标准差计算：{np.std([1, 2, 3, 4])}')

# 方差
print(f'\n方差计算：{np.var([1, 2, 3, 4])}')
