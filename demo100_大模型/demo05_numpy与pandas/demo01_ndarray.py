""""""
"""
ndarray属性案例
"""
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.ndim)  # 维度
print(a.shape)  # 形状
print(a.size)  # 元素个数
print(a.dtype)  # 数据类型
print(a.itemsize)  # 每个元素字节数大小

print()

"""
ndarray的创建方式
"""
"""
array()：将输入数据转换为 ndarray, 会进行 copy
asarray()：将输入数据转换为 ndarray, 如果输入本身是 ndarray, 则不会进行 copy
"""
data = [1, 2, 3]
print(f'元数据地址为：{id(data)}')
arr = np.array(data)
print(f'arr1地址为：{id(arr)}')
print(f'数组数据为：{arr}')

print('-' * 20)
arr2 = np.array(arr)
print(f'arr2地址为：{id(arr2)}')
print(f'arr2数组数据为：{arr2}')

print("-" * 20)
arr3 = np.asarray(arr)
print(f"arr3地址为:{id(arr3)}")
print(f"arr3数组数据为:{arr3}")

print("-" * 20)
arr4 = np.asarray(arr3)
print(f"arr4地址为:{id(arr4)}")
print(f"arr4数组数据为:{arr4}")

print()

"""
zeros()：返回给定形状和类型的新数组，用0填充。
ones()：返回给定形状和类型的新数组，用1填充。
empty()：返回给定形状和类型的未初始化的新数组。
需要注意的是，np.empty 并不保证数组元素被初始化为 0，它只是分配内存空间，数组中的元素值是未初始化的，可能是内存中的任意值。
上述3个方法创建的数组元素类型默认都是float64。
zeros_like()：返回与给定数组具有相同形状和类型的0新数组。
ones_like()：返回与给定数组具有相同形状和类型的1新数组。
empty_like()：返回与给定数组具有相同形状和类型的未初始化的新数组。
"""
arr1 = np.zeros((2, 5))  # 创建全0数组
print(arr1)

arr2 = np.ones_like(arr1)  # 创建喝 arr1 形状相同的全 1 数组
print(arr2)

arr3 = np.empty((2, 3))  # 创建未初始化的数组
print(arr3)

arr4 = np.empty_like(arr3)  # 创建和 arr3 形状相同的未初始化的数组
print(arr4)

print()

"""
full()：返回给定形状和类型的新数组，用指定的值填充。
full_like()：返回与给定数组具有相同形状和类型的用指定值填充的新数组。
"""
arr1 = np.full((2, 3), 6)
print(arr1)

arr2 = np.full_like(arr1, 5)
print(arr2)

print()

"""
arange()：返回在给定范围内用均匀间隔的值填充的一维数组。
"""
arr1 = np.arange(0, 10, 2)
print(arr1)

"""
linspace()：返回指定范围和元素个数的等差数列。数组元素类型为浮点型。
logspace()：返回指定指数范围、元素个数、底数的等比数列。
"""
arr1 = np.linspace(start=0, stop=10, num=5)
print(arr1)

# endpoint=False 表示不包括stop
arr2 = np.linspace(start=0, stop=10, num=5, endpoint=False)
print(arr2)

arr3 = np.logspace(start=2, stop=5, num=5, base=2)
print(arr3)

print()

"""
创建随机数组
random.rand()：返回给定形状的数组，用 [0, 1) 上均匀分布的随机样本填充。
random.randint()：返回给定形状的数组，用从低位(包含)到高位(不包含)上均匀分布的随机整数填充。
random.uniform()：返回给定形状的数组，用从低位(包含)到高位(不包含)上均匀分布的随机浮点数填充。
random.randn()：返回给定形状的数组，用标准正态分布(均值为0，标准差为1)的随机样本填充。
"""
arr1 = np.random.rand(2, 3)
print(arr1)

arr2 = np.random.randint(0, 10, (2, 3))
print(arr2)

arr3 = np.random.uniform(3, 6, (2, 3))
print(arr3)

arr4 = np.random.randn(2, 3)
print(arr4)

print()

"""
matrix为ndarray的子类，只能生成二维的矩阵。
"""
arr1 = np.matrix("1 2; 3 4")
print(arr1)

arr2 = np.matrix([[1, 2], [3, 4]])
print(arr2)

print()

"""
创建数组时可以使用dtype参数指定元素类型
"""
arr1 = np.array([1, 2, 3], dtype=np.float64)
print(arr1)

arr2 = np.array([0.2, 2.5, 4.8], dtype='i8')
print(arr2)

print()

# 可以使用 ndarray.astype() 方法转换数组的元素类型
arr1 = np.array([1, 2, 3], dtype=np.float64)
print(arr1)

