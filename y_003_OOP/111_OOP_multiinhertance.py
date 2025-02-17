# ---------------------------------------------------------
# -- Object Oriented Programming => multiple inheritance --
# ---------------------------------------------------------

class BaseOne:

    def __init_(self):
        print("base one")

    def func_one(self):
        print("one")


class BaseTwo:

    def __init__(self):
        print("base two")

    def func_two(self):
        print("two")


class Derived(BaseOne, BaseTwo):
    pass


my_var = Derived()
print(my_var.func_one)
print(Derived.mro())
