""""""
"""
使用weather（天气）数据集。其中包含6个字段：
	date：日期，年-月-日格式。
	precipitation：降水量。
	temp_max：最高温度。
	temp_min：最低温度。
	wind：风力。
	weather：天气状况。
"""

import pandas as pd

df = pd.read_csv('data/weather.csv')
print(type(df))  # 查看df类型
print(df.shape)  # 查看df形状
print(df.columns)  # 查看df的列名
print()
print(df.dtypes)  # 查看df各列数据类型
print()
df.info()  # 查看df基本信息
print()

# 查看部分数据
print(df.head())
print()
print(df.tail(10))
print()

# 获取一列或多列数据
df_date_series = df['date']  # 返回的是 Series
print(type(df_date_series))
df_date_dateframe = df[['date']]  # 返回的是 DataFrame
print(type(df_date_dateframe))

# 加载多列数据
print(df[['date', 'temp_max', 'temp_min']].head())
print()

# 按行获取数据
# loc：通过行标签获取数据
print(df.loc[1])  # 获取行标签为 1 的数据
print()
print(df.loc[[1, 10, 100]])  # 获取行标签分别为 1、10、100 的数据
print()

# iloc：通过行位置获取数据
print(df.iloc[0])  # 获取行位置为 0 的数据
print()
print(df.iloc[-1])  # 获取行位置为最后一位的数据
print()

# 获取指定行与列的数据
df.loc[1, 'precipitation']  # 获取行标签为1, 列标签为 precipitation的数据
df.loc[:, 'precipitation']  # 获取所有行, 列标签为 precipitation的数据
df.iloc[:, [3, 5, -1]]  # 获取所有行, 列位置为 3, 5, 最后一位的数据
df.iloc[:10, 2:6]  # 获取前10行, 列位置为 2、3、4、5 的数据
df.loc[:10, ['date', 'precipitation', 'temp_max', 'temp_min']]  # 通过行列标签获取数据

"""
分组聚合：
df.groupby("分组字段")["要聚合的字段"].聚合函数()
df.groupby(["分组字段", "分组字段2", ...])[["要聚合的字段", "要聚合的字段2", ...]].聚合函数()
"""
## 将数据按月分组, 并统计最大温度和最小温度的平均值
# step1：将 date 转换为 年-月 的格式
df['month'] = pd.to_datetime(df['date']).dt.to_period('M').astype(str)
# step2：按 month 分组, 返回一个分组对象
df_groupby_date = df.groupby('month')
# step3：从分组对象中选择特定的列
month_temp = df_groupby_date[['temp_max', 'temp_min']]
# step4：对每个列求平均值
month_temp_mean = month_temp.mean()

# 以上2~4代码可以直接写：
month_temp_mean = df.groupby('month')[['temp_max', 'temp_min']].mean()

## 分组频次计算
# 统计每个月不同天气状况的数量
rate_df = df.groupby('month')['weather'].nunique()
print(rate_df)

print('-' * 20)

"""
基本绘图：
plot()：
pandas 提供的绘图方法，它基于 matplotlib 库。将前面计算得到的均值结果绘制成图表，
默认情况下会绘制折线图，其中 "month" 作为 x 轴，"temp_max" 和 "temp_min" 的
均值作为 y 轴。

plt.show() 不可以遗漏, 否则不显示图像
"""
import matplotlib

matplotlib.use('TkAgg')  # 或 'Qt5Agg', 'Agg'（Agg 无窗口，用于保存图像）
import matplotlib.pyplot as plt

df = pd.read_csv('data/weather.csv')
df['month'] = pd.to_datetime(df['date']).dt.to_period('M').astype(str)
df.groupby("month")[["temp_max", "temp_min"]].mean().plot()

# 关键：显示图像（脚本中必须添加）
# plt.show()
print()

"""
常用统计值：

"""
# 查看常用统计信息
print('describe ==>\n', df.describe())
print()
# 行列转置
print('describe.T ==>\n', df.describe().T)
print()

# 可通过 include 参数指定要统计哪些数据类型的列
print('describe include=all ==>\n', df.describe(include='all'))
print()
print('describe include=? ==>\n', df.describe(include='float64'))
print('-' * 20)
print()

"""
常用排序方法：

nlargest(n, [列名1, 列名2, …])：按列排序的最大n个
nsmallest(n, [列名1, 列名2, …])：按列排序的最小n个
sort_values([列名1, 列名2, …], asceding=[True, False, …])：按列升序或降序排序
drop_duplicates(subset=[列名1, 列名2])：按列去重

"""
# 找到最高温度最大的30天
df = pd.read_csv('data/weather.csv')
print(df.nlargest(30, 'temp_max'))
print()

# 从最高温度最大的30天中找出最低温度最小的5天
print('从最高温度最大的30天中找出最低温度最小的5天 ==>\n', df.nlargest(30, 'temp_max').nsmallest(5, 'temp_min'))
print()

# 找出每年的最高温度
df['year'] = pd.to_datetime(df['date']).dt.to_period('Y').astype(str)  # 将 date 转换为年格式
df_sort = df.sort_values(by=['year', 'temp_max'], ascending=[True, False])  # 按 year 升序, temp_max 降序排序
print('df_sort ==> \n', df_sort.drop_duplicates(subset='year'))

print()
print('-' * 50)
print()

"""
案例：简单数据分析练习

使用employees（员工）数据集，其中包含10个字段：
	employee_id：员工id。
	first_name：员工名称。
	last_name：员工姓氏。
	email：员工邮箱。
	phone_number：员工电话号码。
	job_id：员工工种。
	salary：员工薪资。
	commission_pct：员工佣金比例。
	manager_id：员工领导的id。
	department_id：员工的部门id。
"""

# 加载数据
import pandas as pd

# 加载员工数据
df = pd.read_csv('data/employees.csv')

# 查看数据
print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()
print(df.shape)
print()

# 找出薪资最低、最高的员工
print(df[df['salary'] == df['salary'].min()])
print()
print(df.loc[df['salary'] == df['salary'].min()])
print()
print(df[df['salary'] == df['salary'].max()])
print()
print(df.sort_values('salary').head(1))
print()
print(df.sort_values('salary', ascending=False).head(1))
print()

# 找出薪资最高的10名员工
print(df.nlargest(10, 'salary'))
print()

# 查看所有部门id
print(df['department_id'].unique())
print()

# 查看每个部门的员工数
df.groupby('department_id')['employee_id'].count().rename('employee_count').plot(kind='bar')

plt.show()

# 薪资的分布
print(df['salary'].mean())  # 平均值
print(df['salary'].std())  # 标准差
print(df['salary'].median())  # 中位数
print()

# 找出平均薪资最高的部门id
print(df.groupby('department_id')['salary'].mean().nlargest(1))
