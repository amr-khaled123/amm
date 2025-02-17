# ---------
a=[1,2,3,4]
a.clear()
print(a) #=[]

# copy()
b=[1,2,3,4]
c=b.copy()
print(c) # [1, 2, 3, 4]
d=[11,2,3,4,5,4,7,8]
print(d.count(1)) #=0
print(d.count(2)) #=1
print(d.count(4)) #=2

# insert
f=[1,2,3,4,5,"A","c"]
f.insert(0,"c")
print(f) # ['c', 1, 2, 3, 4, 5, 'A', 'c']

# pop
g=[1,2,5,4,6,8,7]
print(g.pop(0)) # 1
print(g) # [2, 5, 4, 6, 8, 7]