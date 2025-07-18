def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # 找到目标值, 返回索引
        elif arr[mid] < target:
            left = mid + 1  # 目标值在右半部分
        elif arr[mid] > target:
            right = mid - 1  # 目标值在左半部分

    return -1  # 没有找到

"""
时间复杂度：
    在循环中, 区间每轮缩小一半, 因此时间复杂度为 O(log n)
空间复杂度：
    使用常数大小的额外空间, 空间复杂度为 O(1)
"""