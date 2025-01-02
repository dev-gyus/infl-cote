
class History:
    def __init__(self, url, prev = None, next = None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory(object):
    def __init__(self, homepage):
        homepage = History(homepage)
        self.head = homepage
        self.tail = homepage
        self.curr = homepage

    def visit(self, url):
        new_history = History(url)
        if self.curr.next is None:
            self.curr.next = new_history
            new_history.prev = self.curr
            self.tail = new_history
        else:
            new_history.next = self.curr.next
            new_history.prev = self.curr
            self.curr.next.prev = new_history
            self.curr.next = new_history
        self.curr = new_history

    def back(self, steps):
        for _ in range(steps):
            if self.curr.prev is None:
                break
            self.curr = self.curr.prev
        return self.curr.url

    def forward(self, steps):
        for _ in range(steps):
            if self.curr.next is None:
                break
            self.curr = self.curr.next
        return self.curr.url

if __name__ == '__main__':
    browserHistory = BrowserHistory('https://www.python.org')
    browserHistory.visit("google.com")
    browserHistory.visit("facebook.com")
    browserHistory.visit("youtube.com")
    print(browserHistory.back(1))
    print(browserHistory.back(1))
    print(browserHistory.forward(1))
    browserHistory.visit("linkedin.com")
    browserHistory.visit("linkedin2.com")
    print(browserHistory.forward(2))
    print(browserHistory.back(2))
    print(browserHistory.back(1))