""""""
"""
堆排序的基本思想是先将输入的数据构建成一个大顶堆, 然后依次将堆顶的元素（即最大元素）移到数组的末尾, 之后重新调整堆的结构, 
并将堆的元素个数减1. 重复这一过程, 直到所有元素都被排好序。
步骤：
    ①构建大顶堆
    ②交换堆顶和堆底元素
    ③重新调整堆
    ④重复②③, 直到堆大小为1
"""


def heapify(arr, n, i):
    """
    堆化
    :param arr: 需要进行堆操作的序列
    :param n: 序列中元素的个数
    :param i: 当前需要进行堆化操作的子树的根节点索引
    """
    largest = i  # 最大节点指向父节点
    left = 2 * i + 1  # 左子节点
    right = 2 * i + 2  # 右子节点

    # 如果左子节点大于父节点, 最大节点指向左子节点
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 如果右子节点大于当前最大节点, 最大节点指向右子节点
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大节点不是父节点, 则交换并递归堆化
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """堆排序"""
    n = len(arr)
    # 构建大顶堆
    # n//2-1 获取最后一个非叶子节点的索引
    # stop 为不包含, 所以意味着循环会一直执行到索引为 0 的节点
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        # 依次将堆顶元素放在末尾，并重新堆化
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    sorted_arr = heap_sort(arr)
    print('排序后的数组：', sorted_arr)


"""
时间复杂度：
    其初始构建堆时间复杂度为 O(n). 正式排序时, 重建堆的时间复杂度为 O(n log n). 所以堆排序的总体时间复杂度为 O(n log n)
    与其他排序算法（如归并排序、快速排序）相比, 堆排序的常数因子较大, 因此在某些情况下效率较低.
空间复杂度：
    就地排序, 空间复杂度为：O(1)
"""