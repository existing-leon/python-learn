""""""
"""
Pandas提供了易于使用的数据结构和数据分析工具, 特别适合处理结构化数据, 如表格型数据(类似于 Excel 表格)

pandas兼具numpy高性能的数组计算功能以及电子表格和关系型数据库（如SQL）灵活的数据处理功能。

pandas功能：
	有标签轴的数据结构
在数据结构中，每个轴都被赋予了特定的标签，这些标签用于标识和引用轴上的数据元素，使得数据的组织、访问和操作更加直观和方便
	集成时间序列功能。
	相同的数据结构用于处理时间序列数据和非时间序列数据。
	保存元数据的算术运算和压缩。
	灵活处理缺失数据。
	合并和其它流行数据库（例如基于SQL的数据库）的关系操作。
"""

"""
Series 是 Pandas 中的一个核心数据结构，类似于一个一维的数组，具有数据和索引。
Series 可以存储任何数据类型（整数、浮点数、字符串等），并通过标签（索引）来访问元素。

Series特点：
	一维数组：Series 中的每个元素都有一个对应的索引值。
	索引： 每个数据元素都可以通过标签（索引）来访问，默认情况下索引是从 0 开始的整数，但你也可以自定义索引。
	数据类型： Series 可以容纳不同数据类型的元素，包括整数、浮点数、字符串、Python 对象等。
	大小不变性：Series 的大小在创建后是不变的，但可以通过某些操作（如 append 或 delete）来改变。
	操作：Series 支持各种操作，如数学运算、统计分析、字符串处理等。
	缺失数据：Series 可以包含缺失数据，Pandas 使用NaN（Not a Number）来表示缺失或无值。
	自动对齐：当对多个 Series 进行运算时，Pandas 会自动根据索引对齐数据，这使得数据处理更加高效。
"""

import pandas as pd

# 通过列表创建 Series
s = pd.Series([4, 7, -5, 3])
print(s, '\n')

# 通过列表创建 Series 时指定索引
s = pd.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'], name='hello_python')
print(s, '\n')

# 直接通过字典创建 Series
dic = {'a': 4, 'b': 7, 'c': -5, 'd': 3}
s = pd.Series(dic)
print(s, '\n')

# 可以通过 key 值指定来实现过滤功能
s1 = pd.Series(dic, index=['a', 'c'], name='aacc')
print(s1, '\n')

"""
Series的常用属性：
index	Series的索引对象
values	Series的值
ndim	Series的维度
shape	Series的形状
size	Series的元素个数
dtype或dtypes	Series的元素类型
name	Series的名称
loc[]	显式索引，按标签索引或切片
iloc[]	隐式索引，按位置索引或切片
at[]	使用标签访问单个元素
iat[]	使用位置访问单个元素
"""

arrs = pd.Series([11, 22, 33, 44, 55], name="xiaofeng", index=["a", "b", "c", "d", "e"])
print(arrs, '\n')
# index Series 的索引对象
print(arrs.index)
for i in arrs.index:
    print(i)

# values Series的值
print(arrs.values, '\n')
# ndim Series的维度
print(arrs.ndim, '\n')
# shape Series的形状
print(arrs.shape, '\n')
# size  Series的元素个数
print(arrs.size, '\n')
# dtype或dtypes  Series的元素类型
print(arrs.dtype, '\n')
print(arrs.dtypes, '\n')
# name  Series的名称
print(arrs.name, '\n')
# loc[] 显式索引，按标签索引或切片
print(arrs.loc["c"], '\n')
print(arrs.loc["c":"d"], '\n')
# iloc[]    隐式索引，按位置索引或切片
print(arrs.iloc[0], '\n')
print(arrs.iloc[0:3], '\n')
# at[]  使用标签访问单个元素
print(arrs.at["a"], '\n')
# iat[] 使用位置访问单个元素
print(arrs.iat[3], '\n')

print('-----------------------------')

"""
Series的常用方法：
head()	查看前n行数据，默认5行
tail()	查看后n行数据，默认5行
isin()	元素是否包含在参数集合中
isna()	元素是否为缺失值（通常为 NaN 或 None）
sum()	求和，会忽略 Series 中的缺失值
mean()	平均值
min()	最小值
max()	最大值
var()	方差
std()	标准差
median()	中位数
mode()	众数（出现频率最高的值），如果有多个值出现的频率相同且都是最高频率，这些值都会被包含在返回的 Series 中
quantile(q,interpolation)	指定位置的分位数
q的取值范围是 0 到 1 之间的浮点数或浮点数列表，如quantile(0.5)表示计算中位数（即第 50 百分位数）;
interpolation：指定在计算分位数时，如果分位数位置不在数据点上，采用的插值方法。默认值是线性插值 'linear'，还有其他可选值如 'lower'、'higher'、'midpoint'、'nearest' 等
describe()	常见统计信息
value_count()	每个元素的个数
count()	非缺失值元素的个数，如果要包含缺失值，用len()
drop_duplicates()	去重
unique()	去重后的数组
nunique()	去重后元素个数
sample()	随机采样
sort_index()	按索引排序
sort_values()	按值排序
replace()	用指定值代替原有值
to_frame()	将Series转换为DataFrame
equals()	判断两个Series是否相同
keys()	返回Series的索引对象
corr()	计算与另一个Series的相关系数 
默认使用皮尔逊相关系数（Pearson correlation coefficient）来计算相关性。要求参与比较的数组元素类型都是数值型。
当相关系数为 1 时，表示两个变量完全正相关，即一个变量增加，另一个变量也随之增加。
当相关系数为 -1 时，表示两个变量完全负相关，即一个变量增加，另一个变量随之减少。
当相关系数为 0 时，表示两个变量之间不存在线性相关性。
例如，分析某地区的气温和冰淇淋销量之间的关系
cov()	计算与另一个Series的协方差
hist()	绘制直方图，用于展示数据的分布情况。它将数据划分为若干个区间（也称为 “bins”），并统计每个区间内数据的频数。
需要安装matplotlib包
items()	获取索引名以及值
"""

