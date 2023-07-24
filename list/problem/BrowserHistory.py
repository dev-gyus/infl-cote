# 링크드 리스트에 들어갈 노드 클래스
class ListNode(object):
    def __init__(self, prev_node, url, next_node):
        self.url = url
        self.prev_node = prev_node
        self.next_node = next_node

#
class BrowserHistory(object):
    def __init__(self, homepage):
        self.current = ListNode(None, homepage, None)
        self.head = self.current
        self.tail = self.current

    def visit(self, url):
        newNode = ListNode(self.current, url, None)
        self.current.next_node = newNode
        self.current = newNode
        self.tail = self.current

    def back(self, steps):
        for idx in range(steps):
            if self.current.prev_node is None:
                return self.current.url
            self.current = self.current.prev_node
        return self.current.url

    def forward(self, steps):
        for idx in range(steps):
            if self.current.next_node is None:
                return self.current.url
            self.current = self.current.next_node
        return self.current.url



browserHistory = BrowserHistory("leetcode.com")
print(browserHistory.visit("google.com"))
print(browserHistory.visit("facebook.com"))
print(browserHistory.visit("youtube.com"))
print(browserHistory.back(1))
print(browserHistory.back(1))
print(browserHistory.forward(1))
print(browserHistory.visit("linkedin.com"))
print(browserHistory.forward(2))
print(browserHistory.back(2))
print(browserHistory.back(7))
