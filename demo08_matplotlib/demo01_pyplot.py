import numpy as np
import matplotlib

matplotlib.use('TkAgg')  # 使用 TkAgg 后端
import matplotlib.pyplot as plt

# # 通过两个坐标 (0,0) 到 (6,100) 来绘制一条线:
# xpoints = np.array([0, 6])
# ypoints = np.array([6, 100])
#
# plt.plot(xpoints, ypoints)
# plt.show()


# # 如果我们只想绘制两个坐标点，而不是一条线，可以使用 o 参数，表示一个实心圈的标记
# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])
#
# plt.plot(xpoints, ypoints, 'o')
# plt.show()


# # 我们也可以绘制任意数量的点，只需确保两个轴上的点数相同即可。
# # 绘制一条不规则线，坐标为 (1, 3) 、 (2, 8) 、(6, 1) 、(8, 10)，
# # 对应的两个数组为：[1, 2, 6, 8] 与 [3, 8, 1, 10]。
# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])
#
# plt.plot(xpoints, ypoints)
# plt.show()


# # 如果我们不指定 x 轴上的点，则 x 会根据 y 的值来设置为 0, 1, 2, 3..N-1
# ypoints = np.array([3, 10])
# plt.plot(ypoints)
# plt.show()
# # 以上结果可以看出 x 的值默认设置为 [0, 1]


# ypoints = np.array([3, 8, 1, 10, 5, 7])
#
# plt.plot(ypoints)
# plt.show()
# # 从上图可以看出 x 的值默认设置为 [0, 1, 2, 3, 4, 5]。


x = np.arange(0, 4 * np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)
plt.plot(x, y, x, z)
plt.show()