import pandas as pd
import numpy as np

arrs = pd.Series([11, 22, np.nan, None, 44, 22], index=['a', 'b', 'c', 'd', 'e', 'f'])
# 查看前n行数据, 默认5行
print(arrs.head(), '\n')
# 查看后n行数据, 默认5行
print(arrs.tail(), '\n')
# 判断数组中的每一个元素是否包含在参数集合中
print(arrs.isin([11]), '\n')
# 判断元素是否为缺失值
print(arrs.isna(), '\n')
# sum() 求和, 会忽略 Series 中的缺失值
print(arrs.sum(), '\n')
# mean() 平均值
print(arrs.mean(), '\n')
# min() 最小值
print(arrs.min(), '\n')
# max() 最大值
print(arrs.max(), '\n')
# var() 方差
print(arrs.var(), '\n')
# std() 标准差
print(arrs.std(), '\n')
# print(arrs.var())
# median()  中位数
print(arrs.median(), '\n')
# mode()    众数
print('众数：', arrs.mode(), '\n')
# quantile()    指定位置的分位数，如quantile(0.5)
print('指定位置的分位数：', arrs.quantile(0.25, interpolation="midpoint"), '\n')

# describe()    常见统计信息
print(arrs.describe(), '\n')
# value_counts()    每个元素的个数
print(arrs.value_counts(), '\n')
# count()   非缺失值元素的个数
print('非缺失值元素的个数：', arrs.count(), '\n')
print(len(arrs), '\n')

# drop_duplicates() 去重  这里可以看出，底层None也作为NaN处理
print(arrs.drop_duplicates(), '\n')
# unique()  去重后的数组
print(arrs.unique(), '\n')

# nunique() 去重后元素个数
print(arrs.nunique(), '\n')
# sample()  随机采样
print('sample()：', arrs.sample(), '\n')

# sort_index()  按索引排序
print('按索引排序\n', arrs.sort_index(), '\n')

# sort_values() 按值排序
print('按值排序\n', arrs.sort_values(), '\n')
# replace() 用指定值代替原有值
print('用指定值代替原有值\n', arrs.replace(22, "haha"), '\n')

# to_frame()    将Series转换为DataFrame
print('将Series转换为DataFrame\n', arrs.to_frame(), '\n')

# equals()  判断两个Series是否相同
arr1 = pd.Series([1, 2, 3])
arr2 = pd.Series([1, 2, 3])
print(arr1.equals(arr2), '\n')
# keys()    返回Series的索引对象
print('返回Series的索引对象\n', arrs.index, '\n')
print('返回Series的索引对象\n', arrs.keys(), '\n')
# corr()    计算与另一个Series的相关系数
arr3 = pd.Series([3, 2, 1])
arr4 = pd.Series([6, 7, 8])
arr5 = pd.Series([1, -1, 1, -1])
arr6 = pd.Series([1, 1, -1, -1])
print('计算与另一个Series的相关系数\n', arr1.corr(arr2), '\n')
print('计算与另一个Series的相关系数\n', arr1.corr(arr3), '\n')
print('计算与另一个Series的相关系数\n', arr1.corr(arr4), '\n')
print('计算与另一个Series的相关系数\n', arr5.corr(arr6), '\n')

# cov() 计算与另一个Series的协方差
print('计算与另一个Series的协方差\n', arr1.corr(arr3), '\n')

# hist()    绘制直方图
arr7 = pd.Series([3, 2, 1, 1, 1, 2, 2])
# 绘制直方图
arr7.hist(bins=3)
# items()   获取索引名以及值
for i, v in arr7.items():
    print(i, v)
print('-' * 10)

"""
可以使用布尔索引从Series中筛选满足某些条件的值。
"""
s = pd.Series({"a": -1.2, "b": 3.5, "c": 6.8, "d": 2.9})
bools = s > s.mean()  # 将大于平均值的元素标记为 True
print(bools, '\n')
print(s[bools], '\n')

"""
标量会与每个元素进行计算。
"""
s = pd.Series({"a": -1.2, "b": 3.5, "c": 6.8, "d": 2.9})
print(s * 10, '\n')

"""
会根据标签索引进行对位计算，索引没有匹配上的会用NaN填充。
"""
s1 = pd.Series([1, 1, 1, 1])
s2 = pd.Series([2, 2, 2, 2], index=[1, 2, 3, 4])
print(s1 + s2, '\n')
