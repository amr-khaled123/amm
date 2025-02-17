# Complixty = O(n*log2(n)) Merge_sort >selection sort >insertion sort > bubble sort
"""def merge_two_list_sort(a, b):
    m = len(a)
    n = len(b)
    j = 0
    i = 0
    result = []
    while i < m and j < n:
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    while i < m:
        result.append(a[i])
        i += 1

    while j < n:
        result.append(b[j])
        j += 1

    return result


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n//2
    a = merge_sort(arr[0:mid])
    b = merge_sort(arr[mid:n])
    r = merge_two_list_sort(a, b)
    return r


x = list(range(1000000, 0, -1))
print(merge_sort(x))"""


def Merge_two_list(x, y):
    n = len(x)
    m = len(y)
    i = 0
    j = 0
    l = []
    while i < n and j < m:
        if x[i] < y[j]:
            l.append(x[i])
            i += 1
        else:
            l.append(y[j])
            j += 1

    while i < n:
        l.append(x[i])
        i += 1

    while j < m:
        l.append(y[j])
        j += 1

    return l


def Merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n//2
    a = Merge_sort(arr[0:mid])
    b = Merge_sort(arr[mid:n])
    r = Merge_two_list(a, b)
    return r


# print(Merge_sort([5, 0, 1, 4]))

# sort but remove rebeat element
def sort(x=[]):
    x = x
    x = list(set(x))
    return x


# print(sort([2, 5, 3, 0, 5]))
