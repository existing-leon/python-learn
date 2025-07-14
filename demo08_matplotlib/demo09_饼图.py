import numpy as np
import matplotlib

matplotlib.use('TkAgg')  # 使用 TkAgg 后端
import matplotlib.pyplot as plt

y = np.array([35, 25, 25, 15])

# # 案例一：最基础的样子
# plt.pie(y)


# # 案例二：设置饼图的各个扇形的标签与颜色
# plt.pie(y, labels=['A', 'B', 'C', 'D'],  # 设置饼图标签
#         colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"]  # 设置饼图颜色
#         )
# plt.title('Runoob Pie Test')  # 设置标题


# # 案例三：突出显示第二个扇形, 并格式化输出百分比
# # 数据
# sizes = [15, 30, 45, 10]
# # 饼图的标签
# labels = ['A', 'B', 'C', 'D']
# # 饼图的颜色
# colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
# # 突出显示第二个扇形
# explode = (0, 0.1, 0, 0)
# # 绘制饼图
# plt.pie(sizes,
#         explode=explode,
#         labels=labels,
#         colors=colors,
#         autopct='%1.1f%%',
#         shadow=True,
#         startangle=90
#         )
# # 标题
# plt.title('Runoob Pie Test')


# 案例四：默认情况下，第一个扇形的绘制是从 x 轴开始并逆时针移动
plt.pie(y,
        labels=['A', 'B', 'C', 'D'],  # 设置饼图标签
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"],  # 设置饼图颜色
        explode=(0, 0.2, 0, 0),  # 第二部分突出显示, 值越大, 距离中心越远
        autopct='%.1f%%'
        )
plt.title('Runoob Pie Test')

plt.show()
