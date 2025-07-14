import numpy as np
import matplotlib

matplotlib.use('TkAgg')  # 使用 TkAgg 后端
import matplotlib.pyplot as plt

# 第一个例子
# x = np.arange(1, 11)
# y = 2 * x + 5
# plt.title('Matplotlib data')
# plt.xlabel('x axis caption')
# plt.ylabel('y axis caption')
# plt.plot(x, y)
# plt.show()


# # fname 为 你下载的字体库路径，注意 SourceHanSansSC-Bold.otf 字体的路径
# zhfont1 = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf")
#
# x = np.arange(1, 11)
# y = 2 * x + 5
# plt.title('教程 - 测试', fontproperties=zhfont1)
#
# # fontproperties设置中文显示, fontsize 设置字体大小
# plt.xlabel('x 轴', fontproperties=zhfont1)
# plt.ylabel('y 轴', fontproperties=zhfont1)
# plt.plot(x, y)
# plt.show()

# 使用 蓝色-圆 替代线条
# x = np.arange(1, 11)
# y = 2 * x + 5
# plt.title("Matplotlib data")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x, y, "ob")
# plt.show()

# # 绘制正弦波
# # 计算正弦曲线上点的 x 和 y 坐标
# x = np.arange(0, 3 * np.pi, 0.1)
# y = np.sin(x)
# plt.title("sine wave form")
# # 使用 matplotlib 来绘制点
# plt.plot(x, y)
# plt.show()

# # subplot() 函数允许你在同一图中绘制不同的东西
# # 计算正弦和余弦曲线上的点的 x 和 y 坐标
# x = np.arange(0, 3 * np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)
# # 建立 subplot 网格，高为 2，宽为 1
# # 激活第一个 subplot
# plt.subplot(2, 1, 1)
# # 绘制第一个图像
# plt.plot(x, y_sin)
# plt.title('Sine')
# # 将第二个 subplot 激活，并绘制第二个图像
# plt.subplot(2, 1, 2)
# plt.plot(x, y_cos)
# plt.title('Cosine')
# # 展示图像
# plt.show()

# # pyplot 子模块提供 bar() 函数来生成条形图
# x = [5, 8, 10]
# y = [12, 16, 6]
# x2 = [6, 9, 11]
# y2 = [6, 15, 7]
# plt.bar(x, y, align='center')
# plt.bar(x2, y2, color='g', align='center')
# plt.title('Bar graph')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# plt.show()

a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
np.histogram(a, bins=[0, 20, 40, 60, 80, 100])
hist, bins = np.histogram(a, bins=[0, 20, 40, 60, 80, 100])
print(hist)
print(bins)

a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
plt.hist(a, bins=[0, 20, 40, 60, 80, 100])
plt.title("histogram")
plt.show()
