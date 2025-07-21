""""""
"""
力扣70题https://leetcode.cn/problems/climbing-stairs/description/
爬有n个台阶的楼梯，每次可以爬1或2个台阶。有多少种不同的方法可以爬到楼顶？
"""

"""
方法一：
由于每次只能个或个台阶，所以第n个台阶可能是从第n-1个台阶爬1阶上来的，也可能是
从第n-2个台阶爬2阶上来的，所以爬到第n阶的方法数就等于爬到第n-1阶的方法数加上
爬到第n-2阶的方法数。故可以得到状态转移方程：f(n) = f(n-1) + f(n-2)。
"""


def climbStairs1(n):
    if n == 1:
        # 如果只有 1 个台阶, 只有一种方式
        return 1
    elif n == 2:
        # 如果只有 2 个台阶, 只有两种方式：一次爬 1 阶, 爬两次; 一次爬两阶, 爬一次
        return 2
    else:
        return climbStairs1(n - 1) + climbStairs1(n - 2)


"""
方法二：
既然f(n) = f(n-1) + f(n-2)，那么我们也可以自下而上从1阶台阶开始逐渐增加，
并记录当前阶方法数和当前阶-1的方法数。
"""


def climbStairs2(n):
    pre = 1
    cur = 1
    for _ in range(1, n):
        pre, cur = cur, pre + cur
    return cur
