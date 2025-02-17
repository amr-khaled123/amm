#----------------------
#--Dictionary Methods--
#----------------------

# Clear()
user={
    "name":"amr"
}
print(user) #{'name': 'amr'}
user.clear()
print(user) #{}
print("="*50)

#Update()
member={
    "name":"amr"
}
print(member) #{'name': 'amr'}
member["age"]=36 # type: ignore
print(member) #{'name': 'amr', 'age': 36}
member.update({"country":"egypt"})
print(member) #{'name': 'amr', 'age': 36, 'country': 'egypt'}
print("="*50)

# Copy()
main={
    "name":"amr"
}
b=main.copy()
print(b) #{'name': 'amr'}
main.update({"age":"18"})
print(b) #{'name': 'amr'}
print(main) #{'name': 'amr', 'age': '18'}
print("="*50)


# Keys() + value()
print(main.keys()) #dict_keys(['name', 'age'])
print(main.values()) #dict_values(['amr', '18'])