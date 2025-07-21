def karatsuba(x, y):
    """卡拉除巴算法"""
    # 将 x 和 y 转换为字符串
    x_str, y_str = str(x), str(y),
    n = max(len(x_str), len(y_str))

    # 如果存在负数, 将其转换为正数再调用 karatsuba
    if x_str[0] == '-':
        return -karatsuba(-x, y)
    if y_str == '-':
        return -karatsuba(x, -y)

    # 如果只剩下 1 位则返回乘积
    if n == 1:
        return x * y

    # 确保数字长度一致
    x_str = x_str.zfill(n)
    y_str = y_str.zfill(n)

    # 计算高低位分割点
    m = n // 2

    # 将数字划分为高位部分和低位部分
    high1, low1 = int(x_str[:-m]), int(x_str[-m:]),
    high2, low2 = int(y_str[:-m]), int(y_str[-m:])

    # 递归调用 karatsuba
    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    return pow(10, 2 * m) * z2 + pow(10, m) * (z1 - z2 - z0) + z0


"""
Karatsuba（卡拉楚巴）算法是一种高效的大整数乘法算法，关键思想是通过分治法减少了传统乘法的计算量，从而降低了乘法的时间复杂度。
现有两个大整数A和B，它们的乘积C=A×B。在传统的朴素乘法算法中，两个n位数的乘积需要进行O(n2)次基本操作。因为每一位数字都需要与另一个数字的每一位相乘，然后再加上进位。
我们将A、B的高位部分和低位部分拆开，取数字长度的一半为m，分别表示为：
A=10m×A1+A0
B=10m×B1+B0
此时可以得到：C=A×B=(10m×A1+A0)×(10m×B1+B0)
=102m×A1×B1 + 10m×(A1×B0+A0×B1) + A0×B0
这个表达式由三项组成：
A1×B1：高位部分的乘积。
A0×B0：低位部分的乘积。
A1×B0+A0×B1：混合部分，涉及到高位与低位的交叉乘积。
注意到，A1×B0+A0×B1可以转换为(A1+A0)×(B1+B0)- A0×B0-A1×B1，即(A1+A0)×(B1+B0)-低位部分的乘积-高位部分的乘积，低位部分乘积和高位部分乘积可以复用，我们只需计算(A1+A0)×(B1+B0)，相较于计算A1×B0+A0×B1，减少了1次乘法计算。
令z0=A0×B0
令z1=(A1+A0)×(B1+B0) 
令z2= A1×B1
此时结果C=102m× z2 + 10m×(z1−z2−z0) + z0
这样，Karatsuba通过减少了1个乘法操作，将原本的4次乘法运算变成了3次乘法运算，时间复杂度：T(n)=3T(n2)+O(n)，O(nlog3)≈O(n1.585)。

"""
