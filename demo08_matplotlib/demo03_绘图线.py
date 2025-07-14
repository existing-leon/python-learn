import numpy as np
import matplotlib

matplotlib.use('TkAgg')  # 使用 TkAgg 后端
import matplotlib.pyplot as plt

ypoints = np.array([6, 2, 13, 10])

## 线的形状
# 使用 linestyle 参数
# plt.plot(ypoints, linestyle='dotted')

# 使用 linestyle 参数的简写 ls
# plt.plot(ypoints, ls='dotted')

# 使用类型的简写
# plt.plot(ypoints, ls='-.')

## 线的颜色
# 使用颜色参数
# plt.plot(ypoints, color='r')

# 自定义颜色
# plt.plot(ypoints, color='#8FBC8F')
# plt.plot(ypoints, color='SeaGreen')

## 线的宽度
# plt.plot(ypoints, linewidth='12.5')


## 多条线绘制
# x 值使用默认值
# y1 = np.array([3, 7, 5, 9])
# y2 = np.array([6, 2, 13, 10])
# 
# plt.plot(y1)
# plt.plot(y2)

# x 值使用自定义值
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 7, 5, 9])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 13, 10])

plt.plot(x1, y1, x2, y2)

plt.show()
