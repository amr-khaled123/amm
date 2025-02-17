class node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class tree(node):
    def __init__(self, data):
        self.poin = data
        self.next = None

    def append(self, val):
        if (self.poin == None):
            self.poin = node(val)
        else:
            self.next = node(val)
            self.next.next = None

    def prin(self):
        while (self.next != None):
            print(self.poin)
            self.next = self.next.next


x = tree(5)
x.append(10)
x.append(15)
x.append(20)
x.prin()
