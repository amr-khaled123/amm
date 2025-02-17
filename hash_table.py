x = [['1 march', 10],
     ['2 march', 20],
     ['3 march', 30],
     ['4 march', 40],
     ['5 march', 50]]

for element in x:
    if element[0] == '5 march':
        print(element[1]+x[1][1])

y = {'1 march': 10,
     '2 march': 20,
     '3 march': 30,
     '4 march': 40,
     '5 march': 50}

# print(y['1 march'])
# print(ord('a'))
# print(ord('m'))
# print(ord('r'))


def get_hash(word):
    h = 0
    for char in word:
        h += ord(char)
    return h % 100


print(get_hash('march 5'))


class HashTable:
    def __init__(self) -> None:
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


obj1 = HashTable()

obj1['13'] = 2
obj1['march 1'] = 10
obj1['march 2'] = 20
obj1['march 2'] = 30
obj1['march 4'] = 40

del obj1['march 1']

print(obj1['march 1'])
# obj1.__setitem__('13', 60)
# print(obj1.get_hash('13'))
# print(obj1.__getitem__('13'))
# print(obj1.arr[0])
