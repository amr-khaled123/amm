#====================
#== Break continue ==
#====================

mynumbers=[1,2,3,4,5,6,7,8,9,10,11]
for number in mynumbers:
    if number == 9:
        continue
    print(number)
print("*"*50)


mynumbers=[1,2,3,4,5,6,7,10,13,14,19]
for number in mynumbers:
    if number == 13:
        break
    print(number)
print("*"*50)


mynumbers=[1,2,3,4,5,6,7,10,13,14,19]
for number in mynumbers:
    print(number)
    if number == 13:
        break
print("*"*50)


mynumbers=[1,2,3,4,5,6,7,10,13,14,19]
for number in mynumbers:
    print(number)
    if number == 13:
        pass
