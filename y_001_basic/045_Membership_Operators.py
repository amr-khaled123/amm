#=========================
#== membership operator ==
#=========================

#string
name="amr"
print("a" in name)
print("="*50)

#List
friends=["amr","ahmed","abdo"]
print("amr" in friends)
print("ahmed" not in friends)
print("="*50)

#using in and not in with condition
countriesone=["egypt","ksa","kuwait","bahrain"]
country1discount=70
countries2=["italy","usa"]
country2discount=50
x=input("enter your country\n".title()).lower()
cprice=200
ccontent="python course"
if (x in countriesone):
    print(f"price of {ccontent} is {cprice - country1discount}".title())
elif (x in countries2):
    print(f"price of {ccontent} is {cprice - country2discount}".title())