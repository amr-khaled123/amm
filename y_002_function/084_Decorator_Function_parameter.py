# --------------------------------------------
# -- Decorators => Function With Parameters --
# --------------------------------------------


def mydecorator(func):
    def nestedfunc(num1,num2):
        if num1<0 and num2<0:
            print("two numbers are minus")
        elif num1<0 or num2<0 and num1<num2:
            print("first number is minus")
        elif num1<0 or num2<0 and num1>num2:
            print("second number is minus")
        func(num1,num2)
    return nestedfunc

@mydecorator
def claculate(n1,n2):
    print(f"{n1} + {n2} = {n1 + n2}")

claculate(-10,-20)