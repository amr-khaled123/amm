# Even And Odd Number
def even_or_odd(number):
    if number % 2 == 0:
        print("\'Even\'")
    elif number % 2 != 0:
        print("\'Odd\'")

#-------------------------
def stringy(size):
    x = int((size) / 2)
    if size %2 ==0:
        return '10'*x
    elif size %2!=0:
        y='10'*x
        return y.ljust(size,'1')
# print(stringy(5))

#-------------------------------------
def double_char(s):
    y=[]
    for i in range(len(s)):
        x=s[i]*2
        y.append(x)
    return "".join(y)

# x=[1,2,5,'amr']
# print(x)
# x.append("khaled")
# print(x)
#-----------------------------------

def billboard(name, price=30):
    x=0
    y=0
    while(x<len(name)):
        y +=price
        x+=1
    return y
#-------------------------------------------
def say_hello(name, city, state):
    x=" "
    return f"Hello, {x.join(name)}! Welcome to {city}, {state}"
#--------------------------------------------------------------
# -- Two Dimension Array
"""x=[]
for i in range(2):
    y=input(f"enter number of {i}\n")
    z=y.split()
    z=list(map(int,z))
    x.append(z)
    i +=1
sum=0
f=1
for row in x:
    for i in row:
        sum = sum + i
        f = f * i
print(sum)
print(f)
print(x)"""

#-------------------------------------------
"""def remove_duplicates(array):
    seen = set()
    result = []
    for element in array:
        if element not in seen:
            seen.add(element)
            result.append(element)
    return result


array = [1, 1,1,2, 2]
print(remove_duplicates(array))"""
#-----------------------------------------
"""def delet(x):
    if x=="":
        return None
    c = x.count(",")
    if c>0:
        n=x.index(",")
    else:
        n=False
    y="".join(x.rsplit(f"{x[-1]}",1))
    z="".join(y.split(f"{x[0]}",1))
    if n!=False:
        m=" ".join(z.split(f"{x[n]}",100))
    elif n==False:
        m="".join(z)
    if m.strip()=="":
        return None
    else:
        return m.strip()
print(delet("4, 41, a5"))"""

#--------------------------------------
# def remove_first_and_last_items(string):
#     c=string.count(",")
#     if c>0:
#         n=string.index(",")
#     else:
#         n=False
#     if n!=False:
#         z="".join(string.split(f"{string[n]}",100))
#         n="".join(z.split(f"{z[0]}",1))
#         y="".join(n.rsplit(f"{n[-1]}",1))
#     else:
#         y="".join(string[1:-1])
#     x=" ".join(y)
#     if  len(x) == 0 :
#         return None
#     elif len(x)>0:
#         return x
#     else:
#         return x
# print(remove_first_and_last_items("a1,2"))