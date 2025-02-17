# ----------------------------------
# -- Date and Time => Date Format --
# ----------------------------------
# http://strftime.org/
# ------- strftimedirectives -------

import datetime
mybirthday = datetime.datetime(2004, 1, 21)
x = datetime.datetime.now()
y = mybirthday
print((x-y).days)
print(mybirthday)
print(mybirthday.strftime("%B"))
print(mybirthday.strftime("%A"))
print(datetime.datetime.now().strftime("%A"))
print(datetime.datetime.now().strftime("%B"))
# print(datetime.datetime(2020,11,27).strftime("%A"))~
print(datetime.datetime(2020, 11, 27).strftime("%B"))
print(datetime.datetime(2020, 11, 27).strftime("%d %B"))
