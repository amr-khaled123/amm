
# n = int(input())
"""y = 0
for i in range(n):
    x = [int(m) for m in input().split()]
    y += x[i] - x[-i-1]
print(abs(y))"""
# ----------------------------------------------
# n = int(input())
"""n = int(input())
m = n
x = 1
for i in range(0, n):
    for j in range(m, 1, -1):
        print(' ', end='')
    for k in range(0, x):
        print('#', end='')
    print()
    m -= 1
    x += 1"""

# x = [int(m) for m in input().split()]
"""y = max(x)
print(y)
print(x.count(y))"""

# make clock if 12am 00 and if pm <12 add to it 12
"""x = [m for m in input().split(':')]
y = int()
if x[-1][2:].lower() == 'pm' and x[0] != str(12):
    y = int(x[0])+12
    x[0] = str(y)
elif x[0] == str(12) and x[-1][2:].lower() == 'am':
    x[0] = str(0)+str(0)
    z = x[-1][0:2]
    x.remove(x[-1])
    x.append(z)
if x[-1][2:].lower() == 'pm':
    z = x[-1][0:2]
    x.remove(x[-1])
    x.append(z)
elif x[-1][2:].lower() == 'am':
    z = x[-1][0:2]
    x.remove(x[-1])
    x.append(z)

print(':'.join(x))"""

# make clock if 12am 00 and if pm <12 add to it 12

"""
def timeConversion(s):
    hours = int(s[:2])
    time = s[3:8]
    meridian = s[-2:]

    if meridian == "PM" and hours < 12:
        hours += 12
    if meridian == "AM" and hours == 12:
        hours = "00"

    return "{:0>2}:{}".format(hours, time)"""

# --------------------
"""n = int(input())
i = 0
y = []
while i < n:
    x = int(input())
    y.append(x)
    i += 1

for i in range(len(y)):
    s = int()
    s = y[i]
    for j in range(0, 20):
        if (y[i] == (5*j)-1 or y[i] == (5*j)-2 or y[i] == (5*j)) and y[i] > 35:
            s = 5*j
        else:
            continue
    print(s)"""


# -----------------
"""def gradingStudents(grades):
    return list(map(lambda grade: 5*(div[0]+1) if grade >= 38 and (div := divmod(grade, 5))[1] >= 3 else grade, grades))


n = int(input())
i = 0
x = []
for i in range(0, n):
    x.append(int(input()))


s = gradingStudents(x)
for i in range(0, len(s)):
    print(s[i])"""

# print(dir(divmod))
x = {5, 9, 6, 2}
print(x)
