# -----------------------
# -- Built in Function --
# -----------------------
# sum()                 -
# round()               -
# range()               -
# print()               -
# -----------------------

# sum(iterable , start)

"""a= [1,10,19,40]
print(sum(a))
print(sum(a , 40))"""

# round(number , num of digits)
"""print(round(150.698))   # =151
print(round(150.501))   # =151
print(round(150.49))    # =150
print(round(150.50))    # =150
print(round(150.426,2)) # =150.43
print(round(150.423,2)) # =150.42
print(round(150.444,2)) # =150.44
print(round(150.445,2)) # =150.44
print(round(150.446,2)) # =150.45d"""

# range(start , end, step)
print(list(range(0)))
print(list(range(10)))
print(list(range(0,20,2)))
print(*list(range(0,20,2)))
a=list(range(1,10,1))
print(a)
print(*a)

# print(1)
# print("hello amr how are you".title())
# print("hello" ,"amr" ,"how" ,"are" ,"you")
# print("hello" ,"amr" ,"how" ,"are" ,"you", sep=" - ")
# print("amr", end=" @\n")
# print("hello")