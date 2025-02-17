# ----------------
# -- Generators --
# ----------------

def mygenerator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6


mygen = mygenerator()
print(mygen)
for letter in mygen:
    print(letter)
