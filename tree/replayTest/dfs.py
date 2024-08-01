
# 재귀 or queue
# 전위 순회 좌측 자식 노드부터 실행
def dfs_pre_order(root):
    if root is None: return
    print(root.value)
    dfs_pre_order(root.left)
    dfs_pre_order(root.right)

# 중위 순회 좌측 자식 노드부터 실행
def dfs_middle_order(root):
    if root is None: return
    dfs_middle_order(root.left)
    print(root.value)
    dfs_middle_order(root.right)

# 후위 순회 좌측 자식 노드부터 실행
def dfs_post_order(root):
    if root is None: return
    dfs_post_order(root.left)
    dfs_post_order(root.right) 
    print(root.value)

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

    print(dfs_pre_order(rootNode))
    print(dfs_middle_order(rootNode))
    print(dfs_post_order(rootNode))
