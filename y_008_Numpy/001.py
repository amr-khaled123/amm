import numpy as np
# print(np.__version__)
my_list = ['1', '2', '3', '4']
my_array = np.array(my_list)

print(my_list)
for i in my_array:
    i = int(i)
print(my_array)
# ------------------------------------------------------------------
a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a)
print('*'*20)
print(a[0][1])
print(a[0, 1, 0])
print(a.ndim)  # number of dimension
# ------------------------------------------------------------------
c = np.array([1, 2, 3], ndmin=3)
print('*'*20)
print(c)
print(c.ndim)
# --------------------
x = np.array([1, np.pi, np.pi/2])
print(x)
y = np.array([[11, 2, 5], [22, 6, 7], [33, 1, 9], [44, 0, 8]])

# print(y, '*'*50)
# print(y*y)
# print(y+y)
# print(y-y)
# print(x.shape)
# print(y.shape)
