#---------------
#--set methods--
#---------------

#clear()
a={1,2,3,4,5,6}
a.clear()
print(a) #set()
print("*"*50)


#union()
b={"one","two","three"}
c={"1","2","3"}
d={"4","5","6"}
print(b | c) #b ithad c
print(b.union(c))# b ithad c
print(b.union(c,d))#b ithad c ithad d
print("*"*50)


#add()
d={1,2,3,4}
d.add(5)
print(d)#{1, 2, 3, 4, 5}
print("*"*50)


#copy()
e={1,2,3,4}
f=e.copy()
print(e)
print(f)
print("="*50)

e.add(5)
print(e)
print(f)
print("*"*50)


#remove()
g={1,2,3,4}
print(g)
g.remove(1)
print(g)
print("*"*50)

#g.remove(5)# error

#discard()
h={1,2,3,4,5}
h.discard(1)
print(h) # {2,3,4,5}
h.discard(5)
print(h) # {2,3,4}
print("="*50)


#pop()
i={"amr",True,5,2}
i.pop()
print(i)
print("="*50)


#update()
j={1,2,3,4}
k={5,6,"amr"}
j.update(["khaled","gamal"]) # type: ignore
print(j) # {'khaled', 1, 2, 3, 4, 'gamal'}
j.update(k)
print(j) # {'khaled', 1, 2, 3, 4, 5, 6, 'amr', 'gamal'}