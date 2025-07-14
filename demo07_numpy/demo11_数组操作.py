import numpy as np

# 修改数组形状
a = np.arange(8)
print(f'原始数组：{a}')
b = a.reshape(4, 2)
print(f'修改后的数组：\n {b}')

# 数组元素迭代器
a = np.arange(9).reshape(3, 3)
print('\n 原始数组：')
for row in a:
    print(row)

# 对数组中每个元素都进行处理, 可以使用flat属性, 该属性是一个数组元素迭代器
print('迭代后的数组：')
for element in a.flat:
    print(element)

# 数组拷贝
a = np.arange(8).reshape(2, 4)
print(f'\n 原数组：\n {a}')
print(f'展开的数组：{a.flatten()}')
print(f'以 F 风格顺序展开的数组：{a.flatten(order="F")}')

# 展平
a = np.arange(8).reshape(2, 4)
print(f'\n 原数组：\n {a}')
print(f'调用 ravel 函数之后：\n {a.ravel()}')
print(f'以 F 风格顺序调用 ravel() 函数之后：\n {a.ravel(order="F")}')

# 翻转数组
a = np.arange(12).reshape(3, 4)
print(f'\n原数组：{a}')
print(f'对换数组：\n {a.transpose()}')

a = np.arange(12).reshape(3, 4)
print(f'\n原数组：{a}')
print(f'转置数组：\n {a.T}')

## 滚动
# 创建一个三维数组
a = np.arange(8).reshape(2, 2, 2)
print(f'\n原始数组：\n{a}')
print(f'获取数组中的一个值的索引：{np.where(a == 6)}')
print(f'根据索引反查数组中的值：{a[1, 1, 0]}')

# 将轴 2 滚动到轴 0 （宽度到深度）
b = np.rollaxis(a, 2, 0)
print(f'调用 rollaxis 函数：\n {b}')
# 查看元素 a[1,1,0], 即 6 的坐标, 变成 [0,1,1]
print(np.where(b == 6))

# 将轴 2 滚动到轴 1 :（宽度到高度）
c = np.rollaxis(a, 2, 1)
print(f'调用 rollaxis 函数：\n {c}')
# 查看元素 a[1,1,0], 即 6 的坐标, 变成 [1,0,1]
print(np.where(c == 6))

## 交换数组的两个轴
# 创建一个三维的 ndarray
a = np.arange(8).reshape(2, 2, 2)
print(f'\n原数组：{a}')
# 交换轴 0 （深度方向）到轴 2 （宽度方向）
print(f'\n调用 swapaxes 函数后的数组：{np.swapaxes(a, 2, 0)}')

## 修改数组的维度
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])

# 对 y 广播 x
b = np.broadcast(x, y)
# 它拥有 iterator 属性, 基于自身组件的迭代器元组

print(f'\n对 y 广播 x：')
r, c = b.iters

print(next(r), next(c))
print(next(r), next(c))
print()

# shape 属性返回广播对象的形状
print(f'广播对象的形状：{b.shape}')

# 手动使用 broadcast 将 x 与 y 相加
b = np.broadcast(x, y)
c = np.empty(b.shape)
print(f'\n手动使用 broadcast 将 x 与 y 相加 {c.shape}')
c.flat = [u + v for (u, v) in b]
print(f'调用 flat 函数：\n{c}')

# 获得了和 Numpy 内建的广播支持相同的结果
print(f'\nx 和 y 的和：\n{x + y}')

a = np.arange(4).reshape(1, 4)
print(f'\n原数组：{a}')
print(f'调用 broadcast_to 函数之后：\n{np.broadcast_to(a, (4, 4))}')

# 扩展
x = np.arange(1, 5).reshape(2, 2)
print(f'\n 数组x：\n{x}')
y = np.expand_dims(x, axis=0)
print(f'\n 数组y：\n{y}')
print(f'\n数组 x 和 y 的形状：{x.shape}, {y.shape}')
# 在位置 1 插入轴
y = np.expand_dims(x, axis=1)
print(f'\n在位置 1 插入轴之后的数组 y：\n{y}')
print(f'x.ndim 和 y.ndim：{x.ndim}, {y.ndim}')
print(f'x.shape 和 y.shape：{x.shape}, {y.shape}')

