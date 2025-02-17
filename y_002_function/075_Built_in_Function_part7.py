# ------------------------
# -- Built in Function  --
# ------------------------

# enumerate (iterable, start=0)

myskills = ['html',"python","CSS","Js"]
myskillswithcount = enumerate(myskills)
# print(type(myskillswithcount))
x=0
for y in myskills:
    print(f"{x}-{y}")
    x+=1
print('*'*40)
for counter,skill in myskillswithcount:
    print(f"{counter}-{skill}")
print('*'*40)

# help()

# print(help(print))
# print(help(sum))
# print('*'*40)

# reversed()

mystring = "elzero"
# print(reversed(mystring))
for letter in reversed(mystring):
    print(f"-{letter}")
print('*'*40)

mystring = "عمرو"
for letter in reversed(mystring):
    print(f"-{letter}")
print('*'*40)

x=reversed(myskills)
for element in x:
    print(f"-{element}")