"""import math
from turtle import *
def hearta(k):
    return 15*math.sin(k)**3
def heartb(n):
    return 12*math.cos(n)-5*\
            math.cos(2*n)-2*\
            math.cos(3*n)-\
            math.cos(4*n)
speed(200000000)
bgcolor("black")
for i in range(10000):
    goto(hearta(i)*20,heartb(i)*20)
    for i in range(5):
        color("#f73487")
    goto(0,0)
done()"""

"""import qrcode
img = qrcode.make('https://iplogger.com/2eB2H4')
img.save('myqrr.png')
img.show()"""
"""for i in range(0, 10, 1):
    if 2**i == 8192:
        print(i)
        break
    else:
        continue"""

"""print(oct(8))
print(hex(48))
print(bin(1))
# 10=1010 =A hex = 12 oct
# 8=1000 = 8 hex = 10 oct
# 20=14 // 32=20 48=30
"""
"""s = {1, 2, 3, 4}
b = {3, 2, 1, 5}
print(b.isdisjoint(s))
"""


"""""import pytube
from time import time
def speed_test(func):
    def wrap():
        start = time()
        func()
        end = time()
        print(f"time = {end-start}")


@speed_test"""


import pytube
link = input('enter: ')
yt = pytube.YouTube(link)
yt.streams.get_highest_resolution().download()
print("good download")
