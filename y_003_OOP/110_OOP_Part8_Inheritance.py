# ------------------------------------------------
# -- Object Oriented Programming => inheritance --
# ------------------------------------------------

def sep():
    print("*"*40)


class Food:

    def __init__(self, name, price, amr, n):
        self.name = name
        self.price = price
        self.amr = amr
        self.n = n
        self.n = int()

    def eat(self):
        print(f"{self.amr} Eat method from base class")

    def sum(self, n):
        if n == 1:
            return 1
        else:
            return n+sum(n-1)


class apple(Food):
    def __init__(self, name, price, amr, n):
        super().__init__(name, price, amr, n)
        print(f"{self.name} this apple from main class {self.price}")


# name_one = Food(10, 10)
name_two = apple("amr", 10, 20, 5)
name_two.eat()
# name_two.sum(5)


def sum(n):
    if n == 1:
        return 1
    else:
        return n+sum(n-1)


print(sum(5))
