from collections import deque


class Node:
    """二叉树节点"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """二叉搜索树"""

    def __init__(self):
        """初始化二叉树"""
        self.__root = None
        self.__size = 0

    def print_tree(self):
        """打印树结构"""

        # 先得到树的层数
        def get_layer(node):
            """递归计算树的层数"""
            if node is None:
                return 0
            else:
                left_depth = get_layer(node.left)
                right_depth = get_layer(node.right)
                return max(left_depth, right_depth) + 1

        layer = get_layer(self.__root)

        # 层序遍历并打印
        queue = deque([self.__root, 1])
        current_level = 1
        while queue:
            node, level = queue.popleft()
            if level > current_level:
                print()
                current_level += 1
            if node:
                print(f'{node.data:^{20 * layer // 2 ** (level - 1)}}', end='')
            else:
                print(f'{"N":^{20 * layer // 2 ** (level - 1)}}', end='')
            if level < layer:
                if node:
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))
                else:
                    queue.append((None, level + 1))
                    queue.append((None, level + 1))
        print()

    @property
    def size(self):
        """返回树中节点的个数"""
        return self.__size

    def is_empty(self):
        """判断树是否为空"""
        return self.__size == 0
