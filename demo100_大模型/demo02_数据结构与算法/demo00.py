"""
理论知识
"""

"""
数据结构是为了高效访问数据而设计出的一种数据的组织和存储方式。
具体来说：一个数据结构包含了一个数据元素的集合、数据元素之间的关系以及访问和操作数据的方法。
"""

"""
数据的逻辑结构反映了数据元素之间的逻辑关系。逻辑结构可分为线性和非线性。
线性：数组、链表、栈、队列
非线性：树、图
"""
"""
数据的物理结构反映了数据在计算机内存中的存储结构。
连续存储：借助数据之间的相对位置来表示数据元素之间的逻辑关系；如：数组
分散存储：借助知识数据位置的指针来表示数据元素之间的逻辑关系；如：链表
"""

"""
算法：一个用于解决特定问题的有限指令序列（计算机可以执行的操作）
五大特性：
    输入：算法具有0个或多个输入
    输出：算法至少有1个输出
    有穷性：算法在有限的步骤之后会自动结束而不会无限循环, 并且每一个步骤可以在可接受的时间内完成
    确定性：算法中的每一步都有确定的含义, 不会出现二义性
    可行性：算法的每一步都是清楚且可行的, 能让用户用纸笔计算而求出答案
"""

"""
# 时间复杂度为 5n + 5, 其中 n 是数组的长度
def sum(nums):
    sum_num = 0  # 1次赋值
    i = -1  # 1次赋值
    while (i := i + 1) < len(nums):  # n+1次加法运算 n+1次赋值运算 n+1次比较运算
        sum_num += nums[i]  # n次加法运算 n次赋值于是暖
    return sum_num


# 按照最大来看, 是5n
def find_max(nums):
    max_num = nums[0]   # 1次赋值
    i = 0   # 1次赋值
    while (i := i + 1) < len(nums): # n次加法运算, n次赋值, n次比较
        if nums[i] > max_num:   # n - 1 次比较运算
            max_num = nums[i]   # 0 ~ (n-1)次赋值
    return max_num
    
# 总结：
# 时间复杂度统计的是算法运行时执行的基本指令数, 而非绝对运行时间
# 时间复杂度体现的是算法基本指令数随输入规模 n 增大时的变化趋势
"""

"""
# 二分查找法, 时间复杂度为 log n
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
"""

"""
# 求数组中所有元素的和, 时间复杂度为 n
def sum(nums):
    sum_num = 0
    for num in nums:
        sum_num += num
    return sum_num
"""

"""
# 归并排序：分而治之, 时间复杂度 n * log n
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result
"""

"""
# 冒泡排序, 时间复杂度为 n 的平方
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
"""

"""
# 全排列, 时间复杂度为 n!
def permute(nums):
    result = []
    if len(nums) == 1:
        return [nums]

    for i in range(len(nums)):
        remaining = nums[:i] + nums[i + 1:]
        for perm in permute(remaining):
            result.append([nums[i]] + perm)
    return result
"""

#########################################################################
"""
抽象数据类型与数据结构的关系：
    抽象数据类型：强调的是数据的逻辑特性和操作的功能, 是一种抽象的概念, 不涉及具体的实现细节。
            它是从用户的角度来描述数据和操作的。
    数据结构：是抽象数据类型的具体实现, 它关注的是数据在计算机内存中的存储方式和操作的具体实现算法。
            例如：栈这种抽象数据类型可以用数组或链表等数据结构来实现。
"""

"""
链表（Linked List）是一个线性结构, 由一系列节点（Node）组成, 每个节点包含一个数据元素和一个指向下一节点的指针（Pointer）。
通常我们将链表中的第一个节点称为头结点, 并将头结点的位置作为整个链表的位置标识。

常见链表分类：
    单向链表：单向链表的节点包含值和指向下一节点的引用。我们将首个节点称为头节点, 将最后一个节点称为尾节点, 尾节点指向空 None。
    环形链表：将单向链表的尾节点指向头节点（首尾相接）, 则得到一个环形链表, 在环形链表中, 任意节点都可以视作头节点。
    双向链表：双向链表记录了两个方向的引用, 同时包含指向后继节点（下一个节点）和前驱节点（上一个节点）的引用。
"""

"""
栈（Stack）是一个线性结构, 其维护了一个有序的数据列表, 列表的一端称为栈顶（top）, 另一端称为栈底（bottom）。
栈对数据的操作有明确限定, 插入元素只能由栈顶进行, 删除元素也只能栈顶开始逐个进行, 通常将插入元素称为入栈（push），删除元素称为出栈（pop）。
栈保证了后进先出的原则（LIFO, Last-In-First-Out）
栈的底层实现既可以选择数组也可以选择链表, 只要能保证后进先出的原则即可。
"""

"""
（1）题目描述
给定一个只包括“(”，“)”，“[”，“]”，“{”，“}”的字符串s，判断字符串是否有效。
有效字符串需满足：
	左括号必须用相同类型的右括号闭合。
	左括号必须以正确的顺序闭合。
	每个右括号都有一个对应的相同类型的左括号。
分析：
遇到左括号则入栈，遇到右括号则出栈一个左括号与之匹配，如果能够匹配则继续，如果匹配失败或者栈为空则返回False。
"""

"""
class Solution:
    def isValid(self, s):
        stack = []
        for i in s:
            match i:
                case '(' | '[' | '{':
                    stack.append(i)
                case ')':
                    if (not stack) or (stack.pop() != '('):
                        return False
                case ']':
                    if (not stack) or (stack.pop() != '['):
                        return False
                case '}':
                    if (not stack) or (stack.pop() != '{'):
                        return False

        return True if not stack else False


if __name__ == "__main__":
    solution = Solution()
    s = "()[]{}"
    print(s, solution.isValid(s))
    s = "(]"
    print(s, solution.isValid(s))
    s = "([)]"
    print(s, solution.isValid(s))
    s = "{[]}"
    print(s, solution.isValid(s))
"""

"""
队列（Queue）也是一个线性结构, 其同样维护了一个有序的数据列表, 队列的一段称为队首, 另一端称为队尾。
队列对数据操作做出了明确限定, 插入元素只能从队尾进行, 删除元素只能从队首进行, 通常将插入操作称为入队（enqueue）, 将删除操作称为出队（dequeue）。
队列保证了先进先出（FIFO, First-In-First-Out）的原则。

队列的底层实现既可以选择数组也可以选择链表, 只要能保证先进先出的原则即可。
常见队列：
    单向队列：只能从一端插入数据, 从另一端删除数据, 遵循先进先出。
    双向队列：在队列的两端都可以进行插入和删除操作。
"""

