import numpy as np

a = np.array([1, 256, 8755], dtype=np.int16)
print(f'原始数组为：\n{a}')
print(f'以16进制表示内存中的数据：{map(hex, a)}')
# byteswap() 函数通过传入 true 来原地交换
print(f'调用 byteswap() 函数：{a.byteswap(True)}')
print(f'16进制形式：{map(hex, a)}')
