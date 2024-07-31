from collections import deque

def bfs(root):
    visit = []
    if root is None: return visit
    queue = deque()
    queue.append(root)
    while queue:
        # 현재 노드
        cur_node: Node = queue.popleft()
        # 방문한 노드값 배열에 추가
        visit.append(cur_node.value)
        # 이번 방문에 대한 값은 배열에 추가 했으므로
        # 다음번에 방문할 노드는 트리의 왼쪽부터 큐에 추가
        if cur_node.left: queue.append(cur_node.left)
        if cur_node.right: queue.append(cur_node.right)
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
