#append()lists
myfriends=["abdo","mohamed","youssef"]
myoldfriends=["kareem","hamada","ali"]
print(myfriends) #=['abdo', 'mohamed', 'youssef']
myfriends.append("khaled")
print(myfriends) #['abdo', 'mohamed', 'youssef', 'khaled']
myfriends.append(100) # type: ignore
print(myfriends) #['abdo', 'mohamed', 'youssef', 'khaled',100]
myfriends.append(myoldfriends) # type: ignore
print(myfriends) #=['abdo', 'mohamed', 'youssef', ['kareem', 'hamada', 'ali']]
print(myfriends[3]) #=['kareem', 'hamada', 'ali']"""

#sort
y=[1,3,8,6,20,0,30,22]
y.sort() #and can sort alpha
print(y) #=[0, 1, 3, 6, 8, 20, 22, 30]
y.reverse() #=true
print(y) #=[30, 22, 20, 8, 6, 3, 1, 0]"""

#reverse()
z=[10,1,9,80,10,"amr",100]
z.reverse()
print(z) #=[100, 'amr', 10, 80, 9, 1, 10]"""

