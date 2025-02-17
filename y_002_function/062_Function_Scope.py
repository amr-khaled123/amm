#====================
#== Function Scope ==
#====================

x=1 # Glopal scope

def one():
    global x
    x=2
    print(f"print function from glopal scope {x}")
def two():
    x=4
    print(f"print function from glopal scope {x}")


one()
print(f"print function from glopal scope {x}")
two()
print(f"print function from glopal scope {x}")