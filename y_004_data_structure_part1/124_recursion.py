def fact(x):
    if x == 1:
        return x
    return x*fact(x-1)


def sum(x):
    if x == 0:
        return x
    return x+sum(x-1)


print(f'-Sum of 5 is:{sum(5)}')
print(f"-Factorial of 5 is:{fact(5)}")


for i in range(10, 0, -1):
    print(f'-Factorial of {i} is {fact(i)}')
    print(f'-Sum of {i} is {sum(i)}')


def dream(x):
    if x == 0:
        return
    print(f'*{x} dream')
    dream(x-1)


print(dream(5))


y = 1
print('*'*20)


def power_of_two(x=float(), y=0):
    if x % 2 != 0:
        return f"{x} mul 2 poewr {y}"
#    if x % 2 == 0:
    return f"{power_of_two(x/2, y+1)}"


print(f"{power_of_two(7)}")
