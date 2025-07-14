import numpy as np
import pandas as pd
import matplotlib
from PIL import Image

matplotlib.use('TkAgg')  # 使用 TkAgg 后端
import matplotlib.pyplot as plt

# 读取图像文件，下载地址：https://static.jyshare.com/images/demo/map.jpeg
img = plt.imread('map.jpeg')

# 显示图像
plt.imshow(img)
plt.show()
