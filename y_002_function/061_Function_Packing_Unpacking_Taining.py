#=========================================
#== Function Packing Unpacking Training ==
#=========================================

def satr():
    print('*'*40)


def show_skills(name,*skills): # type: ignore
    print(f"hello {name} \nskills without progress is: ")
    for skill in n:
        print(f"- {skill}")
satr()

i=int()
n=[]
while(i==0):
    n.append(input("enter object\n"))
    i=int(input("enter zero to continue and any number to stop\n"))
show_skills("Amr",n)


def show_skills(name,*skills,**skillwithprogress):
    print(f"hello {name} \nskills without progress is: ")
    for skill in n:
        print(f"- {skill}")
        print("skills with progress is: ")
    for skill_key,skill_value in skillwithprogress.items():
        print(f"- {skill_key} => {skill_value}")
satr()

i=int()
n=[]
while(i==0):
    n.append(input("enter object\n"))
    i=int(input("enter zero to continue and any number to stop\n"))
show_skills("amr",n,python="80")
satr()

x=['amr',2,'khaled',5]
y=[]
for i in x:
    y.append(i)
    print(y)