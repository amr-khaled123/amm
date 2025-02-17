#======================================
#== Function Parameters And Argument ==
#======================================

a, b, c="amr","ahmed","aymen"
print(f"hello {a}")
print(f"hello {b}")
print(f"hello {c}")
print("*"*50)

#def mean [define]
def say_hello(name):
    print(f"hello {name}")
say_hello(name=input("enter you name\n".title()))
say_hello(a)
say_hello(b)
say_hello(c)
print("*"*50)

def addition(n1,n2):
    print(f"addition of two number= {n1+n2}")
addition(n1=int(input("enter first number\n".title())),n2=int(input("enter second number\n".title())))
print("*"*50)

def full_name(first,middle,last) :
    print(f"hello {first.title().strip()} {middle.title().strip()} {last.title().strip()}")
full_name("  amr  ","  khaled  ","  gamal  ")