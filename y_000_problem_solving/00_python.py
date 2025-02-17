# Second place in comptetion
"""if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores=list(arr)
    scores.sort()
    first,second=-100,-100
    print(scores)
    for score in scores:
        if first < score:
            second=first
            first=score
    print(second
"""
# Average of N numbers
"""n=int(input("How many numbers".title()))
total_sum=0
for numbers in range(n):
   total_sum+=float(input("enter number".title()))
Average=float(total_sum/n)
print(f"Average= {Average}")"""

#Calculate Average Of Number Use While
"""n=float(input("enter number"))
total_sum=0
total_sum= total_sum + n
x=1
while n>0:
    n=float(input("enter numbers and -1 to break".title()))
    if(n>0):
        total_sum=total_sum+n
        x+=1
    else:
        print("finished")
Average=float(total_sum/x)
print(Average)"""


"""import time
def myfunction():
    start_time=time.time()
    s=0
    for i in range(1,n+1):
        s=s+i

    End_time=time.time()
    return s,End_time-start_time
n=5
print(myfunction())"""

"""if __name__ == '__main__':
    N = int(input())
    list1=[]
    i=0
    while(i<N):
        choose1=input().lower()
        if choose1=="insert":
            n=int(input())
            x=int(input())
            list1.insert(n,x)
        elif choose1=="remove":
             n=int(input())
             list1.remove(n)
        elif choose1=="append":
             n=int(input())
             list1.append(n)
        elif choose1=="sort":
             list1.sort()
        elif choose1=="pop":
             list1.pop()
        elif choose1=="reverse":
             list1.reverse()
        else:
             print(list1)
        i+=1
"""

# Reblace in string
"""msg = "I <3 Python And Although <3 Elzero Web School"
x=msg.index("<")
y=msg.index("3")
print(msg.replace(msg[x:y+1],"love"))
print(msg)"""

# Calculate addtion and subtraction
"""def calculation(a, b):
    add= a + b
    sub= a-b
    return add ,abs(sub)
print(calculation(5,6))"""


# Calculator
"""def calculate(a,b,c="a"):
    if c[0]=="a" or c[0]=="A":
        return a+b
    elif c[0]=="s" or c[0]=="S":
        return a-b
    elif c[0]=="m" or c[0]=="M":
        return a*b
    else:
        return 0

print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200dd"""

# function to calculate number
"""def addition(*numbers):
    sum = 0
    for number in numbers:
        if number == 10:
            continue
        elif number == 5:
            sum -= number
            sum -= number
        if number:
            sum += number
    return sum
print(addition(10,5,8,4,7,14))"""

# function to show skill
"""def show_detail(name,*skills):
    if skills == False:
        print("hello amr you have no skill To show")
    else:
        print("hello amr your skill is: ")
        for i in skills:
            print(f"=> {i}")
show_detail("amr","html","Css","Js")"""

# def show_detail(**degrees):
#     print('hello Amr your progress is: ')
#     for mada,value in degrees.items():
#         print(f"{mada} => {value}")
# show_detail(html="70",python=80)

"""def get_people_scores(name, **skills):
  if name is None:
    print("Hello {} You Have No Scores To Show".format(name))
    return

  print("Hello {} This Is Your Score Table:".format(name))
  for skill, score in skills.items():
    print("{} => {}".format(skill, score))
get_people_scores("Ahmed")"""

#function to calculate factorial
"""def fact_num(n):
    if n==0:
        return 1
    else:
        return n*fact_num(n-1)
print(fact_num(n=int(input("Enter number to calculate factorial \n"))))"""

#function to calculate sum
"""def sum_num(n):
    if n==0:
        return 0
    else:
        return n+sum_num(n-1)
print(sum_num(n=int(input("enter number to calculate sum\n"))))"""

#function1 to calculate average
"""def average(n=1):
    sum1=float(0)
    i=0
    n=int(n)
    while n==0:
        numbers=int(input("enter number\n"))
        sum1+=numbers
        i+=1
        n=int(input("enter zero to continue and any number to stop\n"))
    print(f"sum= {sum1/i}")
average()"""

