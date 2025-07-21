""""""
"""
完全背包问题是0-1背包问题的一种扩展。与0-1背包不同，完全背包问题允许每个物品可以被选取多次，也就是说，物品的数量没有限制。
"""
"""
1）方法一
（1）定义状态
定义一个二维数组 dp[i][j]，表示前i个物品中，总重量不超过j的情况下，能够取得的最大价值。
	i：表示考虑第i个物品。
	j：表示背包当前容量为j。
（2）状态转移
相较于0-1背包，仅有选择放入第i个物品时发生了变化。
对于每个物品i，有两个选择：
	不选第i个物品：与0-1背包相同，此时最大价值就是前i−1个物品在容量j下的最大价值，即 dp[i−1][j]。
	选第i个物品：此时背包剩余容量为j−weighti，所以最大价值为valuei+dp[i][j−weighti]。
状态转移方程：dp[i][j] =max( dp[i−1][j] , valuei+dp[i][j−weighti] )
状态转移方程相较于0-1背包问题仅有一处 i-1 变为了 i。
（3）实现步骤
	初始化二维数组dp，i行、W+1列，因为要存放背包容量为0~W时的状态。
	循环中每次增加一个可选物品。
	每增加一个可选物品后遍历背包容量为0~W。考虑该物品是否放得下背包，如果放得下，将放进去后和不放进去进行比较。

"""


def knapsack1(weights, values, W):
    n = len(weights)
    # 初始化二维数组dp，dp[i][j]表示前i个物品中，背包容量为j时的最大价值
    dp = [[0] * (W + 1) for _ in range(n)]

    # 每次增加一个可选物品，增加物品后遍历一次背包重量
    for i in range(n):
        for j in range(1, W + 1):
            # 如果当前物品放的进背包，进行比较
            if weights[i] <= j:
                dp[i][j] = max(dp[i - 1][j], values[i] + dp[i][j - weights[i]])
            # 如果当前物品放不进背包，使用上轮相同j的状态
            else:
                dp[i][j] = dp[i - 1][j]

            print(f"前{i + 1}个物品，背包容量为{j}时")
            for row in range(len(dp)):
                print(dp[row])

    return dp[n - 1][W]


"""
方法二：
方法一同样可以优化为一维数组。可以看到在方法一中我们既使用了上1轮结果，也使用了本轮i之前的结果，但是两者上下没有重叠。
这时我们遍历时需要从前向后遍历，因为可能会用到本轮i之前的结果。
"""


def knapsack2(weights, values, W):
    n = len(weights)
    dp = [0] * (W + 1)

    for i in range(n):
        for j in range(weights[i], W + 1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[W]


if __name__ == "__main__":
    weights = [1, 2, 3]  # 物品的重量
    values = [3, 7, 11]  # 物品的价值
    W = 3  # 背包的最大容量
    print(knapsack1(weights, values, W))
    print('============================')
    print(knapsack2(weights, values, W))

