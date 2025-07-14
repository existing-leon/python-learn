import numpy as np

# 连接
print(f'连接两个字符串：{np.char.add(["hello"], ["hxk"])}')
print(f'连接示例：{np.char.add(["hello ", "hxk "], ["abc", "edf"])}')

# 多重连接
print(f'多重连接：{np.char.multiply("Runoob ", 3)}')

# 填充
# np.char.center(str , width,fillchar) ：
# str: 字符串，width: 长度，fillchar: 填充字符
print(np.char.center('Runoob', 20, fillchar='*'))

# 字符串首字母大写
print(np.char.capitalize('runoob'))

# 将字符串中每个单词的首字母大写
print(np.char.title('i like runoob'))

# 对数组每个元素都转换为小写
# 操作数组
print(np.char.lower(['RUNOOB', 'GOOGLE']))
# 操作字符串
print(np.char.lower('RUNOOB'))

# 对数组每个元素都转换为大写
# 操作数组
print(np.char.upper(['runoob', 'google']))
# 操作字符串
print(np.char.upper('runoob'))

# 分割
# 分隔符默认为空格
print(np.char.split('i like runoob'))
# 指定分隔符
print(np.char.split('www.runoob.com', sep='.'))

# 以换行符作为分隔符
print(np.char.splitlines('i\nlike runoob?'))
print(np.char.splitlines('i\rlike runoob?'))

# 移除开头或结尾处的特定字符
# 移除字符串头尾的 a 字符
print(np.char.strip('ashok arunoob', 'a'))
# 移除数组元素头尾的 a 字符
print(np.char.strip(['arunooba', 'admin', 'java'], 'a'))

# 连接
# 操作字符串
print(np.char.join(':', 'runoob'))
# 指定多个分隔符操作数组元素
print(np.char.join([':', '-'], ['runoob', 'google']))

# 替换
print(np.char.replace('i like runoob', 'oo', 'cc'))

# 编码
a = np.char.encode('runoob', 'cp500')
print(a)

# 解码
a = np.char.encode('runoob', 'cp500')
print(a)
print(np.char.decode(a, 'cp500'))
