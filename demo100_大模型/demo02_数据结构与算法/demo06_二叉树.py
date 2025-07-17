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