#function2 to calculate average
"""def average(list):
    sum = 0
    numbers=list
    for number in numbers:
        sum += number
    return sum / len(numbers)

print(average([1,5,9,6]))"""

#function3 to calculate average
"""def average(numbers):
    return sum(numbers) / len(numbers)

print(average([1, 2, 3, 4, 5]))"""

#function lambda to calculate square
"""square=lambda x:f"square of {x}={x*x}"
print(square(5))"""

#function lambda to calculate sum of two number
"""sum0=lambda x,y:f"{x} + {y} = {x+y}"
print(sum0(x=int(input("enter first number\n")),y=int(input("enter second number\n"))))"""

#function lambda to calculate maximum of number
"""max0=lambda x:f"max number={max(x)}"
x=[]
n=0
while n==0:
    y=int(input("enter number\n"))
    x.append(y)
    n=int(input("enter zero to continue\n"))
print(max0(x))"""

#function lambda to calculate maximum of number
"""max0=lambda x:f"max number={max(x)}"
print(max0([1,2,5,8,9,12]))"""
#-----------------------------------------------------
#-----------------------------------------------------
# values = (0, 1, 2)
#
# if any(values):
#     my_var = 0
# my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]
#
# if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
#     print("Good")
# else:
#     print("Bad")

# v=40
# my_range = list(range(v))
# print(sum(my_range,v))
# print(sum(my_range))

# n=20
# l=list(range(n+1))
# print(sum(l)/n)



# def my_all(list):
#   for i in list:
#     if not i:
#       return False
#   return True
# print(my_all([0,1,2,5,8,9,8]))


"""def my_any(list):
  for i in list:
    if i:
      return True
  return False
print(my_any([0,False,[]]))"""


# def my_min(list):
#     min_v=list[0]
#     for i in list:
#         if i<min_v:
#             min_v=i
#     return min_v
# print(my_min([100,20,80,9]))
#
# def my_max(list):
#     min_v=list[0]
#     for i in list:
#         if i>min_v:
#             min_v=i
#     return min_v
# print(my_max([100,20,80,9]))

# friends_map=['amr','ahmed','mahmoud']
# def remove_chars(string):
#   return string[1:]
#
# cleaned_list = list(map(remove_chars, friends_map))
# print(cleaned_list)
#
# for name in cleaned_list:
#   print(name)

"""def get_names(string):
    return string.endswith("m")

list1=['amr','wessam','weaam','seham','khaled','gamal','ismail']

names=filter(get_names,list1)

names2=filter(lambda nam: nam[-1]=='m',list1)

for i in names:
    print(i)

for i in names2:
    print(i)"""

# num = [2,4,6,2]
# x=1
# for i in num:
#     x=x*i
# print(x)

"""skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
x=50
for i in range(len(skills) -1 ,-1 ,-1):
    if isinstance(skills[i], str):
        print(f"{x} - {skills[i]}")
        x += 1
    else:
        x+=1
        continue"""

"""import random

# Random Number Between 10 And 50 =>
random_number = random.randint(10, 50)
print(f"Random Number Between 10 And 50 => {random_number}")

# Random Even Number Between 2 And 10 =>
random_even_number = random.randint(2, 10)
while random_even_number % 2 != 0:
    random_even_number = random.randint(2, 10)
print(f"Random Even Number Between 2 And 10 => {random_even_number}")

# Random Odd Number Between 1 And 9 =>
random_odd_number = random.randint(1, 9)
while random_odd_number % 2 == 0:
    random_odd_number = random.randint(1, 9)
print(f"Random Odd Number Between 1 And 9 => {random_odd_number}")

# Module Methods Content Here
print(random.__dir__())"""

# def arithm(x,y,z):
#     m=0
#     for i in range(int(z)):
#         m += x+(y*i)
#     return m
# print(arithm(1,-2,10))

"""n=int(input("enter"))
student_marks={}
for _ in range(n):
    name, *line=input("enter n: ").split()
    scores=list(map(float,line))
    student_marks[name]=scores
query_name=input("enter name")
for item,value in student_marks.items():
    item = query_name
    print(f"{item} => {value/3}")"""

# import elzero
# from elzero import power
# print(power(5,2))