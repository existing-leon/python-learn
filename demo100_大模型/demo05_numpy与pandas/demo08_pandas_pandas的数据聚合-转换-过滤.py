""""""
import numpy as np

"""
对DataFrame对象调用groupby()方法后，会返回DataFrameGroupBy对象。
"""
import pandas as pd

df = pd.read_csv('data/employees.csv')
print(df.groupby('department_id'))
print()

## 查看分组
# 通过groups属性查看分组结果，返回一个字典，字典的键是分组的标签，值是属于该组的所有索引的列表
print(df.groupby('department_id').groups)
print()

# 获得分组
# 通过get_group()方法获取分组。
print(df.groupby('department_id').get_group(50))
print()

## 按列取值
print(df.groupby('department_id')['salary'])
print()

# 从原来的DataFrame中取某个列名作为一个Series组。与GroupBy对象一样，直到我们运行累计函数，才会开始计算。
print(df.groupby('department_id')['salary'].mean())
print()

## 按组迭代
# GroupBy对象支持直接按组进行迭代，返回的每一组都是Series或DataFrame。
for dept_id, group in df.groupby('department_id'):
    print(f'当前组为：{dept_id}, 组里的数据情况：{group.shape}：')
    print(group.iloc[:, 0:3])
    print('-----------------------')
print()

## 按多字段分组：按多个字段分组后得到的索引为复合索引
salary_mean = df.groupby(['department_id', 'job_id'])[['salary', 'commission_pct']].mean()
print(salary_mean.index)  # 查看分组后的索引
print()
print(salary_mean.columns)  # 查看分组后的列
print()

# 可通过 reset_index() 方法重置索引
print(salary_mean.reset_index())
print()

# 也可以在分组的时候通过 as_index = False 参数（默认是True）重置索引
salary_mean = df.groupby(['department_id', 'job_id'], as_index=False)[['salary', 'commission_pct']].mean()
print(salary_mean)
print()

## cut()
# pandas.cut()用于将连续数据（如数值型数据）分割成离散的区间。
# 可以使用cut()来将数据划分为不同的类别或范围，通常用于数据的分箱处理。
# cut() 部分参数说明：
#
# x	要分箱的数组或Series，通常是数值型数据。
# bins	切分区间的数值列表或者整数。如果是整数，则表示将数据均匀地分成多少个区间。如果是列表，则需要指定每个区间的边界。
# right	默认True，表示每个区间的右端点是闭区间，即包含右端点。如果设置为False，则左端点为闭区间。
# labels	传入一个列表指定每个区间的标签。
df = pd.read_csv('data/employees.csv')
print(df.iloc[9:16]['salary'])
print()
salary = pd.cut(df.iloc[9:16]['salary'], 3)
print(salary)
print()
salary = pd.cut(df.iloc[9:16]['salary'], [0, 10000, 20000])
print(salary)
salary = pd.cut(df.iloc[9:16]['salary'], 3, labels=['low', 'medium', 'high'])
print(salary)

"""
分组聚合：
- 语法：
df.groupby("分组字段")["要聚合的字段"].聚合函数()
df.groupby(["分组字段", "分组字段2", ...])[["要聚合的字段", "要聚合的字段2", ...]].聚合函数()

- 常用聚合函数：
sum()	    求和
mean()	    平均值
min()	    最小值
max()	    最大值
var()	    方差
std()	    标准差
median()	中位数
quantile()	指定位置的分位数，如quantile(0.5)
describe()	常见统计信息
size()	    所有元素的个数
count() 	非空元素的个数
first	    第一行
last	    最后一行
nth	        第n行

"""

## 一次计算多个统计值
# 可以通过 agg() 或 aggregate() 进行更复杂的操作, 如一次计算多个统计值
df = pd.read_csv('data/employees.csv')
# 按 department_id 分组, 计算 salary 的最小值, 中位数, 最大值
print(df.groupby('department_id')['salary'].agg(['min', 'median', 'max']))
print()

## 多个列计算不同的统计值
# 可以在 agg() 中传入字典, 对多个列计算不同的统计值
df = pd.read_csv('data/employees.csv')
# 按 department_id 分组, 统计 job_id 的种类数, commission_pct 的平均值
print(df.groupby('department_id').agg({'job_id': 'nunique', 'commission_pct': 'mean'}))
print()

## 重命名统计值
# 可以在 agg() 后通过 rename() 对统计后的列重命名
df = pd.read_csv('data/employees.csv')
# 按 department_id 分组, 统计 job_id 的种类数, commission_pct 的平均值
print(
    df.groupby('department_id')
    .agg({'job_id': 'nunique', 'commission_pct': 'mean'})
    .rename(
        columns={'job_id': '工种数', 'commission_pct': '佣金比例平均值'}
    )
)
print()

## 自定义函数
# 可以向 agg() 中传入自定义函数进行计算
df = pd.read_csv('data/employees.csv')


def f(x):
    """统计每个部门员工 last_name 的首字母"""
    result = set()
    for i in x:
        result.add(i[0])
    return result


print(df.groupby('department_id')['last_name'].agg(f))
print()

"""
分组转换：
聚合操作返回的是对组内全量数据缩减过的结果，而转换操作会返回一个新的全量数据。数据经过转换之后，其形状与原来的输入数据是一样的。
"""
## 1）通过 transform() 将每一组的样本数据减去各组的均值, 实现数据标准化
df = pd.read_csv('data/employees.csv')
print(df.groupby('department_id')['salary'].transform(lambda x: x - x.mean()))
print()

## 2）通过 transform() 按分组使用平均值填充缺失值
df = pd.read_csv('data/employees.csv')
na_index = pd.Series(df.index.tolist()).sample(30)  # 随机挑选30条数据
df.loc[na_index, 'salary'] = pd.NA  # 将这30条数据的salary设置为缺失值
print(df.groupby('department_id')['salary'].agg(['size', 'count']))  # 查看每组数据总数与非空数据数
print()


def fill_missing(x):
    # 使用平均值填充, 如果平均值也为NaN, 用0填充
    if np.isnan(x.mean()):
        return 0
    return x.fillna(x.mean())


df['salary'] = df.groupby('department_id')['salary'].transform(fill_missing)
print(df.groupby('department_id')['salary'].agg(['size', 'count']))  # 查看每组数据总数与非空数据数
print()

"""
分组过滤：
过滤操作可以让我们按照分组的属性丢弃若干数据
如：我们可能只需要保留 commission_pct 不包含空值的分组的数据
"""
df = pd.read_csv('data/employees.csv')
commission_pct_filter = df.groupby('department_id').filter(
    lambda x: x['commission_pct'].notnull().all()
)
print(commission_pct_filter)
