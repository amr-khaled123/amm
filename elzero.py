import seaborn as sb


def sayhello(name):
    print(f"hello {name}".title())


def sayhowareyou(name):
    print(f"how are you {name}".title())


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)


def sortk(x=[]):
    x = x
    x = list(set(x))
    return x


def power(x, y):
    i = 0
    answer = 1
    while i < y:
        answer *= x
        i += 1
    return answer


def power_of_2(x=[]):
    square = list(map(lambda x: x*x, x))
    return square

# import termcolor
# import pyfiglet
# for i in range(0,6):
#     print(termcolor.colored(pyfiglet.figlet_format('&'*i),color="green"))


def merge_sort(x, y):
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


def Sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n//2
    a = Sort(arr[0:mid])
    b = Sort(arr[mid:n])
    r = merge_sort(a, b)
    return r


print(help(sb.pairplot))
