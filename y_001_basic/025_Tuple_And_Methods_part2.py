# Tuple
#---------

mytuple1=("amr",)
mytuple2="amr",
print(mytuple1) #("amr",)
print(mytuple2) #("amr",)

print(type(mytuple1)) #<class 'tuple'>
print(type(mytuple2)) #<class 'tuple'>

print(len(mytuple1)) #1
print(len(mytuple2)) #1

# Tuple Concatenation

a=(1,2,3,4)
b=(5,6)

c=a+b
d=a+('a','b',True)+b

print(c) #(1, 2, 3, 4, 5, 6)
print(d) #(1, 2, 3, 4, 'a', 'b', True, 5, 6)

#TUple, List,string,Repeat(*)
mystring="amr"
myList=[1,2]
mytuple=("A","B")

print(mystring*6) #amramramramramramr
print(myList*6) #[1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(mytuple*6) #('A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B')


#Methods=> Count
a=(1,3,8,7,8)
print(a.count(8)) #2
print(a.count(1)) #1


#Methods =>Index()
b=(1,3,7,8,2,6,5)
print(b[0]) #1
print("the position of index is: {:d}".format(b.index(2))) #the position of index is: 4
print(f"the position of index is: {b.index(2)}") #the position of index is: 4


#Tuple Destruct
a=("A","B","C")
x,y,z=a
print(x) #A
print(y) #B
print(z) #C

a=("A","B",4,"C")
x,y,_,z=a
print(x) #A
print(y) #B
print(z) #C

a=("A","B",4,"C")
x,y,_,z=a
print(x) #A
print(y) #B
print(_) #4
print(z) #C