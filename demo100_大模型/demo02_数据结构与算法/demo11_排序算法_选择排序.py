def select_sort(nums):
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]


if __name__ == '__main__':
    nums = [1, 3, 5, 2, 8, 7, 9, 4, 6]
    select_sort(nums)
    print(nums)

"""
时间复杂度：
    上述算法共执行 (n-1)+(n-2)+(n-3)+...+3+2+1=n(n-1)/2 轮循环, 每轮循环都执行常量个基本指令, 时间复杂度为 O(n*n).
空间复杂度：
    就地排序, 使用常数大小的额外空间, 空间复杂度为 O(1).
"""