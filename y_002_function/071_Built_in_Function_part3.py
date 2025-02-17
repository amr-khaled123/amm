# -----------------------
# -- Built in Function --
# -----------------------
# abs()                 -
# pow()                 -
# min()                 -
# max()                 -
# slice()               -
# -----------------------

# abs()
a=-2
print(abs(a))
print(abs(-100))
print(abs(-13.56))
print("*"*50)

# pow()
print(pow(2,2))
print(pow(4,3))
print(pow(2,5,10)) # 2 os 5 %10
print("*"*50)

# min()
a=[5,2,7,8,50,10,2,3,6,1]
print(min(a))
print("*"*50)

# max()
a=[5,2,7,8,50,10,2,3,6,1]
print(max(a))
print("*"*50)

# slice()
a=["A","B","C","D","E","F","G","H","J"]
print(a[slice(0,9,2)])