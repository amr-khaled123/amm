# -----------------------------------------------------
# --Object Oriented Programming => Getters & Setters --
# -----------------------------------------------------


"""class Name:

    def __init__(self, name):
        self.__name = name

    def say_hello(self):
        return f"hello {self.__name}"

    def Get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


one = Name("ahmed")
# one._Name__name = "amr"
# print(one.__name)
one.set_name("amr")
print(one.Get_name())
print(one.say_hello())


class Member:
    def __init__(self, length=0, width=0, r=0, l=0):
        # self.__name = name
        self.length = length
        self.width = width
        self.r = r
        self.l = l

    def area_circel(self):
        pi = 22/7
        return f"area of circel= {pi*self.r*self.r}"

    def area_square(self):
        return f"area of square= {self.l**2}"

    def area_s(self):
        return f"area= {self.length*self.width}"


# shape = Member(r=7, length=4, width=5, l=3)
# print(shape.area_circel())
# print(shape.area_square())
# print(shape.area_s())"""


"""class Employee:

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.fulname = first+''+last
        self.gmail = self.fulname+"@gmail.com"
        try:
            self.pay = int(pay)
        except ValueError:
            print('enter integer number')

    @property
    def email(self):
        return f"{self.gmail}"

    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.fname = first
        self.lname = last

    @fullname.deleter
    def fullname(self):
        print('Deleted name: ')
        self.fname = None
        self.lname = None


employee_1 = Employee('amr', 'khaled', 7000)
employee_2 = Employee('ahmed', 'mohamed', 5000)

print(employee_1.fullname)
del employee_1.fullname
print(employee_1.fullname)"""


class Name:

    def __init__(self, name, age):
        self.__name = name
        self.age = age

    @property
    def say_hello(self):
        return f"hello {self.__name}"

    @property
    def age_in_days(self):
        return f"your age equal {self.age*365} day"


one = Name("ahmed", 19)
# one._Name__name = "amr"
# print(one.__name)

print(one.say_hello)
print(one.age_in_days)
