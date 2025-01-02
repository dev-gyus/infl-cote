
class Node:
    prev = None
    next = None
    def __init__(self, data):
        self.data = data

class LinkedList:

    def __init__(self):
        self.head = None

    # O(n)
    def add(self, node):
        if self.head is None:
            self.head = node
        else:
            last_node = self.__getLastNode(self.head)
            node.prev = last_node
            last_node.next = node
    # O(n)
    def __getLastNode(self, node):
        if node.next == None:
            return node
        else:
            return self.__getLastNode(node.next)

    # O(n)
    def __getIdxNode(self, idx, node):
        if idx == 0:
            return node
        else:
            return self.__getIdxNode(idx - 1, node.next)

    # O(1)
    def addNext(self, target, node):
        if target.next is not None:
            target.next.prev = node
            node.next = target.next
        target.next = node
        node.prev = target

    # O(1)
    def addPrev(self, target, node):
        if target.prev is not None:
            target.prev.next = node
            node.prev = target.prev
        target.prev = node
        node.next = target

    # O(1)
    def remove(self, node):
        if node.next is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node.prev.next = None

    # O(n)
    def toString(self):
        printArr = []
        node = self.start
        printArr.append(node.data)
        while node.next is not None:
            node = node.next
            printArr.append(node.data)
        print(printArr)

if __name__ == '__main__':
    linked_list = LinkedList()
    node1 = Node(1)
    linked_list.add(node1)
    node2 = Node(2)
    linked_list.add(node2)
    node3 = Node(3)
    linked_list.add(node3)

    node5 = Node(5)
    linked_list.addNext(node3, node5)
    linked_list.toString()
    linked_list.remove(node5)

    linked_list.addPrev(node3, node5)
    linked_list.toString()


