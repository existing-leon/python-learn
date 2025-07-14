import time
import tkinter as tk

from PIL import Image, ImageTk

# 定义 RGB 颜色值（范围为 0 到 255）
r, g, b = 51, 153, 204

# for r in range(30, 38):
#     for g in range(34, 40):
#         for b in range(78, 84):

# check_have_fudai 方法 颜色提取
for r in range(194, 200):
    for g in range(187, 193):
        for b in range(241, 247):
            print(f'r ==> {r}, g ==> {g}, b ==> {b}')

            # 创建一个 100x100 的图像，填充指定的 RGB 颜色
            image = Image.new('RGB', (100, 100), (r, g, b))

            # 创建 Tkinter 窗口
            root = tk.Tk()

            # 将 PIL 图像转换为 Tkinter 可以显示的 PhotoImage 对象
            photo = ImageTk.PhotoImage(image)

            # 创建一个 Label 组件来显示图像
            label = tk.Label(root, image=photo)
            label.pack()

            # 设置显示时间（单位：秒）
            display_time = 0.1

            # 设置窗口位置和大小，这里将窗口定位在屏幕坐标 (200, 200) 处，大小为 100x100
            window_width = 100
            window_height = 100
            x_position = 200
            y_position = 200
            root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


            # 定义一个函数用于关闭窗口
            def close_window():
                root.destroy()


            # 在指定时间后调用关闭窗口的函数
            root.after(int(display_time * 1000), close_window)

            # 运行 Tkinter 主循环
            root.mainloop()
