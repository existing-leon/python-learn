""""""
"""
DataFrame 是 Pandas 中的另一个核心数据结构, 类似于一个二维的表格或数据库中的数据表. 
它是一个表格型的数据结构, 它含有一组有序的列, 每列可以是不同的值类型(数值、字符串、布尔类型), 既有行索引也有列索引.
"""
import pandas as pd

"""
直接通过字典创建 DataFrame
"""
df = pd.DataFrame({'id': [101, 102, 103], 'name': ['张三', '李四', '王五'], 'age': [20, 30, 40]})
print(df)
print()

"""
通过字典创建时指定列的顺序和行索引
"""
df = pd.DataFrame(
    data={'age': [20, 30, 40], 'name': ['张三', '李四', '王五']},
    columns=['age', 'name'],
    index=[101, 102, 103]
)
print(df)
print()

"""
DataFrame 的常用属性：
index	DataFrame的行索引
columns	DataFrame的列标签
values	DataFrame的值
ndim	DataFrame的维度
shape	DataFrame的形状
size	DataFrame的元素个数
dtypes	DataFrame的元素类型
T	    行列转置
loc[]	显式索引，按行列标签索引或切片
iloc[]	隐式索引，按行列位置索引或切片
at[]	使用行列标签访问单个元素
iat[]	使用行列位置访问单个元素
"""
df = pd.DataFrame(
    data={'id': [101, 102, 103], 'name': ['张三', '李四', '王五'], 'age': [20, 30, 40]},
    index=['aa', 'bb', 'cc']
)
print(df)
# index DataFrame的行索引
print('行索引：', df.index)
# columns DataDrame的列标签
print('列标签：', df.columns)
# values DataFrame的值
print('值：', df.values)
# ndim DataFrame的维度
print('维度：', df.ndim)
# shape DataFrame的形状
print('形状：', df.shape)
# size DataFrame的元素个数
print('元素个数：', df.size)
# dtypes DataFrame的元素类型
print('元素类型：', df.dtypes)
# T 行列转置
print('行列转置：', df.T)
# loc[] 显示索引, 按行列标签索引或切片
print('loc：', df.loc['aa': 'cc'])
print('loc：', df.loc[:, ['id', 'name']])
# iloc[] 隐式索引, 按行列位置索引或切片
print('iloc：', df.iloc[0:1])
print('iloc：', df.iloc[0:3, 2])
# at[] 使用行列标签访问单个元素
print('at：', df.at['aa', 'name'])
# iat[] 使用行列位置访问单个元素
print('iat：', df.iat[0, 1])
print('-' * 10)
print()

