# calculate summation of number
"""n = 1000
print((int(n*(n+1))/2))
sum = 0"""
"""for i in range(1, n+1):
    sum += i

print(sum)"""


# recursion
"""def fib(n=float()):
    if n < 5:
        return n
    return fib(n/2)


print(fib(32))"""

"""n, m = map(int, input().split())
for i in range(n//2):
    print(('.|.'*(2*i+1)).center(m, '-'))
print('WELCOME'.center(m, '-'))
for i in range(n//2, 0, -1):
    print(('.|.'*(2*i-1)).center(m, '-'))"""

"""n = int(input())
for i in range(1, n+1):
    x = bin(i)
    y = oct(i)
    z = hex(i)
    print(f"{i}   {y[2:]}   {z[2:]}   {x[2:]}")"""


# -----------------------------
"""x = 'e'
y = list
match(x):
    case 'a':
        print('Guinea equ\nNideria\nCote divoire\nguinea-bissau')
    case 'b':
        print('Cape Verde\nEgypt\nGhana\nMozambique')
    case 'c':
        print('Sengal\nCameroon\nGuinea\nGambia')
    case 'd':
        print('Angola\nBurkinaFaso\nMauritania\nAlgeria')
    case 'e':
        print('Mali\nSouthAfrica\nNambia\nTunisia')
    case 'f':
        print('Morocco\nDRCongo\nZambia\nTanzania')"""

# ----------------------------------------------------------
"""x = [0, 1, 2, 3, 4, 3, 6, 9]
y = 5


def search(x, y):
    n = len(x)-1
    for i in range(0, len(x)-1):
        try:
            if x[n] == y:
                return f"{y} at index {n}"
                break
            elif x[n] > y:
                n = int(n/2)
            elif x[n] < y:
                n += 1
        except IndexError:
            return 'not in list'

    return 'not in list'


print(search(x, y))"""
# --------------------------------------------
"""x = [1, 0, 5, 6, 8, 7, 9, 2]
item = 3


def search_binary(list, item):
    low = 0
    high = len(list)-1
    while (low <= high):
        guess1 = list[high]
        guess2 = list[low]
        if guess1 == item:
            return high
        elif guess2 == item:
            return low
        else:
            low += 1
            high -= 1
    return f"item {item} not in list"


print(search_binary(x, item))"""
# ------------------------------------------
"""
for i in range(0, len(x)-1):
    if x[i] == item:
        print(i)
        break
    else:
        continue"""


# ----------sort list-------------
"""def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0  # Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))"""


x = [2, 0, 3, 5, 6, 1, 8, 7]
"""y = input(f"sort this from smaller to greater {x}: ").split()
for i in range(0, len(y)):
    y[i] = int(y[i])  # type: ignore"""


def sort(arr=[]):
    for j in range(0, 1):
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                continue
    return arr


print(sort(x))
