# Searching algorithm
# Binary Search
"""def sort_list(x=[]):
    for j in range(len(x)-1):
        for i in range(len(x)-1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
            else:
                continue
    return x"""


def search(x=[], y=None):
    #    x = sort_list(x)
    for i in range(len(x)):
        index_min = i
        for j in range(i, len(x)):
            if x[j] < x[i]:
                index_min = j
        x[index_min], x[i] = x[i], x[index_min]
    n = len(x)-1  # 5
    while n < len(x):  # 6
        # print(n)
        if x[n] == y:
            return f"{y} at index {n} after sort and sort is {x}"
        elif x[n] > y:
            n = n//2  # 2
        elif x[n] < y:
            n += 1
    return 'not in list'


x = [0, 2, 1, 3, 6, 5, 2, 5, 8, 88, 77, 22, 222, 666, 66, 33]
y = 0

print(search(x, y))
