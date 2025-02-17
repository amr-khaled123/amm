# --------------------------
# -- Iterable VS Iterator --
# --------------------------

# Iterable
mystring = "Amr"
for letter in mystring:
    print(letter, end=" ")
print('\n')
mystring = iter(mystring)
print(next(mystring))
print(next(mystring))
print(next(mystring))

for letter in iter("elzero"):
    print(letter, end=" ")

print('\n')
x = 'elzero'
print(x[-1])
