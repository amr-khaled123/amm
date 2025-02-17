class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' '*self.get_level()*4
        prefix = spaces+"|_>" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def Root():
    root = TreeNode('electronics')

    laptop = TreeNode('Laptpop')
    laptop.add_child(TreeNode('mac'))
    laptop.add_child(TreeNode('HP'))
    laptop.add_child(TreeNode('Dell'))

    CellPhone = TreeNode('CellPhone')

    iphone = TreeNode('iphone')

    Samsung = TreeNode('samsung')

    Oppo = TreeNode('oppo')
    Oppo.add_child(TreeNode('Reno'))
    Oppo.add_child(TreeNode(':F'))

    CellPhone.add_child(iphone)
    CellPhone.add_child(Samsung)
    CellPhone.add_child(Oppo)

    tv = TreeNode('TV')
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('Toshiba'))

    root.add_child(laptop)
    root.add_child(CellPhone)
    root.add_child(tv)
    return root


root = Root()

names = [2, 0, 4, 5, 8, 6]
names_set = set(names)
print(names_set)
