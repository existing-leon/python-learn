num1 = 1_000_000_000_000_000
print(num1)

num1 = 0.1
num2 = 0.2
print(num1 + num2)

# 解决上述问题
from decimal import Decimal

num3 = Decimal('0.1')
num4 = Decimal('0.2')
print(num3 + num4)

# 两个整型进行除法运算结果也是浮点数
num1 = 9
num2 = 1
print(num1 / num2)

# 逻辑运算符
x = False
y = 37
print(x and y)

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i} x {j} = {i * j}', end='\t')
    print()

print()

# zip()函数可以将多个可迭代对象对应元素打包成为一个个元组
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
zipped = zip(list1, list2)
print(list(zipped))
print()

# 元组
tuple_generator = (x for x in range(10))
print(tuple_generator)
tuple1 = tuple(tuple_generator)
print(tuple1)
print()


# 可变参数
# * 会以元组传入, ** 会以字典传入
def printInfo(num, **vardict):
    print(num)
    print(vardict)


printInfo(10, key1=20, key2=30)
print()


# 递归
def get_factorial(n):
    return n * get_factorial(n - 1) if n > 1 else 1


print(get_factorial(5))
print()

# 路径
import os

for root, dirs, files in os.walk(os.getcwd()):
    print('当前路径：', root)
    print('目录：', dirs)
    print('文件：', files)
    print()

# 异常
try:
    try:
        try:
            print(1 / 0)
        except NameError as e:
            print("第三层", e)
    except TypeError as e:
        print("第二层", e)
except Exception as e:
    print("第一层", type(e), e)

print()

# 模块导入
import math

print(dir(math))
print()


# 生成器
def fibo(n):
    """ 斐波那契数列 """
    a, b, counter = 0, 1, 0
    while counter < n:
        yield b
        a, b, counter = b, a + b, counter + 1
    return 'done'


f = fibo(10)
try:
    while True:
        print(next(f))
except StopIteration as result:
    print('StopIteration', result)

print()


# ==============================================
# 闭包
def linear(a, b):
    def inner(x):
        return a * x + b

    return inner


y1 = linear(1, 2)
objects = y1.__closure__
print(objects)
print(objects[0].cell_contents)
print(objects[1].cell_contents)
# ==============================================
# 装饰器
# 多个装饰器装饰的：离函数最近的装饰器先装饰，然后外面的装饰器再进行装饰
from math import sqrt


def decorator(f):
    def inner(x):
        x = abs(x)  # 绝对值
        return f(x)

    return inner


@decorator
def func(x):
    """ 开根号 """
    return sqrt(x)


# 先取绝对值, 然后执行开根号操作
print(func(-4))
