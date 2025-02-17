#==========================
#== Practical membership ==
#==========================

#Lists Contains Admins
admins= ["Ahmed","Osama","Sameh","Manal","Amr"]
#Logain
name=input("enter your name\n".title()).strip().capitalize()
if name in admins:
    print(f"hello {name} welcome back".title())
    option=input('delete or update your name?'.title()).strip().lower()
    if option[0:2]=='up':
        x=admins.index(name)
        thenewname=input("your new name please").strip().capitalize()
        admins[x]=thenewname
        print(admins)
    elif option[0:2]=="de":
        admins.remove(name)
        print("name deleted".title())
    else:
        print("wrong option".title())
else:
    print("you arn\'t admin")
    statue=input("add you yes or no?").strip().lower()
    if statue[0]=="y":
        admins.append(name)
        print(admins)
    else:
        print("you arn\'t admin")