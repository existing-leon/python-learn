import numpy as np

# 使用标量类型
dt1 = np.dtype(np.int32)
print(dt1)

# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2', 'i4', 'i8'代替
dt2 = np.dtype('i4')
print(dt2)

# 字节顺序标注
dt3 = np.dtype('<i4')
print(dt3)

# 首先创建结构化数据类型
dt4 = np.dtype([('age', np.int8)])
print(dt4)

# 将数据类型应用于 ndarray对象
dt5 = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt5)
print(a)

# 类型字段名可以用于存取实际的age列
dt6 = np.dtype([('age', np.int8)])
b = np.array([(10,), (20,), (30,)], dtype=dt6)
print(b['age'])

#
student1 = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student1)

#
student2 = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
c = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student2)
print(c)


