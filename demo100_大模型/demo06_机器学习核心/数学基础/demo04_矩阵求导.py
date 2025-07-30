import numpy as np

# 求梯度向量
f = np.array([1, 2, 4, 7, 11, 16], dtype=float)
print(f)

# 计算方式：比如 7 处的梯度为 (11 - 4) / 两处的索引差 2 = 3.5
# 如果是在两端的数据, 直接做差来减即可
print(np.gradient(f))
print()

# 求梯度矩阵
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)
print()
print(np.gradient(A))
