import numpy as np
import matplotlib

matplotlib.use('TkAgg')  # 使用 TkAgg 后端
import matplotlib.pyplot as plt

# fname 为 你下载的字体库路径，注意 SourceHanSansSC-Bold.otf 字体的路径
zhfont1 = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf")

x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
plt.plot(x, y)

plt.xlabel('x -label')
plt.ylabel('y -label')

# 支持中文显示
plt.title('菜鸟教程 - 测试', fontproperties=zhfont1)

# 所有参数全部都是默认
# plt.grid()

# axis 参数使用 x，设置 x 轴方向显示网格线
# plt.grid(axis='x')

# 添加一个自定义的网格线
plt.grid(color='r', linestyle='--', linewidth=0.5)

plt.show()
