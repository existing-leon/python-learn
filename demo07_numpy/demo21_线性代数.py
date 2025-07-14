import numpy.matlib
import numpy as np

# 数组的点积
a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])
print(np.dot(a, b))

# 向量的点积
# 将数组展开计算内积
print(np.vdot(a, b))

# 一维数组的向量内积
print(np.inner(np.array([1, 2, 3]), np.array([0, 1, 0])))
# 多维数组
a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])
print(np.inner(a, b))
