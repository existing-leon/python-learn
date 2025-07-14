import numpy as np

a = np.array([1, 2, 3, 4, 5])

# 保存到 outfile.npy 文件上
np.save('./data/outfile.npy', a)

# 保存到 outfile2.npy 文件上, 如果文件路径末尾没有扩展名 .npy, 该扩展名会被自动加上
np.save('./data/outfile2', a)

# 使用 load() 函数来读取数据就可以正常显示了
b = np.load('./data/outfile.npy')
print(b)

# savez
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
# c 使用了关键字参数 sinarray
np.savez('./data/runoob.npz', a, b, sin_array=c)
r = np.load('./data/runoob.npz')
print(r.files)  # 查看各个数组的名称
print(r["arr_0"])
print(r["arr_1"])
print(r["sin_array"])

# savetxt()
a = np.array([1, 2, 3, 4, 5])
np.savetxt('./data/out.txt', a)
b = np.loadtxt('./data/out.txt')
print(b)
# 使用 delimiter 参数
a = np.arange(0, 10, 0.5).reshape(4, -1)
# 改为保存为整数, 以逗号分隔
np.savetxt('./data/out.txt', a, fmt='%d', delimiter=',')
b = np.loadtxt('./data/out.txt', delimiter=',')
print(b)
