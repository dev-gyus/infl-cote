class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"value={self.value}, left={str(self.left)}, right={str(self.right)}"

class BinaryTree:
    def __init__(self):
        self.root = None
    def __str__(self):
        return str(self.root)

if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = Node(value = 1)
    bt.root.left = Node(value = 2)
    bt.root.right = Node(value = 3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    bt.root.right.left = Node(6)
    bt.root.right.right = Node(7)

    print(bt)