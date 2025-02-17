#===========
#==Boolean==
#===========

name="l"
print(name.isspace()) # False
print("="*50)

print(100>200) # False
print("="*50)

#True Values
print(bool("osama")) #True
print("="*50)
print(bool(100)) # True
print("="*50)
print(bool(10.5)) # True
print("="*50)
print(bool(True)) # True
print("="*50)
print(bool([1,2,3,4])) # True
print("="*50)

#False Values
print(bool(0))
print(bool(""))
print(bool(''))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(False))
print(bool(None))
print("="*50)
age = 36
txt = (f"My name is John, I am {age} ")
print(txt)