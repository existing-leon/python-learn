""""""
"""
pandas提供了非常方便的绘图功能，可以直接在DataFrame或Series上
调用plot()方法来生成各种类型的图表。底层实现依赖于Matplotlib，
pandas的绘图功能集成了许多常见的图形类型，易于使用。
"""
"""
单变量可视化
使用sleep（睡眠健康和生活方式）数据集，其中包含13个字段：
	person_id：每个人的唯一标识符。
	gender：个人的性别（男/女）。
	age：个人的年龄（以岁为单位）。
	occupation：个人的职业或就业状况（例如办公室职员、体力劳动者、学生）。
	sleep_duration：每天的睡眠总小时数。
	sleep_quality：睡眠质量的主观评分，范围从 1（差）到 10（极好）。
	physical_activity_level：每天花费在体力活动上的时间（以分钟为单位）。
	stress_level：压力水平的主观评级，范围从 1（低）到 10（高）。
	bmi_category：个人的 BMI 分类（体重过轻、正常、超重、肥胖）。
	blood_pressure：血压测量，显示为收缩压与舒张压的数值。
	heart_rate：静息心率，以每分钟心跳次数为单位。
	daily_steps：个人每天行走的步数。
	sleep_disorder：存在睡眠障碍（无、失眠、睡眠呼吸暂停）。
"""
import matplotlib
import numpy as np
import pandas as pd

matplotlib.use('TkAgg')  # 或 'Qt5Agg', 'Agg'（Agg 无窗口，用于保存图像）
import matplotlib.pyplot as plt

df = pd.read_csv('data/sleep.csv')
df.info()

"""
1）柱状图
柱状图用于展示类别数据的分布情况。它通过一系列矩形的高度（或长度）来展示数据值，适合对比不同类别之间的数量或频率。简单直观，容易理解和比较各类别数据。
使用柱状图展示不同睡眠时长的数量。
"""
(pd.cut(df["sleep_duration"],
        [0, 5, 6, 7, 8, 9, 10, 11, 12])
.value_counts()
.plot
.bar(
    color=["red", "green", "blue", "yellow", "cyan", "magenta", "black", "purple"]
))

plt.show()

"""
2）折线图
折线图通常用于展示连续数据的变化趋势。它通过一系列数据点连接成的线段来表示数据的变化。能够清晰地展示数据的趋势和波动。
使用折线图展示不同睡眠时长的数量。
"""
(pd.cut(df["sleep_duration"],
        [0, 5, 6, 7, 8, 9, 10, 11, 12])
 .value_counts()
 .sort_index()
 .plot())

plt.show()

"""
3）面积图
面积图是折线图的一种变体，线下的区域被填充颜色，用于强调数据的总量或变化。可以更直观地展示数据量的变化，适合用来展示多个分类的累计趋势。
使用面积图展示不同睡眠时长的数量。
"""
(pd.cut(df["sleep_duration"], [0, 5, 6, 7, 8, 9, 10, 11, 12])
 .value_counts()
 .sort_index()
 .plot
 .area())

plt.show()

"""
4）直方图
直方图用于展示数据的分布情况。它将数据范围分成多个区间，并通过矩形的高度显示每个区间内数据的频率或数量。可以揭示数据分布的模式，如偏态、峰度等。
使用直方图展示不同睡眠时长的数量。
"""
(df["sleep_duration"]
 .value_counts()
 .plot
 .hist())

plt.show()

"""
5）饼状图
饼状图用于展示一个整体中各个部分所占的比例。它通过一个圆形图形分割成不同的扇形，每个扇形的角度与各部分的比例成正比。能够快速展示各部分之间的比例关系，但不适合用于展示过多的类别或比较数值差异较小的部分。
使用饼状图展示不同睡眠时长的占比。
"""
(pd.cut(df["sleep_duration"],
        [0, 5, 6, 7, 8, 9, 10, 11, 12])
 .value_counts()
 .sort_index()
 .plot
 .pie())
plt.show()
