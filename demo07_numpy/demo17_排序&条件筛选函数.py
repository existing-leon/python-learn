import numpy as np

a = np.array([[3, 7], [9, 1]])
print(f'原始数组为：\n{a}')
print(f'调用 sort() 函数：\n{np.sort(a)}')
print(f'按列排序：\n{np.sort(a, axis=0)}')

# 在 sort 函数中排序字段
dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt)
print(f'\n我们的数组是：\n{a}')
print(f'按照 name 排序：\n{np.sort(a, order="name")}')

# 排序结果的索引
x = np.array([3, 1, 2])
print(f'\n原始数组为：{x}')
y = np.argsort(x)
print(f'对 x 调用 argsort() 函数：{y}')
print(f'以排序后的顺序重构原数组：{x[y]}')
print(f'使用循环重构原数组：')
for i in y:
    print(x[i], end=" ")

# 对多个序列进行排序
nm = ('raju', 'anil', 'ravi', 'amar')
dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
ind = np.lexsort((dv, nm))
print(f'\n\n调用 lexsort() 函数：{ind}')
print(f'使用这个索引来获取排序后的数据：')
print([nm[i] + "," + dv[i] for i in ind])

#
print(f'\n复数排序：{np.sort_complex([5, 3, 6, 2, 1])}')
a = np.array([3, 4, 2, 1])
# 将数组 a 中所有元素（包括重复元素）从小到大排列，3 表示的是排序数组索引为 3 的
# 数字，比该数字小的排在该数字前面，比该数字大的排在该数字的后面
print(f'分区排序：{np.partition(a, 3)}')
# 小于 1 的在前面，大于 3 的在后面，1和3之间的在中间
print(f'分区排序：{np.partition(a, (1, 3))}')

# 最大最小元素的索引
a = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
print(f'\n原始数组为：\n{a}')
print(f'调用 argmax() 函数：{np.argmax(a)}')
print(f'展开数组：{a.flatten()}')
maxindex = np.argmax(a, axis=0)
print(f'沿着轴 0 的最大值索引：{maxindex}')
maxindex = np.argmax(a, axis=1)
print(f'沿着轴 1 的最大值索引：{maxindex}')
minindex = np.argmin(a)
print(f'调用 argmin() 函数：{minindex}')
print(f'展开数组中的最小值：{a.flatten()[minindex]}')
minindex = np.argmin(a, axis=0)
print(f'沿着轴 0 的最小值索引：{minindex}')
minindex = np.argmin(a, axis=1)
print(f'沿着轴 1 的最小值索引：{minindex}')

# 非零索引
a = np.array([[30, 40, 0], [0, 20, 10], [50, 0, 60]])
print(f'\n原始数组为：\n{a}')
print(f'调用 nonzero() 函数：\n{np.nonzero(a)}')

# 给定条件的元素
x = np.arange(9.).reshape(3, 3)
print(f'\n原始数组为：\n{x}')
y = np.where(x > 3)
print(f'大于 3 的元素的索引：{y}')
print(f'使用这些索引来获取满足条件的元素：{x[y]}')

# 抽取
x = np.arange(9).reshape(3, 3)
print(f'\n原始数组为：\n{x}')
# 定义条件：选择偶数元素
condition = np.mod(x, 2) == 0
print(f'按元素的条件值：\n{condition}')
print(f'使用条件提取元素：\n{np.extract(condition, x)}')
