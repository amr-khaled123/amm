# ---------------------------------
# -- Built in Function => Filter --
# ---------------------------------------------------------------
# [1] -----   Filter Take A Function + Iterator   ---------------
# [2] Filter Run A Function on Every Element  -------------------
# [3] The Function Can Be Pre-Defined Function Or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True-
# [5] The function Need to Return Boolean Value  ----------------
# ---------------------------------------------------------------

def check_num(num):
    if num > 10:
        return num


mynumbers = [1, 2, 3, 4, 5, 8, 6, 20, 100, 15]
myresult = list(filter(check_num, mynumbers))

for numero in list(map(check_num, mynumbers)):
    print(numero)
print('*'*40)

print(myresult)
print("*"*50)

# ---------------------------------------------------------


def check_name(name):  # type: ignore
    return name.startswith("a")


mytext = ["amr", "khaled", "gamal", "ahmed", "osama", "osman"]
myreturndata = list(filter(check_name, mytext))

# ------------------------------------------------------------
for nam in list(map(check_name, mytext)):
    print(nam)
print('*'*40)

# ----------------------------------------------------------------
print(myreturndata)
print("*"*50)

# ------------------------------------------------------------------------


def check_name(name):
    return name[0] == "o"


mytext = ["amr", "khaled", "gamal", "osama", "osman"]
myreturndata = filter(check_name, mytext)

for person in list(map(check_name, mytext)):
    print(person)
print('*'*40)

for person in myreturndata:
    print(person)
print("*"*50)

mynames = ["amr", "khaled", "gamal", "osama", "osman"]
myreturn = list(filter(lambda name: name[0] == "o", mynames))
print(myreturn)
