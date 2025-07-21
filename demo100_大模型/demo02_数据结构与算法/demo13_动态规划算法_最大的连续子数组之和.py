""""""
"""
力扣53题https://leetcode.cn/problems/maximum-subarray/description/
找出整数数组nums中数组之和最大的连续子数组（子数组最少包含一个元素），返回其最大和。
示例：
	输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
	输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
"""

"""
用f(x)表示以x结尾的最大子数组之和，考虑处于位置i时，有两种选择：
	与之前的子数组组成连续子数组，此时子数组之和f(i) = f(i-1) + nums[i]。
	中断连续，从头开始一个新的连续子数组，此时f(i) = nums[i]。
得到状态转移方程：f(i) = max( f(i-1) + nums[i] , nums[i] )。
持续组成连续子数组，除非连续子数组之和已经<0，此时中断连续。
"""


def max_subarray(nums):
    result, f = nums[0], 0
    for i in nums:
        # 连续子数组之和若小于0, 则中断连续
        if f < 0:
            f = 0
        # 累加连续子数组的和
        f += i
        # 更新最大值
        if result < f:
            result = f
    return result


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1]
    print(max_subarray(nums))
