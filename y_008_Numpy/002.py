import numpy as np
my_list = [1, 2, 3]
my_array = np.array(my_list)

print(id(my_list[0]))
print(id(my_list[1]))
print(id(my_array[0]))
print(id(my_array[1]))
print('*'*20)

# ----------------------------------
my_list_data = [1, 2, 'a', 'b', True, 10.5]
my_array_data = np.array(my_list_data)

print(my_list_data)
print(my_array_data)

print(type(my_list_data[0]))
print(type(my_array_data[0]))
