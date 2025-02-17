#---------
#--Tuple--
#---------

myawesometuple1=("amr","khaled")
myawesometuple2="amr","khaled"
print(myawesometuple1) #"amr","khaled"
print(myawesometuple2) #"amr","khaled"

print(type(myawesometuple1)) #<class 'tuple'
print(type(myawesometuple2)) #<class 'tuple

#Tuple indexing
myawesometuple3=(1,2,3,4,5)
print(myawesometuple3[0]) #1
print(myawesometuple3[-2]) #4
print(myawesometuple3.index((1))) #0

#Tuple assign value
myawesometuple4=(1,2,3,4,5)
print(myawesometuple4[1]) #=2
print(myawesometuple4) #(1,2,3,4,5)

#Tuple items
myawesometuple5=("amr","amr",1,2,3,100.4,True)
print(myawesometuple5[1]) #amr
print(myawesometuple5[-1]) #True