# bubble sort make it in 2 loop then the big O naotaion will be O(n^2)
def Bubble_sort(x):
    n = len(x)-1
    permutation = True
    while permutation:
        permutation = False
        for i in range(n):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                permutation = True
    return x


print(Bubble_sort([2, 0, 6, 8, 7]))


def Bubble_sort2(x):
    boolean = True
    while boolean:
        boolean = False
        for i in range(0, len(x)-1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                boolean = True
    print(x)


Bubble_sort2([2, 0, 1, 3, 8, 7, 6])
