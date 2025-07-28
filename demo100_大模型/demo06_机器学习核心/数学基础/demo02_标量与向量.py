import numpy as np

x = np.array([2, 5, 8])
print(x)
print(x.shape)

print(x.T)
print(x.T.shape)

y = np.array([1, 3, 7])
print(x + y)

print(x * 3)

# 向量对应元素相乘
print(x * y)

# 计算向量点积
print(x.dot(y))

print(x @ y)

print('------------------------------')

# 求向量范数
print(x)
l0_norm = np.linalg.norm(x, ord=0)
print(f'l0_norm ==> {l0_norm}')

l1_norm = np.linalg.norm(x, ord=1)
print(f'l1_norm ==> {l1_norm}')
