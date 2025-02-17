# Stack
class Stack:
    def __init__(self):
        self.s = []

    # insert new element to the end of the stack
    def push(self, value):
        self.s.append(value)

    # remove the last element in the stack
    def pop(self):
        if self.isEmpty():
            print("can\'t pop because list is empty")
        else:
            self.s.pop()
            return

    # remove item from list
    def remove(self, value):
        try:
            self.s.remove(value)
            print(f"{value} => has been removed")
        except ValueError:
            print(f"{value} => not in stack")

    # print list
    def print_s(self):
        print(f"{self.s}")

    # top of stack
    def top(self):
        if self.isEmpty():
            return f"stack hasn\'t have any element"
        else:
            return f"{self.s[-1]}"

    # size of stack
    def size(self):
        return f"size of stack = {len(self.s)}"

    # listt is impty
    def isEmpty(self):
        return self.s == []


stack1 = Stack()
stack1.push(5)
stack1.push(7)
stack1.push(0)
stack1.push(8)
stack1.push('amr')

print(stack1.top())
stack1.print_s()
stack1.pop()
print(stack1.top())
stack1.print_s()
print(stack1.size())
print(stack1.isEmpty())
