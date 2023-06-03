from utils.decorators import performance_check

class Node:

    def __init__(self, data: int) -> None:
        self._data = data
        self._left: Node = None
        self._right: Node = None
    
    def insert(self, node) -> None:
        if node < self._data:
            if self._left == None:
                self._left = Node(node)
            else:
                self._left.insert(node)
        elif node > self._data:
            if self._right == None:
                self._right = Node(node)
            else:
                self._right.insert(node)
        else:
            pass

    def pre_order(self):
        if self._data != None:
            print(self._data)
            if self._left:
                self._left.pre_order()
            if self._right:
                self._right.pre_order()

    def order(self):
        if self._data != None:
            if self._left:
                self._left.order()
            print(self._data)
            if self._right:
                self._right.order()

    def post_order(self):
        if self._data != None:
            if self._left:
                self._left.post_order()
            if self._right:
                self._right.post_order()
            print(self._data)
    
    def search(self, value: int) -> bool:
        if value == self._data:
            return True
        elif value < self._data:
            if self._left:
                return self._left.search(value)
            else:
                return False
        elif value > self._data:
            if self._right:
                return self._right.search(value)
            else:
                return False

class BinarySearchTree:

    def __init__(self, root = None) -> None:
        self._root = Node(root) if root else Node()

    def insert(self, node_value: int) -> None:
        self._root.insert(node_value)

    def pre_order(self) -> None:
        self._root.pre_order()

    def order(self) -> None:
        self._root.order()

    def post_order(self) -> None:
        self._root.post_order()

    @performance_check
    def search(self, value: int) -> bool:
        return self._root.search(value)
    
    @staticmethod
    @performance_check
    def create_from_list(items: list[int]):
        tree = BinarySearchTree(items[0])
        for item in items:
            tree.insert(item)
        return tree

items = [8, 3, 6, 10, 14, 1, 7, 13, 4]
tree = BinarySearchTree.create_from_list(items)
print(tree.search(4))