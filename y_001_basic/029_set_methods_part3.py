#===============
#==Set Methods==
#===============

#isSuperset()

a={1,2,3,4,5}
b={1,2,3}

print(a.issuperset(b))#True becuase all elements in b are in a
print(b.issuperset(a))#False becuase all elements in a aren't in b
print("="*50)


#issubset()
d={1,2,3,4,5}
e={1,2,3}
print(d.issubset(e))#False becuase you ask him if elements in d are in e
print(e.issubset(d))#True  becuase you ask him if elements in e are in d
#عكس اس سوبر ست
print("="*50)


#isdisjoined() mean ask him if they monfsleen
d={1,2,3,4,5}
e={1,2,3}
print(d.isdisjoint(e))#False
i={1,2,3,4}
j={5,6,7,8}
print(i.isdisjoint(j))#True