# ---------------------------------
# -- Built in Function => reduce --
# ---------------------------------

from functools import reduce
# Sumation of number
def sumAll(num1, num2):
    return num1 + num2

numbers1 = [1, 2, 4, 5, 8, 10]
result = reduce(sumAll, numbers1)

print(result)
print("*"*40)

def sumation(num1, num2):
    return num1 + num2

n = int(input("enter number to calculate sum of number\n".title()))
a = list(range(1, n+1, 1))
mynumbers = a
result = reduce(sumation, mynumbers)

print(f"sum of {n} = {result}")
print('*'*40)

# Factorial of number
def multiplyall(num1, num2):
    return num1 * num2

n = int(input("enter number to calculate factorial\n".title()))
a = list(range(1,n+1,1))
mynumbers = a
result = reduce(multiplyall, mynumbers)

print(f"Factorial of {n} = {result}")
print("*"*40)


# Sumation With Lambda
n = int(input("enter number to calculate sumation\n".title()))
numbers = list(range(1,n+1,1))
result = reduce(lambda num1, num2: num1 + num2, numbers)

print(f"sum of {n} = {result}")
print("*"*40)


# Factorial With Lambda
n = int(input("enter number to calculate factorial\n".title()))
result = reduce(lambda num1, num2: num1 * num2, list(range(1, n+1, 1)))

print(f"Factorial of {n} = {result}")
print("*"*40)
