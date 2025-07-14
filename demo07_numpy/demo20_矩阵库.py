import numpy as np
import numpy.matlib

# 转置矩阵
a = np.arange(12).reshape(3, 4)
print(f'原始数组为：\n{a}')
print(f'转置数组为：\n{a.T}')

# matlib
# 初始化的时候, 里面的数据是随机填充的
print(np.matlib.empty((2, 2)))
print()

print(np.matlib.zeros((2, 2)))
print()

print(np.matlib.ones((2, 2)))
print()

print(np.matlib.eye(n=3, M=4, k=0, dtype=float))
print()

# 大小为 5, 类型为浮点数类型
print(np.matlib.identity(5, dtype=float))
print()

print(np.matlib.rand(3, 3))
print()
