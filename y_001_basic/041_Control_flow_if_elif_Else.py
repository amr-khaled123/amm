#====================
#==  Control Flow  ==
#== IF, Elif, Else ==
#==  Make Decision ==
#====================

uname = input("enter your name\n".title()).lower()
country=input("enter your country\n".title()).lower()
cname = "python course"
cprice = 100

if(country=="egypt".lower()):
    print(f"hello {uname} because you from {country}".title())
    print(f"The Course \"{cname}\" price is: ${cprice - 60}".title())
elif(country=="ksa".lower()):
    print(f"hello {uname} because you from {country}".title())
    print(f"The Course \"{cname}\" price is: ${cprice + 40}".title())
else:
    print(f"Hello {uname} because you are from {country}".title())
    print(f"the course \"{cname}\" price is {cprice - 20}")