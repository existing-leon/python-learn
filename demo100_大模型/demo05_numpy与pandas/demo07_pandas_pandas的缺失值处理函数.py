""""""
"""
pandas使用浮点值NaN（Not a Number）表示缺失数据，使用NA（Not Available）表示缺失值。可以通过isnull()、isna()或notnull()、notna()方法判断某个值是否为缺失值。
Nan通常表示一个无效的或未定义的数字值，是浮点数的一种特殊取值，用于表示那些不能表示为正常数字的情况，如 0/0、∞-∞等数学运算的结果。nan与任何值（包括它自身）进行比较的结果都为False。例如在 Python 中，nan == nan返回False。
NA一般用于表示数据不可用或缺失的情况，它的含义更侧重于数据在某种上下文中是缺失或不存在的，不一定特指数字类型的缺失。
na和nan都用于表示缺失值，但nan更强调是数值计算中的特殊值，而na更强调数据的可用性或存在性。
"""
import pandas as pd
import numpy as np

s = pd.Series([np.nan, None, pd.NA])
print(s)
print()
print(s.isnull())
print()

# 加载数据中包含缺失值
df = pd.read_csv('data/weather_withna.csv')
print(df.tail(5))
print()

# 可以通过 keep_default_na 参数设置是否将空白值设置为缺失值
df = pd.read_csv('data/weather_withna.csv', keep_default_na=False)
print(df.tail(5))
print()

# 可以通过 na_values 参数将指定值设置为缺失值
df = pd.read_csv('data/weather_withna.csv', na_values=['2015-12-31'])
print(df.tail(5))
print()

# 查看缺失值
# 1）通过 isnull() 查看缺失值数量
df = pd.read_csv('data/weather_withna.csv')
print(df.isnull().sum())
print()

# 2）通过missingno条形图展示缺失值
# 先安装missingno包：pip install missingno
import missingno as msno
import matplotlib

matplotlib.use('TkAgg')  # 或 'Qt5Agg', 'Agg'（Agg 无窗口，用于保存图像）
import matplotlib.pyplot as plt

df = pd.read_csv('data/weather_withna.csv')
msno.bar(df)

# 需要添加这个才能显示
# plt.show()

msno.heatmap(df)
# plt.show()

"""
3.7.4 剔除缺失值
通过dropna()方法来剔除缺失值。
"""
# 1）Series 剔除缺失值
s = pd.Series([1, pd.NA, None])
print(s)
print()
print(s.dropna())
print()

# 2）DataFrame剔除缺失值
# 无法从DataFrame中单独剔除一个值，只能剔除缺失值所在的整行或整列。
# 默认情况下，dropna()会剔除任何包含缺失值的整行数据。
df = pd.DataFrame([[1, pd.NA, 2], [2, 3, 5], [pd.NA, 4, 6]])
print(df)
print()
print(df.dropna())
print()

# 可以设置按不同的坐标轴剔除缺失值，比如axis=1（或 axis='columns'）会剔除任何包含缺失值的整列数据。
df = pd.DataFrame([[1, pd.NA, 2], [2, 3, 5], [pd.NA, 4, 6]])
print(df)
print()
print(df.dropna(axis=1))
print()

# 有时只需要剔除全部是缺失值的行或列，或者绝大多数是缺失值的行或列。
# 这些需求可以通过设置how或thresh参数来满足，它们可以设置剔除行或列缺失值的数量阈值。
df = pd.DataFrame([[1, pd.NA, 2], [pd.NA, pd.NA, 5], [pd.NA, pd.NA, pd.NA]])
print(df)
print()
print(df.dropna(how='all'))  # 如果所有值都是缺失值, 则删除这一行
print()
print(df.dropna(thresh=2))  # 如果至少有 2 个值不是缺失值, 则保留这一行
print()

# 可以通过设置 subset 参数来设置某一列有缺失值则进行删除
df = pd.DataFrame([[1, pd.NA, 2], [pd.NA, pd.NA, 5], [pd.NA, pd.NA, pd.NA]])
print(df)
print()
print(df.dropna(subset=[0]))  # 如果0列有缺失值, 则删除这一行
print()

"""
填充缺失值：
"""
# 1）使用固定值填充
# 通过 fillna() 方法, 传入值或字典进行填充
df = pd.read_csv('data/weather_withna.csv')
print(df.fillna(0).tail())  # 使用固定值填充
print()
print(df.fillna({'temp_max': 60, 'temp_min': -60}).tail())  # 使用字典来填充
print()

# 2）使用统计值填充
# 通过 fillna() 方法, 传入统计后的值进行填充
print(df.fillna(df[["precipitation", "temp_max", "temp_min", "wind"]].mean().tail()))
print()

# 3）使用前后的有效值填充
# 通过 ffill() 或 bfill() 方法使用前面或后面的有效值填充
print(df.ffill().tail())
print()

print(df.bfill().tail())
print()

# 4）通过线性插值填充
# 通过interpolate()方法进行线性插值填充。线性插值操作，就是用于在已知数据点之间估算未知数据点的值。interpolate 方法支持多种插值方法，可通过 method 参数指定，常见的方法有：
# 	'linear'：线性插值，基于两点之间的直线来估算缺失值，适用于数据呈线性变化的情况。
# 	'time'：适用于时间序列数据，会考虑时间间隔进行插值。
# 	'polynomial'：多项式插值，通过拟合多项式曲线来估算缺失值，可通过 order 参数指定多项式的阶数。

# 创建包含缺失值的 Series
s = pd.Series([1, np.nan, 3, 4, np.nan, 6])
# 使用默认的线性插值方法填充缺失值
s_interpolated = s.interpolate()
print(s_interpolated)
