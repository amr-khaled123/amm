#---------------------------------
#-- Modules => Built in Modules --
#---------------------------------

# import sys
# print(sys.path)
# sys.path.append(r"F:\pythonpych\elzero.py")

import elzero
from elzero import sayhello
print(dir(sayhello))

sayhello("Ahmed")
elzero.sayhowareyou("Ahmed")

from elzero import factorial
print(factorial(5))