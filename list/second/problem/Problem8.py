from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def MD(root):
    level = 1
    return dfs(root, level)

def dfs(root, level):
    if root is None:
        return
    left_level = dfs(root.left, level + 1)
    right_level = dfs(root.right, level + 1)
    if left_level is None and right_level is None:
        return level
    if left_level and right_level:
        return max(left_level, right_level)

    return left_level or right_level

def MD2(root):
    if root is None:
        return 0
    max_level = 1
    queue = deque()
    queue.append((root, max_level))
    while queue:
        node, level = queue.popleft()
        max_level = max(max_level, level)
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return max_level



if __name__ == '__main__':
    node4 = Node(4, None, None)
    node7 = Node(1, None, None)
    node2 = Node(2, node7, node4)
    node6 = Node(1, None, None)
    node5 = Node(5, node6, node2)
    node8 = Node(8, None, None)
    node0 = Node(0, None, None)
    node1 = Node(1, node0, node8)
    node3 = Node(3, node5, node1)

    md = MD(node3)
    print(md)

    node11 = Node(1, None, None)
    node33 = Node(3, None, node11)

    md2 = MD(node33)
    print(md2)

    md3 = MD2(node3)
    print(md3)
    md4 = MD2(node33)
    print(md4)