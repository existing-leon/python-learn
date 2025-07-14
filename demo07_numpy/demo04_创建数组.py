import numpy as np

# 注意 − 数组元素为随机值，因为它们未初始化。
x = np.empty([3, 2], dtype=int)
print(x)

print()

# 默认为浮点数
x = np.zeros(5)
print(x)
# 设置类型为整数
y = np.zeros((5,), dtype=int)
print(y)
# 自定义类型
z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4',)])
print(z)

print()

# 默认为浮点数
x = np.ones(5)
print(x)
# 自定义类型
x = np.ones([2, 2], dtype=int)
print(x)

print()

# 创建一个 3 * 3 的三维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 创建一个与 arr 形状相同的, 所有元素都为 0 的数组
zeros_arr = np.zeros_like(arr)
print(zeros_arr)

print()

# 创建一个 3 * 3 的三维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 创建一个与 arr 形状相同的, 所有元素都为 1 的数组
zeros_arr = np.ones_like(arr)
print(zeros_arr)
