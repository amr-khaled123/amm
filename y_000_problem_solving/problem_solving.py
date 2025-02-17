"""x = {}
list1 = []
names = []
c = []
for i in range(0, 4, 1):
    name = input("enter name: ")
    score = float(input("enter grade: "))
    list1.append(score)
    x.update({name: score})
list1.sort()
if list1[1] != list1[0]:
    c.append(list1[1])
elif list1[1] != list1[2]:
    c.append(list1[2])
elif list1[1] == list1[2]:
    c.append(list1[3])
for i, k in x.items():
    if c[0] == k:
        names.append(i)
    else:
        continue
names.sort()
for i in names:
    print(i)"""
# Nested List
"""x = 2
y = 2
z = 2
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            print([i, j, k])"""

# print(101010011000101011000111)

# import statistics as st
# a = [1, 2, 4, 5]

# b = st.geometric_mean(a)
# c = st.median(a)
# d = st.mean(a)
# e = st.fmean(a)
# print(b)
# print(c)
# print(d)
# print(e)


"""from time import time
def speedtest(func):
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"function time {end-start}")
    return wrapper"""


# @speedtest
# def prob():
"""n = int(input("enter number: "))
l = []
for i in range(0, n):
    stri = input("enter: ").split()
    if stri[0] == "print":
        print(l)
    elif stri[0][0] == "a":
        for i in stri[1:]:
            a = list(filter(int, i))
            l.append(int(*a))

    elif stri[0][0] == "i":
        l.insert(int(stri[1]), int(stri[2]))
    elif stri[0][0] == "s":
        l.sort()
    elif stri[0][0] == "r" and stri[0][2] == "m":
        l.remove(int(stri[1]))
    elif stri[0][0] == "p" and stri[0][1] == "o":
        l.pop()
    elif stri[0][0] == "r" and stri[0][2] == "v":
        l.reverse()

"""
# prob()
# print(l)

"""l = [10, 5]
l.pop()
print(l)
"""


"""c = []
y = "amr khaLeD"
print(y.swapcase())
# print("".join(y))
for i in range(len(y)):
    if y[i].isupper() == True:
        c.append(y[i].lower())
    elif y[i].islower() == True:
        c.append(y[i].upper())
    else:
        c.append(y[i])
print("".join(c))"""

"""name = 'amr'
owner = 'ahmed'
print(f"Hello {'boss'if name == owner else 'guest'}")"""

# ------------------------------------
# calculate points of won or lose or draw
"""s = ["2:2", "1:2", "3:2"]
m = 0
for i in (s):
    i = i.split(":")
    x = int(i[0])
    y = int(i[1])
    if x > y:
        m += 3
    elif x == y:
        m += 1
    elif x < y:
        m += 0
print(m)

g = s
points = sum((x > y)*3 or x == y for x, _, y in g)
print(points)"""

"""import cmath
print(round(cmath.tan(45*(22/7)/180).real))
m = 0
for i in range(90):
    if cmath.tan(i*(22/7)/180).real == 1 or cmath.tan(i*(22/7)/180).real > 1:
        m += round(cmath.tan(i*(22/7)/180).real)
    print(m)"""

# Lists Hackerrank
"""if __name__ == '__main__':
    N = int(input())
    list1 = []
    for i in range(N):
        inp = input().split()
        match(inp[0]):
            case "insert":
                list1.insert(int(inp[1]), int(inp[2]))
            case "print":
                print(list1)
            case "remove":
                list1.remove(int(inp[1]))
            case "append":
                list1.append(int(inp[1]))
            case "sort":
                list1.sort()
            case "pop":
                list1.pop()
            case "reverse":
                list1.reverse()"""

# tuples hackerrank
# n = int(input())
# t = tuple(map(int, input().split()))

# sort list

"""x = [56, 8, 83, 52, 87, 61, 70, 12, 40, 75, 29, 52, 8, 82, 100]
y = int(len(x))-1
for j in range(y):
    for i in range(y):
        if x[i] > x[i+1]:
            x[i], x[i+1] = x[i+1], x[i]

print(x)
print(y)"""

"""import elzero as m
x = [1, 2, 4, 10, 20, -10, 5]
print(m.sortl(x))
print(m.factorial(5))
print(m.power(2, 5))"""

# mutation
"""def mutate_string(st, p, character):
    l = list(st)
    l[p] = character
    st = ''.join(l)
    return st


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)"""

# find string
"""x = input("enter1")
y = input("ent")
m = 0
for i in range(0, len(x)):
    if x[i:i + len(y)] == y:
        m += 1
print(m)


def counter(string, sub_string):
    count = 0
    for x in range(0, len(string)):
        if string[x:x + len(sub_string)] == sub_string:
            count = count + 1
    return count


print(counter("amramr", "amr"))"""

# string wrap
"""def wrap(string, max_width):
    x = []
    for i in range(0, len(string), max_width):
        x.append((string[i:i+max_width]))
    return '\n'.join(x)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)"""

"""a = 5
b = 6
a = a+b  # 11
b = a-b  # 5
a = a-b  # 6
print(a, b)"""


