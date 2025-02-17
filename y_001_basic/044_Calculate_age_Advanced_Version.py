#===============================
#== Practical your age Detail ==
#===============================

#Collect age data
age=float(input("enter your age\n".title()).strip())

#Collect Time Unit
unit=input("please choose time unit, months, weeks, days\n".title()).strip().lower()

#Get Time unit
months=age*12
weeks=months*4
days=float(age*365.25)

if unit[0]=="m":
    print(f"you live for {months:} month".title())
elif(unit[0]=="w"):
    print(f"you live for {weeks} week".title())
elif(unit[0]=="d"):
    print(f"you live for{days} day".title())
else:
    print("Default")
