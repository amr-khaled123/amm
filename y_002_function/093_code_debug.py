# ----------------
# -- code debug --
# ----------------

my_list = [1,2,3,4,5,6]
my_dictionary = {"name":"osama","age":18,"country":"egypt"}

for num in my_list:
    print(num)

for key,value in my_dictionary.items():
    print(f"{key} => {value}")

def function_one(x):
    print(f"hello {x}")

function_one("amr")