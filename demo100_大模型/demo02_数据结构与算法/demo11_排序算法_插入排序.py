def insert_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] >= nums[j - 1]:
                break
            nums[j], nums[j - 1] = nums[j - 1], nums[j]


if __name__ == '__main__':
    nums = [3, 1, 5, 4, 2]
    insert_sort(nums)
    print(nums)

"""
时间复杂度：
    共执行 (n-1)+(n-2)+(n-3)+...+3+2+1=n(n-1)/2 轮循环, 每轮循环都执行常量个基本指令, 时间复杂度为 O(n*n)
空间复杂度：
    就地排序, 使用常数大小的额外空间, 空间复杂度为 O(1).
"""