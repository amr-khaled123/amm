#==================================
#== Ternary Conditional Operator ==
#==================================

#country="egypt"
#if country=="egypt":print(f"the weather in {country} is 15".title())
#elif country=="ksa":print(f"the weather in {country} is 30".title())
#else:print(f"the weather in {country} 20")

# short if
movierate = 18
age=int(input("enter your age\n".title()))
if age < movierate:
    print("movie isn\'t good for you")
else:
    print("movie is good for you and happy watching".title())

print("movie isn\'t good for you" if age < movierate else "movie is good for you and happy watching".title())