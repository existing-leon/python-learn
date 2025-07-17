class Stack:
    def __init__(self):
        """初始化栈"""
        self.__size = 0
        self.__item = []

    @property
    def size(self):
        """获取栈元素个数"""
        return self.__size

    def is_empty(self):
        """判断栈是否为空"""
        return self.__size == 0

    def push(self, item):
        """入栈"""
        self.__item.append(item)
        self.__size += 1

    def pop(self):
        """出栈"""
        if self.is_empty():
            raise Exception('栈为空')
        item = self.__item[self.__size - 1]
        del self.__item[self.__size - 1]
        self.__size -= 1
        return item

    def peek(self):
        """访问栈顶元素：非弹栈"""
        if self.is_empty():
            raise Exception('栈为空')
        return self.__item[self.__size - 1]


