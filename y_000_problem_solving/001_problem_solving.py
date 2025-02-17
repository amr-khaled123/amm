"""def name(x):
    if len(x) == 1:
        return x
    if x[0] == x[1]:
        return name(x[1:])
    return x[0] + name(x[1:])


y = name("AABCAAADAfg")
print(len(y))
k = int(input("enter number "))
n = int(len(y)/k)
f = n
j = 0
m = 0
while (m < k):
    print(y[j:n])
    m += 1
    j += f
    n += f

x = "amrkha"
print(x[0:2])
print(x[2:4])
print(x[4:6])
"""

"""x = int(input())
y = int(input())
z = int(input())
n = int(input())
l = list()
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+k+j) != n:
                print(l)
                l.append([i, j, k])
print(l)"""


def fun(x):
    x = int(input("enter number"))
    n = 0
    l = list()
    sum = 0
    while n < x:
        m = input("enter: ").split()
        l.append(m)
        n += 1
    name = input("enter name")
    for i in l:
        if i[0] == name:
            for j in (i[1:]):
                sum += int(j)
    print(format((sum/3), '.2f'))


x = 2
print(format(x, '.2f'))
