# -------------------------------------------------
# -- Object Oriented Programming => polymorphism --
# -------------------------------------------------

class a:

    def do_something(self):
        print("from class A")
        raise NotImplementedError("derived class must implement this method")


class b(a):

    def do_something(self):
        print("from class B")


class c(a):

    print("a")


my_instance = c()
my_instance.do_something()
# -------------------------------
"""if __name__ == '__main__':
    n = int(input())
    name1 = float(10**36)
    for _ in range(5):
        name = input()
        score = float(input())
        if name1 > score:
            name1 = score
        _ += 1
    print(f"dfds {name1}")"""
