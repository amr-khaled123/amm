class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, value):
        node = Node(value, self.head)
        self.head = node

    def insert_at_end(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        p = self.head
        while p.next:
            p = p.next
        p.next = Node(value, None)

    def print_llist(self):
        if self.head is None:
            print('list is empty')
            return
        while self.head != None:
            print(f"-{self.head.value}")
            self.head = self.head.next

    def insert_value_beging(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_begining(data)

    def insert_value_end(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid error")
        if index == 0:
            self.head = self.head.next
        p = self.head
        count = 0
        while p:
            if count == index-1:
                p.next = p.next.next
                break
            p = p.next
            count += 1

    def remove_value(self, data):
        p = self.head
        if p.next == data:
            self.remove_index(0)
            return
        count = 0
        while p:
            if p.value == data:
                p = p.next
                break
            p = p.next
            count += 1
        return self.remove_index(count)

    def insert_index(self, index, data):
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        p = self.head
        while p:
            if count == index-1:
                node = Node(data, p.next)
                p.next = node

            p = p.next
            count += 1


obj1 = LinkedList()
# obj1.insert_at_begining(5)
# obj1.insert_at_begining(10)
# obj1.insert_at_begining(6)
# obj1.insert_value_end(['banana', 'mooz', 'tofah', '3enb'])
# obj1.insert_value_beging([1, 2, 5, 0])
# print("the length of list: ", obj1.get_length())
# obj1.print_llist()
# print('*'*20)
# obj1.insert_value_end([1, 2, 5, 0])
# obj1.print_llist()
# print('*'*20)
# print("the length of list: ", obj1.get_length())
obj1.insert_value_end(['amr', 'mooz', 'tofah', '3enb'])
obj1.remove_value('amr')
# obj1.remove_index(0)
obj1.print_llist()
obj1.insert_at_begining([2, 5, 6, 8])
# obj1.remove_value(5)
obj1.print_llist()