arr2 = arr1.astype(np.int64)
print(arr2)

print()

"""
切片和索引
"""
arr = np.arange(10)
print(arr)

# 获取索引为2的数据
print(arr[2])

# 从索引2开始到索引9(不包含)停止, 间隔为2
print(arr[slice(2, 9, 2)])

# 从索引2开始到索引9(不包含)停止, 间隔为2
print(arr[2:9:2])

# 从索引2开始到最后(不包含), 默认间隔为1
print(arr[2:])

# 从索引2开始到索引9(不包含)结束, 默认间隔为1
print(arr[2:9])
print()

"""
基本函数
np.abs()	元素的绝对值，参数是 number 或 array
np.ceil()	向上取整，参数是 number 或 array
np.floor()	向下取整，参数是 number 或 array
np.rint()	四舍五入，参数是 number 或 array
np.isnan()	判断元素是否为NaN(Not a Number) ，参数是 number 或 array
np.multiply()	元素相乘，参数是 number 或 array。如果第二个参数传递的是number，原数组中所有元素乘以这个数字，返回新的数组；如果第二个参数也是一个数组，是将两个数组中对应位置的元素相乘，返回一个新的数组，其形状与输入数组相同。
np.divide()	元素相除，参数是 number 或 array
np.where(condition, x, y)	三元运算符，x if condition else y
"""
arr1 = np.random.randn(2, 3)
print(arr1)

print(np.abs(arr1))
print(np.ceil(arr1))
print(np.floor(arr1))
print(np.rint(arr1))
print(np.isnan(arr1))
print(np.multiply(arr1, 2))
print(np.divide(arr1, arr1))
print(np.where(arr1 > 0, 1, 0))

print()

"""
统计函数：
np.mean()	所有元素的平均值
np.sum()	所有元素的和
np.max()	所有元素的最大值
np.min()	所有元素的最小值
np.std()	所有元素的标准差
np.var()	所有元素的方差
np.argmax()	最大值的下标索引值
np.argmin()	最小值的下标索引值
np.cumsum()	返回一个一维数组，每个元素都是之前所有元素的累加和
np.cumprod()	返回一个一维数组，每个元素都是之前所有元素的累乘积
"""

arr1 = np.random.randint(1, 5, (2, 3))
print(arr1)
print(np.mean(arr1))
print(np.sum(arr1))
print(np.max(arr1))
print(np.min(arr1))
print(np.std(arr1))
print(np.var(arr1))
print(np.argmax(arr1))
print(np.argmin(arr1))
print(np.cumsum(arr1))
print(np.cumprod(arr1))
print(np.cumprod(arr1, axis=1))
print()

"""
比较函数
np.any()	至少有一个元素满足指定条件，就返回True
np.all()	所有的元素都满足指定条件，才返回True
"""
arr1 = np.array([1, 2, 3, 4, 5])
print(np.any(arr1 > 3))
print(np.all(arr1 > 3))
print()

"""
排序函数：
ndarray.sort()：就地排序（直接修改原数组）。
axis：指定排序的轴。默认值为 -1，表示沿着最后一个轴进行排序。在二维数组中，axis = 0 表示按列排序，axis = 1 表示按行排序。
在 NumPy 中，轴是对数组维度的一种抽象描述。对于多维数组，每个维度都对应一个轴，轴的编号从 0 开始。对于二维数组，它有两个轴：
轴 0：代表垂直方向，也就是行的方向。可以把二维数组想象成一个表格，轴 0 就像是表格中从上到下的行索引方向对列数据排序，所以axis=0表示按列排序。
轴 1：代表水平方向，也就是列的方向。就像是表格中从左到右的列索引方向对行数据进行排序，所以axis=1表示按行排序。
"""
arr1 = np.random.randint(0, 10, (3, 3))
print(arr1)
print('-' * 10)
arr1.sort()
print(arr1)
print('-' * 10)
arr1.sort(axis=0)
print(arr1)
print()

"""
np.sort()：返回排序后的副本（创建新的数组）。
"""
arr1 = np.random.randint(0, 10, (3, 3))
print(arr1)
print(np.sort(arr1))
print()

"""
去重函数：
np.unique()：计算唯一值并返回有序结果。
"""
arr1 = np.random.randint(0, 5, (3, 3))
print(arr1)
print(np.unique(arr1))
print()

"""
基本运算：
numpy中的数组不用编写循环即可执行批量运算，称之为矢量化运算。
大小相等的数组之间的任何算术运算都会将运算应用到元素级。
"""
print('基本运算：')
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print()

