# ---------------------------------
# -- Object Oriented Programming --
# ---------------------------------

class member:
    def __init__(self, first_name, middle_name, last_name):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name

    def full_name(self):
        print(f"{self.fname} {self.mname} {self.lname}")


x = member("amr", "khaled", "gamal")
x.full_name()

"""class member:
    def __init__(self,first_name,middle_name,last_name,gender):
        self.fname=first_name
        self.mname=middle_name
        self.lname=last_name
        self.g=gender
    def full_details(self):
        if self.g[0]=="m" or self.g[0]=="M":
            print(f"hello mr {self.fname} {self.mname} {self.lname}".title())
        elif self.g[0]=="f" or self.g[0]=="F":
            print(f"hello ms {self.fname} {self.mname} {self.lname}".title())
        else:
            print("missed gender")

x=member("amr","khaled","gamal","adfvds")
x.full_details()"""


x = []
i = 0
fact = 1
x1 = 1
while (i == 0):
    lists = input(f"enter element of row{x1}: ").split()
    x.append(lists)
    x1 += 1
    i = int(input("enter 0 to continue: "))
z = 0
y = list(filter(int, x[z]))
for n in y:
    for m in range(1, int(n)+1):
        fact *= m
    print(f"factorial of {int(n)} = {fact} ")
    fact = 1


"""x=[]
i=0
fact=1
x1=1
while(i==0):
    lists = input(f"enter element of row{x1}: ").split()
    x.append(lists)
    x1+=1
    i=int(input("enter 0 to continue: "))
print(x)"""
