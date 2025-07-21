""""""
"""
力扣46题https://leetcode.cn/problems/permutations/description/
现有一个不含重复数字的数组nums ，返回其所有可能的全排列。
示例：
	输入：nums = [1,2,3]
	输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

1）思路分析
实现步骤：
	选择：从待排列的元素中选择一个元素作为当前位置的元素。
	递归：将该元素固定在当前位置后，递归排列下一个元素。
	终止条件：所有位置的元素都已确定，添加到结果中并终止递归。
	回溯：回到上一步，撤销当前的选择，尝试下一个可能的元素。

"""


def permute(nums):
    result = []

    def backtrack(start):
        # 到达末尾, 将此时排列结果添加到最终结果中
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            # 选取当前位置的元素：将要选取的元素与此位置的元素互换
            if start != i:
                nums[start], nums[i] = nums[i], nums[start]
            # 递归处理下一个位置的元素
            backtrack(start + 1)
            # 回溯, 恢复原始数组
            if start != 1:
                nums[start], nums[i] = nums[i], nums[start],

    backtrack(0)
    return result


if __name__ == '__main__':
    nums = [1, 2]
    # nums = [1, 2, 3]
    print(permute(nums))
