from collections import deque

if __package__ is None:
    import sys
    from os import path
    print(path.dirname( path.dirname( path.abspath(__file__) ) ))
    sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))
    from tree.node import Node
else:
    from ..node import Node

#dfs 이용해서 p, q 가장 낮은 레벨의 공통 조상 탐색해보기
def lca(root, p, q) :
    # 1. 자기 자신이 없거나 p, q값이 없으면 return none
    if root is None or p is None or q is None: return None
    # 2. 현재 자기 자신의 값이 p or q인경우 자기 자신 리턴
    if root.value is p or root.value is q: return root
    # left 노드측 dfs 순회 해서 값 확인
    left = lca(root.left, p, q)
    # right 노드측 dfs 순회 해서 값 확인
    right = lca(root.right, p, q)
    # 3. 만약 왼쪽과 오른쪽 노드가 모두 값이 있다면 자기 자신을 반환
    if left and right : return root
    # 4. 만약 왼쪽 혹은 오른쪽 한쪽만 값이 있다면 값이 있는 쪽의 노드 반환
    return left or right


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

    print(lca(tree, 8, 1).value)
