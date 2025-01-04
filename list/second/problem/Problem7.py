class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def LCA(root, p, q):
    if root is None:
        return None
    # left 결과물
    l = LCA(root.left, p, q)
    # right 결과물
    r = LCA(root.right, p, q)

    if root == p or root == q:
        return root
    if l is not None and r is not None:
        return root
    return l or r

if __name__ == '__main__':
    node3 = Node(3, None, None)
    node5 = Node(5, None, None)
    node1 = Node(1, node3, node5)
    node4 = Node(4, None, None)
    node2 = Node(2, node1, node4)

    lca = LCA(node2, node5, node1)
    print(lca.data)
