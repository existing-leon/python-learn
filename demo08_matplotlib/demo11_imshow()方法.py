import numpy as np
import pandas as pd
import matplotlib
from PIL import Image

matplotlib.use('TkAgg')  # 使用 TkAgg 后端
import matplotlib.pyplot as plt

# # 案例一：显示灰度图像
# # 生成一个二维随机数组
# img = np.random.rand(10, 10)
# # print(img)
# # 绘制灰度图像
# plt.imshow(img, cmap='gray')  # 设置了 cmap 参数为 gray，这意味着将使用灰度颜色映射显示图像


# # 案例二：显示彩色图像
# # 生成一个随机的彩色图像
# img = np.random.rand(10, 10, 3)
#
# # 绘制彩色图像
# plt.imshow(img)  # 由于彩色图像是三维数组，因此不需要设置 cmap 参数


# # 案例三：显示热力图
# # 生成一个二维随机数组
# data = np.random.rand(10, 10)
#
# # 绘制热力图
# plt.imshow(data, cmap='hot')  # 设置了 cmap 参数为 hot，这意味着将使用热度颜色映射显示图像
#
# # 添加一个颜色条, 以便查看数据的值与颜色之间的关系
# plt.colorbar()


# # 案例四：显示地图
# # 加载地图图像
# img = Image.open('map.jpeg')
#
# # 转换为数组
# data = np.array(img)
#
# # 绘制地图
# plt.imshow(data)
#
# # 隐藏坐标轴
# plt.axis('off')


# # 案例五：显示矩阵
# # 生成一个随机矩阵
# data = np.random.rand(10, 10)
#
# # 绘制矩阵
# plt.imshow(data)


# 更多
# 以下创建了一个 4 * 4 的二维 numpy 数组, 并对其进行了三种不同的 imshow 图像显示
# 第一张展示了灰度的色彩映射方式, 并且没有进行颜色的混合（blending）
# 第二张展示了使用viridis颜色映射的图像, 同样没有进行颜色的混合
# 第三张展示了使用viridis颜色映射的图像, 并且使用了双立方插值方法进行颜色混合
n = 4

# 创建一个 n * n 的二维 numpy 数组
a = np.reshape(np.linspace(0, 1, n ** 2), (4, 4))

# 第一张图展示灰度的色彩映射方式，并且没有进行颜色的混合
plt.subplot(131)
plt.imshow(a, cmap='gray', interpolation='nearest')
plt.xticks(range(n))
plt.yticks(range(n))
# 灰度映射，无混合
plt.title('Gray color map, no blending', y=1.02, fontsize=12)

# 第二张图展示使用viridis颜色映射的图像，同样没有进行颜色的混合
plt.subplot(132)
plt.imshow(a, cmap='viridis', interpolation='nearest')
plt.yticks([])
plt.xticks(range(n))
# Viridis映射，无混合
plt.title('Viridis color map, no blending', y=1.02, fontsize=12)

# 第三张图展示使用viridis颜色映射的图像，并且使用了双立方插值方法进行颜色混合
plt.subplot(133)
plt.imshow(a, cmap='viridis', interpolation='bicubic')
plt.yticks([])
plt.xticks(range(n))
# Viridis 映射，双立方混合
plt.title('Viridis color map, bicubic blending', y=1.02, fontsize=12)

# 显示图像
plt.show()
