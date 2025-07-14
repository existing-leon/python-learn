import numpy as np
import matplotlib

matplotlib.use('TkAgg')  # 使用 TkAgg 后端
import matplotlib.pyplot as plt

## 案例一
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
#
# # 设置图标大小
# sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90])
#
# # 自定义颜色
# colors = np.array(["red", "green", "black", "orange", "purple", "beige", "cyan", "magenta"])
#
# plt.scatter(x, y, s=sizes, c=colors)


## 案例二：设置两组散点图
# x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
# y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
# plt.scatter(x, y, color='hotpink')
#
# x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
# y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
# plt.scatter(x, y, color='#88c999')


# ## 案例三：使用随机数来生成散点图
# # 随机数生成器的种子
# np.random.seed(19680801)
#
# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
# area = (30 * np.random.rand(N)) ** 2  # 0 to 15 point radii
#
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)  # 设置颜色及透明度
#
# plt.title("RUNOOB Scatter Test")  # 设置标题


## 案例四：颜色条
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

# plt.scatter(x, y, c=colors, cmap='viridis')
# 换一个颜色条参数, cmap参数的值改一下 afmhot_r
plt.scatter(x, y, c=colors, cmap='PiYG_r')

# 显示颜色条
plt.colorbar()

plt.show()
