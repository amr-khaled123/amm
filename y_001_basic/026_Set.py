#-----------
#---set-----
#-----------
#Not order and not Indexed
myset1={1,"amr","khaled",5,6}
print(myset1) # {1, 5, 6, 'amr', 'khaled'}
#print(myset[0]) #error
myset2={1,2,5,2,9}
#print(myset2[0:3])error can't be slicing

#Has only immutable Data Types
#myset3={1,2,"amr",10.5,True,[1,2,3]}
#print(myset3) un hashable type

myset3={1,2,"amr",10.5,True,(1,2,5)}
print(myset3) #{1, 2, (1, 2, 5), 'amr', 10.5}

# items is unique

myset4={1,2,"amr",4,"amr",2}
print(myset4) #{'amr', 1, 2, 4}