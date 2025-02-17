# ---------------------------------
# -- Object Orianted Programming --
# ---------------------------------

"""class member:
    not_allowed_name=["hell","fuck","devil"]
    gender_allow=["female","Female","male","Male","male".upper,"female".upper]
    def __init__(self,first_name,middle_name,last_name,gender):
        self.fname=first_name
        self.mname=middle_name
        self.lname=last_name
        self.g=gender
    def full_details(self):
        if self.fname in member.not_allowed_name:
            try :
                print(10/0)
            except ZeroDivisionError:
                print("name not allowed")

        elif self.g not in member.gender_allow:
            try:
                print(10/0)
            except ZeroDivisionError:
                print("gender not mawojod")

        elif self.g[0]=="m" or self.g[0]=="M":
            print(f"hello mr {self.fname} {self.mname} {self.lname}".title())

        elif self.g[0]=="f" or self.g[0]=="F":
            print(f"hello ms {self.fname} {self.mname} {self.lname}".title())



x=member("amr","khaled","gamal","female")
x.full_details()"""


"""class person:
    def __init__(self, names, ages, hieghts):
        self.name1 = names
        self.age1 = ages
        self.hieght1 = hieghts

    def name(self):
        print(self.name1)

    def age(self):
        print(self.age1)

    def hieght(self):
        print(self.hieght1)


y = person("amr", 18, 53)
y.name()"""


class member:
    age = int()
    name = str()
    j = 1

    def __init__(self, age, name):
        self.a = age
        self.n = name

    def fact(self):
        for i in range(1, (self.a)+1):
            self.j *= i
            i += 1
        print(self.j)


y = member(5, "amr")
y.age = 5
y.fact()
