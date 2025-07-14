import numpy as np

# 加减乘除
a = np.arange(9, dtype=np.float64).reshape(3, 3)
print(f'第一个数组：\n{a}')
b = np.array([10, 10, 10])
print(f'第二个数组：\n{b}')
print(f'两个数组相加：\n{np.add(a, b)}')
print(f'两个数组相减：\n{np.subtract(a, b)}')
print(f'两个数组相乘：\n{np.multiply(a, b)}')
print(f'两个数组相除：\n{np.divide(a, b)}')

# 倒数
a = np.array([0.25, 1.33, 1, 100])
print(f'\n原始数组为：{a}')
print(f'调用 reciprocal 函数：{np.reciprocal(a)}')

# 幂计算
a = np.array([10, 100, 1000])
print(f'\n我们的数组是：\n{a}')
print(f'调用 power 函数：\n{np.power(a, 2)}')
b = np.array([1, 2, 3])
print(f'第二个数组：\n{b}')
print(f'再次调用 power 函数：\n{np.power(a, b)}')

# 余数
a = np.array([10, 20, 30])
b = np.array([3, 5, 7])
print(f'\n第一个数组：{a}')
print(f'第二个数组：{b}')
print(f'调用 mod() 函数：\n{np.mod(a, b)}')
print(f'调用 remainder() 函数：\n{np.remainder(a, b)}')
