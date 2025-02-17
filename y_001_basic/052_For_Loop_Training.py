#=================
#== Loop => For ==
#==  Training   ==
#=================

# even=0
# odd=0
# for number in range(1,100):
#     if number % 2==0:
#         even =even + number
#     elif number % 2!=0:
#         odd = odd +number
# print(f"sum of even number= {even} \n")
# print(f"sum of odd number= {odd}")

#Dictionary
myskills={
    "phy" :"15",
    "chem":"14",
    "hist":"12",
    "geo" :"12",
    "math":"36",
    "English":"25",
    "french":"28.5",
    "araby":"45"
}
for skill in myskills:
    print(f"my progress in {skill} is: {myskills[skill]}")