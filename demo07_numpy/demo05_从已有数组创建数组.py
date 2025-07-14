import numpy as np

# 将列表转换为 ndarray
x = [1, 2, 3]
a = np.asarray(x)
print(a)

# 将元组转换为 ndarray
x = (1, 2, 3)
a = np.asarray(x)
print(a)

# 将元组列表转换为 ndarray
x = [(1, 2, 3), (4, 5, 6)]
a = np.asarray(x)
print(a)

# 设置 dtype 参数
x = [1, 2, 3]
a = np.asarray(x, dtype=float)
print(a)

#
s = b'Hello World'
a = np.frombuffer(s, dtype='S1')
print(a)

# 使用 range 函数创建列表对象
list = range(5)
it = iter(list)
# 使用迭代器创建 ndarray
x = np.fromiter(it, dtype=float)
print(x)
