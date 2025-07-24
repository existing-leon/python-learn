""""""
"""
Matplotlib是一个Python绘图库，广泛用于创建各种类型的静态、动态和交互式图表。它是数据科学、机器学习、工程和科学计算领域中常用的绘图工具之一。
	支持多种图表类型：折线图（Line plots）、散点图（Scatter plots）、柱状图（Bar charts）、直方图（Histograms）、饼图（Pie charts）、热图（Heatmaps）、箱型图（Box plots）、极坐标图（Polar plots）、3D图（3D plots，配合 mpl_toolkits.mplot3d）。
	高度自定义：允许用户自定义图表的每个部分，包括标题、轴标签、刻度、图例等。        支持多种颜色、字体和线条样式。提供精确的图形渲染控制，如坐标轴范围、图形大小、字体大小等。
	兼容性：与NumPy、Pandas等库紧密集成，特别适用于绘制基于数据框和数组的数据可视化。可以输出到多种格式（如PNG、PDF、SVG、EPS等）。
	交互式绘图：在Jupyter Notebook 中，Matplotlib支持交互式绘图，可以动态更新图表。支持图形缩放、平移等交互操作。
	动态图表：可以生成动画（使用FuncAnimation类），为用户提供动态数据的可视化。
2）不同开发环境下显示图形
	在一个脚本文件中使用Matplotlib，那么显示图形的时候必须使用plt.show()。
	在Notebook中使用Matplotlib，运行命令之后在每一个Notebook的单元中就会直接将PNG格式图形文件嵌入在单元中。

Matplotlib有两种画图接口：一个是便捷的MATLAB风格的有状态的接口，另一个是功能更强大的面向对象接口。
"""

"""
状态接口
"""
import matplotlib
import numpy as np
import pandas as pd

matplotlib.use('TkAgg')  # 或 'Qt5Agg', 'Agg'（Agg 无窗口，用于保存图像）
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)  # 创建x轴的数据
y1 = np.sin(x)  # 创建y轴的数据
y2 = np.cos(x)  # 创建y轴的数据

plt.figure(figsize=(10, 6))  # 创建画布，并指定画布大小 10*6英寸

plt.subplot(2, 1, 1)  # 创建2行1列个子图，并指定第1个子图
plt.xlim(0, 10)  # 设置x轴的范围
plt.ylim(-1, 1)  # 设置y轴的范围
plt.xlabel("x")  # 设置x轴的标签
plt.ylabel("sin(x)")  # 设置y轴的标签
plt.title("sin")  # 设置子图的标题
plt.plot(x, y1)  # 绘制曲线

plt.subplot(2, 1, 2)  # 创建2行1列个子图，并指定第2个子图
plt.xlim(0, 10)  # 设置x轴的范围
plt.ylim(-1, 1)  # 设置y轴的范围
plt.xlabel("x")  # 设置x轴的标签
plt.ylabel("cos(x)")  # 设置y轴的标签
plt.title("cos")  # 设置子图的标题
plt.plot(x, y2)

plt.show()  # 显示图像

"""
面向对象接口
"""
x = np.linspace(0, 10, 100)  # 创建x轴的数据
y1 = np.sin(x)  # 创建y轴的数据
y2 = np.cos(x)  # 创建y轴的数据

fig, ax = plt.subplots(2, figsize=(10, 6))  # 创建画布，并指定画布大小

ax[0].set_xlim(0, 10)  # 设置x轴的范围
ax[0].set_ylim(-1, 1)  # 设置y轴的范围
ax[0].set_xlabel("x")  # 设置x轴的标签
ax[0].set_ylabel("sin(x)")  # 设置y轴的标签
ax[0].set_title("sin")  # 设置子图的标题
ax[0].plot(x, y1)  # 绘制曲线

ax[1].plot(x, y2)  # 绘制曲线
ax[1].set_xlim(0, 10)  # 设置x轴的范围
ax[1].set_ylim(-1, 1)  # 设置y轴的范围
ax[1].set_xlabel("x")  # 设置x轴的标签
ax[1].set_ylabel("cos(x)")  # 设置y轴的标签
ax[1].set_title("cos")  # 设置子图的标题

plt.show()

"""
单变量可视化
使用weather（天气）数据集。其中包含6个字段：
	date：日期，年-月-日格式。
	precipitation：降水量。
	temp_max：最高温度。
	temp_min：最低温度。
	wind：风力。
	weather：天气状况。
"""
from matplotlib import rcParams

rcParams["font.sans-serif"] = ["SimHei"]  # 指定中文字体
rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

df = pd.read_csv("data/weather.csv")
df.info()
print()

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.hist(df["precipitation"], bins=5)  # 绘制直方图，将降水量均匀分为5组
ax1.set_xlabel("降水量")
ax1.set_ylabel("出现频次")
plt.show()

"""
多变量可视化
1）双变量
使用散点图呈现降水量随最高气温变化的大致趋势。
"""
rcParams["font.sans-serif"] = ["SimHei"]  # 指定中文字体
rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

df = pd.read_csv("data/weather.csv")
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.scatter(df["temp_max"], df["precipitation"])  # 绘制散点图，横轴为最高气温，纵轴为降水量
ax1.set_xlabel("最高气温")
ax1.set_ylabel("降水量")
plt.show()

"""
2）多变量
使用散点图呈现降水量随最高气温变化的大致趋势，用不同颜色区分不同年份的数据。
"""

rcParams["font.sans-serif"] = ["SimHei"]  # 指定中文字体
rcParams["axes.unicode_minus"] = False  # 解决负号显示问题


def year_color(x):
    """添加一列，为不同年份的数据添加不同的颜色"""
    match x.year:
        case 2012:
            return "r"
        case 2013:
            return "g"
        case 2014:
            return "b"
        case 2015:
            return "k"


df = pd.read_csv("data/weather.csv")
df["date"] = pd.to_datetime(df["date"])
df["color"] = df["date"].apply(year_color)
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
# 绘制散点图，横轴为最高气温，纵轴为降水量
# c设置颜色,alpha设置透明度
ax1.scatter(df["temp_max"], df["precipitation"], c=df["color"], alpha=0.5)
ax1.set_xlabel("最高气温")
ax1.set_ylabel("降水量")
plt.show()
