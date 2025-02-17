#=================
#== Loop => For ==
#=================

mynum=[1,2,3,4,5,6,7,8,9]
"""for number in mynum:
    print(f"{number} * 17 = {number*17}")"""
x=0
y=0
for number in mynum:
    #print(number)
    if number % 2 !=0:
        print(f"the number {number} is odd".title())
    elif (number % 2==0 and number >0 ):
        print(f"the number {number} is even".title())

else:
    print("Loop is finished")

name="osama"
for letter in name:
    print(f"[{letter}]")
print("*"*50)
for letter in name:
    print(f"[{letter.upper()}]")