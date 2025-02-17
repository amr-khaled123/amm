# [2,0,4,3]
def insertion_sort(x=[]):
    n = len(x)
    for i in range(1, n):
        j = i  # 4
        print(x)
        while j > 0 and x[j-1] > x[j]:
            x[j-1], x[j] = x[j], x[j-1]
            print(x)
            j = j-1

    return x


print(insertion_sort([9, 8, 7, 6, 5, 0]))
# [8, 9, 7, 6, 5, 0]
# [7, 8, 9, 6, 5, 0]
# [6, 7, 8, 9, 5, 0]
# [5, 6, 7, 8, 9, 0]
# [0, 5, 6, 7, 8, 9]

print('-'*30)


def insertion_sort2(x):
    for i in range(1, len(x)):
        j = i
        while j > 0 and x[j-1] > x[j]:
            x[j-1], x[j] = x[j], x[j-1]
            j = j-1
            print(x)
    print(x)


insertion_sort2([2, 0, 5, 6, 9, 88, 0, 11, 0])
