#===============================================
#===============================================
#== File Handling => Write And Append in File ==
#===============================================
#===============================================

"""myfile=open(r"F:\pythonpych\amory.txt", "a")
myfile.truncate(15)"""

"""myfile=open(r"F:\pythonpych\amory.txt", "a")
print(myfile.tell()"""

myfile=open(r"F:\pythonpych\amory.txt", "r")
myfile.seek(2)
print(myfile.read())
