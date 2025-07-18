def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


"""
时间复杂度：
    共执行 (n-1)+(n-2)+(n-3)+...+3+2+1=n(n-1)/2 轮循环, 每轮循环都执行常量个基本指令, 时间复杂度为 O(n*n)
空间复杂度：
    就地排序, 使用常数大小的额外空间, 空间复杂度为 O(1)
"""