#===============
#==Type Conver==
#===============

#str
a=10
print(type(a))      # <class 'int'>
print(type(str(a))) # <class 'str'>
print(type(a)) # <class 'int'>
#====================
a=10
x=str(a)
print(type(x)) # <class 'str'>
print("*"*50)

#Tuple
c="amr" #string
d=[1,2,3,4,5] #list
e={"a","b","c"} #set
f={"a":1,"b":2,"c":3} #Dictionary

print(tuple(c)) # ('a', 'm', 'r')
print(tuple(d)) # (1, 2, 3, 4, 5)
print(tuple(e)) # ('b', 'c', 'a')
print(tuple(f.items())) # (('a', 1), ('b', 2), ('c', 3))
print(tuple(f.keys())) # ('a', 'b', 'c')
print(tuple(f.values())) # (1, 2, 3)
print("*"*50)

#list
b=(1,"amr",'khaled',4)
c="amr" #string
d=[1,2,3,4,5] #List
e={"a","b","c"} #set
f={"a":1,"b":2,"c":3} #Dictionary

print(list(b)) # [1, 'amr', 'khaled', 4]
print(list(c)) # ['a', 'm', 'r']
print(list(e)) # ['b', 'a', 'c']
print(list(f.keys())) # ['a', 'b', 'c']
print(list(f.values())) # [1, 2, 3]
print("*"*50)

#Set
b=(1,"amr",'khaled',4) #Tuple
c="amr" #string
d=[1,2,3,4,5] #List
e={"a","b","c"} #set
f={"a":"amr","b":2,"c":3} #Dictionary

print(set(b)) # {1, 'khaled', 4, 'amr'}
print(set(c)) # {'m', 'a', 'r'}
print(set(d)) # {1, 2, 3, 4, 5}
print(set(f)) # {'b', 'a', 'c'}
print('*'*50)

#Dictionary
b=(("amr",1),("khaled",2),("gamal",3)) #Tuple
c="amr" #string
d=[["amr",2],["khaled",5],["gamal",6]] #List
e={"a","b","c"} #set
f={"a":"amr","b":2,"c":3} #Dictionary

print(dict(b)) # {'amr': 1, 'khaled': 2, 'gamal': 3}
#print(dict(c))
print(dict(d)) # {'amr': 2, 'khaled': 5, 'gamal': 6}
#print(dict(e))
#print(dict(f))
print(f) # {'a': 'amr', 'b': 2, 'c': 3}
print('*'*50)