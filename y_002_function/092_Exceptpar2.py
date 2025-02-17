# ---------------------------
# -- except Handing part 2 --
# ---------------------------

the_file = None
the_tries = 5

while the_tries > 0:

    try:
        print("enter the absolute path")
        print(f"{the_tries} Tries left")
        file_name_and_path = input("File Name => :").strip()
        the_file = open(file_name_and_path,'r')
        print(the_file.read())
        break

    except FileNotFoundError:
        print("\nthe file not found")
        the_tries -=1

else:
    print("all is done")