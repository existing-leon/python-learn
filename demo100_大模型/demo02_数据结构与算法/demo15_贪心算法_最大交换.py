""""""
"""
力扣670题https://leetcode.cn/problems/maximum-swap/description/
现有一个非负整数，至多可以交换一次数字中的任意两位。返回能得到的最大值。
示例：
	输入：2736
	输出：7236
解释：交换数字2和数字7。

1）思路分析
从右向左遍历，同时维护一个最大数的索引。
	如果当前位置的数大于最大数，则更新最大数索引。
	否则将当前位置的数与最大数进行交换，交换后的数更新到result中，再将两个位置的数交换回来将数组恢复原样。
遍历结束后，result中的数就是能得到的最大值。

"""


def maximumSwap(num):
    result = num
    num_list = list(str(num))
    max_index = -1  # 最大值的索引
    for i in range(len(num_list) - 1, -1, -1):
        # 当前值大于最大值时，更新最大值的索引
        if num_list[i] > num_list[max_index]:
            max_index = i
        # 当前值小于最大值时，交换，更新result，再交换回来
        else:
            num_list[i], num_list[max_index] = num_list[max_index], num_list[i]
            result = max(result, int("".join(num_list)))
            num_list[i], num_list[max_index] = num_list[max_index], num_list[i]
    return result


if __name__ == '__main__':
    print(maximumSwap(2736))
