#=================
#== Loop => For ==
#== Nested Loop ==
#=================

peoples=["osama","amr","khaled","elzero"]
skills=["css","html","js"]

for name in peoples:
    print(f"{name} skills is: ")
    for skill in skills:
        print(skill)
    print("*"*50)


people={
    "osama":{
        "html":"70%",
        "css":"60%",
        "python":"80%",
        "javascript":"50%"
    },
    "Ahmed": {
        "html": "90%",
        "css": "85%",
        "python": "40%",
        "javascript": "65%",
    },
    "sayed": {
        "html": "35%",
        "css": "40%",
        "python": "95%",
        "javascript": "20%"
    }

}


print(people["osama"]['python']) # 80%
print("*"*50)


for name in people:
    print(f"skills and progress for {name} is: ")
    for skill in people[name]:
        print(f"{skill} => {people[name][skill]}")
    print("*"*50)
