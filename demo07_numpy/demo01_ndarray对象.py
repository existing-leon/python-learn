import numpy as np

# 只有一个维度
a = np.array([1, 2, 3])
print(a)

print()

# 多余1个维度
b = np.array([[1, 2], [3, 4]])
print(b)

print()

# 最小维度
c = np.array([1, 2, 3, 4, 5], ndmin=2)
print(c)

print()

# dtype参数
d = np.array([1, 2], dtype=complex)
print(d)

'''
ndarray 对象由计算机内存的连续一维部分组成，并结合索引模式，将每个元素映射到内存块中的一个位置。内存块以行顺序(C样式)或列顺序(FORTRAN或MatLab风格，即前述的F样式)来保存元素。
'''
