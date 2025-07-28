import numpy as np
import matplotlib

matplotlib.use('TkAgg')  # 需在导入pyplot前设置
import matplotlib.pyplot as plt

# 生成数据 y = sinx
x = np.arange(0, 6, 0.1)
y = np.sin(x)
# print(x, y)


# # 画图
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('y = sin(x)')
# plt.show()
#
# # 画出导数的图像 y' = cos(x)
y1 = np.cos(x)
# plt.plot(x, y1)
# plt.xlabel('x')
# plt.ylabel('y1')
# plt.title('y1 = cos(x)')
# plt.show()

# 在同一个图像中显示
plt.plot(x, y, label = 'y = sin(x)')
plt.plot(x, y1, label = 'y = cos(x)', linestyle = '--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = sin(x)')
plt.legend()
plt.show()