#==============
#==user input==
#==============

fname=input("what is your first name ?")
mname=input("what is your mid name ?")
lname=input("what is your Last name ?")
fname=fname.capitalize()
mname=mname.capitalize()
lname=lname.capitalize()
print("{:s} {:s} {:s}".format(fname,mname,lname))
print(f"Hello {fname} {mname:.1s} {lname}")
print("*"*50)

