# print_list
# add item to the lists
class listNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_list(head):
    while head != None:
        print(head.value)
        head = head.next


def append_element(head, value):
    node = listNode(value)
    if head == None:
        head = node
    else:
        while head.next != None:
            head = head.next
        head.next = node
    return head


node1 = listNode(4)
node2 = listNode(1)
node3 = listNode(2)

node1.next = node2
node2.next = node3

head = node1

print('before')
print_list(head)
append_element(head, 10)
print('after')
print_list(head)
