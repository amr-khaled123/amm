# -------------------------
# -- Decorators => Intro --
# -------------------------


def mydecorator(func):
    def nestedfunc():
        print("Before")
        func()
        print("After")
    return nestedfunc

@mydecorator
def sayhello():
    print("hello from say hello function".title())
@mydecorator
def sayhowar():
    print("how are you".title())

# afterdecoration = mydecorator(sayhello)
# afterdecoration()

sayhello()
sayhowar()
def num(i):
    def nested_num():
        print("before")
        i()
        print("after")
    return nested_num()
@num
def n():
    for i in range(10):
        print(i)