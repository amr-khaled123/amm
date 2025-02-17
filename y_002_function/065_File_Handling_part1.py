"""================
== File Handling ==
===================
'a' Append Open File Fore Appending Values, create File If Not Exists
'r' Read   [Default Value] open file for read and give error if file is not exists
'w' write  Open file for writing, create file if not exists
'x' create create file, give error if file exists
==============================================================================="""

import os
print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))
print(os.chdir(os.path.dirname(os.path.abspath(__file__))))
file =open(r"f:\pythonpych\00_python.py")
print(file)