# ----------------------------
"""from array import array
set_data = {1, 2, 2, 3, 4, 4, 5}
unique_set = list(set_data)

list_data = [5, 6, 0, 7, 8, 9, 9]
unique_list = list(set(list_data))

array_data = array('i', [10, 11, 12, 11, 13, 14, 14])
unique_array = array('i', set(array_data))

print(f"using sets {unique_set}")
print(f"using lists {unique_list}")
print(f"using array {set(unique_array)}")"""

# -------------------

"""import math as t
import numpy as n
y = (30/180)*t.pi
x = n.tan(y)
s = (t.sqrt(3))/2
print(0.5/s)
print(n.tan(y))
x = 1
for i in range(1, 5+1):
    x *= i

print(x)"""

# text alighn
"""s = input()
anum = False
abetic = False
digit = False
lower = False
upper = False
for i in s:
    if i.isalnum():
        anum = True
    if i.isalpha():
        abetic = True
    if i.isdigit():
        digit = True
    if i.islower():
        lower = True
    if i.isupper():
        upper = True

print(anum)
print(abetic)
print(digit)
print(lower)
print(upper)"""

"""x = float(40)
y = 0
for i in range(5):
    if x % 2 == 0:
        y += 1
    elif x % 2 != 0:
        continue
    x = x/2

print(y)"""

"""from PIL import Image
inp = 'A:\\خاص\\ALAHLY\\UA0700.jpg'
out = 'UA0700.png'

with Image.open(inp) as img:
    img.save(out, 'PNG', quality=100)

print("image successfully")"""

"""for i in range(10, 0, -1):
    print('*'*i)
for i in range(10, 0, -1):
    print('*'*i)"""


"""import matplotlip as mp
import numpy as np
from cvzone import HandTrackingModule
import cv2
import termcolor
import pyfiglet
x = 'Ultras\n Ahlawy'
print(termcolor.COLORS)
print(termcolor.cprint(pyfiglet.figlet_format(x), color='black'))


cap = cv2.VideoCapture(0)
detector = HandTrackingModule.HandDetector()

while (True):
    success, img = cap.read()
    detector.findHands(img)
    cv2.imshow('img', img)
    cv2.waitKey(1)"""

"""b = 32
if b & b-1 == 0:
    print("power")
else:
    print("df")

a = 13
b = 10
print(((a**5 % b)*(a**6 % b)) % b)
print((13**11) % b)
print(((3**4 % 17)**2) % 11)"""
"""if a % b == 0:
    print("b|a")
else:
    print('b not |a')
print(13 % 10)"""


# from binary to decimal
"""m = bin(5)
x = m[2:]
x = ' '.join(str(x))
x = x.split()
sum = 0
z = 0
x.reverse()
for i in x:
    sum += int(i)*2**z
    z += 1
print(sum)"""

# from octa to decimal
"""x = 1010
x = ' '.join(str(x))
x = x.split()
sum = 0
z = 0
x.reverse()
for i in x:
    sum += int(i)*8**z
    z += 1
print(sum)"""

# even and odd with binary
"""a = int(input("enter: "))
b = a-1
if a | b > a:
    print("a even")
else:
    print("odd")"""

"""x = [2, 5, 6, 4]
for i in range(len(x)):
    for i in range(0, len(x)-1):
        if x[i] > x[i+1]:
            # x[i] = x[i+1]+x[i]
            # x[i+1] = x[i]-x[i+1]
            # x[i] = x[i]-x[i+1]
            x[i], x[i+1] = x[i+1], x[i]
        else:
            x[i], x[i+1] = x[i], x[i+1]

print(x)"""

"""x = int(input("enter number"))
y = False
for i in range(2, 20):
    if x % i == 0 and x != i:
        y = True

if y == True:
    print(f"{x} not prime number ")
elif y == False:
    print(f"{x} is prime number")

print(31*31)
print(5/5)
print(5 % 2)"""


"""from functools import reduce
x = [2, 4, 5, 6]


def tarbe(x):
    m = []
    for j in x:
        m.append(j*j)
    return m


square = list(map(lambda x: x*x, x))
filt = list(filter(lambda x: x > 4, x))
print(tarbe(x))
print(filt)"""

"""import matplotlib.pyplot as pyplot
labels = ('amr', 'ahmed', 'khaled', 'gamal')
size = [45, 30, 15, 10]

pyplot.pie(size, labels=labels, autopct='%1.f%%',
           counterclock=False, startangle=180)
pyplot.show()"""

"""import cv2 as cv20
image = cv20.imread(r"A:\\01\\UA0703.jpg")
if image is None:
    print(False)
else:
    gray_image = cv20.cvtColor(image, cv20.COLOR_BGR2GRAY)
    inverted = 255 - gray_image
    blur = cv20.GaussianBlur(inverted, (21, 21), 0)
    inverted_blur = 255 - blur
    sketch = cv20.divide(gray_image, inverted_blur, scale=256.0)
    cv20.imwrite("sketch image.png", sketch)
    cv20.imshow("sketch", sketch)

    cv20.waitKey(0)
    cv20.destroyAllWindows"""

# even or odd number
"""n = 101
if n & n+1 == n:
    print("even number")
else:
    print("odd number")"""
# --------------------------------
