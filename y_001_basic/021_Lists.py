myawesomelist = ["one", "two", "three", "1", "2", "3"]
print(*myawesomelist)
print(" ".join(myawesomelist))  # one two three 1 2 3
print(myawesomelist[1])  # two
print(myawesomelist)  # =['one', 'two', 'three', '1', '2', '3']
print(myawesomelist[1:4])  # =['two','three',1]
print(myawesomelist[1:])  # =['two','three',1,5,3,4]
print(myawesomelist[1::5])  # ='two'
print(myawesomelist[1::2])  # ['two', '1', '3']
print(myawesomelist[1::3])  # ['two', '2']
print(myawesomelist[::2])  # =['one', 'three', '2']
print(myawesomelist[::1])  # =['one', 'two', 'three', '1', '2', '3']
print(myawesomelist[::3])  # =['one', 1]"""
# print(myawesomelist[150]) #=out of range
# نقدر نعدل على الليست
myawesomelist[0] = "amr"  # ="amr"
print(myawesomelist)  # =['amr','two','three',1,5,3,4]
