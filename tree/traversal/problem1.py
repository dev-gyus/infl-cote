from collections import deque

from ..node import Node

#dfs 이용해서 p, q 공통 조상 탐색해보기
def traversal(root, p, q) :
    if root is None or p is None or q is None: return None
    if root.val == p or root.val == q:
        return root
    pParents = []
    sub_traversal(root.left, p)
    sub_traversal(root.right, p)
    sub_traversal(root.left, q)
    sub_traversal(root.right, q)

def sub_traversal(node, target) :
    if node is None: return None
    if node.val == target:
        return node





if __name__ == '__main__' :
    tree = Node(value = 3)
    tree.left = Node(value = 5)
    tree.left.left = Node(value = 6)
    tree.left.right = Node(value = 2)
    tree.left.right.left = Node(value = 7)
    tree.left.right.right = Node(value = 4)
    tree.right = Node(value = 1)
    tree.right.left = Node(value = 0)
    tree.right.right = Node(value = 8)
