class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, value:any):
        node = Node(value, None)
        if self.head is None:
            self.head = node
            print(self.head.value)
        else:
            currentNode = self.head
            while(currentNode.next):
                currentNode = currentNode.next
            currentNode.next = node
            print(currentNode.next.value)
            #;;
    def __str__(self):
        result = '['
        if self.head is not None:
            current = self.head
            buffer = ""
            while current:
                buffer += (str(current.value) + ',')
                current = current.next
            result += buffer.rstrip(",")
        result += "]"
        return result


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(ll)
