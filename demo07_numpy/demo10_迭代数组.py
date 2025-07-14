import numpy as np

a = np.arange(6).reshape(2, 3)
print(f'原始数组是：\n {a} \n')
print('迭代输出元素：')
for x in np.nditer(a):
    print(x, end=', ')
print('\n')

a = np.arange(6).reshape(2, 3)
for x in np.nditer(a.T):
    print(x, end=', ')
print('\n')

for x in np.nditer(a.T.copy(order='C')):
    print(x, end=', ')
print('\n')

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print(f'原始数组是：\n {a} \n')
b = a.T
print(f'原始数组的转置是：\n {b} \n')
c = b.copy(order='C')
print('以 C 风格顺序排序：')
c = b.copy(order='C')
print(c)
for x in np.nditer(c):
    print(x, end=", ")
print('\n')
print('以 F 风格顺序排序：')
c = b.copy(order='F')
print(c)
for x in np.nditer(c):
    print(x, end=", ")

# 显式设置
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print(f'\n\n 原始数组是：\n {a} ')
print('以 C 风格顺序排序：')
for x in np.nditer(a, order='C'):
    print(x, end=", ")
print('\n')
print('以 F 风格顺序排序：')
for x in np.nditer(a, order='F'):
    print(x, end=", ")

# 修改数组中元素的值
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print(f'\n\n 原始数组是：\n {a}')
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x
print(f'修改后的数组是：\n {a}')

# 使用外部循环
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print(f'\n 原始数组是：\n {a}')
print('修改后的数组是：')
for x in np.nditer(a, flags=['external_loop'], order='F'):
    print(x, end=', ')

# 广播迭代
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print(f'\n\n第一个数组为：\n {a} ')
b = np.array([1, 2, 3, 4], dtype=int)
print(f'第二个数组为：{b}\n')
print('修改后的数组：')
for x, y in np.nditer([a, b]):
    print(f'{x}:{y}', end=", ")