# 删除
x = np.arange(9).reshape(1, 3, 3)
print(f'\n数组 x：\n{x}')
y = np.squeeze(x)
print(f'数组 y：\n{y}')
print(f'数组 x 和 y 的形状：{x.shape}, {y.shape}')

# 连接数组
a = np.array([[1, 2], [3, 4]])
print(f'\n第一个数组：\n{a}')
b = np.array([[5, 6], [7, 8]])
print(f'第二个数组：\n{b}')
# 两个数组的维度相同
print(f'沿轴 0 连接两个数组：\n{np.concatenate((a, b))}')
print(f'沿轴 1 连接两个数组：\n{np.concatenate((a, b), axis=1)}')

a = np.array([[1, 2], [3, 4]])
print(f'第一个数组：\n{a}')
b = np.array([[5, 6], [7, 8]])
print(f'第二个数组：\n{b}')
print(f'沿轴 0 堆叠两个数组：\n{np.stack((a, b), 0)}')

a = np.array([[1, 2], [3, 4]])
print(f'第一个数组：\n{a}')
b = np.array([[5, 6], [7, 8]])
print(f'第二个数组：\n{b}')
print(f'水平堆叠：\n{np.hstack((a, b))}')

a = np.array([[1, 2], [3, 4]])
print(f'第一个数组：\n{a}')
b = np.array([[5, 6], [7, 8]])
print(f'第二个数组：\n{b}')
print(f'竖直堆叠：\n{np.vstack((a, b))}')

## 分割数组
a = np.arange(9)
print(f'\n第一个数组：\n{a}')
b = np.split(a, 3)
print(f'将数组分为三个大小相等的子数组：\n{b}')
b = np.split(a, [4, 7])
print(f'将数组在一维数组中表明的位置分割：\n{b}')

# axis为0时在水平方向分割, axis为1时在垂直方向分割
a = np.arange(16).reshape(4, 4)
print(f'\n第一个数组：\n{a}')
b = np.split(a, 2)
print(f'默认分割（0轴）：\n{b}')
c = np.split(a, 2, 1)
print(f'沿水平方向分割：\n{c}')
d = np.hsplit(a, 2)
print(f'沿水平方向分割：\n{d}')

# numpy.hsplit 函数用于水平分割数组，通过指定要返回的相同形状的数组数量来拆分原数组。
harr = np.floor(10 * np.random.random((2, 6)))
print(f'\n原始array：\n{harr}')
print(f'拆分后：\n{np.hsplit(harr, 3)}')

# numpy.vsplit 沿着垂直轴分割，其分割方式与hsplit用法相同。
a = np.arange(16).reshape(4, 4)
print(f'\n第一个数组：\n{a}')
b = np.vsplit(a, 2)
print(f'竖直分割：\n{b}')

## 数组元素的添加与删除
a = np.array([[1, 2, 3], [4, 5, 6]])
print(f'\n 第一个数组：\n{a}')
print(f'第一个数组的形状：{a.shape}')
b = np.resize(a, (3, 2))
print(f'第二个数组：\n{b}')
print(f'第二个数组的形状：{b.shape}')
b = np.resize(a, (3, 3))
print(f'修改后第二个数组的大小：\n{b}')

# append
a = np.array([[1, 2, 3], [4, 5, 6]])
print(f'\n第一个数组：\n{a}')
print(f'向数组中添加元素：\n{np.append(a, [7, 8, 9])}')
print(f'沿轴 0 添加元素：\n{np.append(a, [[7, 8, 9]], axis=0)}')
print(f'沿轴 1 添加元素：\n{np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1)}')

# insert
a = np.array([[1, 2], [3, 4], [5, 6]])
print(f'\n第一个数组：\n{a}')
print(f'未传递 axis 参数, 在删除之前输入数组会被展开：\n{np.insert(a, 3, [11, 12])}')
print('传递了 axis 参数, 会广播值数组来匹配输入数组')
print(f'沿轴 0 来广播：\n{np.insert(a, 1, [11], axis=0)}')
print(f'沿轴 1 来广播：\n{np.insert(a, 1, [11], axis=1)}')
