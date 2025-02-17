# ---------------------------------
# -- object oriented programming --
# ---------------------------------

class member:
    def __init__(self, first_name, middle_name, last_name):
        self.name = first_name
        self.mname = middle_name
        self.fname = last_name


member_one = member('amr', 'khaled ', 'gamal')
member_two = member('abdelrahman', 'khaled', 'gamal')
member_three = member('manar', 'khaled', 'gamal')
print(member_one.name, member_one.mname, member_one.fname)

# ======================================


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"hello {self.name} your age is {self.age}")


person1 = person("John", 30)
person2 = person("Jane", 25)

person1.speak()
person2.speak()

# =============================================


class car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def show(self):
        print(f"car model is {self.model} car color is {self.color}")


car1 = car("black", "gtr")
car1.show()
