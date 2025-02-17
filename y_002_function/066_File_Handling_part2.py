#================================
#== File Handling => Read File ==
#================================

myfile = open(r"F:\pythonpych\00_python.py")

# print(myfile)
# print("*"*50)
# print(myfile.name)
# print("*"*50)
# print(myfile.mode)
# print("*"*50)
# print(myfile.buffer)
# print("*"*50)
# print(myfile.errors)
# print(myfile.read(5))
# print(myfile.read())
#print(myfile.readline())
#print(myfile.readline())
#print(myfile.readline())
#print(myfile.readline())
#print(myfile.readline())
#print(myfile.readline())
#print(myfile.readline())
#print(myfile.readline())
#print(myfile.readline())
#print(myfile.readline())

#print(myfile.readlines())
#print(myfile.readlines())
#print(myfile.readlines())

for line in myfile:
    print(line)
    if line.startswith("07"):
        break

myfile.close()