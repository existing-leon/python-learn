def merge(left, right):
    """合并两个已排序的数组"""
    merged = []
    i = j = 0
    # 比较两个子数组的元素, 按升序放入 merged 数组
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # 将数组中剩余元素加入 merged
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(arr):
    """归并排序"""
    # 数组长度为 1 时, 不再分割
    if len(arr) <= 1:
        return arr

    # 分割数组
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # 合并已排序的子数组
    return merge(left, right)


if __name__ == '__main__':
    arr = [1, 3, 2, 7, 4, 6, 5, 9, 8]
    sort_arr = merge_sort(arr)
    print(sort_arr)

"""
时间复杂度：
    递归调用 merge_sort() 函数, 二叉树的层数 level 与输入数组长度 n 的关系为 n = 2的level次方, 因此层数 level = log以2为底n的对数.
    该算法循环执行总次数为 n * log以w2为底n的对数（每层循环次数 * 层数）,
    时间复杂度为 O(n * log n)
空间复杂度：
    每次合并操作都需要创建一个数组来临时存放合并结果, 所以空间复杂度主要考虑临时数组占用的空间.
    虽然每次合并操作都会创建临时数组, 但是这些合并操作并不是同时进行. 每次合并操作结束后, 临时数组的空间就会被释放.
    因此：该算法的空间复杂度为 O(n).
"""