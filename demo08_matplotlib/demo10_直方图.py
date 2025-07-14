import numpy as np
import pandas as pd
import matplotlib

matplotlib.use('TkAgg')  # 使用 TkAgg 后端
import matplotlib.pyplot as plt

# # 案例一：演示直方图的基本构成
# # 生成一组随机数据
# data = np.random.randn(1000)
#
# # 绘制直方图
# plt.hist(data, bins=30, color='skyblue', alpha=0.8)
#
# # 设置图标属性
# plt.title('Runoob hist() Test')
# plt.xlabel('Value')
# plt.ylabel('Frequency')


# # 案例二：演示如何使用 hist() 函数绘制多个数据组的直方图, 并进行比较
# # 生成三组随机数据
# data1 = np.random.normal(0, 1, 1000)
# data2 = np.random.normal(2, 1, 1000)
# data3 = np.random.normal(-2, 1, 1000)
#
# # 绘制直方图
# plt.hist(data1, bins=30, alpha=0.5, label='Data 1')
# plt.hist(data2, bins=30, alpha=0.5, label='Data 2')
# plt.hist(data3, bins=30, alpha=0.5, label='Data 3')
#
# # 设置图标属性
# plt.title('Runoob hist() Test')
# plt.xlabel('Value')
# plt.xlabel('Frequency')
# # 显示图例
# plt.legend()


# # 案例三：结合 Pandas 来绘制直方图
# # 使用 Numpy 生成随机数
# random_data = np.random.normal(170, 10, 250)
#
# # 将数据转换为 Pandas DataFrame
# dataframe = pd.DataFrame(random_data)
#
# # 使用 Pandas hist() 方法绘制直方图
# dataframe.hist()
#
# # 设置图标属性
# plt.title('Runoob hist() Test')
# plt.xlabel('X-Value')
# plt.ylabel('Y-Value')


# 案例四：使用Pandas中的Series对象绘制直方图, 需要将数据框中的列替换为Series对象
# 生成随机数据
data = pd.Series(np.random.normal(size=100))

# 绘制直方图
# bins 参数指定了直方图中的柱子数量
plt.hist(data, bins=10)

# 设置图标属性
plt.title('Runoob hist() Test')
plt.xlabel('X-Value')
plt.ylabel('Y-Value')

# 显示图表
plt.show()