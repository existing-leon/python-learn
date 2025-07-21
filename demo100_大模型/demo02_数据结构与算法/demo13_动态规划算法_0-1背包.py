""""""
"""
0-1背包问题是一个经典的动态规划问题。其基本描述是：给定一组物品，每个物品都有一个重量和一个价值，在背包容量有限的情况下，如何选择物品放入背包，使得背包中物品的总价值最大化，且总重量不超过背包的容量。
	物品：有n个物品，每个物品i的重量为weight[i]和价值value[i]。
	背包容量：背包可以承载的最大重量为W。
	目标：选择若干物品放入背包，使得总重量不超过W，且总价值最大。
"""
"""
1）方法一
（1）定义状态
定义一个二维数组 dp[i][j]，表示前i个物品中，总重量不超过j的情况下，能够取得的最大价值。
	i：表示考虑第i个物品。
	j：表示背包当前容量为j。
（2）状态转移
对于每个物品i，有两个选择：
	不选第i个物品：此时最大价值就是前i−1个物品在容量j下的最大价值，即 dp[i−1][j]。
	选第i个物品：此时背包剩余容量为j−weighti，所以最大价值为valuei+dp[i−1][j−weighti]，前提是 j≥wi。
状态转移方程：dp[i][j] =max( dp[i−1][j] , valuei+dp[i−1][j−weighti] )
最大价值会存储在 dp[n][W]中，其中n是物品的数量，W是背包的最大容量。
（3）实现步骤
	初始化二维数组dp，i行、W+1列，因为要存放背包容量为0~W时的状态。
	循环中每次增加一个可选物品。
	每增加一个可选物品后遍历背包容量为0~W。考虑该物品是否放得下背包，如果放得下，将放进去后和不放进去进行比较。
"""


def knapsack1(weights, values, W):
    n = len(weights)
    # 初始化一个二维数组dp, dp[i][j]表示前i个物品中, 背包容量为j时的最大价值
    dp = [[0] * (W + 1) for _ in range(n)]

    # 每次增加一个可选物品, 增加物品后遍历一次背包重量
    for i in range(n):
        for j in range(1, W + 1):
            # 如果当前物品放得进去背包, 进行比较
            if weights[i] <= j:
                dp[i][j] = max(dp[i - 1][j], values[i] + dp[i - 1][j - weights[i]])
            # 如果当前物品放不进背包, 使用上轮相同的j状态
            else:
                dp[i][j] = dp[i - 1][j]

            print(f"前{i + 1}个物品，背包容量为{j}时")
            for row in range(len(dp)):
                print(dp[row])

    return dp[n - 1][W]


"""
方法二：
可以看到在方法一中，我们每轮遍历时只用到上1轮的结果，与这一轮的结果无关，因此我们只用一维数组存储上1轮的结果即可。
并且遍历时需要从后往前遍历，防止这轮结果将还需要用到的上轮结果覆盖。
并且不用全部遍历，遍历到背包当前重量刚好大于当前物品重量即可。
"""


def knapsack2(weights, values, W):
    n = len(weights)
    dp = [0] * (W + 1)
    for i in range(n):
        for j in range(W, weights[i] - 1, -1):  # 从后往前遍历
            dp[j] = max(dp[j], values[i] + dp[j - weights[i]])
    return dp[W]


if __name__ == "__main__":
    weights = [1, 2, 3]  # 物品的重量
    values = [3, 2, 6]  # 物品的价值
    W = 3  # 背包的最大容量
    print(knapsack1(weights, values, W))
    print('==============================')
    print(knapsack2(weights, values, W))
