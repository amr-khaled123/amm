# Stack
class stack:

    def __init__(self, list1):
        self.list1 = []

    def push(self, element):
        self.list1.append(element)

    def isEmp(self):
        if len(self.list1) == 0:
            return True
        else:
            return False

    def pop(self):
        if self.isEmp():
            print("list doesn\'t have any element")
        else:
            self.list1.pop()

    def top(self):
        if self.isEmp():
            print('list doesn\'t have elements')
        else:
            print(self.list1[-1])


object1 = stack([])
# object1.push(0)
# object1.push(1)
# object1.push(3)
# object1.push(2)
# object1.push(5)
# object1.push(4)
# object1.push(6)
# object1.push(8)
# object1.push(7)
# object1.push(9)

print(object1.list1)
object1.pop()
print(object1.list1)
object1.top()
