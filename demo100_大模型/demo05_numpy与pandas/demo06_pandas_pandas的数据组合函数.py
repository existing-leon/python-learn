""""""
"""
concat 连接：

沿着一条轴将多个对象堆叠到一起, 可通过 axis 参数设置沿哪一条轴连接
"""
import pandas as pd

# 1、Series 与 Series 连接
s1 = pd.Series(['A', 'B'], index=[1, 2])
s2 = pd.Series(['D', 'E'], index=[4, 5])
s3 = pd.Series(['G', 'H'], index=[7, 8])

print(pd.concat([s1, s2, s3]))  # 按行连接
print()

print(pd.concat([s1, s2, s3], axis=1))  # 按列连接
print()

# 2、DataFrame 与 Series 连接
df1 = pd.DataFrame(data={'a': [1, 2], 'b': [4, 5]}, index=[1, 2])
s1 = pd.Series([7, 10], index=[1, 2], name='a')

print(pd.concat([df1, s1]))  # 按行连接
print()

print(pd.concat([df1, s1], axis=1))  # 按列连接
print()

# 3、DataFrame 与 DataFrame 连接
df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
df2 = pd.DataFrame(data={"a": [7, 8], "b": [10, 11]}, index=[1, 2])

print(pd.concat([df1, df2]))  # 按行连接
print()

print(pd.concat([df1, df2], axis=1))
print()

# 4、重置索引
df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
df2 = pd.DataFrame(data={"a": [7, 8], "b": [10, 11]}, index=[1, 2])

print(pd.concat([df1, df2], ignore_index=True))  # 重置索引
print()

# 5、类似 join 的连接
# 默认的合并方式是对其他轴进行并集合并（join=outer），可以用join=inner实现其他轴上的交集合并。
df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
df2 = pd.DataFrame(data={"b": [7, 8], "c": [10, 11]}, index=[2, 3])

print(pd.concat([df1, df2]))
print()

print(pd.concat([df1, df2], join='inner'))
print()

"""
merge 合并：
通过一个或多个列将行连接

merge()实现了三种数据连接的类型：一对一、多对一和多对多。
"""
# 一对一连接
df1 = pd.DataFrame(
    {
        'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
        'group': ['Accounting', 'Engineering', 'Engineering', 'HR']
    }
)
df2 = pd.DataFrame(
    {
        "employee": ["Lisa", "Bob", "Jake", "Sue"],
        "hire_date": [2004, 2008, 2012, 2014]
    }
)
print(df1)
print()
print(df2)
print()
df3 = pd.merge(df1, df2)
print(df3)
print()

# 多对一连接
# 在需要连接的两个列中，有一列的值有重复。通过多对一连接获得的结果将会保留重复值。
df1 = pd.DataFrame(
    {
        "employee": ["Bob", "Jake", "Lisa", "Sue"],
        "group": ["Accounting", "Engineering", "Engineering", "HR"]
    }
)
df2 = pd.DataFrame(
    {
        "group": ["Accounting", "Engineering", "HR"],
        "supervisor": ["Carly", "Guido", "Steve"]
    }
)
print(df1)
print()
print(df2)
print()
df3 = pd.merge(df1, df2)
print(df3)
print()

# 多对多连接
# 如果左右两个输入的共同列都包含重复值, 那么合并结果就是一种多对多连接
df1 = pd.DataFrame(
    {
        "employee": ["Bob", "Jake", "Lisa", "Sue"],
        "group": ["Accounting", "Engineering", "Engineering", "HR"]
    }
)
df2 = pd.DataFrame(
    {
        "group": ["Accounting", "Accounting", "Engineering", "Engineering", "HR", "HR"],
        "skills": ["math", "spreadsheets", "coding", "linux", "spreadsheets", "organization"],
    }
)
print(df1)
print()
print(df2)
print()
df3 = pd.merge(df1, df2)
print(df3)
print()

"""
设置合并的键与索引
merge()会将两个输入的一个或多个共同列作为键进行合并. 但由于两个输入要合并的列通常都不是同名的,
因此merge()提供了一些参数处理这个问题.
"""

