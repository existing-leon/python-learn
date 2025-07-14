import numpy as np
import matplotlib

matplotlib.use('TkAgg')  # 使用 TkAgg 后端
import matplotlib.pyplot as plt

# ypoints = np.array([1, 3, 4, 5, 8, 9, 6, 1, 3, 4, 5, 2, 4])
#
# # 定义了实心圆标记
# # plt.plot(ypoints, marker='o')
# # 定义了 * 标记
# # plt.plot(ypoints, marker='*')
# # 定义了 下箭头
# plt.plot(ypoints, marker=matplotlib.markers.CARETDOWNBASE)
# plt.show()


# # fmt 参数
# ypoints = np.array([6, 2, 13, 10])
#
# plt.plot(ypoints, 'o:r')
# plt.show()

# 设置标记大小
ypoints = np.array([6, 2, 13, 10])
# 仅设置标记大小
# plt.plot(ypoints, marker='o', ms=20)
# 设置标记外边框颜色
# plt.plot(ypoints, marker='o', ms=20, mec='r')
# 设置标记内部颜色
# plt.plot(ypoints, marker='o', ms=20, mfc='r')
# 自定义标记内部与边框颜色
plt.plot(ypoints, marker='o', ms=20, mec='#4CAF50', mfc='#4CAF50')
plt.show()
