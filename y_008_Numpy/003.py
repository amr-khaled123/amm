import numpy as np
# np.ones((row,columns),datatype = dtype) zeros as ones
# np.full((rows,columns),item)
# np.eye() identity
# np.diag([1,2,3,4]) diagonol matrix always square matrix
# np.arange(x,y) array from x to y and if didn't put x will make x = 0
a = np.zeros((3, 4))
print(a)
a = np.zeros((3, 4), dtype=int)
print(a)
print('*'*20)

# /////////////////
a = np.ones((3, 4))
print(a)
a = np.ones((3, 4), dtype=int)
print(a)
print('*'*20)

# ////////////////////////
a = np.full((4, 3), 5)  # matrix all items in it is 5
print(a, '\n', '*'*20)

# /////////////////////////
a = np.eye(3)  # identity matrix
print(a, '\n', '*'*20)
a = np.eye(3, dtype=int)
print(a, '\n', '*'*20)

# //////////////////////////
a = np.diag([1, 2, 3, 4])
print(a, '\n', '*'*20)
# diagonol matrix always square matrix
# Main diameter elements

# //////////////////////////
a = np.arange(10)  # from 0 to 9
print(a, '\n', '*'*20)

# /////////////////////////
a = np.arange(4, 10)  # [4,5,6,7,8,9]
print(a, '\n', '*'*20)
# start from 0 to 10

# ////////////////////////////
a = np.arange(0, 14, 3)
print(a, '\n', '*'*20)
# start from 0 to 14 step 3 and 14 is exclusive

# ///////////////////////////
a = np.linspace(0, 25, 10, dtype=int)
print(a, '\n', '*'*20)
# from 0 to 25 length of array 10 and 25 is inclusive

# //////////////////////////////////
a = np.linspace(0, 25, 10, endpoint=False)
print(a, '\n', '*'*20)
# start from 0 to 25 length 10 and 25 is exclusive

# /////////////////////////////////////
a = np.random.rand(3, 3)
print(a, '\n', '*'*20)
# matrix of random float items 3*3 from 0 to 1 and 1 is exclusive

# ////////////////////////////////
a = np.random.uniform(0, 5, size=(3, 3))
print(a, '\n', '*'*20)
# matrix of random items size 3*3 float items from 0 to 5 and 5 exclusive

# /////////////////////////////
a = np.random.randint(0, 5, size=(3, 3))
print(a, '\n', '*'*20)
# matrix of random items size 3*3 integer items from 0 to 5 and 5 is exclusive

# ///////////////////////////////////////
a = np.random.normal(4, 15, size=(3, 3))
print(a, '\n', '*'*20)
# normal distribution mean = 4,standard deviation = 15

# //////////////////////////////
a = np.random.randn(5, 5)
print(a, '\n', '*'*20)
# standard normal distribution

# /////////////////////
a = np.array(['a', 'b', 'c', 'd'])
a1 = np.random.choice(a)
print(a1, '\n', '*'*20)

# ///////////////////////////
a = np.arange(5)
rp = np.random.permutation(a)
print(rp)

# /////////////////////////// mainpulation
a = np.linspace(0, 25, 20, endpoint=False)
print(a, '\n', '*'*20)

# ////////////////////////
a = np.reshape(a, (4, 5))
print(a, '\n==', '*'*20)

# ///////////////////////////////
a = np.reshape(a, (10, 2))
print(a, '\n', '*'*20)

a = np.arange(20).reshape((10, 2))
print(a, '\n', '*'*20)
