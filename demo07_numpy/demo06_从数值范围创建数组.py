import numpy as np

x = np.arange(5)
print(x)

# 设置返回类型为 float
x = np.arange(5, dtype=float)
print(x)

# 设置了起始值、终止值及步长
x = np.arange(10, 20, 2)
print(x)

# ---------------

# 设置起始点为1, 终止点为10, 数列个数为10
a = np.linspace(1, 10, 10)
print(a)

# 设置元素全部是1的等差数列
a = np.linspace(1, 1, 10)
print(a)

# 将 endpoint 设为 false, 不包含终止值
a = np.linspace(10, 20, 5, endpoint=False)
print(a)

# 将 endpoint 设置为 true, 则包含 20
a = np.linspace(10, 20, 6, endpoint=True)
print(a)

# 显示间距
a = np.linspace(1, 10, 10, retstep=True)
print(a)
# 拓展
b = np.linspace(1, 10, 10).reshape([10, 1])
print(b)

# ---------------

# 默认底数是 10
a = np.logspace(1.0, 2.0, num=10)
print(a)

# 将对数的底数设置为2
a = np.logspace(0, 9, 10, base=2)
print(a)
