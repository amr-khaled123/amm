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

    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()

    def minimum(self):
        if self.left is None:
            return self.data
        return self.left.minimum()

    def delete_item(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_item(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_item(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.right.minimum()
            self.data = min_val
            self.right = self.right.delete_item(min_val)
        return self

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


def built_Tree(x):
    root = BinarySearchTree(x[0])
    for i in range(1, len(x)):
        root.add_child(x[i])

    return root


def in_order(root):
    list = []
    if root == None:
        return
    in_order(root.left)
    print(root.data)
    in_order(root.right)


# x = list(map(float, input("enter number: ").split()))
m = [5, 1, 2, 8, 4, 3]
y = built_Tree(m)

print(y.in_order_travarsal())
y.delete_item(4)
# in_order(y)
print(y.in_order_travarsal())
# y.delete_item(20)
# y.delete_item(17)
# print(y.in_order_travarsal())
# print(y.max())
# print(y.minimum())"""


class BinaryTr:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, val):
        if val == self.data:
            return

        if val < self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BinaryTr(val)

        else:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BinaryTr(val)

    def print_Tree(self):
        element = []
        if self.left:
            element += self.left.print_Tree()

        element.append(self.data)
        if self.right:
            element += self.right.print_Tree()

        return element

    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()

    def min_1(self):
        if self.left is None:
            return self.data
        return self.left.min_1()

    def delete(self, val):
        if self.Search(val) != True:
            return
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.right.min_1()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

    def Search(self, val):
        if val == self.data:
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


def build_tree(x):
    root = BinaryTr(x[0])

    for i in range(1, len(x)):
        root.add_child(x[i])

    return root


x = list(map(int, range(500, 0, -1)))
y = build_tree(x)
print(y.print_Tree())
# print(y.max())
# print(y.min())
print(y.delete(4))
print(y.print_Tree())
print(y.Search(3))
#               5
#          1        8
#            2
#               4
#            3   None