"""
数组与标量的算术运算会将标量值传播到各个元素, 不同大小的数组之间的运算叫做广播
"""
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1 + 100)
print(arr1 - 100)
print(arr1 * 100)
print(arr1 / 100)
print()

"""
广播机制是 NumPy 中一个强大的特性，它允许在不同形状的数组之间进行元素级运算。广播机制的规则如下：
	规则1：如果俩个数组的维度数不相同，那么小维度数组的形状将会在最左边补1
"""
# 一维数组
arr1 = np.array([1, 2, 3])  # 形状为 (3,)
# 二维数组
arr2 = np.array([[4], [5], [6]])  # 形状为 (3, 1)
# print(np.shape(arr2))
# 对 arr1 应用规则 1，在其形状最左边补 1，变为 (1, 3)  [[1,2,3]]
# 此时 arr1 形状 (1, 3) 和 arr2 形状 (3, 1) 满足广播条件
result = arr1 + arr2
print("规则 1 示例结果：\n", result)
print()

"""
	规则2：如果俩个数组的形状在任何一个维度上都不匹配，那么数组的形状会沿着维度大
小（元素个数）为1的维度开始扩展 ，（维度必须是1开始）直到所有维度都一样， 以匹配另一个数组的形状。
"""
# 二维数组
arr3 = np.array([[1, 2, 3]])  # 形状为 (1, 3)
# 二维数组
arr4 = np.array([[4], [5], [6]])  # 形状为 (3, 1)

# arr3 沿着第0个维度扩展,将原有的一行数据复制成3行,为 (3, 3)=>[[1,2,3], [1,2,3], [1,2,3]]
# arr4 沿着第1个维度扩展, (3, 3)=>[[4,4,4], [5,5,5], [6,6,6]]
result = arr3 + arr4
print("规则 2 示例结果：\n", result)
print()

"""
	规则3：如果俩个数组的形状在任何一个维度上都不匹配，并且没有任何一个维度大小等于1，那么会引发异。
"""
# 一维数组
arr5 = np.array([1, 2, 3])  # 形状为 (3,)
# 一维数组
arr6 = np.array([4, 5])  # 形状为 (2,)
try:
    result = arr5 + arr6
    print(result)
except ValueError as e:
    print(f"规则 3 示例错误信息：{e}")

print()

"""
矩阵乘法：
通过*运算符和np.multiply()对两个数组相乘进行的是对位乘法而非矩阵乘法运算。
"""
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[6, 5, 4], [3, 2, 1]])
print(arr1 * arr2)
print(np.multiply(arr1, arr2))
print()

"""
使用np.dot()、ndarray.dot()、@可以进行矩阵乘法运算。

矩阵乘法的规则是：结果矩阵中第 i 行第 j 列的元素等于第一个矩阵的第 i 行与第二个矩阵的第 j 列对应元素乘积之和。
	结果矩阵第一行第一列的元素：
计算 arr1 的第一行 [1, 2, 3] 与 arr2 的第一列 [6, 4, 2] 对应元素乘积之和，即 1*6 + 2*4 + 3*2 = 6 + 8 + 6 = 20。
	结果矩阵第一行第二列的元素：
计算 arr1 的第一行 [1, 2, 3] 与 arr2 的第二列 [5, 3, 1] 对应元素乘积之和，即 1*5 + 2*3 + 3*1 = 5 + 6 + 3 = 14。
	结果矩阵第二行第一列的元素：
计算 arr1 的第二行 [4, 5, 6] 与 arr2 的第一列 [6, 4, 2] 对应元素乘积之和，即 4*6 + 5*4 + 6*2 = 24 + 20 + 12 = 56。
	结果矩阵第二行第二列的元素：
计算 arr1 的第二行 [4, 5, 6] 与 arr2 的第二列 [5, 3, 1] 对应元素乘积之和，即 4*5 + 5*3 + 6*1 = 20 + 15 + 6 = 41。
所以，手动计算得到的结果矩阵是 [[20, 14], [56, 41]]。

"""
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[6, 5], [4, 3], [2, 1]])
# 对于矩阵乘法来说，要求第一个矩阵的列数等于第二个矩阵的行数
print(arr1)
print(arr2)
print('-' * 10)
print(arr1.shape, arr2.shape)
print('-' * 10)
print(np.dot(arr1, arr2))
print('-' * 10)
print(arr1.dot(arr2))
print('-' * 10)
print(arr1 @ arr2)
print('-' * 10)
# 一个二维数组跟一个大小合适的一维数组的矩阵点积运算之后将会得到一个一维数组
arr3 = np.array([6, 5, 4])
print(arr1 @ arr3)
