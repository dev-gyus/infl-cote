# queue 사용
from collections import deque


def bfs(root) :
    visit = []
    if root is None : return visit
    queue = deque()
    queue.append(root)
    while queue:
        cur_node = queue.popleft()
        visit.append(cur_node.value)
        if cur_node.left is not None:
            queue.append(cur_node.left)
        if cur_node.right is not None:
            queue.append(cur_node.right)
    return visit

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        print(path.dirname( path.dirname( path.abspath(__file__) ) ))
        sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))
        from tree.node import Node
    else:
        from ..node import Node

    rootNode = Node(value = 'A')
    rootNode.left = Node(value = 'B')
    rootNode.right = Node(value = 'C')
    rootNode.left.left = Node('D')
    rootNode.left.right = Node('E')
    rootNode.right.left = Node('F')
    rootNode.right.right = Node('G')

    print(bfs(rootNode))