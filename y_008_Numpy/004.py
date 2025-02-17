import numpy as np
a = np.linspace(0, 50, 10, dtype=int, endpoint=False).reshape((5, 2))
print(a, '\n', '*'*20)
transpot_a = a.T
print(transpot_a, '\n', '*'*20)

# ///////////////////////////////////
a = np.array([1, 2, 3, 4, 5])
print(f"array before delete=> {a}")
a = np.delete(a, [0, 4])
print(f"array after delete=> {a}\n", '*'*20)  # delete index 0 and index 4

# ======================================================
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"array before delete=> \n{a}")
a = np.delete(a, 1, axis=1)
print(f"array after delete=> \n{a}\n", '*'*20)
# when axis is 0 delete row and first number is index when axis is 1 delete column

# ===========================================
a = np.linspace(0, 9, 9, dtype=int).reshape((3, 3))
print(f"{a}\n")
a = np.append(a, [[10, 11, 12]], axis=0)
print(f"{a}\n{'*'*20}")

# ========================================
a = np.arange(0, 9, dtype=int).reshape((3, 3))
print(f"{a}\n")
a = np.insert(a, 1, [10, 11, 12], axis=0)
print(f"{a}\n{'*'*20}")

# ================================================
a = np.arange(0, 9, dtype=int).reshape((3, 3))
print(f"{a}\n")
a = np.insert(a, 1, 10, axis=1)
print(f"{a}\n{'*'*20}")

# =========================================
a = np.arange(3, 7).reshape((2, 2))
print(f"{a}\n")
a1 = np.array([1, 2]).reshape(2, 1)

# a = np.vstack((a1, a))
# print(f"{a}\n{'*'*20}") [[1 2] [3 4] [5 6]]
a = np.hstack((a, a1))
print(f"hstack :{a}\n", '*'*20)

# =========================================
a = np.arange(0, 9).reshape((3, 3))
print(f"{a}\n")

a = np.split(a, 3)
print(f"{a}\n{'*'*20}")

# =========================================
# checking for nan(not number)
a = np.array([1, 2, 3, np.nan])
print(f"{a}\n")
print(np.isnan(a), '\n', '*'*20)

# =========================================
# checking for positive and negative infinty
a = np.array([1, 2, 3, np.inf, -np.inf])
print(f"{a}\n")
print(f"{np.isinf(a)}\n", '*'*20)

# ===============================
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.concatenate((a, b))
print(f"concatenate=> {c}\n", '*'*20)

print(f"{np.array_equal(a, a)}\n", '*'*20)
print(f"{np.array_equal(a, b)}\n", '*'*20)
print(f"{np.array_equal(a, c)}\n", '*'*20)
print(f"{np.equal(a, b)}\n", '*'*20)
print(f"{np.not_equal(a, b)}\n", '*'*20)

print((50*11*60)/1024)
