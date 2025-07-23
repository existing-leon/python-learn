""""""
import numpy as np
import pandas as pd

"""
apply()函数可以对DataFrame或Series的数据进行逐行、逐列或逐元素的操作。
可以使用自定义函数对数据进行变换、计算或处理，通常用于处理复杂的变换逻辑，
或者处理不能通过向量化操作轻松完成的任务。
"""

"""
1） Series使用apply()
"""


def f(x):
    return x * 10


df = pd.DataFrame(
    {
        'a': [10, 20, 30],
        'b': [40, 50, 60]
    }
)
print(df['a'].apply(f))
print()

# 也可以传入 lambda 表达式
print(df['a'].apply(lambda x: x * 10))
print()


# 传入带参数的函数
def f(x, y=10):
    return x * y


print(df['a'].apply(f, y=5))
print()

"""
DataFrame 使用 apply()
"""


def f(x):
    return x * 10


df = pd.DataFrame(
    {
        'a': [10, 20, 30],
        'b': [40, 50, 60]
    }
)
print(df.apply(f))
print()


# 默认是 axis = 0, 按行方向进行操作, 对列进行统计
# 可以设置 axis = 1, 按照列的方向进行操作, 参数设置按行处理
def f(x):
    return x['a'] / x['b']


df = pd.DataFrame(
    {
        'a': [10, 20, 30],
        'b': [40, 50, 60]
    }
)
print(df.apply(f, axis=1))
print()
"""
注意：df.apply 一次只能处理一个 Series（当 axis=0 时处理列，当 axis=1 时处理行），
而你定义的函数 f 接收两个参数，不能直接使用 df.apply(f)
"""

"""
向量化函数
"""


def f(x, y):
    if y == 0:
        return np.nan
    return x / y


df = pd.DataFrame(
    {
        'a': [10, 20, 30],
        'b': [40, 0, 60]
    }
)

# print(f(df['a'], df['b']))
# 上述代码会报错，因为y==0中，y为向量而0为标量。

# 修改如下：通过 np.vectorize() 将函数向量化进行计算
f_vec = np.vectorize(f)
print(f_vec(df['a'], df['b']))
print()


# 也可以使用 @np.vectorize 装饰器将函数向量化
@np.vectorize
def f(x, y):
    if y == 0:
        return np.nan
    return x / y


df = pd.DataFrame(
    {
        "a": [10, 20, 30],
        "b": [40, 0, 60]
    }
)
print(f(df["a"], df["b"]))
