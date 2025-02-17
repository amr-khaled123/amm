# ----------------------------------
# -- Date and Time => Introductio --
# ----------------------------------

import datetime
# print(dir(datetime))
# print(dir(datetime.datetime))

# print the current date and time

"""print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)"""

# Print Start and End of Date
# print(datetime.datetime.min)
# print(datetime.datetime.max)
# print("*"*40)

# print(datetime.datetime.now().time())
# print('*'*40)
# print(datetime.datetime.now().time().hour)
# print('*'*40)
# print(datetime.datetime.now().time().minute)
# print('*'*40)

# print(datetime.datetime(2020,11,27,9))
# print(((datetime.datetime.now())-(datetime.datetime(2004,11,21))))
# x=((datetime.datetime.now())-(datetime.datetime(2004,11,21)))

x = datetime.datetime.now()
y = datetime.datetime(2004, 11, 21)

print(x)
print(y)
# z = (x-y).days
# print(z)
