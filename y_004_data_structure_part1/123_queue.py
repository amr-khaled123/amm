# Queue
class Queue:
    def __init__(self, value=[]):
        self.value = value

    def enqueue(self, value):
        self.value.append(value)

    def dequeue(self):
        if self.isEmpty():
            print('list is empty')
        else:
            self.value.remove(self.value[0])

    def isEmpty(self):
        return self.value == []


queue = Queue()
queue.dequeue()
queue.enqueue(0)
queue.enqueue(10)
print(queue.value)