"""
DataFrame的常用方法：

head()	查看前n行数据，默认5行
tail()	查看后n行数据，默认5行
isin()	元素是否包含在参数集合中
isna()	元素是否为缺失值
sum()	求和
mean()	平均值
min()	最小值
max()	最大值
var()	方差
std()	标准差
median()	中位数
mode()	众数
quantile()	指定位置的分位数，如quantile(0.5)
describe()	常见统计信息
info()	基本信息
value_counts()	每个元素的个数
count()	非空元素的个数
drop_duplicates()	去重
sample()	随机采样
replace()	用指定值代替原有值
equals()	判断两个DataFrame是否相同
cummax()	累计最大值
cummin()	累计最小值
cumsum()	累计和
cumprod()	累计积
diff()	一阶差分，对序列中的元素进行差分运算，也就是用当前元素减去前一个元素得到差值，默认情况下，它会计算一阶差分，即相邻元素之间的差值。参数：
periods：整数，默认为 1。表示要向前或向后移动的周期数，用于计算差值。正数表示向前移动，负数表示向后移动。
axis：指定计算的轴方向。0 或 'index' 表示按列计算，1 或 'columns' 表示按行计算，默认值为 0。
sort_index()	按行索引排序
sort_values()	按某列的值排序，可传入列表来按多列排序，并通过ascending参数设置升序或降序
nlargest()	返回某列最大的n条数据
nsmallest()	返回某列最小的n条数据

在Pandas的 DataFrame 方法里，axis 是一个非常重要的参数，它用于指定操作的方向。
axis 参数可以取两个主要的值，即 0 或 'index'，以及 1 或 'columns' ，其含义如下：
	axis=0 或 axis='index'：表示操作沿着行的方向进行，也就是对每一列的数据进行处理。例如，当计算每列的均值时，就是对每列中的所有行数据进行计算。
	axis=1 或 axis='columns'：表示操作沿着列的方向进行，也就是对每行的数据进行处理。例如，当计算每行的总和时，就是对每行中的所有列数据进行计算。

"""
df = pd.DataFrame(
    data={'id': [101, 102, 103, 104, 105, 106, 101],
          'name': ['张三', '李四', '王五', '赵六', '冯七', '周八', '张三'],
          'age': [10, 20, 30, 40, None, 60, 10]},
    index=['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'aa']
)
# head() 查看前n行数据, 默认5行
print('head()：', df.head())
# tail() 查看后n行数据, 默认5行
print('tail()：', df.tail())
# isin()    元素是否包含在参数集合中
print('元素是否包含在参数集合中：', df.isin([103, 106]))
# isna()    元素是否为缺失值
print('元素是否为缺失值：', df.isna())
# sum() 求和
print('求和：', df["age"].sum())
# mean()    平均值
print('平均值：', df["age"].mean())
# min() 最小值
print('最小值：', df["age"].min())
# max() 最大值
print('最大值：', df["age"].max())
# var() 方差
print('方差：', df["age"].var())
# std() 标准差
print('标准差：', df["age"].std())
# median()  中位数
print('中位数：', df["age"].median())
# mode()    众数
print('众数：', df["age"].mode())
# quantile()    指定位置的分位数，如quantile(0.5)
print('指定位置的分位数：', df["age"].quantile(0.5))
# describe()    常见统计信息
print('常见统计信息：', df.describe())
# info()    基本信息
print('基本信息：', df.info())
# value_counts()    每个元素的个数
print('每个元素的个数：', df.value_counts())
# count()   非空元素的个数
print('非空元素的个数：', df.count())
# drop_duplicates() 去重
print('去重：', df.duplicated(subset="age"))
# sample()  随机采样
print('随机采样：', df.sample())
# replace() 用指定值代替原有值
print("----------------")
print('用指定值代替原有值：', df.replace(20, "haha"))
# equals()  判断两个DataFrame是否相同
df1 = pd.DataFrame(data={"id": [101, 102, 103], "name": ["张三", "李四", "王五"], "age": [10, 20, 30]})
df2 = pd.DataFrame(data={"id": [101, 102, 103], "name": ["张三", "李四", "王五"], "age": [10, 20, 30]})
print('判断两个DataFrame是否相同：', df1.equals(df2))
# cummax()  累计最大值
df3 = pd.DataFrame({'A': [2, 5, 3, 7, 4], 'B': [1, 6, 2, 8, 3]})
# 按列  等价于axis=0 默认
print('按列累计最大值：', df3.cummax(axis="index"))
# 按行  等价于axis=1
print('按行累计最大值：', df3.cummax(axis="columns"))
# cummin()  累计最小值
print('累计最小值：', df3.cummin())
# cumsum()  累计和
print('累计和：', df3.cumsum())
# cumprod() 累计积
print('累计积：', df3.cumprod())
# diff()    一阶差分
print('一阶差分：', df3.diff())
# sort_index()  按行索引排序
print('按行索引排序：', df.sort_index())
# sort_values() 按某列的值排序，可传入列表来按多列排序，并通过ascending参数设置升序或降序
print('按某列的值排序：', df.sort_values(by="age"))
# nlargest()    返回某列最大的n条数据
print('返回某列最大的n条数据：', df.nlargest(n=2, columns="age"))
# nsmallest()   返回某列最小的n条数据
print('返回某列最小的n条数据：', df.nsmallest(n=1, columns="age"))
print('-' * 15)
print()

"""
可以使用布尔索引从 DataFrame 中筛选满足某些条件的行
"""
df = pd.DataFrame(
    data={'age': [20, 30, 40, 10],
          'name': ['张三', '李四', '王五', '赵六']},
    columns=['name', 'age'],
    index=[101, 104, 103, 102]
)
print(df['age'] > 25)
print()
print(df[df['age'] > 25])
print('-' * 15)
print()

"""
DataFrame 的运算：
DataFrame与标量运算：标量与每个元素进行计算
"""
df = pd.DataFrame(
    data={'age': [20, 30, 40, 10],
          'name': ['张三', '李四', '王五', '赵六']},
    columns=['name', 'age'],
    index=[101, 104, 103, 102]
)
print(df * 2)
print('-' * 15)
print()

"""
DataFrame 的运算：
DataFrame与DataFrame运算：根据标签索引进行对应计算, 索引没有匹配上的用NaN填充
"""
df1 = pd.DataFrame(
    data={"age": [10, 20, 30, 40], "name": ["张三", "李四", "王五", "赵六"]},
    columns=["name", "age"],
    index=[101, 102, 103, 104],
)
df2 = pd.DataFrame(
    data={"age": [10, 20, 30, 40], "name": ["张三", "李四", "王五", "田七"]},
    columns=["name", "age"],
    index=[102, 103, 104, 105],
)
print(df1 + df2)
print('-' * 15)
print()

"""
DataFrame 的更改操作：
设置行索引：创建 DataFrame 时如果不指定行索引, pandas 会自动添加从 0 开始的索引
"""
df = pd.DataFrame(
    {'age': [20, 30, 40, 10],
     'name': ['张三', '李四', '王五', '赵六'],
     'id': [101, 102, 103, 104]
     })
print(df)
print('-' * 15)
print()

"""
通过 set_index() 设置行索引
"""
df.set_index('id', inplace=True)
print(df)
print('-' * 15)
print()

"""
通过 reset_index() 重置行索引
"""
df.reset_index(inplace=True)
print(df)
print('-' * 15)
print()

"""
修改行索引名和列名：
通过 rename() 修改行索引名和列名
"""
df = pd.DataFrame(
    {'age': [20, 30, 40, 10],
     'name': ['张三', '李四', '王五', '赵六'],
     'id': [101, 102, 103, 104]})
df.set_index('id', inplace=True)
print(df)
print('-' * 15)
print()

df.rename(index={101: '一', 102: '二', 103: '三', 104: '四'},
          columns={'age': '年龄', 'name': '姓名'},
          inplace=True)
print(df)
print('-' * 15)
print()

"""
将 index 和 columns 重新赋值
"""
df.index = ['I', 'II', 'III', 'IV']
df.columns = ['年龄', '名称']
print(df)
print('-' * 15)
print()

"""
添加列：通过 df['列名'] 添加列
"""
df["phone"] = ["13333333333", "14444444444", "15555555555", "16666666666"]
print(df)
print('-' * 15)
print()

"""
删除列：通过 df.drop('列名', axis=1) 删除, 也可以删除行 axis=0
"""
# df.drop('phone', axis=1, inplace=True)
# print(df)
# print('-' * 15)
# print()

"""
通过 del df['列名'] 删除
"""
del df['phone']
print(df)
print('-' * 15)
print()

"""
插入列：通过 insert(loc, column, value) 插入. 该方法没有 inplace 参数, 直接在原数据上修改.
"""
df = pd.DataFrame(
    {'age': [20, 30, 40, 10],
     'name': ['张三', '李四', '王五', '赵六'],
     'id': [101, 102, 103, 104]})
df.insert(loc=0, column='phone', value=df['age'] * df.index)
print(df)
print('-' * 15)
print('-' * 15)
print('-' * 15)
print()

"""
DataFrame 数据的导入与导出：

导出数据：

to_csv()	将数据保存为csv格式文件，数据之间以逗号分隔，可通过sep参数设置使用其他分隔符，可通过index参数设置是否保存行标签，可通过header参数设置是否保存列标签。
to_pickle()	如要保存的对象是计算的中间结果，或者保存的对象以后会在Python中复用，可把对象保存为.pickle文件。如果保存成pickle文件，只能在python中使用。文件的扩展名可以是.p、.pkl、.pickle。
to_excel()	保存为Excel文件，需安装openpyxl包。
to_clipboard()	保存到剪切板。
to_dict()	保存为字典。
to_hdf()	保存为HDF格式，需安装tables包。
to_html()	保存为HTML格式，需安装lxml、html5lib、beautifulsoup4包。
to_json()	保存为JSON格式。
to_feather()	feather是一种文件格式，用于存储二进制对象。feather对象也可以加载到R语言中使用。feather格式的主要优点是在Python和R语言之间的读写速度要比csv文件快。feather数据格式通常只用中间数据格式，用于Python和R之间传递数据，一般不用做保存最终数据。需安装pyarrow包。
to_sql()	保存到数据库。
"""
import os
import pandas as pd

os.makedirs('data', exist_ok=True)
df = pd.DataFrame(
    {
        "age": [20, 30, 40, 10],
        "name": ["张三", "李四", "王五", "赵六"],
        "id": [101, 102, 103, 104]
    }
)
df.set_index("id", inplace=True)
df.to_csv('data/df.csv')
df.to_csv("data/df.tsv", sep="\t")  # 设置分隔符为 \t
df.to_csv("data/df_noindex.csv", index=False)  # index=False 不保存行索引
df.to_pickle("data/df.pkl")
df.to_excel("data/df.xlsx")
df.to_clipboard()
df_dict = df.to_dict()
df.to_hdf("data/df.h5", key="df")
df.to_html("data/df.html")
df.to_json("data/df.json", force_ascii=False)
df.to_feather("data/df.feather")

"""
导入数据：

read_csv()	加载csv格式的数据。可通过sep参数指定分隔符，可通过index_col参数指定行索引。
read_pickle()	加载pickle格式的数据。
read_excel()	加载Excel格式的数据。
read_clipboard()	加载剪切板中的数据。
read_hdf()	加载HDF格式的数据。
read_html()	加载HTML格式的数据。
read_json()	加载JSON格式的数据。
read_feather()	加载feather格式的数据。
read_sql()	加载数据库中的数据。
"""
df_csv = pd.read_csv("data/df.csv", index_col="id")  # 指定行索引
df_tsv = pd.read_csv("data/df.tsv", sep="\t")  # 指定分隔符
df_pkl = pd.read_pickle("data/df.pkl")
df_excel = pd.read_excel("data/df.xlsx", index_col="id")
df_clipboard = pd.read_clipboard(index_col="id")
df_from_dict = pd.DataFrame(df_dict)
df_hdf = pd.read_hdf("data/df.h5", key="df")
df_html = pd.read_html("data/df.html", index_col=0, encoding='utf-8')[0]
df_json = pd.read_json("data/df.json")
df_feather = pd.read_feather("data/df.feather")

print(df_csv)
print(df_tsv)
print(df_pkl)
print(df_excel)
print(df_clipboard)
print(df_from_dict)
print(df_hdf)
print(df_html)
print(df_json)
print(df_feather)
