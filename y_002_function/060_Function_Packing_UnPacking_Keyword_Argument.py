#==================================================
#== Function Packing, Unpacking Arguments KWArgs ==
#==================================================

myskills={
    "html":"88",
    "python":"70"
}
def show_skills(**skills):
    #print(type(skills))
    for skill,value in skills.items():
        print(f"{skill} => {value}")
def satr():
    print('*'*40)

show_skills(html="80%",Css="70%",Js="66%")
satr()
show_skills(**myskills)