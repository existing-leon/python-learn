def partition(nums, left, right):
    """选择基准并按基准划分"""
    pivot = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot
    return left


def quick_sort(nums, left, right):
    """快速排序"""
    if left < right:
        mid = partition(nums, left, right)
        quick_sort(nums, left, mid - 1)
        quick_sort(nums, mid + 1, right)


if __name__ == '__main__':
    nums = [4, 9, 3, 6, 4, 2, 7, 8, 5]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)

"""
时间复杂度：
    最佳情况下是：也就是每次选取的 pivot 恰好都是所有数据的中位数, 也就是恰好能将数组均匀的一分为二. O(n * log n)
    最差情况下是：每次选取的 pivot 都是所有数据的最大值或最小值, 也就是将长度为 n 的数组分为长度为 0 和长度为 n - 1 的两个数组, 时间复杂度为 O(n * n)
    大多数情况下, 快速排序算法的平均时间复杂度依然可以达到 O(n * log n).
空间复杂度：
    最佳情况：同时存在的最多的未返回的方法栈数量等于递归树的深度, 每个方法栈都只保存常量个变量, 所以空间复杂度为 O(log n).
    最差情况：同时存在的最多的未返回的方法栈的数量等与 n-1, 所以空间复杂度为 O(n).
    大多数情况下, 快速排序法的平均空间复杂度可以达到 O(log n)
"""