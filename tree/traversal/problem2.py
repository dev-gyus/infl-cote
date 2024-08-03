from collections import deque

if __package__ is None:
    import sys
    from os import path
    print(path.dirname( path.dirname( path.abspath(__file__) ) ))
    sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))
    from tree.node import Node
else:
    from ..node import Node

# 이진 트리가 하나 주어질때 그 트리의 Max Depth Level 구하기

# level order 방식으로 풀어보기
def mdbt_level_order(root, p, q):
    maximum_level = 0
    if root is None: return maximum_level
    queue = deque()
    queue.append((root, 1))
    while queue:
        cur_tuple = queue.popleft()
        cur_node = cur_tuple[0]
        maximum_level = cur_tuple[1]
        if cur_node.left is not None:
            queue.append((cur_node.left, maximum_level + 1))
        if cur_node.right is not None:
            queue.append((cur_node.right, maximum_level + 1))
    return maximum_level


# post order 방식으로 풀어보기
def mdbt_post_order(root, p, q):
    if root is None : return 0
    left_level = mdbt_post_order(root.left, p, q) + 1
    right_level = mdbt_post_order(root.right, p, q) + 1
    return max(left_level, right_level)


if __name__ == '__main__' :
    tree = Node(value = 3)
    tree.left = Node(value = 5)
    tree.left.left = Node(value = 6)
    tree.left.right = Node(value = 2)
    tree.left.right.left = Node(value = 7)
    tree.left.right.right = Node(value = 4)
    tree.left.right.right.left = Node(value = 9)
    tree.right = Node(value = 1)
    tree.right.left = Node(value = 0)
    tree.right.right = Node(value = 8)

    print(mdbt_post_order(tree, 8, 1))
    print(mdbt_level_order(tree, 8, 1))