# dfs 구현은 스택, 재귀 두 가지로 구현 가능
# 여기서는 재귀로 구현
# dfs를 구현할때는 좌측노드부터 우선적으로 탐색할지, 우측노드부터 우선적으로 탐색할지 결정가능
# 접근과 방문

# 접근 및 전위순회(preorder)
# 자식 노드에 접근하기 전에 부모 노드(자기 자신)부터 방문하는 방식
def dfs_preorder(root):
    if root is None:
        return
    print(root.value)
    dfs_preorder(root.left)
    dfs_preorder(root.right)

# 접근 및 중위순회(inorder)
# 왼쪽 자식 노드부터 방문 후 부모 노드(자기 자신) -> 우측 자식 노드 방문하는 방식
def dfs_inorder(root):
    if root is None:
        return
    dfs_inorder(root.left)
    print(root.value)
    dfs_inorder(root.right)

# 접근 및 후위순회(postorder)
# 자식 노드를 모두 방문 하고 난 다음 부모 노드(자기 자신)을 방문하는 방식
def dfs_postorder(root):
    if root is None:
        return
    dfs_postorder(root.left)
    dfs_postorder(root.right)
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
    rootNode.left.left = Node(value = 'D')
    rootNode.left.right = Node(value = 'E')
    rootNode.right.left = Node(value = 'F')
    rootNode.right.right = Node(value = 'G')

    dfs_preorder(rootNode)
    print('')
    dfs_inorder(rootNode)
    print('')
    dfs_postorder(rootNode)