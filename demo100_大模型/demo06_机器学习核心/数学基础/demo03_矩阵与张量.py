import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 3, 7], [5, 0, 2]])

print(A.shape)
print()
print(A.T)
print()
print(A + B)
print()

print((A + B).T)
print()
print(A.T + B.T)
print()

print(A)
print()
print(f'A * 3 ==> \n{A * 3}')
print()
print(B)
print()
# 哈达玛积
print(f' A * B ==> \n{A * B}')
print()
# 矩阵乘法
print(f' A 与 B 的乘法 ==> \n{A.dot(B.T)}')
print()
print(f' A 与 B 的乘法 ==> \n{A @ B.T}')
print()
print(A.flatten())
print()
# 矩阵内积
print(np.sum(A * B))
print()
# 克罗内克积
print(np.kron(A, B))
print()
# 求逆
C = np.array([[1, 2], [3, 5]])
C_inv = np.linalg.inv(C)
C_inv = np.around(C_inv).astype(int)
print(C_inv)
print(C @ C_inv)
print()
# 非方阵可以求伪逆
print(np.linalg.pinv(A))
