#=========================
#==Practical Email slice==
#=========================

email=input("enter your email\n")
x=email.index("@")
y=email.index(".")
print(f"your user name is {email[:x]}")
print(f"your email is {email[x+1:y]}")