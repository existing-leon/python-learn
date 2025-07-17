class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None  # 头指针：指向链表的第一个节点, 初始为 None （空链表）

    def is_empty(self):
        """判空操作"""
        return self.head is None

    def length(self):
        """获取链表长度"""
        count = 0
        current = self.head  # 从head开始遍历
        while current:
            count += 1
            current = current.next  # 移动到下一个节点
        return count

    def traverse(self):
        """遍历列表并打印所有元素"""
        if self.is_empty():
            print('链表为空')
            return
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print(None)  # 尾节点的 next 为 None

    def insert_head(self, data):
        """头部插入"""
        new_node = Node(data)  # 创建新节点
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        """尾部插入"""
        new_node = Node(data)  # 创建新节点
        if self.is_empty():
            # 空链表时, 新节点直接作为头节点
            self.head = new_node
            return
            # 非空链表, 遍历到尾节点（next为None的节点）：链表需要从头开始往后找, 一直找到old链表的尾节点为止
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_index(self, index, data):
        """在中间插入"""
        if index < 0 or index > self.length():
            raise IndexError('插入位置超出链表范围')
        if index == 0:
            # 索引为0等价于从头部插入
            self.insert_head(data)
            return
            # 重点在与找到索引为 index 的前一个节点
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        # 创建新节点并调整指针
        new_node = Node(data)
        new_node.next = prev.next  # 新节点指向 prev 曾指向的下一个节点
        prev.next = new_node  # prev 指向新节点

    def find(self, data):
        """查找元素"""
        """返回第一个匹配的元素的索引, 如果没找到就返回 -1"""
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1  # 没找到

    def delete_head(self):
        """删除头部元素"""
        if self.is_empty():
            raise ValueError('链表为空, 无法删除')
        # 头指针指向原头节点的下一个节点
        self.head = self.head.next

    def delete_tail(self):
        """删除尾部节点"""
        if self.is_empty():
            raise ValueError('链表为空, 无法删除')
        if self.length() == 1:
            # 只有一个节点的时候, 清空链表
            self.head = None
        # 找到倒数第二个节点（prev）
        prev = self.head
        while prev.next.next:
            prev = prev.next
        prev.next = None  # 改变倒数第二个节点的指向

    def delete_at_index(self, index):
        """删除指定索引的节点"""
        if self.is_empty():
            raise ValueError('链表为空, 无法删除')
        if index < 0 or index > self.length():
            raise IndexError('删除位置超出链表范围')
        if index == 0:
            # 索引为 0 等价于删除头部
            self.delete_head()
            return
            # 找到索引为 index - 1 的前驱节点（prev）
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        # 将 pre 的 next 指向待删除节点的下一个节点
        prev.next = prev.next.next

    def delete_by_value(self, data):
        """删除指定值的第一个节点"""
        if self.is_empty():
            raise ValueError('链表为空, 无法删除')
        if self.head.data == data:
            # 如果指定值刚好和头节点的值相等
            self.head = self.head.next
        # 重点在找到待删除节点的前驱节点（prev）
        prev = self.head
        while prev.next:
            if prev.next.data == data:
                # 找到结果后直接跳过待删除节点
                prev.next = prev.next.next
                return
            prev = prev.next

        raise ValueError(f'链表中不存在值为 {data} 的节点')


if __name__ == '__main__':
    # 初始化链表
    linked_list = SingleLinkedList()
    print('初始链表：', end='')
    linked_list.traverse()  # 输出：链表为空

    # 尾部插入元素
    linked_list.insert_tail(10)
    linked_list.insert_tail(20)
    linked_list.insert_tail(30)
    print('尾部插入 10, 20, 30 后：', end='')
    linked_list.traverse()

    # 头部插入元素
    linked_list.insert_head(5)
    print('头部插入 5 后：', end='')
    linked_list.traverse()

    # 中间插入元素
    linked_list.insert_at_index(2, 15)
    print('索引 2 处插入 15 后：', end='')
    linked_list.traverse()

    # 查找元素
    print('查找 20 的索引：', linked_list.find(20))
    print('查找 88 的索引：', linked_list.find(88))

    # 删除头部节点
    linked_list.delete_head()
    print('删除头部后：', end='')
    linked_list.traverse()

    # 删除尾部节点
    linked_list.delete_tail()
    print('删除尾部后：', end='')
    linked_list.traverse()

    # 删除指定索引节点
    linked_list.delete_at_index(1)
    print('删除索引为 1 后：', end='')
    linked_list.traverse()

    # 删除指定值节点
    linked_list.delete_by_value(20)
    print('删除值为 20 的节点后：', end='')
    linked_list.traverse()

    # 输出链表长度
    print('链表长度：', linked_list.length())
