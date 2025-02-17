#=====================
#==Boolean Operators==
#=====================

age=18
Country="Egypt"
print(age>15)
print(Country=="Egypt")
print(age>15 and Country=="saudi")  # False
print(age>20 and Country=="Egypt")   # False
print(age>20 or Country=="Egypt") # True
print(age>15 or Country=="Saudi") # True
print(not age>15) # False
print(not Country=="Suadi") # True
print(not(age>15 or Country=="Egypt")) # False
print(not(age>15 or Country=="Saudi")) # False
print(not (age>15 and Country=="Saudi")) # True
print(not (age>20 and Country=="Egypt")) # # True
print(not (age>15 and Country=="Egypt")) # False