# （1）通过 on 指定使用某个列连接, 只能在有共同列名的时候使用
df1 = pd.DataFrame(
    {
        "employee": ["Bob", "Jake", "Lisa", "Sue"],
        "group": ["Accounting", "Engineering", "Engineering", "HR"]
    }
)
df2 = pd.DataFrame(
    {
        "employee": ["Lisa", "Bob", "Jake", "Sue"],
        "hire_date": [2004, 2008, 2012, 2014]
    }
)
print(df1)
print()
print(df2)
print()
df3 = pd.merge(df1, df2, on='employee')
print(df3)
print()

# （2）两对象列名不同，通过left_on和right_on分别指定列名
df1 = pd.DataFrame(
    {
        "employee": ["Bob", "Jake", "Lisa", "Sue"],
        "group": ["Accounting", "Engineering", "Engineering", "HR"]
    }
)
df2 = pd.DataFrame(
    {
        "name": ["Bob", "Jake", "Lisa", "Sue"],
        "salary": [70000, 80000, 120000, 90000]
    }
)
print(df1)
print()
print(df2)
print()
df3 = pd.merge(df1, df2, left_on='employee', right_on='name')
print(df3)
print()

# （3）通过left_index和right_index设置合并的索引
# 通过设置merge()中的left_index、right_index参数将索引设置为键来实现合并。
df1 = pd.DataFrame(
    {
        "employee": ["Bob", "Jake", "Lisa", "Sue"],
        "group": ["Accounting", "Engineering", "Engineering", "HR"]
    }
)
df2 = pd.DataFrame(
    {
        "employee": ["Lisa", "Bob", "Jake", "Sue"],
        "hire_date": [2004, 2008, 2012, 2014]
    }
)
df1.set_index("employee", inplace=True)
df2.set_index("employee", inplace=True)
print(df1)
print()
print(df2)
print()
df3 = pd.merge(df1, df2, left_index=True, right_index=True)
print(df3)
print()

# DataFrame实现了join()方法，可以按照索引进行数据合并。
# 但要求没有重叠的列，或通过lsuffix、rsuffix指定重叠列的后缀。
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'key': ['B', 'C', 'D'],
    'value2': [4, 5, 6]
})
# 合并两个 DataFrame，并处理列名冲突
print(df1.join(df2, lsuffix='_left', rsuffix='_right'))
print()

"""
3）设置数据连接的集合操作规则
当一个值出现在一列，却没有出现在另一列时，就需要考虑集合操作规则了。
"""
df1 = pd.DataFrame(
    {
        "name": ["Peter", "Paul", "Mary"],
        "food": ["fish", "beans", "bread"]
    },
    columns=["name", "food"]
)
df2 = pd.DataFrame(
    {
        "name": ["Mary", "Joseph"],
        "drink": ["wine", "beer"]
    },
    columns=["name", "drink"]
)
print(df1)
print()
print(df2)
print()
print(pd.merge(df1, df2))
print()

"""
合并两个数据集，在name列中只有一个共同的值Mary。默认情况下，结果中只会包含两个输入集合的交集，
这种连接方式被称为内连接（inner join）。
我们可以通过how参数设置连接方式，默认值为inner。how参数支持的数据连接方式还有outer、left
和right。外连接（outer join）返回两个输入列的并集，所有缺失值都用 NaN 填充。
"""
print(pd.merge(df1, df2, how='outer'))
print()

# 左连接（left join）和右连接（right join）返回的结果分别只包含左列和右列。
print(pd.merge(df1, df2, how='left'))

"""
4）重复列名的处理
可能会遇到两个输入DataFrame有重名列的情况，merge()会自动为其增加后缀_x和_y，也可以通过suffixes参数自定义后缀名。
"""
df1 = pd.DataFrame(
    {
        "name": ["Bob", "Jake", "Lisa", "Sue"],
        "rank": [1, 2, 3, 4]
    }
)
df2 = pd.DataFrame(
    {
        "name": ["Bob", "Jake", "Lisa", "Sue"],
        "rank": [3, 1, 4, 2]
    }
)
print(df1)
print()
print(df2)
print()
print(pd.merge(df1, df2, on='name'))
print()
print(pd.merge(df1, df2, on='name', suffixes=('_df1', '_df2')))
