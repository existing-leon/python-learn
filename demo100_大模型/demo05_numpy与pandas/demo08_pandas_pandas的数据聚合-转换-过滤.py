""""""
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
