#---------------------------------
#-- Modules => Built in Modules --
#---------------------------------
# [1] Module is A file contain A set of Functions
# [2] you Can Import Modules in Your App To Help You
# [3] You Can IMport Multiple Modules
# [4] You CAn Create Your own Modules
# [5] Modules Save your Item
#---------------------------------
# import random
# Import Main Module
import random
print(random)
print('*'*40)
print(f"print Random Float Number {random.random()}")
print('*'*40)
# Show All Function Inside Module
import random
print(dir(random))
print('*'*40)

# import one or two Functions from modules
from random import randint, random
print(f"print random integer {randint(0,100)}")