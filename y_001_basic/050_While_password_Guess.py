#====================
#==== While Loop ====
#== password Guess ==

tries = 4
mainpassword =input("Enter your password".title())
inputpassword = input("write ypur password".title())

while inputpassword != mainpassword:
    tries -=1
    print(f"Wrong Password,{'Last' if tries==0 else tries} chances lefts")
    inputpassword=input("write ypur password".title())
    if tries == 0:
        print("All Tries is finished")
        break
        print("Will Not Print")
else:
    print("Correct Password")