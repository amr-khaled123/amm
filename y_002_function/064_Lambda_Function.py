#========================
#== Function => Lambda ==
#========================
# [1] it has no name
# [2] you can call it inline without defining it
# [3] you can use it in return data from another function
# [4] lambda function used for simple function and def handla the large tasks
# [5] lambda is one single expression not block of code
# [6] lambda type is function
#=========================

def say_hello(name) : return f"hello {name}"
hello =lambda name:f"hello {name}"
detail =lambda name,age:f"hello {name} your age is: {age}"
print(hello("ahmed"))
print(detail("amr",19))
print(say_hello.__name__) # say_hello
print(hello.__name__) # lambda
print(type(say_hello))
print(type(hello))