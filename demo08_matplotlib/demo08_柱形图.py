import numpy as np
import matplotlib

matplotlib.use('TkAgg')  # 使用 TkAgg 后端
import matplotlib.pyplot as plt

x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
y = np.array([12, 22, 6, 18])

# 常规的矩形图
# plt.bar(x, y)

# 垂直方向的柱形图
# plt.barh(x, y)

# 设置柱形图的颜色
# plt.bar(x, y, color='#4CAF50')

# 自定义各个柱形的颜色
# plt.bar(x, y, color=["#4CAF50", "red", "hotpink", "#556B2F"])

# 设置柱形图宽度, bar() 方法使用 width 设置, barh() 方法使用 height 设置 height
# plt.bar(x, y, width=0.1)
plt.barh(x, y, height=0.1)

plt.show()
