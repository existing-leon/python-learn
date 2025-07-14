import numpy as np
import pandas as pd
import matplotlib
from PIL import Image

matplotlib.use('TkAgg')  # 使用 TkAgg 后端
import matplotlib.pyplot as plt

# # 案例一
# # 创建一个二维的图像数据
# img_data = np.random.random((100, 100))
#
# # 显示图像
# plt.imshow(img_data)
#
# # 保存图像到磁盘上
# plt.imsave('runoob-test.png', img_data)

# 案例二：将一个灰度图像和一幅彩色图像保存到当前目录上
# 创建一幅灰度图像
img_gray = np.random.random((100, 100))

# 创建一幅彩色图像
img_color = np.zeros((100, 100, 3))
img_color[:, :, 0] = np.random.random((100, 100))
img_color[:, :, 1] = np.random.random((100, 100))
img_color[:, :, 2] = np.random.random((100, 100))

# 显示灰度图像
plt.imshow(img_gray, cmap='gray')

# 保存灰度图像到磁盘上
plt.imsave('test_gray.png', img_gray, cmap='gray')

# 显示彩色图像
plt.imshow(img_color)

# 保存彩色图像到磁盘上
plt.imsave('test_color.jpg', img_color)
