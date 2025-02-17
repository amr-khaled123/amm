#==========================================
#== Function Packing,Unpacking Arguments ==
#==========================================

mylist1=[1,2,3,4,5]
mylist2=["amr","khaled","gamal"]
print(*mylist1)
print(*mylist2)
print("*"*50)


"""def say_hello(n1,n2,n3,n4):
    peoples = [n1, n2, n3, n4]
    print(peoples)
    print(*peoples, end='')
say_hello(n1=input("enter name\n".title()),n2=input("enter name\n".title()),n3=input("enter name\n".title()),n4=input())
print("*"*50)"""


"""def show_details(skill1,skill2):
    skills=[skill1,skill2]
    print("hello amr your skills is: ")
    for skill in skills:
        print(f"{skill}")
show_details(skill1=input(),skill2=input())
print("*"*50)"""


def show_detail(name,*skills):
    print(f"hello {name} your skills is: ")
    for skill in skills:
        print(skill)
    print('*'*40)
show_detail("amr",'html','java',"C++",'python')
show_detail("ahmed","html","cpp","python","java script")