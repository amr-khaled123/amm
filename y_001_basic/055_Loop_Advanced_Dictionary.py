#==============================
#== Advanced Dictionary Loop ==
#==============================

myskills = {
    "html":"80%",
    "Js" : "70%",
    "PHP": "60%",
    "python": "80%",
}

for skill in myskills :
    print(f"{skill} => {myskills[skill]}") #'html' => '80%;
print('*'*50)

for key,value in myskills.items():
    print(f"{key.title()} => {value}") #'html' => 80%
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
for key,value in people.items():
    print(f"progress of {key} ")
    for second_key,second_value in value.items():
        print(f"- {second_key} => {second_value}") #progress of osama - html' =>70
    print("*"*50)