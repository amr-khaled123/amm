# -------------------------------------------
# --Doc string & commenting vs documenting --
# -------------------------------------------

def amr_function(name):
    "amrkhaled gamal"
    print(f"hello {name}")


print('*'*40)
amr_function("amr")
print('*'*40)
print(dir(amr_function))
print('*'*40)
print(amr_function.__doc__)
print('*'*40)
help(amr_function)
