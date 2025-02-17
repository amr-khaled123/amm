class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_travarsal(self):
        element = []
        # visit left node
        if self.left:
            element += self.left.in_order_travarsal()

        # visit base(parent) node
        element.append(self.data)

        # visit right node
        if self.right:
            element += self.right.in_order_travarsal()

        return element

    def count_of_element(self, value):
        return self.in_order_travarsal().count(float(value))

    def Search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.Search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.Search(val)
            else:
                return False

    def max(self):
        x = self.in_order_travarsal()
        return x[len(x)-1]

    def minimum(self):
        x = self.in_order_travarsal()
        return x[0]


def built_Tree(x):
    root = BinarySearchTree(x[0])
    for i in range(1, len(x)):
        root.add_child(x[i])

    return root


x = list(map(float, input("enter number: ").split()))
y = built_Tree(x)
print(y.max())
print(y.minimum())
print(y.in_order_travarsal())
print(y.count_of_element(2.0))
