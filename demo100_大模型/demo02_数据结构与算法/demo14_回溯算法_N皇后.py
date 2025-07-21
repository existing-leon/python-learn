""""""
"""
力扣51题https://leetcode.cn/problems/n-queens/description/
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n皇后问题研究的是如何将n个皇后放置在n×n的棋盘上，并且使皇后彼此之间不能相互攻击。给一个整数n，返回所有的解决方案。每一个方案中 'Q' 和 '.' 分别代表了皇后和空位。

	输入：n = 4
	输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4皇后问题存在两个不同的解法。
1）思路分析
实现步骤：
	选择：从棋盘每行中选择一个列放置棋子。
	验证合法性：每次放置一个皇后时，检查该位置是否与其他已经放置的皇后在列或对角线上发生冲突。
	递归：棋子放置位置合法则递归放置下一个棋子。
	终止条件：若所有棋子都放置完则终止递归。
	回溯：回到上一步，尝试下一个位置。

"""


def n_queens(n):
    result = []
    cols = set()  # 记录哪些列有皇后
    diag1 = set()  # 记录哪些主对角线上有皇后
    diag2 = set()  # 记录哪些副对角线上有皇后

    # 初始化棋盘
    board = [["." for _ in range(n)] for _ in range(n)]

    def backtrack(row):
        # 如果已经放置了n个皇后，说明找到一个解
        if row == n:
            result.append(["".join(row) for row in board])
            return

        for col in range(n):
            # 检查当前列和对角线是否有皇后
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue  # 如果有冲突，跳过当前列

            # 放置皇后
            board[row][col] = "Q"
            # 标记当前列和对角线
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            # 递归处理下一行
            backtrack(row + 1)

            # 回溯，删除当前位置的皇后，并清理列和对角线的标记
            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return result


if __name__ == '__main__':
    n = 4
    list = n_queens(n)
    for item in list:
        for i in item:
            print(i)
        print()
