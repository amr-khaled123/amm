#==============
#==Dictionary==
#==============

user={
    "name":"amr",
    "age":18,
    "country":"Egypt",
    "family":["khaled","randa","mariem","manar","mona","abdo","zainb"],
    "rating":1.95
}
print(user.keys())#dict_keys(['name', 'age', 'country', 'family', 'rating'])
print(user.values())#dict_values(['amr', 18, 'Egypt', ['khaled', 'randa', 'mariem', 'manar', 'mona', 'abdo', 'zainb'], 1.95])
print(user["family"])#['khaled', 'randa', 'mariem', 'manar', 'mona', 'abdo', 'zainb']
print("="*50)

#Two_Dimensional_Dictionary
language={
    "one":{1:"amory",2:"khaled"},
    "two":{"khaled",4},
    "three":{"gamal,5"}
}
print(language["one"]) # {1: 'amory', 2: 'khaled'}
print(language["two"]) #{4, 'khaled'}
print(language["three"]) #{'gamal,5'}

print(len(language["one"])) # 2

framework1={
    "name":"js",
    "progress":"80%"
}
framework2={
    "name":"rejs",
    "progress":"80%"
}

allframework={
    "one":framework1,
    "two":framework2
}
print(allframework) #{'one': {'name': 'js', 'progress': '80%'}, 'two': {'name': 'rejs', 'progress': '80%'}}