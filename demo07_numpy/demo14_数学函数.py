import numpy as np

a = np.array([0, 30, 45, 60, 90])
# 通过乘以 pi / 180 转化为弧度
print(f'不同角度的正弦值：{np.sin(a * np.pi / 180)}')
print(f'数组中角度的余弦值：{np.cos(a * np.pi / 180)}')
print(f'数组中角度的正切值：{np.tan(a * np.pi / 180)}')

print()

# 反三角函数
a = np.array([0, 30, 45, 60, 90])
sin = np.sin(a * np.pi / 180)
print(f'含有正弦值的数组：{sin}')
inv = np.arcsin(sin)
print(f'计算角度的反正弦, 返回值以弧度为单位：{inv}')
print(f'通过转化为角度制来检查结果：{np.degrees(inv)}\n')
cos = np.cos(a * np.pi / 180)
print(f'含有余弦值的数组：{cos}')
inv = np.arccos(cos)
print(f'计算角度的反余弦, 返回值以弧度为单位：{inv}')
print(f'通过转化为角度制来检查结果：{np.degrees(inv)}\n')
tan = np.tan(a * np.pi / 180)
print(f'含有正切值的数组：{tan}')
inv = np.arctan(tan)
print(f'计算角度的反正切, 返回值以弧度为单位：{inv}')
print(f'通过转化为角度制来检查结果：{np.degrees(inv)}\n')

# 舍入函数
a = np.array([1.0, 5.55, 123, 0.567, 25.532])
print(f'原数组：{a}')
print(f'舍入后：{np.around(a)}')
print(f'舍入后：{np.around(a, decimals=1)}')
print(f'舍入后：{np.around(a, decimals=-1)}')

# 向下取整
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print(f'\n提供的数组：{a}')
print(f'修改后的数组：{np.floor(a)}')

# 向上取整
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print(f'\n提供的数组：{a}')
print(f'修改后的数组：{np.ceil(a)}')
