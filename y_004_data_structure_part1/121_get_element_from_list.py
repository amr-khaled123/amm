class list_node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_list(head):
    p = head
    while p != None:
        print(f" - {p.value}")
        p = p.next


def append_element(head, value):
    node = list_node(value)
    p = head
    if p == None:
        p = node
    else:
        while p.next != None:
            p = p.next
        p.next = node
    return head


def get_elem(head, index):
    i = 0
    p = head
    while i < index and head != None:
        p = p.next
        i += 1
    if head != None:
        return head.value
    else:
        return "index error"


def remove_element(head, item):
    p = head
    q = None
    while p != None and p.value != item:
        q = p
        p = p.next
    if p == None:
        print("doesn\'t exist")
    else:
        if p == head:
            head = head.next
        else:
            q.next = p.next
    return head


node1 = list_node(10)
node2 = list_node(5)
node3 = list_node(6)

node1.next = node2
node2.next = node3

head = node1

# print(get_elem(head, 0)) 10
# print(get_elem(head, 2)) 6

append_element(head, 7)

print_list(head)
remove_element(head, 2)
remove_element(head, 5)
print_list(head)
