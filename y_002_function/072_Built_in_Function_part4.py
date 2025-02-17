# -----------------------
# -- Built in Function --
# -----------------------
# [1] Map Take A Function + Iterator
# [2] M
# [3]
# -----------------------

def foratext(text):
    return f"- {text} -".title()

a=["amr","khaled","gamal","ismail"]
# print(foratext)

print(list(map(foratext,a)))
for name in list(map(foratext,a)):
    print(name)
print("*"*50)
print("\n")


a=["amr","khaled","gamal","ismail"]

for name in list(map(lambda text : f"- {text.title()} -", a)):
    print(name)
print('*'*40)

x=['html','python','CSS','JS']
def names(skills):
    return f"- {skills} -"
for skill in map(names,x):
    print(skill)
print('*'*40)

skilld=map(lambda skiil: f'- {skiil} -',x)
for skill in skilld:
    print(skill)