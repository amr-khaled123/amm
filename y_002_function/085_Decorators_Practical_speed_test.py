# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------

from time import time


def mydecorator(func):
    def nestedfunc(*numbers):
        for number in numbers:
            if number < 0:
                print("one of number are minus")
        func(*numbers)
    return nestedfunc


@mydecorator
def calculate(*x):
    print(sum(x))


calculate(10, -20, 30)


def speedtest(func):
    def wrapper():
        start = time()
        print("before")
        func()
        end = time()
        print(f"function time {end-start}")
    return wrapper


"""@speedtest
def bigloop():
    for number in range(50):
        print(number)


bigloop()"""


@speedtest
def sortl(x=[]):
    y = int(len(x))-1
    for j in range(y):
        for i in range(y):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    print(x)


sortl()
