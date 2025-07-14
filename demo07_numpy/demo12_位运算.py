import numpy as np

arr1 = np.array([True, False, True], dtype=bool)
arr2 = np.array([False, True, False], dtype=bool)

result_and = np.bitwise_and(arr1, arr2)
result_or = np.bitwise_or(arr1, arr2)
result_xor = np.bitwise_xor(arr1, arr2)
result_not = np.bitwise_not(arr1)

print(f'AND: {result_and}')
print(f'OR: {result_or}')
print(f'XOR: {result_xor}')
print(f'NOT: {result_not}')

# 按位取反
arr_invert = np.invert(np.array([1, 2], dtype=np.int8))
print(f'Invert：', arr_invert)

# 左移位运算
arr_left_shift = np.left_shift(5, 2)
print(f'LeftShift: {arr_left_shift}')

# 右移位运算
arr_right_shift = np.right_shift(10, 1)
print(f'RightShift: {arr_right_shift}')

# bitwise_and
print(f'\n13 和 17 的二进制形式：{bin(13), bin(17)}')
print(f'13 和 17 的位与：{np.bitwise_and(13, 17)}')

# bitwise_or
print(f'13 和 17 的位与：{np.bitwise_or(13, 17)}')

# invert
print(f'\n13 的位反转, 其中 ndarray 的 dtype 是 uint8：{np.invert(np.array([13], dtype=np.uint8))}')
print(f'13 的二进制表示：{np.binary_repr(13, width=8)}')
print(f'242 的二进制表示：{np.binary_repr(242, width=8)}')

# left_shift
print(f'\n将 10 左移两位：{np.left_shift(10, 2)}')
print(f'10 的二进制表示：{np.binary_repr(10, width=8)}')
print(f'40 的二进制表示：{np.binary_repr(40, width=8)}')

# right_shift
print(f'\n将 40 左移两位：{np.right_shift(40, 2)}')
print(f'40 的二进制表示：{np.binary_repr(40, width=8)}')
print(f'10 的二进制表示：{np.binary_repr(10, width=8)}')

