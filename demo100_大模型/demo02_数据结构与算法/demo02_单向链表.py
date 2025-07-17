class Node:
    def __init__(self, data, next=None):
        self.data = data  # 数据域：存储节点值
        self.next = next  # 指针域：指向后继节点, 初始为 None


class LinkedList:
    def __init__(self):
        """初始化链表"""
        self.__head = None
        self.__size = 0

    def __str__(self):
        """打印链表"""
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next
        return '->'.join(result)

    @property
    def size(self):
        """获取链表元素个数"""
        return self.__size

    def is_empty(self):
        """判断链表是否为空"""
        return self.__size == 0

    def insert(self, index, item):
        """插入元素"""
        if index < 0 or index > self.__size:
            raise IndexError
        if index == 0:
            # 插入数据到头部
            self.__head = Node(item, self.__head)
        else:
            # 插入数据到中间
            # 链表只能从头开始查找
            prev = self.__head
            for i in range(index - 1):
                prev = prev.next
            # 创建新节点并调整指针
            # new_node = Node(item, prev.next)
            # new_node.next = prev.next
            # prev.next = new_node
            # 合并来写就是：
            prev.next.next = Node(item, prev.next)


"""
# 链表的插入原理
step01：找到目标位置的前一个节点, 记为 prev
新节点的指针指向 prev 的后继节点：
new_node.next = prev.next
prev.next = new_node

已有链表：A -> B -> C -> null
1.头部插入：新节点 X
    X.next = head
    X -> A -> B -> C -> null
    
2.中间插入：在 A 和 B 之间
    前驱节点 A：prev = A
    新节点 X 指向 A 的后继节点 B ：X.next = A.next
    A 指向 X, A.next = X
    A -> X -> B -> C -> null

3.尾部插入：在 C 后面插入 X
    找到尾节点 C：prev = C
    新节点 X 的指针设为 null：X.next = null
    C 的指针指向 X：C.next = null
"""
if __name__ == '__main__':
    linked_list = LinkedList()
    print(linked_list)
