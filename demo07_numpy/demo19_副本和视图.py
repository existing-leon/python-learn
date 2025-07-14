import numpy as np

a = np.arange(6)
print(f'原始数组为：\n{a}')
print(f'调用 id() 函数：{id(a)}')
b = a
print(f'b 数组为：\n{b}')
# 根据结果可以看出, b 拥有和 a 相同的 id()
print(f'b 数组调用 id() 函数：{id(b)}')
# 修改 b 的形状
b.shape = 3, 2
print(f'当前 b 数组为：\n{b}')
print(f'当前 a 数组为：\n{a}')

# 定义一个 3 * 2 的数组
a = np.arange(6).reshape(3, 2)
print(f'\n原始数组为：\n{a}')
# 创建 a 的视图
b = a.view()
print(f'b 数组为：\n{b}')
# 比较两个数组的 id()
print(f'a 数组调用 id() 函数：{id(a)}')
print(f'b 数组调用 id() 函数：{id(b)}')
# 修改 b 的形状, 并不会修改 a
b.shape = 2, 3
print(f'b 的形状：\n{b}')
print(f'a 的形状：\n{a}')

# 切片视图
arr = np.arange(12)
print(f'\n原始数组：\n{arr}')
# 创建切片
a = arr[3:]
b = arr[3:]
a[1] = 123
b[2] = 234
print(arr)
print(id(a), id(b), id(arr[3:]))

# 副本和深拷贝
a = np.array([[10, 10], [2, 3], [4, 5]])
print(f'\n原始数组：\n{a}')
# 创建 a 的深层拷贝
b = a.copy()
print(f'b 数组为：\n{b}')
# b 与 a 不共享任何内容
print(b is a)  # False
# 修改 b 的内容
b[0, 0] = 100
print(f'修改 b 后 b 数组为：\n{b}')
print(f'修改 b 后 a 数组为：\n{a}')
