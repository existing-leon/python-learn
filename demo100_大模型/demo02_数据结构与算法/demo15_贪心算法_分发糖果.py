""""""
"""
力扣135题https://leetcode.cn/problems/candy/description/
n个孩子站成一排。用一个整数数组ratings表示每个孩子的评分。按照以下要求，给这些孩子分发糖果：
	每个孩子至少分配到1个糖果。
	相邻两个孩子评分更高的孩子会获得更多的糖果。
给每个孩子分发糖果，计算并返回需要准备的最少糖果数目。
"""

"""
1）方法一
每个孩子先分发1个糖果。
从左向右遍历，如果右边孩子比左边孩子评分高，则右边孩子糖果数量应该>左边孩子糖果数量，这时令右边孩子糖果数量为左边孩子糖果数量+1。
再从右向左遍历，如果左边孩子比右边孩子评分高，则左边孩子糖果数量应该为max(右边孩子糖果数量+1, 自己糖果数量)。
"""


def candy(ratings):
    n = len(ratings)

    # 每个孩子先分发 1 个糖果
    candy_num = [1] * len(ratings)

    # 从左向右遍历, 如果右边评分更高, 则右边孩子的糖果数改为左边孩子的糖果数 +1
    for pos in range(n - 1):
        if ratings[pos] < ratings[pos + 1]:
            candy_num[pos + 1] = candy_num[pos] + 1

    # 从右向左遍历, 如果左边评分更高, 则左边孩子的糖果数改为右边孩子的糖果数 +1
    total_candies = candy_num[-1]
    for pos in range(n - 2, -1, -1):
        if ratings[pos] > ratings[pos + 1]:
            if candy_num[pos] <= candy_num[pos + 1]:
                candy_num[pos] = candy_num[pos + 1] + 1
        total_candies += candy_num[pos]
    return total_candies
