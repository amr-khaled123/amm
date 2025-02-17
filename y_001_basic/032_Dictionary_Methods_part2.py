#----------------------
#--Dictionary Methods--
#----------------------
print("="*50)


#setdefault()
user={
    "name":"amr"
}
print(user) # {'name': 'amr'}
print(user.setdefault("age","16")) #16
print(user) # {'name': 'amr', 'age': '16'}
print("="*50)


#popitem()
member={
    "name":"amr",
    "skill":"A7A"
}
print(member) # {'name': 'amr', 'skill': 'A7A'}
member.update({"age":18}) # type: ignore
print(member) # {'name': 'amr', 'skill': 'A7A', 'age': 18}
print(member.popitem()) #('age', 18)
print("="*50)


# item()
View={
    "name":"amr",
    "skill":"nothing"
}
allitem=View.items()
allvalue=View.values()
print(View)  # {'name': 'amr', 'skill': 'nothing'}
View["age"]=18 # type: ignore
print(allitem) # dict_items([('name', 'amr'), ('skill', 'nothing'), ('age', 18)])
print(allvalue) # dict_values(['amr', 'nothing', 18])
print("="*50)

# fromkeys()

a={'mykeyone','mykeytwo','mykeythreee'}
b="x"
print(dict.fromkeys(a,b)) # {'mykeytwo': 'x', 'mykeyone': 'x', 'mykeythreee': 'x'}