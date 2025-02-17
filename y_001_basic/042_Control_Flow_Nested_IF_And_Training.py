#===============
#== Nested IF ==
#===============

uname = input("enter your name\n".title()).lower()
country=input("enter your country\n".title()).lower()
isstudent=input("are you student\n".title()).lower()
cname = "python course"
cprice = 100

if(country=="egypt" or country=="ksa"):
    print(f"hello {uname} because you from {country} and student".title())
    if isstudent=="yes":
        print(f"The Course \"{cname}\" price is: ${cprice - 70}")
    else:
        print(f"The Course \"{cname}\" price is: ${cprice - 60}".title())

elif(country=="kuwait" or country=="bahrain"):
    print(f"hello {uname} because you from {country} and student".title())
    if isstudent=="yes":
        print(f"The Course \"{cname}\" price is: ${cprice - 50}".title())
    else:
        print(f"The Course \"{cname}\" price is: ${cprice - 40}".title())

else:
    print(f"Hello {uname} because you are from {country}".title())
    print(f"the course \"{cname}\" price is {cprice - 20}")