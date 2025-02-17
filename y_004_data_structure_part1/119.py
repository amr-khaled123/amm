# node

class listNode:
    def __init__(self, value, next=None):
        self.value = [value]
        self.next = next

    def push(self, val):
        self.value.append(val)

    def delete(self, val):
        if val == True:
            self.value.remove(val)
        else:
            print('not in list')

    def pop(self):
        self.value.pop()


node1 = listNode(1)
node2 = listNode(2)
node3 = listNode(3)

node1.push(5)
node1.delete(1)
print(node1.value)

node1.next = node2
node2.next = node3

head = node1

# --------------------------------------------
"""
# import numpy as np
# np.array = [[1, 2, 2], [3, 5, 6], [2, 4, 8]]

# for i in range(0, len(np.array)):
#     print(f"row {i}:", end=" ")
#     for j in range(0, len(np.array[0])):
#         print(f"{np.array[i][j]}", end=" ")
#     print()"""
